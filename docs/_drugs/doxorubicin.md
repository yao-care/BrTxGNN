---
layout: default
title: Doxorubicin
parent: 僅模型預測 (L5)
nav_order: 229
evidence_level: L5
indication_count: 10
---

# Doxorubicin
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

# Doxorubicin: De Antineoplásico Sistêmico ao Sarcoma de Ewing

## Resumo em Uma Frase

Doxorubicin é uma antraciclina amplamente utilizada no tratamento de neoplasias malignas como leucemias agudas, linfomas, carcinoma de mama e sarcomas.
O modelo TxGNN prevê que pode ser eficaz para o **Sarcoma de Ewing (Ewing sarcoma)**,
atualmente com **47 ensaios clínicos** e **20 publicações** apoiando esta direção, incluindo múltiplos estudos de Fase III concluídos que já consolidaram o fármaco como componente central do tratamento padrão internacional.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Antineoplásico de amplo espectro — leucemias agudas, linfomas, carcinoma de mama, sarcomas (sem registro ativo no Brasil) |
| Nova Indicação Prevista | Sarcoma de Ewing (Ewing sarcoma) |
| Pontuação de Previsão TxGNN | 99,90% |
| Nível de Evidência | L1 |
| Situação no Mercado Brasileiro | Não comercializado |
| Número de Registros | 0 |
| Decisão Recomendada | Proceed with Guardrails |

---

## Por que Esta Previsão é Razoável?

Doxorubicin é uma antraciclina cujo mecanismo de ação envolve a inibição da Topoisomerase II e a intercalação direta na dupla hélice do DNA, induzindo quebras de dupla fita irreversíveis que bloqueiam simultaneamente a replicação e a transcrição celular. Esse processo desencadeia apoptose dependente de caspase, com eficácia especialmente pronunciada em células tumorais de alta taxa proliferativa. Os dados formais de mecanismo de ação via DrugBank não foram recuperados nesta análise, mas o mecanismo é amplamente documentado na literatura oncológica e está descrito na racionalidade mecanística deste Evidence Pack.

O Sarcoma de Ewing é um tumor maligno primitivo de células redondas, predominantemente de origem óssea, que acomete crianças, adolescentes e adultos jovens. As células tumorais são impulsionadas pela proteína de fusão oncogênica **EWSR1-FLI1**, resultante de translocações cromossômicas características, e apresentam alta sensibilidade ao dano ao DNA induzido por antraciclinas. Essa vulnerabilidade biológica fundamenta o papel central de Doxorubicin no esquema padrão **VDC-IE** (Vincristina/Doxorubicin/Ciclofosfamida alternando com Ifosfamida/Etoposídeo), adotado pelos principais grupos cooperativos internacionais (COG, EURO-EWING, EpSSG).

Diferentemente de um reposicionamento clássico, a previsão do TxGNN representa neste caso uma **validação computacional de uma indicação já consolidada clinicamente**, com suporte de mais de quinze anos de evidências de Fase III. A pontuação de 99,90% reflete precisamente essa robustez: o fármaco é reconhecido pelo grafo de conhecimento como tendo relações biológicas e clínicas profundamente estabelecidas com esta neoplasia.

---

## Evidências de Ensaios Clínicos

