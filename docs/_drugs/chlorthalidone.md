---
layout: default
title: Chlorthalidone
parent: 僅模型預測 (L5)
nav_order: 185
evidence_level: L5
indication_count: 10
---

# Chlorthalidone
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

Usando o skill `txgnn-pipeline` para contextualizar e gerando o relatório de avaliação de reposicionamento conforme o formato prescrito:

---

# Clortalidona: Da Hipertensão ao Cor Pulmonale Crônico

## Resumo em Uma Frase

Clortalidona é um diurético tiazídico-símile com uso consagrado no tratamento da hipertensão arterial e edema sistêmico.
O modelo TxGNN prevê que pode ser eficaz para **Doença Cardíaca Pulmonar Crônica (Chronic Pulmonary Heart Disease / Cor Pulmonale)** — a indicação com maior suporte clínico dentre as 10 previsões analisadas neste pacote, com **1 observação clínica direta** (PMID 5597001) e **2 publicações de suporte histórico** identificadas.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Hipertensão arterial e edema (uso farmacológico consagrado; sem registros ANVISA ativos) |
| Nova Indicação Prevista | Doença Cardíaca Pulmonar Crônica (Chronic Pulmonary Heart Disease) |
| Pontuação de Previsão TxGNN | 99.82% |
| Nível de Evidência | L3 |
| Situação no Mercado Brasileiro | Não comercializado |
| Número de Registros | 0 |
| Decisão Recomendada | Hold |

---

## Por que Esta Previsão é Razoável?

Atualmente, não há dados formais de mecanismo de ação no Evidence Pack (DG002). Com base no conhecimento farmacológico estabelecido, clortalidona é um diurético da classe tiazídico-símile que inibe o cotransportador sódio-cloreto (NCC) no túbulo contorcido distal renal, promovendo excreção de sódio e água, redução da volemia e queda sustentada da pressão arterial — ação com meia-vida longa (40–60 horas), diferenciando-a dos tiazídicos convencionais.

A doença cardíaca pulmonar crônica (cor pulmonale) é caracterizada por disfunção e dilatação do ventrículo direito secundária à hipertensão pulmonar crônica, frequentemente associada a DPOC ou fibrose pulmonar. Nesses pacientes, congestão sistêmica com edema periférico, ascite e ingurgitamento jugular são manifestações prevalentes da insuficiência cardíaca direita descompensada. O mecanismo diurético da clortalidona — redução da pré-carga venosa e alívio da sobrecarga hídrica — possui coerência fisiopatológica direta com o quadro clínico.

Dentre as 10 indicações previstas pelo TxGNN neste pacote, o cor pulmonale crônico é a única com evidência clínica direta: o estudo PMID 5597001 (1967) relata uso de clortalidona em insuficiência cardíaca congestiva causada por cor pulmonale crônico, com eficácia diurética observada. Embora o estudo seja historicamente datado e os diuréticos de alça (furosemida) sejam atualmente preferidos nas diretrizes, o papel adjuvante dos tiazídicos em casos refratários permanece uma questão de pesquisa legítima, sem exploração por estudos controlados modernos.

---

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos com clortalidona em doença cardíaca pulmonar crônica registrados.

> **Nota:** O ensaio NCT05580510 (Empagliflozin + Sacubitril/Valsartan em insuficiência cardíaca associada a cardiopatia congênita) foi recuperado pelo sistema de busca no contexto desta patologia, mas não investiga clortalidona e possui status UNKNOWN. Relevância grau C — não incluído na análise principal.

---

## Evidências da Literatura

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [5597001](https://pubmed.ncbi.nlm.nih.gov/5597001/) | 1967 | Observação Clínica | La Clinica Terapeutica | **Evidência direta:** relato de uso de clortalidona em insuficiência cardíaca congestiva causada por cor pulmonale crônico, com observação de eficácia diurética |
| [431831](https://pubmed.ncbi.nlm.nih.gov/431831/) | 1979 | Observação Clínica | Minerva Medica | Terapia de depleção (incluindo diuréticos) reverteu alterações radiológicas em 5 pacientes com doença broncopulmonar crônica e "pulmão úmido"; sugere papel da descompressão hídrica pulmonar |
| [28711447](https://pubmed.ncbi.nlm.nih.gov/28711447/) | 2017 | Review | JACC Heart Failure | Revisão da transição hipertensão → insuficiência cardíaca; remodelamento cardíaco por sobrecarga pressórica e implicações terapêuticas — contexto de fundo relevante |

---

## Informações de Comercialização no Brasil

Clortalidona **não possui registros ativos na ANVISA** e não está comercializada no mercado brasileiro.

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
A única evidência clínica direta disponível (PMID 5597001) é uma observação histórica de 1967, sem delineamento controlado adequado aos padrões contemporâneos de evidência. A coerência mecanística é sólida, mas o conjunto de dados — ausência de ensaios clínicos modernos, fármaco não registrado no Brasil e lacunas críticas de segurança (DG001, DG002) — não justifica avanço imediato para uso clínico.

**Para prosseguir, é necessário:**
- Preencher as lacunas de dados críticos: MOA completo via DrugBank (DG002) e advertências/contraindicações via ANVISA/bula (DG001)
- Realizar revisão sistemática sobre tiazídicos como adjuvantes ao tratamento da insuficiência cardíaca direita e cor pulmonale
- Avaliar perfil de segurança específico: risco de hipocalemia e hiponatremia em pacientes com DPOC e hipoxemia crônica
- Investigar potencial interação farmacodinâmica com diuréticos de alça em regime combinado
- Avaliar viabilidade de protocolo de pesquisa prospectivo (ex.: tiazídico vs. placebo como adjuvante em cor pulmonale com edema refratário à furosemida)
- Verificar necessidade de registro ANVISA antes de qualquer ensaio clínico no Brasil
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

