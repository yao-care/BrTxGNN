"""
Módulos de coleta de notícias para monitoramento de saúde no Brasil.

Fetchers disponíveis:
- google_rss: Google News Brasil (Saúde e Ciência)
"""

from .google_rss import fetch_google_news_brazil

__all__ = ["fetch_google_news_brazil"]
