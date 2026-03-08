#!/usr/bin/env python3
"""
Google News RSS Fetcher - Brasil

Busca RSS do canal de saúde do Google News (Brasil), salva em data/news/google_rss.json
"""

import json
import hashlib
from datetime import datetime, timezone
from pathlib import Path

import feedparser

# Diretório raiz do projeto
PROJECT_ROOT = Path(__file__).parent.parent.parent
DATA_DIR = PROJECT_ROOT / "data" / "news"

# Google News - Canal de Saúde (Português Brasileiro)
GOOGLE_NEWS_HEALTH_RSS = (
    "https://news.google.com/rss/topics/"
    "CAAqJQgKIh9DQkFTRVFvSUwyMHZNR3QwTlRFU0JYQjBMVUpTS0FBUAE"
    "?hl=pt-BR&gl=BR&ceid=BR:pt-419"
)

# Google News - Canal de Ciência (complementar)
GOOGLE_NEWS_SCIENCE_RSS = (
    "https://news.google.com/rss/topics/"
    "CAAqKggKIiRDQkFTRlFvSUwyMHZNRFp0Y1RjU0JYQjBMVUpTR2dKQ1VpZ0FQAQ"
    "?hl=pt-BR&gl=BR&ceid=BR:pt-419"
)


def generate_id(title: str, link: str) -> str:
    """Gerar ID de notícia (hash baseado em título e link)"""
    content = f"{title}:{link}"
    return hashlib.md5(content.encode()).hexdigest()[:12]


def parse_source(entry) -> dict:
    """Extrair informações da fonte do entry RSS"""
    # Tag source do RSS do Google News
    source_name = "Google News"
    if hasattr(entry, "source") and hasattr(entry.source, "title"):
        source_name = entry.source.title

    return {
        "name": source_name,
        "link": entry.get("link", "")
    }


def parse_published(entry) -> str:
    """Parsear data de publicação, converter para formato ISO 8601"""
    published = entry.get("published_parsed")
    if published:
        try:
            dt = datetime(*published[:6], tzinfo=timezone.utc)
            return dt.isoformat()
        except Exception:
            pass

    # Se falhar o parse, usar hora atual
    return datetime.now(timezone.utc).isoformat()


def clean_summary(summary: str) -> str:
    """Limpar texto do resumo (remover tags HTML etc.)"""
    import re
    # Remover tags HTML
    clean = re.sub(r"<[^>]+>", "", summary)
    # Remover espaços em branco extras
    clean = re.sub(r"\s+", " ", clean).strip()
    return clean[:500] if len(clean) > 500 else clean


def fetch_rss_feed(url: str, source_name: str) -> list[dict]:
    """Buscar feed RSS específico"""
    print(f"Buscando {source_name}...")
    print(f"  URL: {url[:80]}...")

    feed = feedparser.parse(url)

    if feed.bozo:
        print(f"  Aviso: Problema ao parsear RSS - {feed.bozo_exception}")

    news_items = []

    for entry in feed.entries:
        title = entry.get("title", "")
        link = entry.get("link", "")

        if not title or not link:
            continue

        news_id = generate_id(title, link)
        source = parse_source(entry)
        published = parse_published(entry)
        summary = clean_summary(entry.get("summary", ""))

        news_items.append({
            "id": news_id,
            "title": title,
            "published": published,
            "summary": summary,
            "sources": [source]
        })

    print(f"  Encontradas {len(news_items)} notícias")
    return news_items


def fetch_google_news_brazil() -> list[dict]:
    """Buscar notícias de saúde do Google News Brasil"""
    all_news = []

    # Buscar canal de saúde
    health_news = fetch_rss_feed(GOOGLE_NEWS_HEALTH_RSS, "Google News Saúde BR")
    all_news.extend(health_news)

    # Buscar canal de ciência (pode ter notícias de pesquisas médicas)
    science_news = fetch_rss_feed(GOOGLE_NEWS_SCIENCE_RSS, "Google News Ciência BR")
    all_news.extend(science_news)

    # Remover duplicatas por ID
    seen_ids = set()
    unique_news = []
    for item in all_news:
        if item["id"] not in seen_ids:
            seen_ids.add(item["id"])
            unique_news.append(item)

    return unique_news


def main():
    # Garantir que o diretório existe
    DATA_DIR.mkdir(parents=True, exist_ok=True)

    # Buscar notícias
    news_items = fetch_google_news_brazil()

    # Saída
    output = {
        "source": "google_rss_br",
        "fetched_at": datetime.now(timezone.utc).isoformat(),
        "count": len(news_items),
        "news": news_items
    }

    output_path = DATA_DIR / "google_rss.json"
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(output, f, ensure_ascii=False, indent=2)

    print(f"\nSaída: {output_path}")
    print(f"  - Total de notícias: {len(news_items)}")


if __name__ == "__main__":
    main()
