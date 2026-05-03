---
layout: default
title: Voxilaprevir
parent: 僅模型預測 (L5)
nav_order: 507
evidence_level: L5
indication_count: 10
---

# Voxilaprevir
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

Com base no Evidence Pack fornecido, segue o relatório de avaliação de reposicionamento de Voxilaprevir.

---

# Voxilaprevir: Do tratamento da hepatite C à infecção pelo vírus da hepatite B

## Resumo em Uma Frase

Voxilaprevir é um inibidor pan-genotípico da protease NS3/4A do VHC, aprovado como componente da combinação Vosevi® (sofosbuvir/velpatasvir/voxilaprevir) para o tratamento de infecção crônica pelo vírus da hepatite C.
O modelo TxGNN prevê potencial eficácia para **Infecção pelo Vírus da Hepatite B (hepatitis B virus infection)** com pontuação de **99,84%**, porém a análise mecanística e de evidências demonstra que esta previsão é um **falso positivo** — todos os ensaios clínicos e publicações identificados referem-se a estudos de hepatite C, não de hepatite B.
Foram recuperados **5 ensaios clínicos** e **10 publicações**, nenhum deles diretamente relacionado ao uso de Voxilaprevir em VHB.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Hepatite C crônica (componente do Vosevi®) |
| Nova Indicação Prevista | Infecção pelo vírus da hepatite B (Hepatitis B virus infection) |
| Pontuação de Previsão TxGNN | 99,84% |
| Nível de Evidência | L4 |
| Situação no Mercado Brasileiro | ✓ Comercializado |
| Número de Registros | 1 |
| Decisão Recomendada | Hold |

---

## Por que Esta Previsão é Razoável?

Atualmente, os dados de mecanismo de ação não estão disponíveis no Evidence Pack. Com base nas informações conhecidas na literatura científica, Voxilaprevir é um **inibidor pan-genotípico da protease NS3/4A** — uma serina protease viral exclusiva do VHC — e atua bloqueando a clivagem proteolítica necessária para a maturação das proteínas não estruturais do vírus. Como componente de Vosevi®, demonstrou taxas de resposta virológica sustentada (SVR) superiores a 95% em múltiplos estudos de Fase 3, incluindo pacientes que falharam a regimes anteriores de antivirais de ação direta (DAAs).

No entanto, a previsão para hepatite B **não encontra respaldo mecanístico**. O vírus da hepatite B (VHB) replica-se por um mecanismo completamente diferente: utiliza uma **transcriptase reversa** para converter pgRNA em DNA viral, além de proteínas de cerne (core/HBc) para encapsidação — sem qualquer serina protease NS3/4A ou sequência homóloga em seu genoma. Em termos moleculares, o alvo de Voxilaprevir simplesmente não existe no VHB.

A pontuação elevada do TxGNN parece resultar da **similaridade ontológica** entre as doenças no grafo de conhecimento biológico: ambas são infecções virais hepáticas com perfil epidemiológico sobreposto, o que induz o modelo a uma generalização incorreta. Esta limitação — conhecida como "viés de coocorrência de nó" — é observada em modelos de reposicionamento baseados em grafos quando doenças fenomenologicamente similares são agrupadas na ontologia, sem distinção de mecanismo molecular.

---

## Evidências de Ensaios Clínicos

> ⚠️ **Alerta de Qualidade de Dados:** Todos os 5 ensaios abaixo foram recuperados pela busca com a combinação Voxilaprevir + hepatite B, mas a análise de conteúdo confirma que são **estudos de hepatite C (VHC)**, incorretamente classificados. Nenhum ensaio clínico investigando Voxilaprevir para VHB foi identificado.