| Número do Ensaio | Fase | Status | Participantes | Principais Achados |
|---------|------|------|------|---------|
| [NCT02063022](https://clinicaltrials.gov/study/NCT02063022) | Phase 3 | Concluído | 278 | RCT controlado avaliando intensificação de dose versus tratamento padrão em Sarcoma de Ewing não-metastático; Doxorubicin como componente central dos braços de indução |
| [NCT00006734](https://clinicaltrials.gov/study/NCT00006734) | Phase 3 | Concluído | 587 | Comparação randomizada de regimes de quimioterapia com compressão de intervalo para Sarcoma de Ewing e PNET; Doxorubicin presente no braço padrão e experimental |
| [NCT01231906](https://clinicaltrials.gov/study/NCT01231906) | Phase 3 | Concluído | 642 | Adição de VTC (Vincristina-Topotecano-Ciclofosfamida) ao esquema padrão VDC-IE com Doxorubicin em Sarcoma de Ewing não-metastático; resultado primário publicado |
| [NCT02306161](https://clinicaltrials.gov/study/NCT02306161) | Phase 3 | Em andamento (sem recrutamento) | 312 | Adição de ganitumab (anticorpo anti-IGF-1R) à quimioterapia comprimida por intervalo com Doxorubicin em Sarcoma de Ewing metastático recém-diagnosticado |
| [NCT06820957](https://clinicaltrials.gov/study/NCT06820957) | Phase 2/3 | Em andamento (sem recrutamento) | 437 | Comparação de VIrR + VDC/IE versus VDC/IE padrão (com Doxorubicin) em Sarcoma de Ewing metastático recém-diagnosticado; estudo de plataforma adaptativo |
| [NCT03011528](https://clinicaltrials.gov/study/NCT03011528) | Phase 2 | Concluído | 45 | CombinaiR3: tratamento de primeira linha com esquema contendo Doxorubicin em tumores de Ewing com disseminação extrapulmonar primária; evidência direta de maior relevância |
| [NCT03277924](https://clinicaltrials.gov/study/NCT03277924) | Phase 1/2 | Concluído | 197 | Sunitinib e/ou Nivolumab adicionados a quimioterapia de base com Doxorubicin em sarcomas ósseos e de tecidos moles, incluindo Sarcoma de Ewing |
| [NCT07321912](https://clinicaltrials.gov/study/NCT07321912) | Phase 2 | Ainda não iniciado | 406 | Eflornithine (DFMO) como terapia adicional e de manutenção associada a quimioterapia com Doxorubicin em Sarcoma de Ewing e Osteossarcoma; 5 coortes cobertas |
| [NCT00002643](https://clinicaltrials.gov/study/NCT00002643) | Phase 2 | Concluído | 130 | Terapia intensiva de alta dose com suporte de fator de crescimento em Sarcoma de Ewing metastático recém-diagnosticado; Doxorubicin como componente principal |
| [NCT00001209](https://clinicaltrials.gov/study/NCT00001209) | Phase 1 | Concluído | 120 | Estudo piloto histórico com VAC (Vincristina/Doxorubicin/Ciclofosfamida) alternando com IE em sarcomas de alto risco; base fundacional do esquema VDC-IE moderno |

---

## Evidências da Literatura

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [12594313](https://pubmed.ncbi.nlm.nih.gov/12594313/) | 2003 | Phase III RCT | N Engl J Med | INT-0091: adição de ifosfamida e etoposídeo ao esquema padrão com Doxorubicin melhorou significativamente a sobrevida em Sarcoma de Ewing; estudo fundador do protocolo VDC-IE |
| [36522207](https://pubmed.ncbi.nlm.nih.gov/36522207/) | 2022 | RCT | Lancet | EE2012: primeiro RCT a comparar diretamente os esquemas europeu e norte-americano com Doxorubicin em Sarcoma de Ewing recém-diagnosticado; eficácia equivalente entre as abordagens |
| [23091096](https://pubmed.ncbi.nlm.nih.gov/23091096/) | 2012 | RCT | J Clin Oncol | AEWS0031: compressão de intervalo no esquema VDC/IE com Doxorubicin melhorou de forma estatisticamente significativa a sobrevida livre de eventos em Sarcoma de Ewing localizado |
| [35427190](https://pubmed.ncbi.nlm.nih.gov/35427190/) | 2022 | RCT | J Clin Oncol | Ewing 2008R3 (12 países): avaliou consolidação com TreoMel em alta dose versus padrão em Sarcoma de Ewing de alto risco; esquema de indução baseado em Doxorubicin |
| [36669140](https://pubmed.ncbi.nlm.nih.gov/36669140/) | 2023 | Phase III RCT | J Clin Oncol | AEWS1221: ganitumab adicionado ao esquema comprimido com Doxorubicin não melhorou a sobrevida livre de eventos em Sarcoma de Ewing metastático; demostra a dificuldade de superar o esquema padrão |
| [31952545](https://pubmed.ncbi.nlm.nih.gov/31952545/) | 2020 | RCT Internacional | Trials | Euro Ewing 2012: protocolo multicêntrico internacional comparando dois esquemas de indução e consolidação com Doxorubicin em tumores da família de Ewing |
| [37651654](https://pubmed.ncbi.nlm.nih.gov/37651654/) | 2023 | Seguimento de RCT | J Clin Oncol | Resultados de longo prazo do AEWS0031: confirmação duradoura do benefício da compressão de intervalo com esquema VDC/IE contendo Doxorubicin em Sarcoma de Ewing localizado |
| [20152770](https://pubmed.ncbi.nlm.nih.gov/20152770/) | 2010 | Revisão | Lancet Oncol | Revisão abrangente do Sarcoma de Ewing: evolução histórica do tratamento, papel central das antraciclinas, sobrevida ~75% nos tumores localizados versus prognóstico sombrio nos metastáticos |
| [26304893](https://pubmed.ncbi.nlm.nih.gov/26304893/) | 2015 | Revisão | J Clin Oncol | Sarcoma de Ewing — situação atual e direções futuras por colaboração internacional; síntese de décadas de evidências para Doxorubicin nos protocolos multidisciplinares |
| [37093679](https://pubmed.ncbi.nlm.nih.gov/37093679/) | 2023 | Coorte Retrospectiva | Jpn J Clin Oncol | Características clínicas do Sarcoma de Ewing cutâneo e subcutâneo; análise de estratégias de tratamento com esquemas baseados em Doxorubicin em subgrupo raro |

---

## Informações de Comercialização no Brasil

Doxorubicin **não possui nenhum registro ativo na ANVISA**. O fármaco não está comercializado no Brasil pelos canais regulatórios identificados neste sistema (total de registros: 0). O acesso ao medicamento pode ser viabilizado por meio de importação excepcional ou Programa de Acesso Expandido, conforme regulamentação da RDC ANVISA aplicável.

---

## Citotoxicidade

| Item | Conteúdo |
|------|------|
| Classificação de Citotoxicidade | Citotóxico convencional — antraciclina (intercalante de DNA / inibidor de Topoisomerase II) |
| Risco de Mielossupressão | **Alto** — leucopenia, neutropenia e trombocitopenia são efeitos dose-limitantes frequentes e previsíveis; monitoramento hematológico obrigatório a cada ciclo |
| Classificação de Emetogenicidade | **Moderada a alta** — doses ≥60 mg/m² são classificadas como altamente emetogênicas segundo diretrizes MASCC/ESMO; antiemético profilático obrigatório |
| Itens de Monitoramento | Hemograma completo com diferencial (CBC); função cardíaca — FEVE por ecocardiograma ou cintilografia antes do início e periodicamente durante o tratamento; função hepática (ALT, AST, bilirrubinas); dose cumulativa total (limite clássico: ≤550 mg/m²; ≤400 mg/m² com irradiação mediastinal prévia) |
| Proteção no Manuseio | Necessário seguir normas de manuseio de agentes citotóxicos; uso obrigatório de EPI (luvas de nitrila dupla, avental impermeável de manga longa, proteção ocular); preparo em câmara de fluxo laminar vertical Classe II; descarte como resíduo quimioterápico (Grupo B/Classe D conforme ANVISA RDC 222/2018) |

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Proceed with Guardrails**

**Justificativa:**
Doxorubicin apresenta o mais alto nível de evidência clínica disponível (L1) para o Sarcoma de Ewing, sendo componente central do esquema padrão VDC-IE há mais de quinze anos, com respaldo de múltiplos ensaios de Fase III de grande escala; a ausência de registro ativo na ANVISA constitui a principal barreira regulatória para uso formal no Brasil.

**Para prosseguir, é necessário:**
- Regularização do registro junto à ANVISA ou avaliação de acesso via importação excepcional / Programa de Acesso Expandido
- Obtenção da bula oficial aprovada pela ANVISA para levantamento completo de advertências, contraindicações e interações medicamentosas
- Consulta ao DrugBank API para recuperação dos dados formais de mecanismo de ação (pendente nesta análise — DG002)
- Implementação de protocolo institucional de monitoramento cardíaco com controle rigoroso da dose cumulativa máxima de Doxorubicin (≤550 mg/m²)
- Confirmação de protocolos de acesso ao medicamento para populações pediátricas, dado que o Sarcoma de Ewing acomete predominantemente crianças e adolescentes
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

