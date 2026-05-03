---
layout: default
title: Deferasirox
parent: 僅模型預測 (L5)
nav_order: 212
evidence_level: L5
indication_count: 5
---

# Deferasirox
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

Using the `txgnn-pipeline` skill for context. Now proceeding to generate the report from the Evidence Pack.

---

# Deferasirox: Da quelação crônica de ferro à infecção por HIV

## Resumo em Uma Frase

Deferasirox é um quelante de ferro oral aprovado para o tratamento da sobrecarga crônica de ferro decorrente de transfusões sanguíneas frequentes.
O modelo TxGNN prevê que pode ser eficaz para **Infecção por HIV (HIV Infectious Disease)**,
atualmente com **0 ensaios clínicos** e **2 publicações** apoiando esta direção.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|----------|
| Indicação Original | Sobrecarga crônica de ferro por transfusões sanguíneas repetidas |
| Nova Indicação Prevista | Infecção por HIV (HIV Infectious Disease) |
| Pontuação de Previsão TxGNN | 99,40% |
| Nível de Evidência | L4 |
| Situação no Mercado Brasileiro | ✓ Comercializado |
| Número de Registros | 10 |
| Decisão Recomendada | Hold |

---

## Por que Esta Previsão é Razoável?

Deferasirox é um quelante de ferro oral tridentado que forma complexos estáveis e de alta afinidade com Fe³⁺, promovendo sua excreção predominantemente pelas fezes. Clinicamente, é o tratamento padrão para a sobrecarga de ferro transfusional em pacientes com talassemia, anemia falciforme e síndromes mielodisplásicas que necessitam de suporte transfusional crônico.

A ligação mecanicista com o HIV baseia-se no papel essencial que o ferro desempenha no ciclo replicativo do vírus. O Fe³⁺ é cofator da ribonucleotídeo redutase viral e regula a conformação ativa da proteína transativadora Tat do HIV-1. O estudo PMID 34550543 demonstrou in vitro que o ferro armazenado em endolisossomas controla a oligomerização da proteína Tat: ao restringir o ferro endolisossomal, induz-se a oligomerização do Tat e, consequentemente, a inibição da transativação do promotor LTR do HIV-1 — este sendo o gatilho central da replicação viral. Trata-se de um downstream direto e plausível da quelação intracelular de ferro mediada por deferasirox.

No entanto, a evidência permanece exclusivamente em nível in vitro e em contexto neurológico (HAND — HIV-associated neurocognitive disorder). A aplicação clínica enfrenta barreiras relevantes: deferasirox apresenta penetração no sistema nervoso central inferior a 1%; não existem modelos animais validando o efeito antiviral sistêmico; e não há qualquer ensaio clínico registrado. A hipótese é biologicamente plausível, mas a distância translacional é considerável.

---

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados.

---

## Evidências da Literatura

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|-----------|-------------------|
| [34550543](https://pubmed.ncbi.nlm.nih.gov/34550543/) | 2021 | Estudo mecanicista in vitro | Journal of Neurovirology | O ferro endolisossomal regula a oligomerização do HIV-1 Tat e suprime a transativação do LTR; a limitação do ferro intracelular (mecanismo compatível com deferasirox) reduz a replicação viral in vitro |
| [16529348](https://pubmed.ncbi.nlm.nih.gov/16529348/) | 2006 | Revisão / Comentário farmacêutico | J Am Pharmacists Assoc (JAPhA) | Revisão introdutória de deferasirox como novo fármaco aprovado; não apresenta dados de eficácia anti-HIV, mas contextualiza o perfil farmacológico do fármaco |

---

## Informações de Comercialização no Brasil

Deferasirox está registrado no Brasil com **10 registros ativos** e situação de comercialização confirmada. Os detalhes individuais dos registros (número, nome comercial, forma farmacêutica, indicação aprovada) não estão disponíveis neste conjunto de dados. Para consulta completa dos registros, acesse o portal de consulta de medicamentos da ANVISA.

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
As únicas evidências disponíveis são um estudo mecanicista in vitro realizado em modelo de neurotoxicidade por HIV e um comentário farmacêutico introdutório de 2006, sem qualquer ensaio clínico registrado em nenhuma base global. Embora a hipótese de que a quelação de ferro intracelular interfira na replicação do HIV-1 seja biologicamente coerente, o nível de evidência atual (L4) e as barreiras farmacocinéticas conhecidas (baixa penetração em SNC, ausência de dados em células imunes) não justificam avanço imediato.

**Para prosseguir, é necessário:**
- Validação em modelos animais do efeito de deferasirox sobre a carga viral do HIV-1 (murino ou primata não humano)
- Estudos de distribuição intracelular em linfócitos CD4⁺ e macrófagos — células-alvo primárias do HIV
- Obtenção do mecanismo de ação completo via DrugBank (lacuna DG002)
- Obtenção de advertências, contraindicações e interações via bula oficial da ANVISA (lacuna DG001 — nível Blocking)
- Avaliação de interações farmacológicas com antirretrovirais de uso concomitante habitual (ITRN, ITRNN, IP, inibidores de integrase)
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

