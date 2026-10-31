---
layout: default
title: Ceftriaxone
parent: Apenas Predição do Modelo (L5)
nav_order: 211
evidence_level: L5
indication_count: 7
monitor_inn: "Ceftriaxone"
predicted_indications: ["hyperamylasemia", "polyclonal hyperviscosity syndrome", "congenital analbuminemia", "infectious otitis media", "blood group incompatibility", "suppurative otitis media", "chronic otitis media"]
last_modified_at: 2026-10-31
description: "Ceftriaxone: nova indicação prevista, Hiperamilasemia (nível de evidência L5). Indicação original: Cefalosporinas"
---

# Ceftriaxone
{: .fs-9 }

Nível de evidência: **L5** | Indicações previstas: **7** 
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

## Ceftriaxona: De classe das cefalosporinas a hiperamilasemia
{: .text-alpha }

## Resumo em Uma Frase

A ceftriaxona é um antibiótico cefalosporínico, comercializado no Brasil com o registro descrito apenas como "cefalosporinas".
O modelo TxGNN prevê que ela poderia ser útil para **hiperamilasemia (hyperamylasemia)**. Porém, não há **nenhum ensaio clínico** e há apenas **3 publicações** associadas, e nenhuma delas testa a ceftriaxona como tratamento dessa condição.
Esta previsão tem pouco respaldo e provavelmente é um artefato do modelo.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Cefalosporinas (texto do registro, que indica a classe do fármaco e não uma doença) |
| Nova Indicação Prevista | Hiperamilasemia |
| Pontuação de Previsão TxGNN | 0,9939 |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | Comercializado (registros ativos: 15 de 54) |
| Número de Registros | 54 (ativos: 15) |
| Decisão Recomendada | Hold |

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação nos dados compilados para este relatório. Segundo informações conhecidas, a ceftriaxona é um antibiótico beta-lactâmico da classe das cefalosporinas e atua inibindo a síntese da parede celular bacteriana. Seu uso estabelecido é o tratamento de infecções bacterianas.

A hiperamilasemia é um achado laboratorial (amilase elevada no sangue), não uma infecção, e portanto não há alvo antibiótico definido. Não foi identificado vínculo mecanístico plausível entre o fármaco e essa condição. A pontuação alta do TxGNN provavelmente reflete proximidade na rede de conhecimento, não farmacologia.

A relação pode até ser inversa. A ceftriaxona está associada a lama biliar e pseudolitíase, que podem causar pancreatite e elevar a amilase. O fármaco pode, portanto, causar esse achado em vez de tratá-lo.

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados.

