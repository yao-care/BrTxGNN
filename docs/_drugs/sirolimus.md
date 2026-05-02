---
layout: default
title: Sirolimus
parent: 僅模型預測 (L5)
nav_order: 440
evidence_level: L5
indication_count: 10
---

# Sirolimus
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

# Sirolimus: Do transplante renal ao liposarcoma

## Resumo em Uma Frase

Sirolimus (Rapamicina) é um inibidor de mTOR originalmente aprovado como imunossupressor para prevenção de rejeição em transplante renal.
O modelo TxGNN prevê que pode ser eficaz para **Liposarcoma (Liposarcoma)**, com **5 ensaios clínicos** e **12 publicações** apoiando esta direção, incluindo um ensaio Phase 2 multicêntrico concluído que testou diretamente o Sirolimus nesta indicação.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Imunossupressão em transplante renal (prevenção de rejeição) |
| Nova Indicação Prevista | Liposarcoma (Liposarcoma) |
| Pontuação de Previsão TxGNN | 99,89% |
| Nível de Evidência | L2 |
| Situação no Mercado Brasileiro | ✗ Não registrado na ANVISA |
| Número de Registros | 0 |
| Decisão Recomendada | Proceed with Guardrails |

---

## Por que Esta Previsão é Razoável?

Sirolimus (Rapamicina) é o protótipo dos rapalogues — inibidores alostéricos de mTOR (mechanistic Target Of Rapamycin). Ele atua ligando-se à proteína FKBP12 e, em seguida, ao complexo mTORC1, bloqueando sua atividade quinase. Essa inibição interrompe a sinalização downstream dos efetores S6K1 e 4E-BP1, resultando em supressão da síntese proteica, bloqueio da progressão do ciclo celular na fase G1 e redução da neovascularização tumoral. Originalmente aprovado como imunossupressor no transplante renal, o Sirolimus passou a ser investigado em oncologia justamente porque o eixo PI3K/AKT/mTOR é aberrantemente ativado em múltiplos tipos tumorais.

No liposarcoma desdiferenciado (DDL) — o subtipo mais agressivo desta neoplasia mesenquimal — estudos translacionais em 99 espécimes confirmaram ativação das vias Akt-mTOR e MAPK (PMID 26518767), fornecendo uma base mecanística direta e precisa para o uso de inibidores de mTOR. Modelos de xenoenxerto derivado de paciente (PDX) demonstraram que a combinação de Rapamicina com Cloroquina suprime o crescimento tumoral do DDL com efeito sinérgico (PMID 36309387, PMID 37400145), reforçando a plausibilidade biológica in vivo.

A evidência clínica mais direta é o NCT02821507, um ensaio Phase 2 de braço único multicêntrico que testou especificamente a combinação de **Sirolimus + Ciclofosfamida** em liposarcoma mixoide e condrossarcoma metastático ou irressecável, com 70 participantes e concluído em 2021. Além disso, análogos de mTOR (Everolimus, Temsirolimus, Ridaforolimus) foram extensivamente testados em sarcomas de tecidos moles — incluindo DDL e leiomiossarcoma (LMS) — fornecendo um corpo consistente de evidências de classe que apoia a relevância do alvo terapêutico nesta família de tumores.

---

## Evidências de Ensaios Clínicos

