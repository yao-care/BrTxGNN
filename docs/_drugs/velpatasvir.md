---
layout: default
title: Velpatasvir
parent: 僅模型預測 (L5)
nav_order: 502
evidence_level: L5
indication_count: 10
---

# Velpatasvir
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

Usando o skill `txgnn-pipeline` para orientação e aplicando o template de relatório v5 ao Evidence Pack do Velpatasvir.

---

# Velpatasvir: Da Hepatite C à Infecção por Vírus da Hepatite B

## Resumo em Uma Frase

Velpatasvir é um inibidor do NS5A do vírus da hepatite C (HCV), utilizado em combinação com sofosbuvir (Epclusa®) para o tratamento da hepatite C crônica de todos os genótipos.
O modelo TxGNN prevê potencial eficácia para a **Infecção por Vírus da Hepatite B (Hepatitis B Virus Infection)**, com pontuação de 99,87%.
No entanto, das **26 buscas em ensaios clínicos** e **20 publicações** identificadas, todos os estudos são direcionados ao HCV — não há evidência direta de atividade antiviral de velpatasvir contra o HBV.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Hepatite C crônica (HCV) — inferido do contexto clínico |
| Nova Indicação Prevista | Infecção por Vírus da Hepatite B |
| Pontuação de Previsão TxGNN | 99,87% |
| Nível de Evidência | L4 |
| Situação no Mercado Brasileiro | ✓ Comercializado |
| Número de Registros | 2 |
| Decisão Recomendada | Hold |

---

## Por que Esta Previsão é Razoável?

Velpatasvir é um inibidor de segunda geração da proteína NS5A do HCV — uma proteína multifuncional essencial para a montagem do complexo de replicação viral. Ao bloquear a NS5A, velpatasvir interrompe a replicação do RNA viral. Em combinação com sofosbuvir (inibidor da polimerase NS5B), forma o Epclusa®, aprovado globalmente para tratamento pan-genotípico do HCV com taxas de resposta virológica sustentada (SVR12) superiores a 95%.

A relação clínica entre hepatite C e hepatite B é a de doenças virais hepáticas crônicas compartilhando complicações de longo prazo — cirrose e carcinoma hepatocelular (CHC). Essa proximidade no grafo de conhecimento biomédico provavelmente fundamenta a previsão do TxGNN. No entanto, os mecanismos de replicação são radicalmente distintos: o HCV é um vírus RNA positivo que utiliza NS5A como proteína de andaime replicativo; o HBV é um vírus DNA parcialmente dupla-fita que se replica via transcriptase reversa a partir de um intermediário cccDNA, sem qualquer proteína homóloga à NS5A do HCV.

A única conexão biológica documentada entre velpatasvir e HBV é um caso clínico de **reativação do HBV** em paciente HBcAb-positivo durante tratamento com SOF/VEL para HCV (PMID 31542053). Isso representa um sinal de **segurança** — não de eficácia terapêutica contra o HBV. A previsão do TxGNN parece ser um artefato de proximidade topológica no grafo de doenças hepáticas virais, sem suporte mecanístico direto.

---

## Evidências de Ensaios Clínicos

> ⚠️ **Nota de relevância**: Nenhum dos ensaios identificados avalia velpatasvir como agente anti-HBV. Os estudos abaixo são ensaios de HCV recuperados por co-ocorrência de termos. O único ensaio com envolvimento direto de HBV é o NCT04997564 (co-infecção HCV/HBV, onde TAF protege o HBV).

