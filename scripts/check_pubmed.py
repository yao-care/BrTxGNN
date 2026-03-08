#!/usr/bin/env python3
"""
Verificar PubMed para novas publicações relacionadas à nossa lista de medicamentos.
Cria Issues no GitHub quando novas publicações são encontradas.
"""

import json
import os
import time
from datetime import datetime, timedelta
from pathlib import Path

import requests

from github_utils import create_issue, issue_exists, close_older_pubmed_issues

# Configuração
EUTILS_BASE = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils"
CACHE_FILE = Path(__file__).parent.parent / "data" / "cache" / "pubmed_cache.json"
DRUG_LIST_FILE = Path(__file__).parent / "drug_list.json"
GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN")
NCBI_API_KEY = os.environ.get("NCBI_API_KEY")
RATE_LIMIT_DELAY = 0.35  # segundos entre chamadas da API (NCBI rate limit)


def load_cache() -> dict:
    """Carregar o cache de PMIDs já vistos."""
    if CACHE_FILE.exists():
        with open(CACHE_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {"last_check": None, "seen_pmids": {}}


def save_cache(cache: dict):
    """Salvar o cache."""
    CACHE_FILE.parent.mkdir(parents=True, exist_ok=True)
    cache["last_check"] = datetime.now().isoformat()
    with open(CACHE_FILE, "w", encoding="utf-8") as f:
        json.dump(cache, f, indent=2, ensure_ascii=False)


def load_drug_list() -> list:
    """Carregar a lista de medicamentos."""
    if not DRUG_LIST_FILE.exists():
        print(f"Arquivo de lista de medicamentos não encontrado: {DRUG_LIST_FILE}")
        print("Execute extract_drug_list.py primeiro para gerar a lista.")
        return []

    with open(DRUG_LIST_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data.get("drugs", [])


def search_pubmed(drug_name: str, days_back: int = 7) -> list:
    """Buscar artigos publicados nos últimos N dias."""
    min_date = (datetime.now() - timedelta(days=days_back)).strftime("%Y/%m/%d")
    max_date = datetime.now().strftime("%Y/%m/%d")

    # Busca por reposicionamento de medicamentos
    query = f'"{drug_name}"[Title/Abstract] AND ("drug repurposing"[Title/Abstract] OR "drug repositioning"[Title/Abstract] OR "repurposed"[Title/Abstract])'

    params = {
        "db": "pubmed",
        "term": query,
        "mindate": min_date,
        "maxdate": max_date,
        "datetype": "pdat",
        "retmax": 50,
        "retmode": "json"
    }

    if NCBI_API_KEY:
        params["api_key"] = NCBI_API_KEY

    try:
        # Buscar IDs
        search_url = f"{EUTILS_BASE}/esearch.fcgi"
        response = requests.get(search_url, params=params, timeout=30)
        response.raise_for_status()
        data = response.json()

        id_list = data.get("esearchresult", {}).get("idlist", [])
        if not id_list:
            return []

        # Buscar detalhes
        time.sleep(RATE_LIMIT_DELAY)
        summary_url = f"{EUTILS_BASE}/esummary.fcgi"
        summary_params = {
            "db": "pubmed",
            "id": ",".join(id_list),
            "retmode": "json"
        }
        if NCBI_API_KEY:
            summary_params["api_key"] = NCBI_API_KEY

        summary_response = requests.get(summary_url, params=summary_params, timeout=30)
        summary_response.raise_for_status()
        summary_data = summary_response.json()

        articles = []
        result = summary_data.get("result", {})
        for pmid in id_list:
            if pmid in result:
                article = result[pmid]
                articles.append({
                    "pmid": pmid,
                    "title": article.get("title", ""),
                    "authors": article.get("authors", []),
                    "source": article.get("source", ""),
                    "pubdate": article.get("pubdate", "")
                })

        return articles

    except requests.RequestException as e:
        print(f"Erro ao buscar PubMed para {drug_name}: {e}")
        return []


def create_github_issue(drug_name: str, new_articles: list):
    """Criar uma Issue no GitHub para novas publicações encontradas."""
    title = f"📚 Nova Literatura: {drug_name} ({len(new_articles)} artigos)"

    if not GITHUB_TOKEN:
        print(f"[DRY RUN] Criaria issue para {drug_name} com {len(new_articles)} novos artigos")
        for article in new_articles[:3]:
            print(f"  - PMID {article['pmid']}: {article['title'][:60]}...")
        return

    # Fechar issues mais antigas deste medicamento antes de criar uma nova
    closed_count = close_older_pubmed_issues(drug_name)
    if closed_count > 0:
        print(f"  → Fechadas {closed_count} issue(s) mais antigas para {drug_name}")

    # Formatar detalhes dos artigos
    article_details = []
    for article in new_articles:
        authors = article.get("authors", [])
        first_author = authors[0].get("name", "Desconhecido") if authors else "Desconhecido"
        if len(authors) > 1:
            first_author += " et al."

        article_details.append(
            f"### PMID {article['pmid']}\n"
            f"- **Título**: {article['title']}\n"
            f"- **Autores**: {first_author}\n"
            f"- **Revista**: {article.get('source', 'Desconhecido')}\n"
            f"- **Data**: {article.get('pubdate', 'Desconhecido')}\n"
            f"- **Link**: https://pubmed.ncbi.nlm.nih.gov/{article['pmid']}/\n"
        )

    body = f"""## 📚 Detecção Automática de Nova Literatura

Esta Issue foi criada automaticamente pelo GitHub Actions.

### Nome do Medicamento
{drug_name}

### Fonte de Dados
PubMed

### Tipo de Evidência
Novas publicações sobre reposicionamento de medicamentos

### Informações Detalhadas
Encontrados **{len(new_articles)}** artigos novos:

{"".join(article_details)}

### Ações Sugeridas
- [ ] Revisar conteúdo dos artigos
- [ ] Avaliar se é necessário atualizar o nível de evidência do relatório do medicamento
- [ ] Adicionar citações relevantes ao relatório

---
*Tempo de detecção automática: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} UTC*
"""

    # Criar a issue com verificação de deduplicação
    labels = ["auto-detected", "needs-review", "pubmed"]
    create_issue(title, body, labels)


def main():
    print("=" * 60)
    print("Verificador de Evidências PubMed")
    print(f"Iniciado em: {datetime.now().isoformat()}")
    print("=" * 60)

    # Carregar dados
    cache = load_cache()
    drugs = load_drug_list()

    if not drugs:
        print("Nenhum medicamento encontrado. Saindo.")
        return

    print(f"Carregados {len(drugs)} medicamentos da lista")
    print(f"Última verificação: {cache.get('last_check', 'Nunca')}")
    print(f"NCBI API Key: {'Configurada' if NCBI_API_KEY else 'Não configurada'}")

    # Verificar cada medicamento
    new_findings = []
    seen_pmids = cache.get("seen_pmids", {})

    for i, drug in enumerate(drugs):
        drug_name = drug["name"]
        print(f"\n[{i+1}/{len(drugs)}] Verificando: {drug_name}")

        articles = search_pubmed(drug_name, days_back=7)
        time.sleep(RATE_LIMIT_DELAY)  # Limitação de taxa

        if not articles:
            continue

        # Filtrar para artigos realmente novos
        drug_seen = seen_pmids.get(drug_name, [])
        is_initial_discovery = not drug_seen
        new_articles = []

        for article in articles:
            pmid = article.get("pmid")
            if pmid and pmid not in drug_seen:
                new_articles.append(article)
                drug_seen.append(pmid)

        if new_articles:
            if is_initial_discovery:
                print(f"  Descoberta inicial: {len(new_articles)} artigos (nenhuma issue criada, linha de base estabelecida)")
            elif len(new_articles) < 2:
                print(f"  Apenas {len(new_articles)} artigo encontrado - abaixo do limite, ignorando issue")
            else:
                print(f"  Encontrados {len(new_articles)} novos artigos!")
                new_findings.append({
                    "drug": drug_name,
                    "articles": new_articles
                })

        seen_pmids[drug_name] = drug_seen

    # Atualizar cache
    cache["seen_pmids"] = seen_pmids
    save_cache(cache)

    # Criar issues para novos achados
    print("\n" + "=" * 60)
    print("Criando Issues para Novos Achados")
    print("=" * 60)

    if new_findings:
        for finding in new_findings:
            create_github_issue(finding["drug"], finding["articles"])
    else:
        print("Nenhuma nova publicação encontrada.")

    print(f"\nConcluído em: {datetime.now().isoformat()}")


if __name__ == "__main__":
    main()
