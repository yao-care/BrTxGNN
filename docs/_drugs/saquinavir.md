---
layout: default
title: Saquinavir
parent: 僅模型預測 (L5)
nav_order: 435
evidence_level: L5
indication_count: 6
---

# Saquinavir
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

Usando o skill `txgnn-pipeline` para orientar o formato e contexto do relatório. Vou agora gerar o relatório completo com base no Evidence Pack fornecido.

---

# Saquinavir: Do HIV/AIDS à infecção por vírus da imunodeficiência símia (SIV)

## Resumo em Uma Frase

Saquinavir é o primeiro inibidor de protease do HIV aprovado pelo FDA (1995), utilizado como componente da terapia antirretroviral combinada (HAART) no tratamento da infecção por HIV/AIDS.
O modelo TxGNN prevê que pode ser eficaz para a **infecção por vírus da imunodeficiência símia (Simian Immunodeficiency Virus Infection)**, atualmente sem **ensaios clínicos registrados** e com **4 publicações** apoiando esta direção — todas em contexto pré-clínico ou animal.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | HIV/AIDS — terapia antirretroviral combinada (dados de registro ANVISA não disponíveis neste pacote) |
| Nova Indicação Prevista | Infecção por vírus da imunodeficiência símia (SIV) |
| Pontuação de Previsão TxGNN | 99,97% |
| Nível de Evidência | L3 |
| Situação no Mercado Brasileiro | ✓ Comercializado |
| Número de Registros | 14 |
| Decisão Recomendada | Hold |

---

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação disponíveis neste pacote de evidências. Com base no conhecimento amplamente estabelecido na literatura científica, Saquinavir é um inibidor competitivo da protease do HIV-1 — enzima viral essencial para a clivagem de poliproteínas precursoras (Gag-Pol) durante a maturação de viriões infecciosos. Sem essa clivagem, as partículas virais produzidas são estruturalmente imaturas e incapazes de infectar novas células.

O vírus da imunodeficiência símia (SIV) é filogeneticamente próximo ao HIV-1 e compartilha alta homologia estrutural na região da protease viral. Estudos in vitro confirmam que a protease do SIVmac239 é susceptível à inibição por saquinavir com EC₅₀ de 55 ± 3 nM, valor comparável ao obtido para HIV-1 (47 ± 10 nM), demonstrando que a actividade inibitória se preserva entre espécies virais aparentadas. Esta similaridade molecular é suficiente para justificar a elevada pontuação TxGNN.

**Importante ressalva clínica:** SIV infecta exclusivamente primatas não-humanos (macaco rhesus, chimpanzé etc.) e não representa uma doença humana com cenário terapêutico directo. O contexto de aplicação é restrito à investigação básica — nomeadamente como modelo animal para estudar a neuroAIDS, reservatórios virais no SNC e eficácia de regimes HAART. Esta previsão reflecte a homologia biológica explorada pelo grafo de conhecimento do TxGNN, e não configura oportunidade de reposicionamento clínico convencional.

---

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados para esta indicação.

---

## Evidências da Literatura

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|-----------|-------------------|
| [12709355](https://pubmed.ncbi.nlm.nih.gov/12709355/) | 2003 | In Vitro / Pré-clínico | Antimicrob Agents Chemother | SIVmac239 é inibido por saquinavir com EC₅₀ de 55 ± 3 nM, comparável ao HIV-1 (47 ± 10 nM); confirma susceptibilidade cruzada da protease SIV a inibidores de protease do HIV |
| [15040537](https://pubmed.ncbi.nlm.nih.gov/15040537/) | 2004 | In Vitro Comparativo | Antiviral Therapy | 16 fármacos antirretrovirais aprovados avaliados contra HIV-2, SIV e SHIV; saquinavir demonstra actividade anti-SIV e anti-SHIV, com implicações para profilaxia pós-exposição em laboratório |
| [20497048](https://pubmed.ncbi.nlm.nih.gov/20497048/) | 2010 | Estudo Animal (Macaco) | J Infect Dis | HAART (contendo saquinavir) reduz replicação viral e inflamação no SNC de macacos infectados por SIV, porém o DNA viral persiste; modelo relevante para neuroAIDS |
| [16809296](https://pubmed.ncbi.nlm.nih.gov/16809296/) | 2006 | Biologia Estrutural | J Virology | Análise do resíduo invariante Thr80 na protease do HIV-1; dados estruturais com implicações para a compreensão da selectividade de inibidores de protease entre HIV-1 e SIV |

---

## Informações de Comercialização no Brasil

Saquinavir possui **14 registros** ativos no mercado brasileiro (situação: comercializado). Os dados detalhados de nome comercial, forma farmacêutica e indicação aprovada por produto não constam neste pacote de evidências. Recomenda-se consulta direta à base de dados da ANVISA (Consulta de Produtos Registrados) para informações completas dos registros vigentes.

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
A previsão TxGNN para infecção por SIV é mecanisticamente coerente — a elevada homologia estrutural entre as proteases de SIV e HIV-1 fundamenta a susceptibilidade cruzada observada in vitro — mas o SIV não é uma doença humana, pelo que esta indicação não representa uma oportunidade de reposicionamento clínico com impacto em pacientes.

**Para prosseguir, é necessário:**

- **Redirecionar análise para indicações com relevância clínica humana:** este pacote contém indicações de maior impacto terapêutico com evidências mais robustas:
  - **Rank 5 — AIDS Related Complex (ARC):** nível L1, 8 ensaios clínicos (incluindo Phase 3 com n=3.000), decisão *Proceed with Guardrails* — representa a oportunidade de reposicionamento com maior base de evidências
  - **Rank 6 — HIV Congénito (vertical):** nível L2, 1 ensaio clínico pediátrico directo com saquinavir/ritonavir (NCT00623597, n=18), decisão *Research Question* — potencial para desenvolvimento pediátrico
- Obter dados regulatórios detalhados dos 14 registros ANVISA (nome comercial, forma farmacêutica, indicação aprovada)
- Recuperar o mecanismo de ação completo via DrugBank API (dados actualmente ausentes neste pacote — DG002)
- Consultar a bula ANVISA para advertências e contra-indicações (DG001 — severidade Blocking para avaliação de segurança)
- Caso o objectivo seja utilização de Saquinavir em modelos animais SIV (investigação básica), esta previsão é suporte válido; nesse caso, definir protocolo de modelo animal e parceiros de investigação
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

