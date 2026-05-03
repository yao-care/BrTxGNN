---
layout: default
title: Aripiprazole
parent: 僅模型預測 (L5)
nav_order: 70
evidence_level: L5
indication_count: 10
---

# Aripiprazole
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

# Aripiprazole: Da esquizofrenia ao transtorno afetivo maior

## Resumo em Uma Frase

Aripiprazole é um antipsicótico atípico de segunda geração reconhecido internacionalmente pelo tratamento de esquizofrenia e transtorno bipolar, porém **sem qualquer registro junto à ANVISA** no Brasil.
O modelo TxGNN prevê que pode ser eficaz para **Transtorno Afetivo Maior (Major Affective Disorder)**, com **mais de 10 ensaios clínicos de Fase 3/4 concluídos** apoiando diretamente essa indicação.
A ausência de registro nacional representa uma oportunidade concreta de reposicionamento, visto que a evidência clínica internacional já atingiu nível L1.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Esquizofrenia e transtorno bipolar (aprovação internacional; sem registro ANVISA) |
| Nova Indicação Prevista | Transtorno Afetivo Maior (Major Affective Disorder) |
| Pontuação de Previsão TxGNN | 99,62% |
| Nível de Evidência | L1 |
| Situação no Mercado Brasileiro | Não comercializado |
| Número de Registros ANVISA | 0 |
| Decisão Recomendada | Proceed with Guardrails |

---

## Por que Esta Previsão é Razoável?

Aripiprazole pertence à classe dos antipsicóticos atípicos de segunda geração e possui um perfil farmacológico multimodal distinto. Embora dados detalhados do MOA não estejam disponíveis no pacote de evidências atual, com base no conhecimento farmacológico consolidado, sabe-se que o aripiprazole atua como **agonista parcial dos receptores D2/D3 de dopamina e do receptor 5-HT1A de serotonina**, além de **antagonista do receptor 5-HT2A**. Este perfil — único entre os antipsicóticos, que em geral são antagonistas puros de D2 — permite estabilizar os circuitos dopaminérgicos e serotoninérgicos de forma modulada, sem bloqueio total, o que é especialmente relevante para os transtornos do humor.

O transtorno afetivo maior engloba condições como o transtorno depressivo maior (TDM) e o transtorno bipolar, ambos caracterizados por desregulação dos sistemas dopaminérgico e serotoninérgico — exatamente os alvos primários do aripiprazole. A sobreposição fisiopatológica entre os transtornos psicóticos (indicação de origem) e os transtornos afetivos maiores é amplamente reconhecida, com circuitos mesolímbicos e córtico-prefrontais compartilhados. O agonismo parcial em 5-HT1A, em particular, está associado à redução da ansiedade e da anedonia, sintomas centrais na depressão maior.

No contexto internacional, o aripiprazole já possui aprovação pelo FDA (EUA) como **terapia adjuvante ao antidepressivo em TDM** e para o **tratamento do transtorno bipolar tipo I** — indicações que compõem diretamente o espectro de "transtorno afetivo maior". A inexistência de registro na ANVISA não reflete uma lacuna científica, mas sim uma lacuna regulatória de acesso. Os ensaios clínicos de Fase 3 identificados, com milhares de participantes, confirmam esta indicação com o mais alto nível de evidência disponível.

---

## Evidências de Ensaios Clínicos

