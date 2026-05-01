---
layout: default
title: Captopril
parent: 僅模型預測 (L5)
nav_order: 163
evidence_level: L5
indication_count: 4
---

# Captopril
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
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

# Captopril: Da hipertensão arterial à doença renal hipertensiva maligna

## Resumo em Uma Frase

Captopril é um inibidor da enzima conversora de angiotensina (IECA), originalmente utilizado no tratamento da hipertensão arterial e insuficiência cardíaca.
O modelo TxGNN prevê que pode ser eficaz para **Doença Renal Hipertensiva Maligna (Malignant Hypertensive Renal Disease)**,
atualmente com **0 ensaios clínicos** e **1 publicação** apoiando esta direção.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Hipertensão arterial, insuficiência cardíaca |
| Nova Indicação Prevista | Doença Renal Hipertensiva Maligna (Malignant Hypertensive Renal Disease) |
| Pontuação de Previsão TxGNN | 99.28% |
| Nível de Evidência | L4 |
| Situação no Mercado Brasileiro | ✓ Comercializado |
| Número de Registros | 20 |
| Decisão Recomendada | Hold |

---

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação disponíveis no Evidence Pack. Segundo informações farmacológicas estabelecidas, Captopril é um inibidor competitivo da enzima conversora de angiotensina (ECA), que bloqueia a conversão de angiotensina I em angiotensina II (Ang II) e inibe a degradação de bradicinina. Sua eficácia no controle da hipertensão arterial e na proteção cardiorrenal foi amplamente comprovada ao longo de décadas de uso clínico.

A patologia da doença renal hipertensiva maligna é impulsionada pela hiperativação do sistema renina-angiotensina (SRA), no qual a Ang II em excesso induz espasmo das arteríolas aferentes e eferentes, culminando em necrose fibrinoide e lesão isquêmica renal acelerada. O bloqueio da ECA por Captopril reduz diretamente os níveis de Ang II, conferindo teoricamente um efeito nefroprotetor e anti-hipertensivo direcionado ao mecanismo central desta doença.

Contudo, existe uma ressalva clínica importante: em pacientes com estenose arterial renal bilateral ou rim único funcionante, a pressão de filtração glomerular depende da vasoconstrição mediada por Ang II na arteríola eferente. O uso de IECA nesse subgrupo pode precipitar insuficiência renal aguda grave. A indicação, portanto, exige triagem cuidadosa da anatomia vascular renal e monitoramento rigoroso da função renal antes e após o início do tratamento.

---

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados.

---

## Evidências da Literatura

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [28902735](https://pubmed.ncbi.nlm.nih.gov/28902735/) | 2017 | Case Report | Clinical Nuclear Medicine | Relato de cintilografia renal com Captopril positiva sem estenose de artéria renal, mas com carcinoma de células renais cromófobo volumoso. A hipertensão renina-dependente foi resolvida após nefrectomia, ilustrando que a positividade ao Captopril pode ocorrer em contextos de hipertensão mediada por renina além da estenose clássica. |

---

## Informações de Comercialização no Brasil

O Evidence Pack confirma **20 registros ativos** junto à ANVISA com status de comercialização vigente. Os detalhes individuais dos registros (número, nome comercial, forma farmacêutica, indicação aprovada) não estão disponíveis no pacote de dados atual e deverão ser obtidos diretamente no portal da ANVISA.

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
As evidências disponíveis para a indicação de doença renal hipertensiva maligna limitam-se a um único relato de caso (nível L4), sem ensaios clínicos registrados. Embora a conexão mecanística entre a inibição da ECA e a patologia do SRA seja racionalmente sólida, o risco de insuficiência renal aguda em subgrupos com comprometimento vascular renal constitui uma barreira de segurança que impede progressão imediata.

**Para prosseguir, é necessário:**
- Obter dados completos de MOA e perfil de segurança via consulta ao DrugBank API (DG002)
- Baixar e analisar o PDF da bula oficial da ANVISA para advertências e contraindicações (DG001)
- Realizar busca sistemática por estudos observacionais e séries de casos de Captopril em hipertensão maligna com nefropatia
- Definir critérios de exclusão formais para pacientes com estenose arterial renal bilateral ou rim único
- Avaliar os dados de evidência L3 disponíveis para a indicação relacionada **Malignant Renovascular Hypertension** (Rank 2, 20 publicações, recomendação *Proceed with Guardrails*), que pode oferecer base mecanística comparável com suporte bibliográfico mais robusto para embasar um redesenho da estratégia de investigação
---

