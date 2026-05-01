---
layout: default
title: Bevacizumab
parent: 僅模型預測 (L5)
nav_order: 116
evidence_level: L5
indication_count: 10
---

# Bevacizumab
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

# Bevacizumab: De múltiplos cânceres sólidos ao neoplasma da epiglote

## Resumo em Uma Frase

Bevacizumab é um anticorpo monoclonal anti-VEGF aprovado para o tratamento de diversos cânceres sólidos (incluindo carcinoma colorretal, pulmonar e ovariano), atuando pela inibição da angiogênese tumoral. O modelo TxGNN prevê que pode ser eficaz para **Neoplasma da Epiglote (Epiglottis Neoplasm)**, com pontuação de previsão de **99,90%**, porém atualmente **sem nenhum ensaio clínico nem publicação científica** específica apoiando esta direção — trata-se de previsão puramente computacional.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Tratamento de cânceres sólidos (carcinoma colorretal, pulmonar, ovariano, entre outros) |
| Nova Indicação Prevista | Neoplasma da Epiglote (Epiglottis Neoplasm) |
| Pontuação de Previsão TxGNN | 99,90% |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | ✓ Comercializado |
| Número de Registros | 12 |
| Decisão Recomendada | Hold |

---

## Por que Esta Previsão é Razoável?

Bevacizumab atua bloqueando o VEGF-A (Fator de Crescimento do Endotélio Vascular A), suprimindo a formação de novos vasos sanguíneos que nutrem tumores — mecanismo conhecido como antiangiogênese. Esta ação é a base de sua eficácia comprovada em múltiplos tipos de câncer e justifica sua inclusão nas diretrizes oncológicas internacionais para carcinoma colorretal, câncer de pulmão de células não pequenas, carcinoma ovariano e outros tumores sólidos com alta dependência vascular.

Os tumores da epiglote estão situados na região da cabeça e pescoço, contexto anatômico onde a superexpressão de VEGF foi documentada em outros sítios adjacentes — como o carcinoma escamocelular de cabeça e pescoço (HNSCC). Nesse sentido, há plausibilidade teórica de que neoplasmas da epiglote possam compartilhar o perfil de dependência de VEGF observado em neoplasias da mesma região, o que o modelo TxGNN captura ao analisar padrões de similaridade entre doenças no grafo de conhecimento.

No entanto, esta previsão é estritamente computacional (L5): não existem dados publicados de expressão de VEGF em tumores de epiglote, nenhum ensaio clínico avaliou Bevacizumab neste sítio específico, e não há evidências pré-clínicas diretas. A raridade desta neoplasia e a ausência de dados moleculares tornam a extrapolação altamente incerta no estado atual do conhecimento.

---

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados.

---

## Evidências da Literatura

Atualmente não há literatura relacionada.

---

## Citotoxicidade

| Item | Conteúdo |
|------|------|
| Classificação de Citotoxicidade | Terapia alvo — anticorpo monoclonal anti-VEGF (não é agente citotóxico convencional) |
| Risco de Mielossupressão | Baixo (Bevacizumab isolado não causa mielossupressão direta; o risco aumenta quando combinado com quimioterapia convencional) |
| Classificação de Emetogenicidade | Baixa (mínimo potencial emetogênico como agente único) |
| Itens de Monitoramento | Pressão arterial (hipertensão é efeito adverso frequente), proteinúria (urinálise periódica), função renal, avaliação de cicatrização de feridas, sinais de sangramento e tromboembolismo |
| Proteção no Manuseio | Seguir procedimentos padrão para biológicos e anticorpos monoclonais; preparação em ambiente controlado conforme regulamentação vigente |

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
A previsão do TxGNN para neoplasma da epiglote não possui nenhum suporte empírico — a ausência total de ensaios clínicos, dados pré-clínicos, literatura científica e informações sobre expressão de VEGF neste tumor específico impede qualquer avanço responsável sem estudos exploratórios preliminares.

**Para prosseguir, é necessário:**
- Estudos de expressão de VEGF/VEGFR em amostras anatomopatológicas de neoplasmas da epiglote
- Modelos pré-clínicos (in vitro e xenoenxerto) para validar atividade antitumoral neste sítio
- Perfil de segurança completo por meio da bula oficial registrada na ANVISA (Gap DG001)
- Dados formalizados de mecanismo de ação via DrugBank API (Gap DG002)
- Detalhamento dos 12 registros na ANVISA (nome comercial, forma farmacêutica, indicação aprovada)
- Considerar como alternativa prioritária o **Neoplasma Cístico (Rank 7, Nível L1)**, que dispõe de ensaio Phase 3 RCT (n=1.052) e 20 publicações com recomendação **Proceed with Guardrails**
---

