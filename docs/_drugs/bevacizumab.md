---
layout: default
title: Bevacizumab
parent: Apenas Predição do Modelo (L5)
nav_order: 132
evidence_level: L5
indication_count: 10
monitor_inn: "Bevacizumab"
predicted_indications: ["epiglottis neoplasm", "benign neoplasm of tongue", "tumor of testis and paratestis", "benign neoplasm of hypopharynx", "benign neoplasm of floor of mouth", "cervical neuroblastoma", "cystic neoplasm", "nasal cavity inverting papilloma", "mesenchymoma", "schwannoma of jugular foramen"]
last_modified_at: 2026-11-24
description: "Bevacizumab: nova indicação prevista, neoplasia da epiglote (epiglottis neoplasm) (nível de evidência L5). No Brasil, registros na ANVISA: 12 (ativos: 10)"
---

# Bevacizumab
{: .fs-9 }

Nível de evidência: **L5** | Indicações previstas: **10** 
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

## Bevacizumabe: anticorpo monoclonal anti-VEGF-A → neoplasia da epiglote (epiglottis neoplasm)
{: .text-alpha }

## Resumo em Uma Frase

Bevacizumabe é um anticorpo monoclonal que neutraliza o fator de crescimento do endotélio vascular A (VEGF-A) e é usado em oncologia.
O modelo TxGNN prevê que pode ser eficaz para **neoplasia da epiglote (epiglottis neoplasm)**,
mas atualmente há **0 ensaios clínicos** e **0 publicações** apoiando esta direção específica; a previsão se baseia apenas no modelo computacional.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Não consta nos dados locais |
| Nova Indicação Prevista | neoplasia da epiglote (epiglottis neoplasm) |
| Pontuação de Previsão TxGNN | 0,9990 |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | Comercializado (registros ativos: 10 de 12) |
| Número de Registros | 12 (ativos: 10) |
| Decisão Recomendada | Hold |

## Por que Esta Previsão é Razoável?

Segundo a seção “Mechanism of Action” da bula aprovada pela FDA dos EUA (Prescribing Information) para Bevacizumab (tradução não oficial): “Os produtos de bevacizumabe se ligam ao VEGF e impedem a interação do VEGF com seus receptores (Flt-1 e KDR) na superfície das células endoteliais. A interação do VEGF com seus receptores leva à proliferação de células endoteliais e à formação de novos vasos sanguíneos em modelos in vitro de angiogênese.” Texto original em inglês: "Bevacizumab products bind VEGF and prevent the interaction of VEGF to its receptors (Flt-1 and KDR) on the surface of endothelial cells. The interaction of VEGF with its receptors leads to endothelial cell proliferation and new blood vessel formation in in vitro models of angiogenesis." ([DailyMed: Vegzelma (bevacizumab-adcd) prescribing information, CELLTRION USA, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=4cdcccda-7b9a-49d0-ac50-f4605a3c0ebe), versão de 2026-08-21; acessado em 2026-11-19). Segundo informações conhecidas, o bevacizumabe neutraliza o VEGF-A, bloqueando a angiogênese que sustenta o crescimento de tumores.

Tumores de cabeça e pescoço, região a que pertence a epiglote, costumam depender de vascularização, de modo que o bloqueio do VEGF-A é mecanisticamente plausível. Porém, a pontuação alta (0,9990) é apenas uma previsão computacional: não foram fornecidos ensaios clínicos nem literatura para esta doença, e a similaridade com as indicações originais ainda não foi avaliada.

## Informações de Comercialização no Brasil

<!-- licenses:begin -->

