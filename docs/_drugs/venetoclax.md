---
layout: default
title: Venetoclax
parent: 僅模型預測 (L5)
nav_order: 503
evidence_level: L5
indication_count: 10
---

# Venetoclax
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

Usando o **txgnn-pipeline** para orientar a produção do relatório de avaliação de repositionamento.

---

# Venetoclax: Da leucemia linfocítica crônica ao subtipo CLL/SLL com hipermutação IGHV

## Resumo em Uma Frase

Venetoclax é um inibidor seletivo de BCL-2 (BH3-mimético), aprovado internacionalmente para o tratamento da leucemia linfocítica crônica/linfoma linfocítico pequeno (CLL/SLL) e leucemia mieloide aguda (AML) — indicações sustentadas por múltiplos ensaios clínicos de Fase 3.
O modelo TxGNN prevê que pode ser eficaz para o subtipo específico **CLL/SLL com hipermutação somática IGHV (IGHV-mutated CLL/SLL)**, atualmente sem **ensaios clínicos dedicados** e sem **publicações** específicas para este subgrupo molecular.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Dados de indicação aprovada não disponíveis no registro consultado |
| Nova Indicação Prevista | CLL/SLL com hipermutação IGHV (*IGHV-mutated CLL/SLL*) |
| Pontuação de Previsão TxGNN | 99,55% |
| Nível de Evidência | L4 |
| Situação no Mercado Brasileiro | ✓ Comercializado |
| Número de Registros | 1 |
| Decisão Recomendada | Hold |

---

## Por que Esta Previsão é Razoável?

Venetoclax atua bloqueando seletivamente a proteína anti-apoptótica BCL-2, impedindo que ela sequestre as proteínas pró-apoptóticas BAX e BAK. Ao liberar essas proteínas, o fármaco restaura a morte celular programada pela via mitocondrial (apoptose intrínseca) em células tumorais que dependem da superexpressão de BCL-2 para sobreviver — mecanismo que define a classe dos miméticos BH3.

Na CLL/SLL, a superexpressão de BCL-2 é uma característica molecular praticamente universal e independe do status mutacional IGHV. O subtipo previsto — **CLL/SLL IGHV-mutado** — corresponde ao subconjunto de células B tumorais que carregam marcas de terem passado pelo centro germinativo, o que confere prognóstico geralmente mais favorável em relação ao subtipo pré-germinal (IGHV não-mutado). Em ambos os subtipos, a dependência a BCL-2 como mecanismo central de sobrevivência permanece biologicamente relevante e clinicamente explorável.

Os grandes ensaios de referência de venetoclax em CLL — como o **MURANO** (Phase 3, venetoclax + rituximabe em CLL recidivada/refratária) e o **CLL14** (Phase 3, venetoclax + obinutuzumabe em CLL não tratada) — já incluíram pacientes com IGHV-mutado em suas populações, com benefício clínico demonstrado neste subgrupo. A previsão do TxGNN, portanto, reflete uma sub-especificação molecular dentro de uma indicação já estabelecida, e não um repositionamento para uma doença inteiramente nova. Para caracterizar o diferencial de eficácia e o potencial de remissão livre de tratamento (TFR) neste subtipo específico, análises de subgrupo nos estudos existentes são necessárias.

---

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados especificamente para CLL/SLL com hipermutação IGHV.

---

## Evidências da Literatura

Atualmente não há literatura relacionada específica para esta subpopulação.

---

## Informações de Comercialização no Brasil

Os dados detalhados do registro (número de registro, nome comercial, forma farmacêutica e indicação aprovada) não estão disponíveis na base de dados consultada. Venetoclax consta como **comercializado no Brasil** com **1 registro ativo** junto à ANVISA.

---

## Citotoxicidade

| Item | Conteúdo |
|------|------|
| Classificação de Citotoxicidade | Terapia alvo — Inibidor seletivo de BCL-2 (classe BH3-mimético); não é citotóxico convencional |
| Risco de Mielossupressão | Médio — Linfopenia é o achado mais frequente; neutropenia grau ≥3 ocorre em ~20–30% dos pacientes em esquemas combinados; trombocitopenia e anemia possíveis |
| Classificação de Emetogenicidade | Baixa |
| Itens de Monitoramento | Hemograma completo com diferencial; função renal (creatinina); eletrólitos (K⁺, Ca²⁺, PO₄³⁻); ácido úrico — monitoramento rigoroso para **Síndrome de Lise Tumoral (TLS)**, especialmente na fase de ramp-up de dose |
| Proteção no Manuseio | Seguir protocolos institucionais para manuseio de agentes antineoplásicos orais |

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
O subtipo CLL/SLL IGHV-mutado já está contido nas populações dos ensaios clínicos de Fase 3 aprovados de venetoclax em CLL (MURANO, CLL14), não configurando um repositionamento independente; a previsão do TxGNN representa uma sub-especificação molecular da indicação existente, sem lacuna clínica não coberta que justifique prioridade de desenvolvimento.

**Para prosseguir, é necessário:**
- Análises de subgrupo estratificadas por status IGHV nos ensaios MURANO, CLL14 e GAIA/CLL13 para quantificar o diferencial de eficácia
- Avaliação da taxa de negatividade para MRD (doença residual mínima) e potencial de remissão livre de tratamento (TFR) estratificada por IGHV-mutado vs. não-mutado
- Confirmação dos dados de registro da ANVISA: número de registro, nome comercial, indicação aprovada completa e posologia
- Recuperação dos dados de MOA e de advertências/contraindicações a partir da bula registrada na ANVISA (DG001 e DG002 pendentes)
---