## Evidências da Literatura

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [7522351](https://pubmed.ncbi.nlm.nih.gov/7522351/) | 1994 | Coorte | Southern Medical Journal | Em 38 pacientes com hemorragia intracraniana, 25 tiveram lipase elevada e 17 desses também tiveram amilase elevada, sem pancreatite. Estuda a hiperamilasemia, mas não avalia a ceftriaxona. |
| [10458061](https://pubmed.ncbi.nlm.nih.gov/10458061/) | 1999 | Estudo clínico (desenho pouco claro) | Bratislavske Lekarske Listy | Ceftriaxona 1 g como profilaxia em 30 pacientes após papilosfincterotomia endoscópica, comparados com 30 sem antibiótico. As bactérias da bile eram sensíveis à ceftriaxona. O trecho disponível não mostra resultado sobre amilase. |
| [36263834](https://pubmed.ncbi.nlm.nih.gov/36263834/) | 2023 | Relato de caso | Revista Española de Enfermedades Digestivas | Síndrome de Weil (leptospirose grave) com hemorragia digestiva alta. É um relato isolado, sem evidência de benefício da ceftriaxona sobre a hiperamilasemia. |

## Informações de Comercialização no Brasil

| Registro | Produto | Empresa detentora | Situação |
|------|------|------|------|
| 100430706 | CEFTRIAXONA DISSÓDICA HEMIEPTAIDRATADA | EUROFARMA LABORATORIOS S.A. | Ativo |
| 100430710 | CEFTRIAXONA DISSÓDICA HEMIEPTAIDRATADA | EUROFARMA LABORATORIOS S.A. | Ativo |
| 100431422 | TRIAXIN | EUROFARMA LABORATORIOS S.A. | Ativo |
| 100630003 | AMPLOSPEC | INSTITUTO BIOCHIMICO INDÚSTRIA FARMACÊUTICA LTDA | Ativo |
| 101000132 | ROCEFIN | PRODUTOS ROCHE QUÍMICOS E FARMACÊUTICOS S.A. | Ativo |
| 103700348 | TEUCEF | LABORATÓRIO TEUTO BRASILEIRO S/A | Ativo |
| 103700712 | CEFTRIAXONA DISSÓDICA | LABORATÓRIO TEUTO BRASILEIRO S/A | Ativo |
| 110110018 | CEFTRIAXONA DISSÓDICA HEMIEPTAIDRATADA | NEWCOM FARMACEUTICA LTDA. | Ativo |
| 110110046 | CEFTRIONA | NEWCOM FARMACEUTICA LTDA. | Ativo |
| 116370101 | TRIAXTON | BLAU FARMACÊUTICA S.A. | Ativo |
| 116370174 | CEFTRIAXONA DISSÓDICA | BLAU FARMACÊUTICA S.A. | Ativo |
| 116370179 | CEFTRIAXONA DISSÓDICA | BLAU FARMACÊUTICA S.A. | Ativo |
| 155620009 | KEFTRON | ANTIBIÓTICOS DO BRASIL LTDA | Ativo |
| 155620054 | CEFTRIAXONA DISSÓDICA HEMIEPTAIDRATADA | ANTIBIÓTICOS DO BRASIL LTDA | Ativo |
| 174200016 | CEFTRIAXONA SÓDICA | EUGIA PHARMA INDUSTRIA FARMACEUTICA LTDA | Ativo |
| 100410189 | CEFTRIONA | FRESENIUS KABI BRASIL LTDA | Cancelado |
| 100410211 | CEFTRIAXONA DISSÓDICA HEMIEPTAIDRATADA | FRESENIUS KABI BRASIL LTDA | Cancelado |
| 100410230 | CEFTRIAXONA DISSÓDICA HEMIEPTAIDRATADA | FRESENIUS KABI BRASIL LTDA | Cancelado |
| 100431011 | TRIAXIN | EUROFARMA LABORATORIOS S.A. | Cancelado |
| 100470438 | CEFTRIAXONA | SANDOZ DO BRASIL INDÚSTRIA FARMACÊUTICA LTDA | Cancelado |
| 100680879 | CEFTRIAXONA SÓDICA | NOVARTIS BIOCIENCIAS S.A | Cancelado |
| 102350350 | CEFTRIAX | EMS S/A | Cancelado |
| 102350450 | CEFTRIAXONA SODICA | EMS S/A | Cancelado |
| 102700088 | TRIAXTON | ARISTON INDS QUIMS FTCAS LTDA | Cancelado |
| 103110145 | CEFTRIAXONA DISSÓDICA | HALEX ISTAR INDÚSTRIA FARMACÊUTICA SA | Cancelado |
| 103920049 | TRAXON | VITAMEDIC INDUSTRIA FARMACEUTICA LTDA | Cancelado |
| 104080065 | CEFTRIAXONA | ROYTON QUÍMICA FARMACÊUTICA LTDA | Cancelado |
| 104650135 | NEOCEFTRIONA | LABORATÓRIO NEO QUÍMICA COMÉRCIO E INDÚSTRIA LTDA | Cancelado |
| 104650398 | CEFTRIAXONA SODICA | LABORATÓRIO NEO QUÍMICA COMÉRCIO E INDÚSTRIA LTDA | Cancelado |
| 104970178 | TRIOXINA | UNIÃO QUÍMICA FARMACÊUTICA NACIONAL S/A | Cancelado |

A tabela mostra até 30 registros (os ativos primeiro). A lista completa está na consulta de medicamentos da ANVISA (https://consultas.anvisa.gov.br/#/medicamentos/).

Os registros listados são de medicamentos com ceftriaxona isolada. O texto de indicação registrado indica apenas a classe farmacológica. Hiperamilasemia não consta como indicação em nenhum deles.

## Considerações de Segurança

- **Relações de contraindicação no grafo de conhecimento** (não vêm do texto da bula): doença hepática, doença da vesícula biliar, icterícia neonatal, colite por *Clostridium difficile*, enterocolite necrosante perinatal e anemia hemolítica.
- **Interações medicamentosas** (100 interações registradas):
  - **Graves:** cloreto de cálcio, glucoheptonato de cálcio e gluconato de cálcio.
  - **Moderadas:** canamicina, neomicina, estreptomicina e ácido picossulfúrico.
  - Há ainda interações de gravidade não classificada, por exemplo com anfotericina B, ácido acetilsalicílico, amoxicilina e pantoprazol.

Consulte a bula para as advertências e contraindicações oficiais.

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
- Não há ensaios clínicos nem estudo que teste a ceftriaxona para hiperamilasemia, e não existe mecanismo plausível. O nível de evidência é L5.
- A ceftriaxona pode elevar a amilase indiretamente, por lama biliar e pancreatite, o que torna a hipótese ainda menos favorável.

**Para prosseguir, seria necessário:**
- Obter e analisar a bula da ANVISA, com advertências e contraindicações oficiais.
- Obter dados de mecanismo de ação no DrugBank.
- Identificar uma justificativa biológica ou clínica para tratar uma alteração laboratorial com antibiótico, o que hoje não existe.
- Se houver interesse no tema, investigar a ceftriaxona como causa de hiperamilasemia e pancreatite biliar, em vez de tratamento.
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