| Registro | Produto | Empresa detentora | Situação |
|------|------|------|------|
| 100330214 | ELOVIE | LIBBS FARMACÊUTICA LTDA | Ativo |
| 101000637 | AVASTIN | PRODUTOS ROCHE QUÍMICOS E FARMACÊUTICOS S.A. | Ativo |
| 102440012 | MVASI | AMGEN BIOTECNOLOGIA DO BRASIL LTDA. | Ativo |
| 103700790 | SIMBEVA | LABORATÓRIO TEUTO BRASILEIRO S/A | Ativo |
| 116640001 | ABEVMY | BIOCON BIOLOGICS DO BRASIL LTDA | Ativo |
| 121100474 | ZIRABEV | PFIZER BRASIL LTDA | Ativo |
| 133480004 | BEVYX | BIOMM SA | Ativo |
| 145310002 | BEVANOVIS | BIONOVIS S.A. - COMPANHIA BRASILEIRA DE BIOTECNOLO | Ativo |
| 159210006 | ONBEVZI | SAMSUNG BIOEPIS BR PHARMACEUTICAL LTDA. | Ativo |
| 192160005 | VEGZELMA | CELLTRION HEALTHCARE DISTRIBUICAO DE PRODUTOS FARM | Ativo |
| 167130002 | ABEVMY | EQUILIBRIO COMERCIO DE PRODUTOS FARMACEUTICOS LTDA | Cancelado |
| 188300094 | ABEVMY | VIATRIS FARMACEUTICA DO BRASIL LTDA | Cancelado |

<!-- licenses:end -->

Segundo os dados compilados, o medicamento consta como comercializado, com 10 registros válidos e 2 cancelados.

<!-- review:begin br-lic-20261124c-bevacizumab-1 -->

> **Correção de verificação (2026-11-24)**: Texto original: “A lista detalhada de registros (nome comercial, forma farmacêutica) não está disponível nos dados compilados.” Removido: a frase dizia que a lista de registros não estava disponível ou não seria apresentada; esta seção agora traz a tabela de registros gerada por programa a partir dos dados abertos de medicamentos da ANVISA, com todos os registros do medicamento nos dados (os números atualizados estão no resumo rápido e na tabela). Fonte: [ANVISA – Dados abertos de medicamentos](https://dados.anvisa.gov.br/dados/DADOS_ABERTOS_MEDICAMENTOS.csv).

<!-- review:end br-lic-20261124c-bevacizumab-1 -->

## Considerações de Segurança

- **Interações Medicamentosas**: foram identificadas 22 interações no total. As de gravidade **maior** incluem:
  - Deferipona
  - Samário (153Sm) lexidronato
  - Panitumumabe
  - Sunitinibe
  - Talidomida

  As demais são de gravidade **moderada**, entre elas bisfosfonatos (alendronato, risedronato, etidronato, ibandronato, pamidronato, tiludronato), fatores estimuladores de colônias (filgrastim, pegfilgrastim, sargramostim), palifermina, estrôncio-89, idelalisibe, rádio-223, romosozumabe e fosfato de sódio monobásico (P32).

Para advertências e contraindicações, consulte a bula.

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
- A previsão para neoplasia da epiglote (epiglottis neoplasm) tem apenas suporte computacional, sem ensaios clínicos nem publicações que estudem diretamente esta doença (nível L5).

**Para prosseguir, é necessário:**
- Levantamento de estudos pré-clínicos ou clínicos em neoplasias da epiglote ou da laringe
- Dados do mecanismo de ação detalhado
- Advertências e contraindicações extraídas da bula na ANVISA
- Análise da similaridade com as indicações já registradas e da compatibilidade de vias de administração

<!-- review:begin log -->

## Registro de verificação

Abaixo está o registro de verificação desta página: afirmações conferidas com os dados oficiais de registro (dados abertos de medicamentos da ANVISA). As correções se limitam a fatos básicos; as previsões do modelo, os níveis de evidência e as conclusões não foram reescritos. A frase que dizia não haver dados sobre o mecanismo de ação foi substituída por um trecho da bula oficial citada (com tradução não oficial).

| Data da verificação | Item | Ação | Fonte |
|------|------|------|------|
| 2026-11-19 | Frase “não há dados sobre o mecanismo de ação” substituída por trecho da bula dos EUA | Frase sobre a falta de dados do mecanismo de ação substituída por um trecho com fonte | [DailyMed: Vegzelma (bevacizumab-adcd) prescribing information, CELLTRION USA, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=4cdcccda-7b9a-49d0-ac50-f4605a3c0ebe) |
| 2026-11-24 | Removido: “A lista detalhada de registros (nome comercial, forma farmacêutica) não está disponível nos dados compilados.” | Corrigido | [ANVISA – Dados abertos de medicamentos](https://dados.anvisa.gov.br/dados/DADOS_ABERTOS_MEDICAMENTOS.csv) |

<!-- review:end log -->

## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

