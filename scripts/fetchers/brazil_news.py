#!/usr/bin/env python3
"""
Brazil Health News Fetcher

Coleta notícias de saúde do Brasil:
- Google News Brasil categoria Saúde
- Google News Brasil categoria Ciência

Saída: data/news/brazil_news.json
"""

import hashlib
import json
import re
import time
from datetime import datetime, timezone
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

import feedparser

# Diretório raiz do projeto
PROJECT_ROOT = Path(__file__).parent.parent.parent
DATA_DIR = PROJECT_ROOT / "data" / "news"

# Google News Brasil Saúde RSS
GOOGLE_NEWS_HEALTH_RSS = (
    "https://news.google.com/rss/topics/"
    "CAAqJQgKIh9DQkFTRVFvSUwyMHZNR3QwTlRFU0JYQjBMVUpTS0FBUAE"
    "?hl=pt-BR&gl=BR&ceid=BR:pt-419"
)

# Google News Brasil Ciência e Tecnologia RSS
GOOGLE_NEWS_SCIENCE_RSS = (
    "https://news.google.com/rss/topics/"
    "CAAqKggKIiRDQkFTRlFvSUwyMHZNRFp0Y1RjU0JYQjBMVUpTR2dKQ1VpZ0FQAQ"
    "?hl=pt-BR&gl=BR&ceid=BR:pt-419"
)

# Intervalo entre requisições
REQUEST_DELAY = 1.0  # segundos


def generate_id(title: str, link: str) -> str:
    """Gerar ID da notícia (baseado em hash do título e link)"""
    content = f"{title}:{link}"
    return hashlib.sha256(content.encode()).hexdigest()[:12]


def parse_source(entry, default_source: str = "Desconhecido") -> dict:
    """Extrair informações da fonte do RSS"""
    source_name = default_source
    if hasattr(entry, "source") and hasattr(entry.source, "title"):
        source_name = entry.source.title

    return {
        "name": source_name,
        "link": entry.get("link", "")
    }


def parse_published(entry) -> str:
    """Analisar data de publicação e converter para ISO 8601"""
    published = entry.get("published_parsed")
    if published:
        try:
            dt = datetime(*published[:6], tzinfo=timezone.utc)
            return dt.isoformat()
        except Exception:
            pass

    # Usar hora atual se falhar
    return datetime.now(timezone.utc).isoformat()


def clean_summary(summary: str) -> str:
    """Limpar texto do resumo (remover tags HTML, etc.)"""
    # Remover tags HTML
    clean = re.sub(r"<[^>]+>", "", summary)
    # Remover espaços em branco extras
    clean = re.sub(r"\s+", " ", clean).strip()
    return clean[:500] if len(clean) > 500 else clean


def fetch_rss(url: str, source_name: str) -> list[dict]:
    """Buscar notícias da URL RSS"""
    print(f"  Buscando: {source_name}")
    print(f"    URL: {url[:70]}...")

    try:
        # Buscar com cabeçalhos personalizados
        headers = {
            "User-Agent": "Mozilla/5.0 (compatible; BrTxGNN/1.0; +https://brtxgnn.yao.care)",
            "Accept": "application/rss+xml, application/xml, text/xml",
            "Accept-Language": "pt-BR,pt;q=0.9,en;q=0.8",
        }
        request = Request(url, headers=headers)
        with urlopen(request, timeout=30) as response:
            content = response.read()
    except (HTTPError, URLError) as e:
        print(f"    Erro: {e}")
        return []

    feed = feedparser.parse(content)

    if feed.bozo:
        print(f"    Aviso: Problema na análise RSS - {feed.bozo_exception}")

    news_items = []

    for entry in feed.entries:
        title = entry.get("title", "")
        link = entry.get("link", "")

        if not title or not link:
            continue

        news_id = generate_id(title, link)
        source = parse_source(entry, source_name)
        published = parse_published(entry)
        summary = clean_summary(entry.get("summary", "") or entry.get("description", ""))

        news_items.append({
            "id": news_id,
            "title": title,
            "published": published,
            "summary": summary,
            "sources": [source]
        })

    print(f"    Obtidas: {len(news_items)} notícias")
    return news_items


