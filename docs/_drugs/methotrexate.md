---
layout: default
title: Methotrexate
parent: 僅模型預測 (L5)
nav_order: 347
evidence_level: L5
indication_count: 10
---

# Methotrexate
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

O skill `txgnn-pipeline` confirma o contexto do projecto. A tarefa aqui é gerar um relatório de avaliação de reposicionamento seguindo o formato do Prompt v5. Vou proceder directamente com a geração do relatório a partir do Evidence Pack.

---

# Metotrexato: De Neoplasias e Doenças Autoimunes ao Blastoma Pulmonar

## Resumo em Uma Frase

Metotrexato (MTX) é um antimetabólito clássico utilizado há décadas no tratamento de neoplasias hematológicas e sólidas — linfomas, leucemias, osteossarcoma — e de doenças autoimunes como artrite reumatoide e psoríase. O modelo TxGNN prevê que pode ser eficaz para **Blastoma Pulmonar (Pulmonary Blastoma)**, porém **não há ensaios clínicos nem publicações científicas** que investiguem diretamente essa aplicação. A previsão baseia-se exclusivamente em similaridades no grafo de conhecimento biológico, sem qualquer validação empírica disponível até o momento.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Neoplasias (linfomas, leucemias, osteossarcoma) e doenças autoimunes (artrite reumatoide, psoríase) |
| Nova Indicação Prevista | Blastoma Pulmonar (Pulmonary Blastoma) |
| Pontuação de Previsão TxGNN | 99,45% |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | ✗ Não comercializado |
| Número de Registros | 0 |
| Decisão Recomendada | Hold |

---

## Por que Esta Previsão é Razoável?

Metotrexato é um inibidor da diidrofolato redutase (DHFR), enzima essencial para a síntese de purinas e timidilato. Ao bloquear essa via, o MTX priva as células tumorais dos precursores necessários para a replicação do DNA, interrompendo efetivamente a divisão celular. Esse mecanismo é particularmente potente em tecidos com alta taxa proliferativa, o que conferiu ao MTX ampla aplicabilidade em cânceres hematológicos — e, em menor escala, em tumores sólidos — ao longo de décadas de uso clínico.

Blastoma pulmonar é uma neoplasia rara e agressiva de natureza bifásica, composta por elementos embrionários epiteliais (semelhantes ao adenocarcinoma fetal bem diferenciado) e por um componente mesenquimal semelhante a sarcoma. Pela sua natureza de alta proliferação celular e pela similaridade biológica com outros tumores embrionários onde agentes antimetabólitos já foram explorados, a previsão do modelo TxGNN possui coerência mecanística em nível teórico.

Contudo, blastoma pulmonar é uma das neoplasias primárias de pulmão mais raras conhecidas, e **nenhum estudo clínico ou pré-clínico publicado** investigou o uso de MTX nesta indicação específica. A conexão mecanística permanece no nível de inferência computacional, sem suporte experimental ou clínico direto. O score elevado do modelo (99,45%) reflete principalmente padrões de similaridade no grafo de conhecimento biológico, e não deve ser interpretado como sinal de eficácia.

---

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados.

---

## Evidências da Literatura

Atualmente não há literatura relacionada.

---

## Citotoxicidade

| Item | Conteúdo |
|------|------|
| Classificação de Citotoxicidade | Citotóxico convencional — classe Antimetabólito / Antifolato |
| Risco de Mielossupressão | **Alto** — leucopenia, neutropenia e trombocitopenia são efeitos dose-dependentes esperados, especialmente com doses intermediárias e altas |
| Classificação de Emetogenicidade | Baixa a Moderada (dose-dependente; infusão IV em altas doses pode alcançar nível moderado) |
| Itens de Monitoramento | Hemograma completo com diferencial (CBC), creatinina e clearance renal, TGO / TGP / bilirrubinas, nível sérico de MTX — obrigatório leucovorin rescue em doses altas |
| Proteção no Manuseio | **Obrigatório** — preparo em cabine de segurança biológica (Classe II B2), EPI completo, descarte conforme regulamentação de resíduos citotóxicos (RDC ANVISA) |

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
Não existem evidências clínicas ou pré-clínicas publicadas que avaliem o Metotrexato especificamente para blastoma pulmonar. A previsão de 99,45% pelo modelo TxGNN reflete similaridade computacional no grafo de conhecimento, mas não constitui evidência de eficácia — e a raridade extrema desta neoplasia torna ainda mais improvável que dados clínicos existam em volume suficiente para avaliação nos próximos anos.

**Para prosseguir, é necessário:**
- Estudos pré-clínicos (in vitro e in vivo) em linhagens celulares e modelos animais de blastoma pulmonar para verificar atividade antiproliferativa do MTX
- Caracterização da expressão de DHFR e receptores de folato (FRα) nesta neoplasia
- Revisão de séries de casos e relatos de blastoma pulmonar para mapear agentes com atividade relatada
- Obtenção de dados de segurança via ANVISA (bula oficial) para suprir as lacunas de advertências e contraindicações
- Consulta ao DrugBank API para formalizar o perfil de MOA e interações medicamentosas
- Avaliação de indicações com evidência mais robusta neste mesmo Evidence Pack (ex.: linfoma de Hodgkin — L2, Proceed with Guardrails) como prioridade de investigação paralela
---

