---
layout: default
title: Citalopram
parent: 僅模型預測 (L5)
nav_order: 188
evidence_level: L5
indication_count: 5
---

# Citalopram
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

Usando o skill `txgnn-pipeline` para orientação de contexto TxGNN. Agora vou gerar o relatório completo com base no Evidence Pack fornecido.

---

# Citalopram: Do Transtorno Depressivo Maior ao Transtorno Obsessivo-Compulsivo

## Resumo em Uma Frase

Citalopram é um inibidor seletivo da recaptação de serotonina (ISRS), amplamente utilizado no tratamento do transtorno depressivo maior e reconhecido como referência desta classe farmacológica.
O modelo TxGNN prevê que pode ser eficaz para o **Transtorno Obsessivo-Compulsivo (obsessive-compulsive disorder)**, com pontuação de previsão de **99,74%** e nível de evidência pré-atribuído **L2**.
A consulta automatizada de evidências não retornou ensaios clínicos ou publicações específicas neste ciclo de coleta, sendo recomendada busca manual complementar para consolidar o dossiê.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Transtorno Depressivo Maior |
| Nova Indicação Prevista | Transtorno Obsessivo-Compulsivo (obsessive-compulsive disorder) |
| Pontuação de Previsão TxGNN | 99,74% |
| Nível de Evidência | L2 |
| Situação no Mercado Brasileiro | ✓ Já comercializado |
| Número de Registros | 20 |
| Decisão Recomendada | Proceed with Guardrails |

---

## Por que Esta Previsão é Razoável?

Citalopram pertence à classe dos ISRS e atua inibindo com alta seletividade o transportador de serotonina (SERT), elevando a disponibilidade sináptica de serotonina. Embora os dados detalhados de mecanismo de ação (MOA) não estejam disponíveis neste Evidence Pack, essa propriedade farmacológica fundamental é amplamente documentada na literatura científica e representa um dos perfis ISRS mais seletivos em uso clínico.

O transtorno obsessivo-compulsivo compartilha com a depressão uma base neurobiológica central: a disfunção do circuito orbitofrontal–estriatado (*orbitofrontal-striatal circuit*). Nesse circuito, a sinalização serotoninérgica deficiente gera a hiperatividade característica que se manifesta como pensamentos obsessivos e comportamentos compulsivos. A inibição do SERT pelo citalopram potencializa esse sinal, funcionando como correção direta do substrato patofisiológico do TOC — não apenas como efeito secundário, mas como mecanismo primário.

Essa relação não é meramente teórica: os ISRS são a opção farmacológica de primeira linha para o TOC nas diretrizes do APA, NICE e WHO. A pontuação TxGNN de 99,74% é coerente com esse alinhamento mecanístico e epidemiológico. A previsão do modelo reflete, portanto, uma extensão racionalmente fundamentada da indicação original.

---

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados na consulta automatizada deste ciclo.

> **Nota:** A ausência de resultados reflete a limitação da busca automatizada neste ciclo de coleta (data de corte: 2026-04-25), e não necessariamente a inexistência de ensaios clínicos publicados. Recomenda-se busca manual em ClinicalTrials.gov com os termos "citalopram OCD" e "citalopram obsessive-compulsive".

---

## Evidências da Literatura

Atualmente não há literatura relacionada na consulta automatizada deste ciclo.

> **Nota:** Analogamente aos ensaios clínicos, a busca automatizada retornou zero resultados para o par Citalopram × TOC. Dado que os ISRS possuem literatura extensa para essa indicação, recomenda-se busca manual no PubMed com MeSH terms: *("citalopram"[MeSH] AND "obsessive-compulsive disorder"[MeSH])*.

---

## Informações de Comercialização no Brasil

Citalopram possui **20 registros ativos na ANVISA** com situação **comercializado**. Os dados detalhados de cada registro (número de registro, nome comercial, forma farmacêutica, indicação aprovada) não foram retornados neste Evidence Pack. Recomenda-se consulta direta ao [Consulta de Medicamentos da ANVISA](https://consultas.anvisa.gov.br/) pelo nome do princípio ativo "CITALOPRAM" para obter o detalhamento completo dos registros vigentes.

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

> **Atenção:** Os dados de advertências, contraindicações e interações medicamentosas não estão disponíveis neste Evidence Pack (itens DG001 e DG002 pendentes). A obtenção da bula ANVISA é classificada como **bloqueadora** (DG001 — Severity: Blocking) para avançar à avaliação de segurança inicial (Estágio S1).

---

## Conclusão e Próximos Passos

**Decisão: Proceed with Guardrails**

**Justificativa:**
O citalopram possui mecanismo de ação (inibição seletiva do SERT) diretamente relacionado à neurobiologia do TOC, e a classe ISRS já constitui o padrão farmacológico de primeira linha para esta condição nas principais diretrizes internacionais — tornando esta previsão mecanisticamente robusta e clinicamente plausível. A pontuação TxGNN de 99,74% reforça a coerência do sinal preditivo.

**Para prosseguir, é necessário:**
- **[Bloqueador — DG001]** Obter bula ANVISA para levantar advertências e contraindicações, habilitando a entrada na avaliação de segurança (Estágio S1)
- **[Alta prioridade — DG002]** Complementar dados de MOA via DrugBank API para consolidar a análise de mecanismo
- Realizar nova consulta de evidências com termos expandidos (*"citalopram OCD"*, *"SSRI obsessive-compulsive disorder"*) para capturar ensaios clínicos e literatura relevantes não retornados neste ciclo
- Confirmar indicações aprovadas nos 20 registros ANVISA via consulta direta ao portal
- Verificar interações medicamentosas em bases alternativas (DDI retornou zero resultados neste ciclo)
---

