---
layout: default
title: Ritonavir
parent: 僅模型預測 (L5)
nav_order: 429
evidence_level: L5
indication_count: 3
---

# Ritonavir
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

Com base no Evidence Pack fornecido, aqui está o relatório de avaliação de reposicionamento:

---

# Ritonavir: Do Tratamento do HIV/AIDS à Síndrome de Imunodeficiência Adquirida Felina

## Resumo em Uma Frase

Ritonavir é um inibidor de protease retroviral amplamente utilizado no tratamento do HIV/AIDS em humanos, atuando tanto como agente antirretroviral quanto como potencializador farmacocinético (booster) de outros inibidores de protease. O modelo TxGNN prevê que pode ser eficaz para a **Síndrome de Imunodeficiência Adquirida Felina** (*Feline Acquired Immunodeficiency Syndrome* — doença viral de gatos causada pelo FIV), atualmente com **1 ensaio clínico de relevância indireta** (grau C) e **nenhuma publicação direta** apoiando esta indicação veterinária.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|----------|
| Indicação Original | HIV/AIDS — dados de indicação aprovada não disponíveis neste Evidence Pack |
| Nova Indicação Prevista | Síndrome de Imunodeficiência Adquirida Felina (*Feline Acquired Immunodeficiency Syndrome*) |
| Pontuação de Previsão TxGNN | 99,92% |
| Nível de Evidência | L4 |
| Situação no Mercado Brasileiro | ✓ Comercializado |
| Número de Registros | 20 |
| Decisão Recomendada | **Hold** |

---

## Por que Esta Previsão é Razoável?

Não há dados detalhados de mecanismo de ação (MOA) disponíveis neste Evidence Pack. Com base em conhecimento farmacológico estabelecido, Ritonavir é um inibidor de protease do HIV-1 que bloqueia a enzima responsável pela clivagem da poliproteína Gag-Pol viral, impedindo a maturação de novos vírions. Em doses mais baixas, age como inibidor potente do CYP3A4, sendo amplamente co-administrado como booster farmacocinético de outros inibidores de protease.

A plausibilidade mecanística para a síndrome de imunodeficiência adquirida felina (FIV) existe em tese: o FIV (*Feline Immunodeficiency Virus*) é um lentivírus, assim como o HIV-1, e sua protease pertence à mesma família das proteases aspárticas, com sítio catalítico conservado. Essa homologia estrutural é provavelmente o caminho de inferência percorrido pelo modelo TxGNN no grafo de conhecimento.

No entanto, a transferibilidade do mecanismo é limitada por diferenças biológicas relevantes: o sítio de ligação da protease do FIV apresenta especificidade de substrato substancialmente distinta da do HIV-1, e dados experimentais in vitro disponíveis na literatura indicam que a atividade inibitória de ritonavir sobre o FIV é consideravelmente menor. Acrescenta-se que esta é uma indicação **veterinária** — o que implica um contexto clínico, regulatório e de desenvolvimento de produto completamente diferente do uso humano.

---

## Evidências de Ensaios Clínicos

| Número do Ensaio | Fase | Status | Participantes | Principais Achados |
|---------|------|------|------|---------|
| [NCT02770508](https://clinicaltrials.gov/study/NCT02770508) | Phase 4 | Concluído | 145 | Estudo em **humanos** com HIV-1 (não em gatos): compara ritonavir-boosted darunavir + lamivudina versus regimes com tenofovir/emtricitabina em pacientes naïve ao tratamento antirretroviral. A relevância para a síndrome felina é **indireta (grau C)** — suspeita-se de erro de categorização no banco de dados ao vincular este ensaio humano ao nó de doença felina. |

> ⚠️ **Alerta de qualidade de dados:** O único ensaio identificado é um estudo conduzido em humanos com HIV-1 e não possui relação direta com o FIV em gatos. Não há ensaios clínicos veterinários registrados para esta indicação.

---

## Evidências da Literatura

Atualmente não há literatura diretamente relacionada ao uso de ritonavir na síndrome de imunodeficiência adquirida felina.

---

## Informações de Comercialização no Brasil

Os dados detalhados dos registros (número, nome comercial, forma farmacêutica, indicação aprovada) não foram populados neste Evidence Pack. O sistema confirma a existência de **20 registros ativos** de ritonavir no Brasil, com situação de comercialização ativa.

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
Apesar da pontuação TxGNN elevada (99,92%), as evidências de suporte para esta indicação específica são praticamente inexistentes: o único ensaio identificado é um estudo em humanos sem relação direta com o contexto veterinário felino, e não há literatura publicada sobre o uso de ritonavir em gatos com FIV. Somam-se a isso diferenças biológicas relevantes entre as proteases do FIV e do HIV-1, e o fato de se tratar de uma indicação veterinária — inteiramente fora do escopo regulatório humano coberto por este pipeline.

**Para prosseguir, é necessário:**
- Busca ativa de estudos veterinários publicados sobre inibidores de protease em modelos felinos de FIV
- Obtenção de dados in vitro de atividade de ritonavir especificamente contra a protease do FIV
- Definição do escopo de desenvolvimento: indicação veterinária ou humana — caminhos regulatórios e de investimento são completamente distintos
- Auditoria da base de dados de evidências para corrigir o possível erro de categorização (NCT02770508 vinculado à doença felina)
- Resgate dos dados completos de registro ANVISA (indicações aprovadas, formas farmacêuticas disponíveis, advertências da bula)
- Obtenção dos dados de MOA a partir do DrugBank API (remediação prevista no DG002 do Evidence Pack)
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

