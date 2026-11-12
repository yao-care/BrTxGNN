---
noindex: true
sitemap: false
layout: default
title: Atezolizumabe
parent: Apenas Predição do Modelo (L5)
nav_order: 86
evidence_level: L5
indication_count: 0
last_modified_at: 2026-11-12
predicted_indications: []
---

# Atezolizumabe
{: .fs-9 }

Nível de evidência: **L5** | Indicações previstas: **0** 
{: .fs-6 .fw-300 }

---

## Índice
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Relatório de avaliação farmacêutica

</div>

## Atezolizumabe: Avaliação de Reposicionamento — Sem Previsão TxGNN Disponível
{: .text-alpha }

---

## Resumo em Uma Frase

Atezolizumabe é um anticorpo monoclonal anti-PD-L1 (inibidor de checkpoint imunológico) utilizado no tratamento oncológico.
O Evidence Pack atual **não contém previsões TxGNN** para novas indicações — o pipeline de predição não retornou candidatos para este fármaco.
As lacunas de dados de severidade *Blocking* e *High* precisam ser corrigidas antes de qualquer análise de reposicionamento.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|----------|
| Indicação Original | Não disponível no Evidence Pack |
| Nova Indicação Prevista | Sem previsão TxGNN disponível |
| Pontuação de Previsão TxGNN | — |
| Nível de Evidência | N/D (nenhuma previsão gerada) |
| Situação no Mercado Brasileiro | Comercializado (registros ativos: 1 de 1) |
| Número de Registros | 1 (ativos: 1) |
| Decisão Recomendada | **Hold** |

---

## Por que Esta Previsão é Razoável?

Esta seção não é aplicável no momento — o Evidence Pack não contém previsões TxGNN para atezolizumabe, e portanto não há relação de reposicionamento a avaliar.

Atualmente, não há dados detalhados sobre o mecanismo de ação no Evidence Pack. Com base em informações conhecidas, atezolizumabe é um anticorpo monoclonal humanizado da classe IgG1 que se liga à proteína PD-L1 (*Programmed Death-Ligand 1*), bloqueando sua interação com os receptores PD-1 e B7.1 nos linfócitos T. Este mecanismo desinibe a resposta imunológica antitumoral, potencialmente aplicável a qualquer neoplasia com expressão de PD-L1.

Para que a análise de reposicionamento possa ser conduzida, é necessário primeiro corrigir as lacunas de dados identificadas (DG001 e DG002) e reexecutar o pipeline TxGNN.

---

## Informações de Comercialização no Brasil

O fármaco consta como **comercializado** com **1 registro** no mercado brasileiro.

<!-- review:begin br-lic-20261106-atezolizumabe-1 -->