| Número do Ensaio | Fase | Status | Participantes | Principais Achados |
|---------|------|------|------|---------|
| [NCT04997564](https://clinicaltrials.gov/study/NCT04997564) | Phase 4 | Desconhecido | 120 | SOF/VEL 12 semanas + TAF profilático para co-infectados HCV/HBV (genótipos 1–6), com ou sem cirrose compensada — TAF previne reativação do HBV, velpatasvir trata o HCV |
| [NCT01858766](https://clinicaltrials.gov/study/NCT01858766) | Phase 2 | Concluído | 379 | Estudo fundacional de SOF + velpatasvir (GS-5816) ± ribavirina em pacientes naive para HCV genótipos 1–6 |
| [NCT02996682](https://clinicaltrials.gov/study/NCT02996682) | Phase 3 | Concluído | 102 | SOF/VEL ± ribavirina 12 semanas para HCV com cirrose descompensada; avaliação de eficácia e segurança |
| [NCT02201901](https://clinicaltrials.gov/study/NCT02201901) | Phase 3 | Concluído | 268 | SOF/VEL com e sem ribavirina para HCV com cirrose Child-Pugh B; SOF/VEL 24 semanas |
| [NCT02625909](https://clinicaltrials.gov/study/NCT02625909) | Phase 3 | Concluído | 222 | SOF/VEL para HCV recentemente adquirido em usuários de drogas injetáveis e co-infectados HIV; avaliação de encurtamento de tratamento |
| [NCT03250910](https://clinicaltrials.gov/study/NCT03250910) | Phase 4 | Concluído | 228 | VEL/SOF genérico ± ribavirina 12 semanas para HCV em co-infectados HIV; comparação de eficácia e segurança entre grupos |
| [NCT02480712](https://clinicaltrials.gov/study/NCT02480712) | Phase 3 | Concluído | 107 | SOF/velpatasvir 12 semanas para HCV em co-infectados HIV-1; eficácia e segurança avaliadas em população HIV+ |
| [NCT04653818](https://clinicaltrials.gov/study/NCT04653818) | Phase 4 | Concluído | 84 | ECA: efeito de DAAs na recorrência de CHC relacionado ao HCV após ablação percutânea — relevante para vigilância de CHC compartilhada com HBV |
| [NCT03549312](https://clinicaltrials.gov/study/NCT03549312) | Phase 4 | Desconhecido | 25 | Estudo de viabilidade: switch ARV para E/C/F/TAF → SOF/VEL (HCV) → B/F/TAF em co-infectados HIV/HCV em terapia de substituição opiácea |
| [NCT03579576](https://clinicaltrials.gov/study/NCT03579576) | N/A | Concluído | 803 | Modelo simplificado de tratamento HCV integrado com HIV em populações-chave em Mianmar — contexto de co-infecções múltiplas |

---

## Evidências da Literatura

> ⚠️ **Nota de relevância**: As publicações são majoritariamente sobre tratamento do HCV. Os itens com maior relevância direta ao HBV aparecem nas primeiras posições.

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [31542053](https://pubmed.ncbi.nlm.nih.gov/31542053/) | 2019 | Relato de Caso | J Med Case Reports | Reativação do HBV por mutante de escape imune em paciente HBcAb+ durante SOF/VEL para HCV — **sinal de segurança**, não de eficácia anti-HBV |
| [32935438](https://pubmed.ncbi.nlm.nih.gov/32935438/) | 2021 | Coorte | J Viral Hepatitis | SOF/VEL em Mianmar: co-infectados HBV receberam tenofovir concomitante — confirma necessidade de profilaxia HBV durante DAA para HCV |
| [39735164](https://pubmed.ncbi.nlm.nih.gov/39735164/) | 2024 | Vida Real | J Virus Eradication | SOF/VEL para HCV na China incluindo co-infectados HCV/HBV e HCV/HIV; dados escassos para co-infecção HBV destacados como lacuna |
| [34092970](https://pubmed.ncbi.nlm.nih.gov/34092970/) | 2021 | Revisão | World J Gastroenterol | Avanços no tratamento pediátrico de hepatite B e C; perspectivas de DAAs para HCV pediátrico e limitações para HBV |
| [29369303](https://pubmed.ncbi.nlm.nih.gov/29369303/) | 2018 | Conferência | AIDS Reviews | Conferência Internacional de Hepatite Viral 2017: metas da OMS para eliminação de HBV e HCV até 2030; perspectivas de novas terapias |
| [41734217](https://pubmed.ncbi.nlm.nih.gov/41734217/) | 2025 | Retrospectivo | Klin Mikrobiol Infekc Lek | Tratamento antiviral de hepatite viral B e C crônica em crianças em Ostrava; avaliação de frequência, eficácia e tolerância |
| [40414600](https://pubmed.ncbi.nlm.nih.gov/40414600/) | 2025 | Transversal | Ann Hepatology | Comparação global de preços de antivirais para HBV e HCV; custos nos EUA até 3× mais altos que outros países de alta renda |
| [35248213](https://pubmed.ncbi.nlm.nih.gov/35248213/) | 2022 | Coorte | Lancet Gastroenterol Hepatol | SOF/VEL para HCV genótipo 4 no Ruanda; eficácia contra subtipos com substituições de resistência NS5A |
| [33217040](https://pubmed.ncbi.nlm.nih.gov/33217040/) | 2021 | Vida Real | J Gastroenterol Hepatol | SOF/VEL ± RBV para HCV genótipo 3 em contexto real, incluindo cirrose descompensada e CHC — compartilha complicações com HBV |
| [38910758](https://pubmed.ncbi.nlm.nih.gov/38910758/) | 2024 | Descritivo | Cureus | Eficácia de SOF/VEL para HCV em pacientes com doença renal crônica — relevante para populações de risco com possível co-morbidade HBV |

---

## Informações de Comercialização no Brasil

Velpatasvir está registrado no Brasil com **2 licenças ativas** (status: comercializado). Os detalhes individuais de cada registro — número ANVISA, nome comercial, forma farmacêutica e texto de indicação aprovada — não constam nos dados fornecidos neste Evidence Pack.

> É amplamente conhecido que velpatasvir é comercializado como componente da combinação sofosbuvir/velpatasvir (Epclusa®) para tratamento de hepatite C crônica, mas esses dados devem ser confirmados diretamente junto à ANVISA antes de qualquer tomada de decisão regulatória.

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

> **Alerta clínico relevante ao contexto de reposicionamento**: Há caso documentado (PMID 31542053) de reativação do HBV em paciente com infecção prévia por HBV (HBcAb+) durante tratamento com SOF/VEL para HCV. Este achado representa uma **contraindicação relativa** ao uso de velpatasvir em pacientes com HBV subjacente sem profilaxia adequada, não um sinal de atividade terapêutica.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
Velpatasvir é um inibidor altamente específico da NS5A do HCV — proteína sem homólogo no HBV. A análise dos 26 ensaios clínicos e 20 publicações confirmou que toda a evidência se refere ao tratamento do HCV; a única conexão com HBV é um caso de reativação (sinal de segurança). A previsão do TxGNN com score de 99,87% reflete proximidade topológica no grafo de doenças hepáticas virais, mas sem suporte mecanístico ou clínico para atividade anti-HBV.

**Para prosseguir, é necessário:**
- Dados de atividade inibitória in vitro de velpatasvir contra replicação do HBV (IC₅₀ em modelos celulares de HBV, como HepAD38 ou HepG2.2.15)
- Identificação de alvo molecular no HBV com similaridade estrutural à NS5A do HCV que possa ser modulado por velpatasvir
- Esclarecimento do MOA completo via consulta ao DrugBank API (DB11613)
- Obtenção dos dados completos dos 2 registros ANVISA (indicações aprovadas, advertências, contraindicações da bula brasileira)
- Caso seja de interesse o manejo de co-infecção HCV/HBV, avaliar o NCT04997564 como modelo de estudo (SOF/VEL + TAF profilático), que já demonstra viabilidade clínica da combinação
---

