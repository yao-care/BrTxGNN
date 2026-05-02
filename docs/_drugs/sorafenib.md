---
layout: default
title: Sorafenib
parent: 僅模型預測 (L5)
nav_order: 448
evidence_level: L5
indication_count: 10
---

# Sorafenib
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Sorafenib: Do carcinoma hepatocelular ao lipossarcoma

## Resumo em Uma Frase

Sorafenib (Nexavar®) é um inibidor oral de multicinase aprovado para o tratamento de carcinoma hepatocelular avançado, carcinoma de células renais e carcinoma diferenciado de tireoide.
O modelo TxGNN prevê que pode ser eficaz para **Lipossarcoma (Liposarcoma)**, com **2 ensaios clínicos** — incluindo 1 estudo de Fase 2 que avaliou diretamente Sorafenib em sarcomas de partes moles avançados — apoiando esta direção.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Carcinoma hepatocelular avançado; carcinoma de células renais; carcinoma diferenciado de tireoide |
| Nova Indicação Prevista | Lipossarcoma (Liposarcoma) |
| Pontuação de Previsão TxGNN | 99.82% |
| Nível de Evidência | L3 |
| Situação no Mercado Brasileiro | ✓ Comercializado |
| Número de Registros | 4 |
| Decisão Recomendada | Hold |

---

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação disponíveis neste Evidence Pack. Com base nas informações conhecidas, Sorafenib é um inibidor oral de multicinase que bloqueia simultaneamente múltiplos receptores de tirosina quinase — VEGFR-1/2/3, PDGFR-β, KIT, FLT-3, RET — e membros da família RAF (Raf-1, B-RAF). Esses dois eixos de atuação interrompem tanto a proliferação direta das células tumorais quanto a formação de novos vasos que nutrem o tumor. Sua eficácia em carcinoma hepatocelular, carcinoma de células renais e carcinoma diferenciado de tireoide está amplamente estabelecida.

Lipossarcomas frequentemente apresentam sobreexpressão de PDGFR e amplificações de CDK4/MDM2. A inibição de VEGFR/PDGFR-β pelo Sorafenib interfere diretamente na angiogênese tumoral e na sinalização do estroma mesenquimal; a inibição da via RAF/MEK/ERK acrescenta uma base antiproliferativa adicional. Essa sobreposição de alvos moleculares — compartilhada entre as indicações já aprovadas e o lipossarcoma — torna a hipótese de reposicionamento mecanisticamente plausível.

O ensaio NCT00217620 (Fase 2, concluído, n=51) avaliou diretamente Sorafenib em sarcomas de partes moles avançados, categoria que inclui o lipossarcoma como subtipo histológico. Esse estudo constitui o principal pilar de evidência clínica disponível até o momento. A confirmação de eficácia específica no subgrupo lipossarcoma — a partir dos dados publicados desse ensaio — é o próximo passo crítico para justificar progressão.

---

## Evidências de Ensaios Clínicos

| Número do Ensaio | Fase | Status | Participantes | Principais Achados |
|---------|------|------|------|---------|
| [NCT00217620](https://clinicaltrials.gov/study/NCT00217620) | Phase 2 | Concluído | 51 | Sorafenib (BAY-9006) avaliado em sarcomas de partes moles avançados; estuda o bloqueio de enzimas necessárias ao crescimento celular e a inibição do fluxo sanguíneo tumoral — inclui lipossarcoma como subtipo histológico elegível |
| [NCT02048371](https://clinicaltrials.gov/study/NCT02048371) | Phase 2 | Concluído | 131 | **Regorafenib** (não Sorafenib) em subtipos selecionados de sarcoma; destaca precedente histórico de atividade de Sorafenib em osteossarcoma — evidência indireta de classe, não aplicável diretamente |

---

## Evidências da Literatura

Atualmente não há literatura relacionada a Sorafenib + lipossarcoma registrada neste Evidence Pack.

---

## Informações de Comercialização no Brasil

Sorafenib possui **4 registros ativos** no Brasil. Os detalhes individuais de cada registro (número, nome comercial, forma farmacêutica e texto da indicação aprovada) não estão disponíveis nos dados processados deste Evidence Pack. Para consulta completa, acesse o portal da ANVISA: [https://consultas.anvisa.gov.br/](https://consultas.anvisa.gov.br/)

---

## Citotoxicidade

Sorafenib é um agente antineoplásico de uso sistêmico. Esta seção se aplica.

| Item | Conteúdo |
|------|------|
| Classificação de Citotoxicidade | Terapia alvo — inibidor oral de multicinase (classe dos inibidores de tirosina quinase) |
| Risco de Mielossupressão | Baixo a médio (menos mielossupressivo que quimioterapia citotóxica convencional; leucopenia e trombocitopenia podem ocorrer) |
| Classificação de Emetogenicidade | Baixa (agente oral; náuseas e vômitos possíveis, porém geralmente de baixo grau) |
| Itens de Monitoramento | Pressão arterial, hemograma completo (CBC), provas de função hepática (ALT, AST, bilirrubina), TSH, eletrólitos séricos, lipase pancreática |
| Proteção no Manuseio | Manejo como antineoplásico oral; uso de luvas ao manipular comprimidos; seguir protocolos institucionais para medicamentos citotóxicos |

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
Existe 1 ensaio clínico de Fase 2 concluído (NCT00217620) que avalia diretamente Sorafenib em sarcomas de partes moles — categoria que inclui o lipossarcoma — mas os dados de eficácia específicos para esse subtipo histológico ainda não foram confirmados a partir dos resultados publicados. A ausência de literatura dedicada e a indisponibilidade de dados de segurança da bula ANVISA impedem a progressão imediata.

**Para prosseguir, é necessário:**
- Recuperar e confirmar os resultados do subgrupo lipossarcoma no NCT00217620
- Obter dados detalhados do mecanismo de ação (MOA) via DrugBank API
- Verificar advertências, contraindicações e interações medicamentosas na bula ANVISA (DG001 — Blocking)
- Recuperar os detalhes dos 4 registros ANVISA (número, nome comercial, indicações aprovadas)
- Definir hipótese de pesquisa formal e desenho de estudo de Fase 2 específico para lipossarcoma com Sorafenib, caso os dados do NCT00217620 confirmem atividade no subgrupo
---

