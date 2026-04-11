#!/usr/bin/env python3
"""
Script de processamento de notícias BrTxGNN

Funcionalidades:
1. Ler arquivos de notícias de data/news/*.json
2. Carregar keywords.json para correspondência de palavras-chave
3. Remover notícias duplicadas entre fontes
4. Gerar news-index.json para o frontend
"""

import json
import re
from datetime import datetime, timezone, timedelta
from difflib import SequenceMatcher
from pathlib import Path

# Diretório do projeto
PROJECT_ROOT = Path(__file__).parent.parent
DATA_DIR = PROJECT_ROOT / "data" / "news"
DOCS_DIR = PROJECT_ROOT / "docs"
NEWS_INDEX_PATH = DOCS_DIR / "data" / "news-index.json"

# Configurações
SIMILARITY_THRESHOLD = 0.8  # Limiar de similaridade de título
TIME_WINDOW_HOURS = 24  # Janela de tempo para detecção de duplicatas (horas)
MAX_NEWS_AGE_DAYS = 30  # Número máximo de dias para manter notícias


def load_json(path: Path) -> dict | list:
    """Carregar arquivo JSON"""
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def save_json(data: dict | list, path: Path):
    """Salvar arquivo JSON"""
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def load_all_sources() -> list[dict]:
    """Carregar notícias de todas as fontes"""
    all_news = []
    excluded = {"keywords.json", "synonyms.json", "synonyms.json.template"}

    for json_file in DATA_DIR.glob("*.json"):
        if json_file.name in excluded:
            continue

        try:
            data = load_json(json_file)
            source_name = data.get("source", json_file.stem)

            # Suportar formatos news e articles
            news_items = data.get("news", data.get("articles", []))
            print(f"  - {json_file.name}: {len(news_items)} notícias")

            for item in news_items:
                item["_source_file"] = source_name
                all_news.append(item)

        except Exception as e:
            print(f"  Aviso: Não foi possível carregar {json_file.name} - {e}")

    return all_news


def filter_old_news(news_items: list[dict]) -> list[dict]:
    """Filtrar notícias com mais de 30 dias"""
    cutoff = datetime.now(timezone.utc) - timedelta(days=MAX_NEWS_AGE_DAYS)
    filtered = []

    for item in news_items:
        try:
            pub_str = item.get("published", "")
            if pub_str:
                published = datetime.fromisoformat(pub_str.replace("Z", "+00:00"))
                if published >= cutoff:
                    filtered.append(item)
            else:
                # Sem data, manter
                filtered.append(item)
        except (ValueError, TypeError):
            filtered.append(item)

    removed = len(news_items) - len(filtered)
    if removed > 0:
        print(f"  Notícias antigas filtradas: {removed}")

    return filtered


def title_similarity(title1: str, title2: str) -> float:
    """Calcular similaridade de títulos"""
    clean1 = re.sub(r"\s*[-–—]\s*[^\s]+$", "", title1).strip()
    clean2 = re.sub(r"\s*[-–—]\s*[^\s]+$", "", title2).strip()
    return SequenceMatcher(None, clean1, clean2).ratio()


def deduplicate_news(news_items: list[dict]) -> list[dict]:
    """Remover notícias duplicadas entre fontes, mesclando fontes de notícias similares"""
    sorted_news = sorted(
        news_items,
        key=lambda x: x.get("published") or "",
        reverse=True
    )

    merged = []
    used_indices = set()

    for i, item in enumerate(sorted_news):
        if i in used_indices:
            continue

        similar_items = [item]

        try:
            pub_str = item.get("published") or datetime.now(timezone.utc).isoformat()
            item_time = datetime.fromisoformat(pub_str.replace("Z", "+00:00"))
        except (ValueError, TypeError):
            item_time = datetime.now(timezone.utc)

        for j, other in enumerate(sorted_news[i + 1:], start=i + 1):
            if j in used_indices:
                continue

            try:
                pub_str = other.get("published") or datetime.now(timezone.utc).isoformat()
                other_time = datetime.fromisoformat(pub_str.replace("Z", "+00:00"))
            except (ValueError, TypeError):
                other_time = datetime.now(timezone.utc)

            time_diff = abs((item_time - other_time).total_seconds() / 3600)

            if time_diff > TIME_WINDOW_HOURS:
                continue

            if title_similarity(item.get("title", ""), other.get("title", "")) >= SIMILARITY_THRESHOLD:
                similar_items.append(other)
                used_indices.add(j)

        # Mesclar fontes de notícias
        all_sources = []
        seen_links = set()
        for sim_item in similar_items:
            sources = sim_item.get("sources", [])
            if not sources:
                link = sim_item.get("link", "")
                source_name = sim_item.get("source", sim_item.get("_source_file", "Unknown"))
                if link:
                    sources = [{"name": source_name, "link": link}]

            for source in sources:
                link = source.get("link", "")
                if link and link not in seen_links:
                    seen_links.add(link)
                    all_sources.append(source)

        # Usar a data de publicação mais antiga
        try:
            pub_times = []
            for s in similar_items:
                pub_str = s.get("published")
                if pub_str:
                    pub_times.append(datetime.fromisoformat(pub_str.replace("Z", "+00:00")))
            earliest_time = min(pub_times) if pub_times else datetime.now(timezone.utc)
        except (ValueError, TypeError):
            earliest_time = datetime.now(timezone.utc)

        # Criar ID a partir do hash do título
        import hashlib
        news_id = hashlib.md5(item.get("title", "").encode()).hexdigest()[:12]

        merged_item = {
            "id": item.get("id", news_id),
            "title": re.sub(r"\s*[-–—]\s*[^\s]+$", "", item.get("title", "")).strip(),
            "published": earliest_time.isoformat(),
            "summary": item.get("summary", ""),
            "sources": all_sources,
            "matched_keywords": []
        }
        merged.append(merged_item)
        used_indices.add(i)

    print(f"  Após remoção de duplicatas: {len(merged)} notícias ({len(news_items) - len(merged)} mescladas)")
    return merged