def fetch_google_news_health() -> list[dict]:
    """Buscar Google News Brasil categoria Saúde"""
    return fetch_rss(GOOGLE_NEWS_HEALTH_RSS, "Google News Brasil Saúde")


def fetch_google_news_science() -> list[dict]:
    """Buscar Google News Brasil categoria Ciência"""
    return fetch_rss(GOOGLE_NEWS_SCIENCE_RSS, "Google News Brasil Ciência")


def deduplicate_news(news_items: list[dict]) -> list[dict]:
    """Remover notícias duplicadas (baseado em ID)"""
    seen_ids = set()
    unique_items = []

    for item in news_items:
        if item["id"] not in seen_ids:
            seen_ids.add(item["id"])
            unique_items.append(item)

    return unique_items


def filter_health_keywords(news_items: list[dict]) -> list[dict]:
    """Filtrar por palavras-chave relacionadas à saúde"""
    health_keywords = [
        # Médico / Saúde geral (Português)
        "médico", "medicina", "medicamento", "remédio", "tratamento",
        "terapia", "diagnóstico", "cirurgia", "hospital", "clínica",
        "saúde", "doença", "enfermidade", "sintoma", "infecção",
        "vírus", "bactéria",
        # Nomes de doenças
        "câncer", "diabetes", "hipertensão", "coração", "AVC",
        "derrame", "demência", "Alzheimer", "depressão", "insônia",
        "asma", "alergia", "hepatite", "rim", "fígado", "pulmão",
        # Medicamentos / Tratamentos
        "ANVISA", "aprovação", "ensaio clínico", "vacina", "anticorpo",
        "imunoterapia", "terapia gênica", "célula-tronco",
        # Pesquisa
        "pesquisa", "descoberta", "desenvolvimento", "eficácia",
        "efeito colateral", "risco", "estudo",
        # Farmacêutica
        "farmacêutica", "biotecnologia", "laboratório",
        # Palavras em inglês (para notícias internacionais)
        "drug", "FDA", "clinical trial", "vaccine", "cancer",
    ]

    filtered = []
    for item in news_items:
        text = f"{item['title']} {item.get('summary', '')}".lower()
        if any(keyword.lower() in text for keyword in health_keywords):
            filtered.append(item)

    return filtered


def main():
    print("Coletando notícias de saúde do Brasil...")

    # Garantir que o diretório existe
    DATA_DIR.mkdir(parents=True, exist_ok=True)

    all_news = []

    # Google News Brasil Saúde
    news = fetch_google_news_health()
    all_news.extend(news)
    time.sleep(REQUEST_DELAY)

    # Google News Brasil Ciência
    news = fetch_google_news_science()
    all_news.extend(news)

    # Remover duplicatas
    unique_news = deduplicate_news(all_news)
    print(f"\nApós remoção de duplicatas: {len(unique_news)} itens")

    # Filtrar por saúde
    health_news = filter_health_keywords(unique_news)
    print(f"Após filtro de saúde: {len(health_news)} itens")

    # Ordenar por data (mais recente primeiro)
    health_news.sort(key=lambda x: x["published"], reverse=True)

    # Saída
    output = {
        "source": "brazil_news",
        "fetched_at": datetime.now(timezone.utc).isoformat(),
        "total_fetched": len(all_news),
        "unique_count": len(unique_news),
        "health_related_count": len(health_news),
        "news": health_news
    }

    output_path = DATA_DIR / "brazil_news.json"
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(output, f, ensure_ascii=False, indent=2)

    print(f"\nSaída: {output_path}")
    print(f"  - Total buscado: {len(all_news)}")
    print(f"  - Único: {len(unique_news)}")
    print(f"  - Relacionado à saúde: {len(health_news)}")


if __name__ == "__main__":
    main()