| Número do Ensaio | Fase | Status | Participantes | Principais Achados |
|---------|------|------|------|---------|
| [NCT03823911](https://clinicaltrials.gov/study/NCT03823911) | Phase 4 | Concluído | 87 | Desfechos cardiovasculares após erradicação do VHC em indivíduos HIV/VHC coinfectados vs. controles HIV mono-infectados |
| [NCT04695769](https://clinicaltrials.gov/study/NCT04695769) | Phase 4 | Concluído | 281 | Papel adjuvante da ribavirina ao SOF/VEL/VOX no retreatment de hepatite C crônica com falha prévia (RCT) |
| [NCT06180590](https://clinicaltrials.gov/study/NCT06180590) | N/A | Em recrutamento | 200 | Coorte prospectivo de eficácia do Vosevi® em pacientes com falha a DAAs anteriores de VHC |
| [NCT02938013](https://clinicaltrials.gov/study/NCT02938013) | Phase 4 | Concluído | 15 | deLIVER: Cinética do VHC durante tratamento com SOF/VEL (2 DAAs) versus SOF/VEL/VOX (3 DAAs) |
| [NCT02533427](https://clinicaltrials.gov/study/NCT02533427) | Phase 1 | Concluído | 15 | Interação farmacocinética entre SOF/VEL/VOX e contraceptivo hormonal (norgestimato/etinilestradiol) |

---

## Evidências da Literatura

> ⚠️ **Alerta de Qualidade de Dados:** As publicações recuperadas abordam hepatite C ou apenas mencionam VHB como contexto epidemiológico ou de política de saúde. Nenhum estudo de eficácia ou mecanismo de Voxilaprevir em VHB foi identificado.

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [35248212](https://pubmed.ncbi.nlm.nih.gov/35248212/) | 2022 | Real-world cohort | Lancet Gastroenterol Hepatol | SOF/VEL/VOX em retreatment de VHC genótipo 4 em Ruanda (SHARED-3); altas taxas de SVR mesmo em subtipos com RAS de NS5A |
| [36535062](https://pubmed.ncbi.nlm.nih.gov/36535062/) | 2022 | Real-world cohort | J Gastrointest Liver Dis | Eficácia e segurança de SOF/VEL/VOX em pacientes romenos com VHC genótipo 1b não respondedores a DAAs |
| [31041789](https://pubmed.ncbi.nlm.nih.gov/31041789/) | 2019 | Review | Semin Liver Dis | Retreatment de VHC após falha a DAAs; SOF/VEL/VOX como opção de resgate pan-genotípica |
| [30964552](https://pubmed.ncbi.nlm.nih.gov/30964552/) | 2019 | Basic research | Hepatology | Padrões de resistência de inibidores de protease do VHC e persistência de variantes resistentes em diferentes genótipos |
| [31114957](https://pubmed.ncbi.nlm.nih.gov/31114957/) | 2019 | Review | Clin Pharmacokinetics | Considerações farmacocinéticas e farmacodinâmicas da terapia para VHC (2019), incluindo SOF/VEL/VOX |
| [29369303](https://pubmed.ncbi.nlm.nih.gov/29369303/) | 2018 | Conference report | AIDS reviews | Conferência Internacional de Hepatites Virais 2017; VHB mencionado apenas no contexto do roadmap OMS de eliminação |
| [40414600](https://pubmed.ncbi.nlm.nih.gov/40414600/) | 2025 | Análise de políticas | Ann Hepatol | Comparação global de preços de antivirais para VHB e VHC; VHB aparece como referência comparativa de política de saúde |
| [31915372](https://pubmed.ncbi.nlm.nih.gov/31915372/) | 2020 | Review | Nat Rev Gastroenterol Hepatol | Transplante com órgãos virêmicos e terapias antivirais; VHB mencionado como contexto de manejo em transplante |
| [40611935](https://pubmed.ncbi.nlm.nih.gov/40611935/) | 2025 | Cohort | J Clin Exp Hepatol | Impacto de substituições associadas à resistência (RAS) e preditores de falha terapêutica em programa de eliminação do VHC na Índia |
| [41570233](https://pubmed.ncbi.nlm.nih.gov/41570233/) | 2025 | Epidemiológico | Vopr Virusol | Prevalência de HIV, VHB e VHC em pacientes de clínicas odontológicas; análise filogenética das cepas circulantes |

---

## Informações de Comercialização no Brasil

Os dados detalhados de registro (número ANVISA, nome comercial, forma farmacêutica e indicação aprovada) não estão disponíveis no Evidence Pack atual. Consta apenas 1 registro ativo com comercialização confirmada no Brasil.

| Número de Registro | Nome Comercial | Forma Farmacêutica | Indicação Aprovada |
|---------|------|------|-----------|
| Dados indisponíveis | Dados indisponíveis | Dados indisponíveis | Dados indisponíveis (ver DG001) |

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
A previsão do TxGNN para hepatite B é um **falso positivo mecanístico confirmado**: Voxilaprevir inibe a serina protease NS3/4A do VHC, enquanto o VHB não codifica nenhuma protease homóloga — replicando-se via transcriptase reversa, um alvo completamente distinto. Nenhum dos 5 ensaios clínicos e nenhuma das 10 publicações recuperados apresenta dados diretos de Voxilaprevir em VHB; todos referem-se a estudos de VHC classificados erroneamente pela ontologia de doenças do grafo de conhecimento.

**Nota sobre outras indicações previstas:**
Das 10 indicações previstas pelo TxGNN, as únicas com potencial de hipótese explorável são **febre hemorrágica de Omsk** (rank 5) e **doença da floresta de Kyasanur** (rank 6) — ambos flavivírus com NS3 serina protease de homologia remota com o VHC. Essas indicações receberam recomendação "Research Question" no Evidence Pack, sendo candidatas a ensaios de inibição enzimática in vitro em ambiente BSL-3/4.

**Para prosseguir com qualquer indicação, é necessário:**
- Preenchimento dos dados de advertências, contraindicações e indicação aprovada via bula ANVISA (Data Gap DG001 — severidade Blocking)
- Obtenção de dados de MOA completos via DrugBank (Data Gap DG002 — severidade High)
- Preenchimento dos dados de registro ANVISA no Evidence Pack (número, nome comercial, forma farmacêutica)
- Para Omsk/Kyasanur: ensaios in vitro de inibição da protease NS3 dos vírus-alvo por Voxilaprevir em laboratório BSL-3/4
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

