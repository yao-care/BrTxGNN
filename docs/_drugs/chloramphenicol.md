---
layout: default
title: Chloramphenicol
parent: Apenas Predição do Modelo (L5)
nav_order: 219
evidence_level: L5
indication_count: 8
last_modified_at: 2026-11-24
monitor_inn: "chloramphenicol"
predicted_indications: ["diffuse scleroderma", "postinfectious vasculitis", "post-bacterial disorder", "post-infectious syndrome", "infective urethral stricture", "Chagas cardiomyopathy", "infection-related hemolytic uremic syndrome", "punctate epithelial keratoconjunctivitis"]
description: "Chloramphenicol: nova indicação prevista, Esclerodermia difusa (diffuse scleroderma) (nível de evidência L5). Indicação original: CLORANFENICOL E ANALOGOS"
---

# Chloramphenicol
{: .fs-9 }

Nível de evidência: **L5** | Indicações previstas: **8** 
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

## Chloramphenicol: Esclerodermia difusa (diffuse scleroderma)
{: .text-alpha }

## Resumo em Uma Frase

Cloranfenicol é um antibiótico de amplo espectro que atua inibindo a síntese de proteínas bacterianas.
O modelo TxGNN prevê que pode ser eficaz para **esclerodermia difusa (diffuse scleroderma)**, mas **não há ensaios clínicos** e as **4 publicações** encontradas são estudos básicos in vitro sobre a regulação do gene do colágeno em fibroblastos, sem relação demonstrada com o fármaco.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | CLORANFENICOL E ANALOGOS; CICATRIZANTES; OUTROS MEDICAMENTOS COM ACAO NO APARELHO VISUAL |
| Nova Indicação Prevista | Esclerodermia difusa (diffuse scleroderma) |
| Pontuação de Previsão TxGNN | 0.9965 |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | Comercializado (registros ativos: 7 de 8) |
| Número de Registros | 8 (ativos: 7) |
| Decisão Recomendada | Hold |

## Por que Esta Previsão é Razoável?

Segundo as seções “Clinical Pharmacology” e “Microbiology” da bula aprovada pela FDA dos EUA (Prescribing Information) para Chloramphenicol (tradução não oficial): “O cloranfenicol é um antibiótico de amplo espectro originalmente isolado de Streptomyces venezuelae. Ele inibe a síntese proteica bacteriana ao interferir na transferência de aminoácidos ativados do RNA solúvel para os ribossomos.” Texto original em inglês: "Chloramphenicol is a broad-spectrum antibiotic originally isolated from Streptomyces venezuelae. It inhibits bacterial protein synthesis by interfering with the transfer of activated amino acids from soluble RNA to ribosomes." ([DailyMed: chloramphenicol sodium succinate prescribing information, Fresenius Kabi USA, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=aed29594-211d-49ef-813f-131975a8d0e3), versão de 2024-10-10; acessado em 2026-11-19). Pelo conhecimento geral, o cloranfenicol é um antibiótico que bloqueia a síntese proteica bacteriana, e não há mecanismo farmacológico estabelecido que o ligue à esclerodermia difusa.

As publicações recuperadas tratam da regulação do gene do pró-colágeno α1(I) em fibroblastos de esclerodermia (promotor, Smad3/Sp1/p300, sinalização do TGF-β). Os títulos não mencionam o cloranfenicol. A associação provavelmente é um artefato de ensaios com gene repórter (cloranfenicol acetiltransferase, CAT), e não um efeito farmacológico.

Portanto, a pontuação alta do modelo não é sustentada por evidência clínica ou mecanística. Além disso, o uso sistêmico do cloranfenicol traz risco de toxicidade medular, desfavorável para uma doença crônica autoimune e fibrosante.

