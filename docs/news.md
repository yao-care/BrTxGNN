---
layout: default
title: Notícias de Saúde
nav_order: 8
description: "Monitoramento de notícias de saúde relacionadas a reposicionamento de medicamentos."
permalink: /news/
---

# Notícias de Saúde

<div class="key-takeaway">
Monitoramento automático de notícias de saúde do Brasil relacionadas aos medicamentos e indicações do BrTxGNN.
</div>

---

## Fontes Monitoradas

| Fonte | Descrição | Frequência |
|-------|-----------|------------|
| Google News Brasil | Notícias de saúde em português | A cada hora |
| Google News Ciência | Notícias de pesquisa científica | A cada hora |

---

## Categorias

### Notícias Relacionadas a Medicamentos

Notícias que mencionam medicamentos monitorados pelo BrTxGNN:
- Novos usos terapêuticos
- Resultados de ensaios clínicos
- Aprovações regulatórias

### Notícias Relacionadas a Doenças

Notícias sobre as indicações previstas:
- Avanços em tratamentos
- Descobertas científicas
- Novas terapias

---

## Como Funciona

1. **Coleta**: Google News RSS é monitorado a cada hora
2. **Matching**: Notícias são comparadas com palavras-chave de medicamentos e doenças
3. **Relevância**: Notícias relevantes são destacadas
4. **Arquivo**: Histórico mantido para referência

---

## Últimas Notícias

<div class="disclaimer">
O monitoramento de notícias será ativado após a execução das previsões do modelo e geração das palavras-chave.
</div>

Para configurar o monitoramento:

```bash
# Gerar palavras-chave
uv run python scripts/generate_news_keywords.py

# Executar fetcher de notícias
uv run python scripts/fetchers/google_rss.py
```

---

## Alertas

Você pode acompanhar novos achados através do GitHub:

- **Issues Automáticas**: Criadas quando novas evidências são encontradas
- **Rótulos**: `auto-detected`, `needs-review`, `clinicaltrials`, `pubmed`

[Ver Issues Abertas](https://github.com/yao-care/BrTxGNN/issues?q=is%3Aopen+label%3Aauto-detected){: .btn .btn-primary }

---

## Isenção de Responsabilidade

<div class="disclaimer">
<strong>Aviso</strong><br>
As notícias são coletadas automaticamente e não são verificadas editorialmente. Sempre verifique as fontes originais antes de tomar qualquer decisão com base nestas informações.
</div>