| Número do Ensaio | Fase | Status | Participantes | Principais Achados |
|---------|------|------|------|---------|
| [NCT02821507](https://clinicaltrials.gov/study/NCT02821507) | Phase 2 | Concluído | 70 | **Ensaio direto de Sirolimus** combinado com Ciclofosfamida em liposarcoma mixoide e condrossarcoma metastático/irressecável; baseia-se em modelos in vivo demonstrando inibição de mTOR como estratégia eficaz nesses subtipos |
| [NCT03114527](https://clinicaltrials.gov/study/NCT03114527) | Phase 2 | Ativo, não recrutando | 48 | Ribociclib + Everolimus (inibidor de mTOR da mesma classe) em DDL e LMS avançados; resultados publicados (PMID 37967116) demonstram atividade antitumoral em liposarcoma desdiferenciado |
| [NCT00093080](https://clinicaltrials.gov/study/NCT00093080) | Phase 2 | Concluído | 216 | Ridaforolimus (inibidor de mTOR) em sarcoma avançado; maior ensaio de classe com 216 pacientes, administrado 5 dias consecutivos a cada 2 semanas, fornece evidência robusta sobre eficácia da classe no grupo de sarcomas |
| [NCT01614795](https://clinicaltrials.gov/study/NCT01614795) | Phase 2 | Concluído | 46 | Cixutumumab + Temsirolimus (inibidor de mTOR) em sarcoma pediátrico recorrente/refratário; inclui subtipos de sarcoma de tecido mole e fornece evidência de segurança da combinação |
| [NCT00949325](https://clinicaltrials.gov/study/NCT00949325) | Phase 1/2 | Concluído | 24 | Temsirolimus + Doxorrubicina lipossomal em sarcoma de tecido mole e ósseo avançado; identificou dose segura para a combinação e avaliou eficácia em sarcoma recorrente |

---

## Evidências da Literatura

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [37967116](https://pubmed.ncbi.nlm.nih.gov/37967116/) | 2024 | Phase 2 RCT | Clin Cancer Res | Ribociclib + Everolimus em DDL e LMS avançados; inibição combinada de CDK4/6 e mTOR demonstra atividade antitumoral e valida mecanisticamente o alvo mTOR em DDL |
| [37400145](https://pubmed.ncbi.nlm.nih.gov/37400145/) | 2023 | Pré-clínico + PDX | Cancer Genomics Proteomics | Rapamicina + Cloroquina inibe autofagia e induz apoptose em liposarcoma bem diferenciado; modelo PDX demonstra eficácia in vivo |
| [36309387](https://pubmed.ncbi.nlm.nih.gov/36309387/) | 2022 | Pré-clínico | In Vivo | Rapamicina + Cloroquina interrompe crescimento em modelo PDOX de liposarcoma desdiferenciado; efeito sinérgico sobre supressão tumoral documentado |
| [26518767](https://pubmed.ncbi.nlm.nih.gov/26518767/) | 2016 | Translacional | Tumour Biology | Ativação confirmada das vias Akt-mTOR e MAPK em 99 espécimes de DDL; in vitro, inibidor de mTOR suprimiu proliferação celular; base mecanística direta para o uso de Sirolimus |
| [25519700](https://pubmed.ncbi.nlm.nih.gov/25519700/) | 2015 | Pré-clínico | Mol Cancer Ther | MLN0128 (inibidor dual mTORC1/mTORC2) demonstra atividade antitumoral superior aos rapalogues de primeira geração em modelos de sarcoma ósseo e de tecidos moles |
| [39796641](https://pubmed.ncbi.nlm.nih.gov/39796641/) | 2024 | Review | Cancers | Panorama dos novos agentes aprovados em sarcoma de tecido mole; contextualiza o papel dos inibidores de mTOR frente a imunoterapia e inibidores de tirosina quinase |
| [37222206](https://pubmed.ncbi.nlm.nih.gov/37222206/) | 2023 | Review | Curr Opin Oncol | Revisão dos fundamentos e resultados de ensaios clínicos com agentes moleculares-alvo em sarcomas avançados; inclui rapalogues como estratégia emergente |
| [20497911](https://pubmed.ncbi.nlm.nih.gov/20497911/) | 2010 | Review | Bull Cancer | Classificação molecular de 6 subgrupos de sarcoma e respectivos tratamentos-alvo; discute mTOR como alvo terapêutico em subtipos com deleção de PTEN |
| [16434506](https://pubmed.ncbi.nlm.nih.gov/16434506/) | 2006 | Coorte | JASN | Sirolimus reduz significativamente a incidência de neoplasias em transplantados renais comparado à ciclosporina; suporta efeito antiproliferativo intrínseco do fármaco |
| [32711543](https://pubmed.ncbi.nlm.nih.gov/32711543/) | 2020 | Série de Casos | Diagn Pathology | Anomalia fibro-adiposa vascular (FAVA) com mutação PIK3CA e ativação de mTOR; Sirolimus utilizado como abordagem terapêutica, ilustrando aplicabilidade em tumores mTOR-driven de tecidos moles |

---

## Citotoxicidade

Sirolimus pertence à classe dos rapalogues (inibidores alostéricos de mTORC1), amplamente utilizados como agentes antineoplásicos de terapia-alvo em oncologia. Análogos estruturais como Everolimus e Temsirolimus possuem aprovação regulatória para múltiplas indicações oncológicas (carcinoma renal, câncer de mama HR+/HER2−, tumores neuroendócrinos pancreáticos, linfoma de células do manto). Embora Sirolimus não seja um citotóxico convencional, sua aplicação proposta em liposarcoma requer as seguintes considerações:

| Item | Conteúdo |
|------|------|
| Classificação de Citotoxicidade | Terapia-alvo — Inibidor de mTOR (rapalouge); não se enquadra como citotóxico convencional |
| Risco de Mielossupressão | Baixo a Médio (anemia, leucopenia e trombocitopenia reportadas em contexto de transplante; intensidade inferior à quimioterapia citotóxica) |
| Classificação de Emetogenicidade | Baixa |
| Itens de Monitoramento | Hemograma completo (CBC com diferencial), creatinina e ureia (função renal), AST/ALT/bilirrubina (função hepática), triglicerídeos e colesterol (dislipidemia frequente), glicemia em jejum, nível sérico de Sirolimus (monitoramento farmacocinético recomendado) |
| Proteção no Manuseio | Precauções farmacêuticas padrão; não classificado como agente citotóxico perigoso pelas regulamentações de manuseio específicas para quimioterápicos |

---

## Considerações de Segurança

Os dados específicos de advertências e contraindicações não foram recuperados automaticamente nesta consulta. Com base na literatura clínica disponível sobre o uso de Sirolimus como imunossupressor e em estudos oncológicos, os principais pontos de atenção incluem: imunossupressão com risco aumentado de infecções oportunistas (incluindo pneumonia por *Pneumocystis*), pneumonite intersticial não infecciosa, comprometimento da cicatrização de feridas (especialmente no pós-operatório), dislipidemia (hipertrigliceridemia e hipercolesterolemia), hiperglicemia e necessidade de monitoramento dos níveis séricos para ajuste de dose.

Consulte a bula oficial e fontes regulatórias (DrugBank, FDA/EMA labeling) para a lista completa de advertências, contraindicações e interações medicamentosas antes de qualquer uso clínico.

---

## Conclusão e Próximos Passos

**Decisão: Proceed with Guardrails**

**Justificativa:**
Existe um ensaio Phase 2 multicêntrico concluído (NCT02821507, n=70) que testou diretamente Sirolimus em liposarcoma mixoide, apoiado por sólida base mecanística (ativação confirmada de mTOR em DDL) e por evidências robustas de classe com análogos de mTOR em sarcomas de tecidos moles. O nível de evidência L2 é suficiente para prosseguir com investigação clínica estruturada, porém o Sirolimus não está registrado na ANVISA e os dados de segurança completos ainda precisam ser formalmente compilados.

**Para prosseguir, é necessário:**
- Recuperação e análise dos resultados publicados do NCT02821507 para avaliação da eficácia e perfil de toxicidade específico em liposarcoma
- Compilação completa dos dados de segurança via DrugBank API, bula FDA/EMA e literatura de transplante (advertências, contraindicações, interações com imunossupressores e quimioterápicos)
- Avaliação do processo de registro junto à ANVISA ou estratégia de uso compassivo/ensaio clínico local
- Definição do subgrupo de pacientes mais propenso a responder: liposarcoma desdiferenciado com ativação confirmada de mTOR por biópsia (imuno-histoquímica para pS6, p4E-BP1)
- Elaboração de plano de monitoramento de imunossupressão, infecções oportunistas e dislipidemia em contexto oncológico
---