> **Correção de verificação (2026-11-06)**: Texto original: “O fármaco consta como **comercializado** com **1 registro** no mercado brasileiro. No entanto, os detalhes do registro (número, nome comercial, forma farmacêutica e indicação aprovada) **não estão disponíveis** no Evidence Pack atual — os campos retornaram vazios na consulta à base regulatória.” Removido: a descrição dos produtos não correspondia aos dados de registro (dados abertos de medicamentos da ANVISA, em 2026-11-06). Nos dados (dados abertos de medicamentos da ANVISA) constam 1 registros para este medicamento, 1 válidos; os números atualizados estão no resumo rápido e nas informações de comercialização. Fonte: [ANVISA – Dados abertos de medicamentos](https://dados.anvisa.gov.br/dados/DADOS_ABERTOS_MEDICAMENTOS.csv).

<!-- review:end br-lic-20261106-atezolizumabe-1 -->

---

## Citotoxicidade

> Atezolizumabe é um antineoplásico da classe imunoterapia. Esta seção é exibida por se enquadrar nos critérios de fármaco antineoplásico.

| Item | Conteúdo |
|------|----------|
| Classificação de Citotoxicidade | Imunoterapia — Inibidor de Checkpoint Imunológico (anti-PD-L1); **não** é citotóxico convencional |
| Risco de Mielossupressão | Baixo (ação imunomediada; não suprime diretamente a medula óssea) |
| Classificação de Emetogenicidade | Mínima |
| Itens de Monitoramento | Função tireoidiana (TSH), enzimas hepáticas (ALT/AST), função pulmonar, glicemia, função suprarrenal, creatinina |
| Proteção no Manuseio | Seguir protocolos de anticorpos monoclonais; sem risco de citotoxicidade por contato direto |

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

> As advertências e contraindicações constam como lacuna de dados de severidade **Blocking** (DG001). A remediação recomendada é o download e análise do PDF da bula disponível na base regulatória.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
O Evidence Pack está incompleto em camadas críticas: nenhuma previsão TxGNN foi gerada e as informações de segurança apresentam lacunas classificadas como *Blocking* — tornando inviável qualquer recomendação de reposicionamento neste momento.

<!-- review:begin br-lic-20261106-atezolizumabe-2 -->

> **Correção de verificação (2026-11-06)**: Texto original: “O Evidence Pack está incompleto em camadas críticas: nenhuma previsão TxGNN foi gerada, os detalhes do registro regulatório estão vazios e as informações de segurança apresentam lacunas classificadas como *Blocking* — tornando inviável qualquer recomendação de reposicionamento neste momento.” Removido: a afirmação contradizia os dados de registro (dados abertos de medicamentos da ANVISA, em 2026-11-06). Nos dados (dados abertos de medicamentos da ANVISA) constam 1 registros para este medicamento, 1 válidos; os números atualizados estão no resumo rápido e nas informações de comercialização. Fonte: [ANVISA – Dados abertos de medicamentos](https://dados.anvisa.gov.br/dados/DADOS_ABERTOS_MEDICAMENTOS.csv).

<!-- review:end br-lic-20261106-atezolizumabe-2 -->

**Para prosseguir, é necessário:**
- **[DG001 — Blocking]** Baixar e analisar o PDF da bula para obter advertências principais e contraindicações
- **[DG002 — High]** Consultar a API do DrugBank para obter o DrugBank ID, MOA completo e categorias farmacológicas
- **Reexecutar o pipeline TxGNN** para gerar candidatos de novas indicações — sem previsões, o relatório de reposicionamento não pode ser produzido
- **Completar os dados de registro**: número de registro, nome comercial, forma farmacêutica e texto da indicação aprovada
- **Após obtenção das previsões**, retornar para avaliação completa, incluindo análise de ensaios clínicos e literatura

<!-- review:begin br-lic-20261106-atezolizumabe-3 -->

> **Correção de verificação (2026-11-06)**: Texto original: “**[DG001 — Blocking]** Baixar e analisar o PDF da bula (ANVISA/TFDA) para obter advertências principais e contraindicações” Removido: texto residual do modelo taiwanês (TFDA), que não se aplica a esta página. Fonte: [ANVISA – Dados abertos de medicamentos](https://dados.anvisa.gov.br/dados/DADOS_ABERTOS_MEDICAMENTOS.csv).

<!-- review:end br-lic-20261106-atezolizumabe-3 -->

<!-- review:begin log -->

## Registro de verificação

Abaixo está o registro de verificação desta página: afirmações conferidas com os dados oficiais de registro (dados abertos de medicamentos da ANVISA). As correções se limitam a fatos básicos; as previsões do modelo, os níveis de evidência e as conclusões não foram reescritos.

| Data da verificação | Item | Ação | Fonte |
|------|------|------|------|
| 2026-11-06 | Removido: “No entanto, os detalhes do registro (número, nome comercial, forma farmacêutica e indicação aprovada) **não estão disponíveis** no Evidence ” | Corrigido | [ANVISA – Dados abertos de medicamentos](https://dados.anvisa.gov.br/dados/DADOS_ABERTOS_MEDICAMENTOS.csv) |
| 2026-11-06 | Removido: “os detalhes do registro regulatório estão vazios” | Corrigido | [ANVISA – Dados abertos de medicamentos](https://dados.anvisa.gov.br/dados/DADOS_ABERTOS_MEDICAMENTOS.csv) |
| 2026-11-06 | Removido: “(ANVISA/TFDA)” | Corrigido | [ANVISA – Dados abertos de medicamentos](https://dados.anvisa.gov.br/dados/DADOS_ABERTOS_MEDICAMENTOS.csv) |

<!-- review:end log -->

## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