def match_keywords(news_items: list[dict], keywords: dict) -> list[dict]:
    """Correspondência de palavras-chave em notícias"""
    drugs = keywords.get("drugs", [])
    indications = keywords.get("indications", [])

    # Construir mapa slug -> name dos medicamentos
    drug_name_map = {d["slug"]: d["name"] for d in drugs}

    matched_count = 0

    for item in news_items:
        text_to_search = f"{item['title']} {item.get('summary', '')}".lower()
        matches = []

        # Correspondência de medicamentos
        for drug in drugs:
            drug_name = drug["name"]
            drug_slug = drug["slug"]

            # Palavras-chave em inglês
            for kw in drug["keywords"].get("en", []):
                if kw.lower() in text_to_search:
                    matches.append({
                        "type": "drug",
                        "slug": drug_slug,
                        "keyword": kw,
                        "name": drug_name,
                        "url": drug["url"]
                    })
                    break  # Registrar apenas 1 vez por medicamento

            # Palavras-chave em português
            for kw in drug["keywords"].get("pt", []):
                if kw.lower() in text_to_search:
                    # Evitar duplicatas
                    if not any(m["slug"] == drug_slug for m in matches):
                        matches.append({
                            "type": "drug",
                            "slug": drug_slug,
                            "keyword": kw,
                            "name": drug_name,
                            "url": drug["url"]
                        })
                    break

        # Correspondência de indicações
        for ind in indications:
            ind_name = ind["name"]

            # Converter related_drugs de slug para {slug, name}
            related_drugs = [
                {"slug": slug, "name": drug_name_map.get(slug, slug)}
                for slug in ind.get("related_drugs", [])
            ]

            # Palavras-chave em inglês
            for kw in ind["keywords"].get("en", []):
                if kw.lower() in text_to_search:
                    matches.append({
                        "type": "indication",
                        "name": ind_name,
                        "keyword": kw,
                        "related_drugs": related_drugs
                    })
                    break

            # Palavras-chave em português
            for kw in ind["keywords"].get("pt", []):
                if kw.lower() in text_to_search:
                    # Evitar duplicatas
                    if not any(m.get("keyword") == kw and m["type"] == "indication" for m in matches):
                        matches.append({
                            "type": "indication",
                            "name": ind_name,
                            "keyword": kw,
                            "related_drugs": related_drugs
                        })
                    break

        item["matched_keywords"] = matches
        if matches:
            matched_count += 1

    print(f"  Correspondência de palavras-chave: {matched_count} notícias")
    return news_items


def generate_news_index(matched_news: list[dict]):
    """Gerar arquivo news-index.json para o frontend"""
    indexed_news = [
        {
            "id": item["id"],
            "title": item["title"],
            "published": item["published"],
            "sources": item["sources"],
            "keywords": item["matched_keywords"]
        }
        for item in matched_news
        if item.get("matched_keywords")
    ]

    output = {
        "generated": datetime.now(timezone.utc).isoformat(),
        "count": len(indexed_news),
        "news": indexed_news
    }

    save_json(output, NEWS_INDEX_PATH)
    print(f"  Índice gerado: {NEWS_INDEX_PATH}")
    print(f"  Total de notícias: {len(indexed_news)}")


def main():
    print("=" * 60)
    print("Processamento de Notícias de Saúde - BrTxGNN")
    print("=" * 60)

    # 1. Carregar notícias de todas as fontes
    print("\n1. Carregando arquivos de notícias:")
    all_news = load_all_sources()
    print(f"  Total: {len(all_news)} notícias")

    if not all_news:
        print("\n  Nenhuma notícia encontrada. Execute os fetchers primeiro.")
        return

    # 2. Filtrar notícias antigas
    print("\n2. Filtrando notícias antigas:")
    all_news = filter_old_news(all_news)

    # 3. Remover duplicatas
    print("\n3. Removendo duplicatas:")
    all_news = deduplicate_news(all_news)

    # 4. Carregar keywords e fazer correspondência
    print("\n4. Correspondência de palavras-chave:")
    keywords_path = DATA_DIR / "keywords.json"
    if not keywords_path.exists():
        print(f"  Não encontrado: {keywords_path}")
        return

    keywords = load_json(keywords_path)
    print(f"  Palavras-chave: {keywords.get('drug_count', 0)} medicamentos + {keywords.get('indication_count', 0)} indicações")
    all_news = match_keywords(all_news, keywords)

    # 5. Gerar news-index.json
    print("\n5. Gerando índice de notícias:")
    generate_news_index(all_news)

    # 6. Mostrar exemplos
    matched = [n for n in all_news if n.get("matched_keywords")]
    if matched:
        print("\n6. Exemplos de notícias correspondentes:")
        for item in matched[:3]:
            print(f"   - {item['title'][:60]}...")
            drugs = [k["name"] for k in item["matched_keywords"] if k["type"] == "drug"]
            diseases = [k["name"] for k in item["matched_keywords"] if k["type"] == "indication"]
            print(f"     Medicamentos: {', '.join(drugs[:3])}")
            print(f"     Indicações: {', '.join(diseases[:3])}")

    print("\nConcluído!")


if __name__ == "__main__":
    main()