| Número do Ensaio | Fase | Status | Participantes | Principais Achados |
|---------|------|------|------|---------|
| [NCT00095823](https://clinicaltrials.gov/study/NCT00095823) | Phase 3 | Concluído | 1.200 | Estudo duplo-cego, placebo-controlado de 14 semanas avaliando segurança e eficácia de aripiprazole como adjuvante a antidepressivo em curso em pacientes com TDM |
| [NCT00876343](https://clinicaltrials.gov/study/NCT00876343) | Phase 3 | Concluído | 586 | Aripiprazole vs placebo como adjuvante de ISRS/IRSN em TDM; confirmou eficácia e tolerabilidade da terapia combinada |
| [NCT02046564](https://clinicaltrials.gov/study/NCT02046564) | Phase 3 | Concluído | 412 | Combinação ASC-01 (aripiprazole + sertralina) vs sertralina em monoterapia em TDM com resposta incompleta ao antidepressivo |
| [NCT00683852](https://clinicaltrials.gov/study/NCT00683852) | Phase 3 | Concluído | 225 | Aripiprazole em dose reduzida como adjuvante a antidepressivo em TDM com resposta inadequada; investigou perfil de dose-resposta |
| [NCT00882362](https://clinicaltrials.gov/study/NCT00882362) | Phase 3 | Concluído | 155 | Administração de longo prazo de aripiprazole adjuvante a ISRS/IRSN em TDM; avaliou segurança e eficácia sustentada |
| [NCT00277212](https://clinicaltrials.gov/study/NCT00277212) | Phase 4 | Concluído | 1.169 | Aripiprazole em combinação com lamotrigina no tratamento de manutenção de longo prazo do transtorno bipolar I com episódio maníaco ou misto recente |
| [NCT02305823](https://clinicaltrials.gov/study/NCT02305823) | Phase 4 | Concluído | 203 | Comparação direta de efetividade de aripiprazole, quetiapina e ziprasidona no primeiro episódio psicótico não-afetivo (estudo PAFIP II) |
| [NCT03423680](https://clinicaltrials.gov/study/NCT03423680) | Phase 3 | Em andamento | 390 | Aripiprazole (Abilify®) adjuvante a estabilizador do humor em episódio depressivo maior associado a transtorno bipolar I ou II sem características psicóticas |
| [NCT01386086](https://clinicaltrials.gov/study/NCT01386086) | Phase 3 | Concluído | 10 | Aripiprazole como terapia de aumento em depressão pós-parto resistente a antidepressivos; forneceu dados iniciais de segurança nesta subpopulação |
| [NCT07153406](https://clinicaltrials.gov/study/NCT07153406) | Phase 3 | Ainda não iniciado | 220 | Comparação de esketamina nasal vs aripiprazole (ambos + ISRS/IRSN) em TDM resistente em idosos (>60 anos); início previsto para setembro de 2025 |

---

## Evidências da Literatura

Atualmente não há literatura relacionada disponível no banco de dados para esta combinação fármaco-indicação.

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

> **Nota:** Os dados de advertências, contraindicações e interações medicamentosas não estão disponíveis no pacote de evidências atual. Recomenda-se consultar a bula aprovada pelo FDA (*ABILIFY® Prescribing Information*) ou pelo EMA como fonte primária de referência de segurança antes de qualquer avaliação clínica.

---

## Conclusão e Próximos Passos

**Decisão: Proceed with Guardrails**

**Justificativa:**
Aripiprazole possui múltiplos ensaios clínicos de Fase 3 concluídos e com amostras robustas (incluindo estudos com N>1.000) que confirmam sua eficácia como terapia adjuvante em transtorno depressivo maior e no transtorno bipolar, respaldando classificação L1. A previsão do TxGNN (99,62%) é altamente coerente com o perfil farmacológico e com as aprovações internacionais consolidadas — a lacuna identificada é regulatória (ausência de registro ANVISA), não científica.

**Para prosseguir, é necessário:**
- Obter dados completos do mecanismo de ação (MOA) via DrugBank API (DB01238)
- Baixar e extrair advertências e contraindicações da bula FDA/EMA para preenchimento do perfil de segurança
- Realizar busca estruturada de interações medicamentosas (DDI) em base especializada (ex: DrugBank, Lexicomp)
- Definir estratégia regulatória junto à ANVISA, aproveitando o histórico de aprovação FDA/EMA como referência para dossiê de registro
- Identificar parceiro comercial ou titular de registro potencial no Brasil
- Delimitar a subpopulação-alvo prioritária para o mercado brasileiro (ex: TDM com resposta inadequada a antidepressivos isolados)
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