## Evidências da Literatura

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [8702443](https://pubmed.ncbi.nlm.nih.gov/8702443/) | 1996 | Pesquisa básica (in vitro) | Arthritis and Rheumatism | Ativação transcricional do gene COL1A1 em fibroblastos dérmicos de esclerose sistêmica difusa; papel de sequências intrônicas |
| [9811061](https://pubmed.ncbi.nlm.nih.gov/9811061/) | 1998 | Pesquisa básica (in vitro) | Arthritis and Rheumatism | Elementos do promotor de COL1A1 envolvidos na sua expressão aumentada na esclerose sistêmica |
| [11229480](https://pubmed.ncbi.nlm.nih.gov/11229480/) | 2001 | Pesquisa básica (in vitro) | Arthritis and Rheumatism | O bloqueio da sinalização do TGF-β previne a síntese aumentada de colágeno em fibroblastos de esclerodermia |
| [16319104](https://pubmed.ncbi.nlm.nih.gov/16319104/) | 2006 | Pesquisa básica (in vitro) | Rheumatology (Oxford) | Smad3 fosforilado de forma constitutiva interage com Sp1 e p300 em fibroblastos de esclerodermia |

Nenhum desses estudos avalia o cloranfenicol como tratamento.

## Informações de Comercialização no Brasil

<!-- licenses:begin -->

| Registro | Produto | Situação |
|------|------|------|
| 102980017 | FIBRINASE COM CLORANFENICOL | Ativo |
| 102980493 | REGENCEL | Ativo |
| 102980505 | KOLLAGENASE COM CLORANFENICOL | Ativo |
| 103720287 | DBRIZ | Ativo |
| 105530259 | IRUXOL | Ativo |
| 116370118 | ARIFENICOL | Ativo |
| 156510092 | KOLPOCERVIX | Ativo |
| 100410201 | SUCCINATO SÓDICO DE CLORANFENICOL | Cancelado |

<!-- licenses:end -->

<!-- review:begin br-lic-20261124b-chloramphenicol-1 -->

> **Correção de verificação (2026-11-24)**: Texto original: “A lista mostra os 5 principais registros; há” Removido: a frase descrevia quantos registros a tabela antiga mostrava; a tabela de registros desta seção agora é gerada por programa a partir dos dados abertos de medicamentos da ANVISA (os ativos primeiro), e os números atualizados estão no resumo rápido. Fonte: [ANVISA – Dados abertos de medicamentos](https://dados.anvisa.gov.br/dados/DADOS_ABERTOS_MEDICAMENTOS.csv).

<!-- review:end br-lic-20261124b-chloramphenicol-1 -->

Há 8 registros no total, dos quais 7 estão válidos.

## Considerações de Segurança

- **Interações Medicamentosas**: foram identificadas 478 interações. Entre as listadas, as de nível maior são com **cisaprida** e **naloxegol**. Há interações moderadas com metronidazol, budesonida, aprepitanto, sulfonilureias (clorpropamida, glimepirida, glipizida, glibenclamida), repaglinida, rosuvastatina, sinvastatina, saxagliptina, ferro, entre outras.
- Para advertências e contraindicações de bula, consulte a bula.

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
- A previsão se baseia apenas no modelo (L5): não há ensaios clínicos e a literatura são estudos in vitro sem relação farmacológica com o cloranfenicol, provavelmente um artefato de ensaio com gene repórter CAT.
- O risco de toxicidade medular do uso sistêmico é desfavorável para uma doença crônica.

**Para prosseguir, é necessário:**
- Dados de mecanismo de ação do fármaco
- Evidência pré-clínica que demonstre efeito antifibrótico real do cloranfenicol, independente de ensaios com repórter CAT
- Advertências e contraindicações extraídas das bulas da ANVISA
- Avaliação de segurança hematológica caso se considere o uso sistêmico

<!-- review:begin log -->

## Registro de verificação

Abaixo está o registro de verificação desta página: afirmações conferidas com os dados oficiais de registro (dados abertos de medicamentos da ANVISA). As correções se limitam a fatos básicos; as previsões do modelo, os níveis de evidência e as conclusões não foram reescritos. A frase que dizia não haver dados sobre o mecanismo de ação foi substituída por um trecho da bula oficial citada (com tradução não oficial).

| Data da verificação | Item | Ação | Fonte |
|------|------|------|------|
| 2026-11-19 | Frase “não há dados sobre o mecanismo de ação” substituída por trecho da bula dos EUA | Frase sobre a falta de dados do mecanismo de ação substituída por um trecho com fonte | [DailyMed: chloramphenicol sodium succinate prescribing information, Fresenius Kabi USA, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=aed29594-211d-49ef-813f-131975a8d0e3) |
| 2026-11-24 | “A lista mostra os 5 principais registros; há” → “Há” | Corrigido | [ANVISA – Dados abertos de medicamentos](https://dados.anvisa.gov.br/dados/DADOS_ABERTOS_MEDICAMENTOS.csv) |

<!-- review:end log -->

## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

