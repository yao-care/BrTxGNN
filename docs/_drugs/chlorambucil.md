---
layout: default
title: Chlorambucil
parent: Evidência Moderada (L3-L4)
nav_order: 218
evidence_level: L4
indication_count: 8
---

# Chlorambucil
{: .fs-9 }

Nível de evidência: **L4** | Indicações previstas: **8** 
{: .fs-6 .fw-300 }

---

## Índice
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Relatório de avaliação farmacêutica

</div>

# Clorambucila: De outros antineoplásicos para leucemia linfocítica crônica (subtipo pré-centro germinativo)

## Resumo em Uma Frase

Clorambucila (chlorambucil) é um agente alquilante, registrado na ANVISA com a indicação genérica "outros antineoplásicos".
O modelo TxGNN prevê que pode ser eficaz para **leucemia linfocítica crônica / linfoma linfocítico de pequenas células do subtipo pré-centro germinativo (pregerminal center chronic lymphocytic leukemia/small lymphocytic lymphoma)**,
mas atualmente há **0 ensaios clínicos** e apenas **1 publicação** (uma revisão de 2003) apoiando esta direção. Trata-se, na prática, de uma doença em que o fármaco já é um tratamento estabelecido, e não de um reposicionamento genuíno.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Outros antineoplásicos |
| Nova Indicação Prevista | Leucemia linfocítica crônica/linfoma linfocítico de pequenas células do subtipo pré-centro germinativo (Pregerminal center CLL/SLL) |
| Pontuação de Previsão TxGNN | 99,72% |
| Nível de Evidência | L4 |
| Situação no Mercado Brasileiro | ✗ Apenas registros cancelados |
| Número de Registros | 1 |
| Decisão Recomendada | Hold |

---

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação na base compilada. Segundo informações conhecidas, a clorambucila é um agente alquilante da classe das mostardas nitrogenadas, que forma ligações cruzadas no DNA de células linfoides em proliferação. Seu uso em leucemia linfocítica crônica (LLC) e linfoma linfocítico de pequenas células (LLPC) é histórico, de modo que a aplicabilidade mecanística é plausível.

A indicação original registrada ("outros antineoplásicos") é genérica e inclui as neoplasias linfoides. A nova indicação prevista é um subtipo molecular da LLC/LLPC (tipo pré-centro germinativo, caracterizado por genes de imunoglobulina não mutados). Ou seja, a previsão recai sobre uma doença na qual o fármaco já é conhecido, e não sobre uma doença distante da original.

O único artigo disponível é uma revisão de 2003 sobre abordagem de LLC adaptada ao risco. Ele descreve os dois subtipos da doença, mas não demonstra eficácia específica da clorambucila no subtipo pré-centro germinativo. A pontuação TxGNN é muito alta, porém é apenas uma previsão computacional.

### Outras indicações previstas (resumo)

O modelo também previu outras indicações, todas com evidência limitada:

| Indicação prevista | Pontuação TxGNN | Nível | Observação |
|------|------|------|------|
| LLC/LLPC com hipermutação somática do gene IGHV | 99,72% | L5 | Subtipo geralmente mais indolente; sem dados específicos |
| Linfoma de grandes células B ALK-positivo | 99,61% | L5 | Linfoma raro e agressivo; sem estudos |
| Linfoma pulmonar primário | 99,42% | L3 | Maioria é linfoma MALT pulmonar; evidência indireta e retrospectiva (questão de pesquisa) |
| Adenocarcinoma fetal bem diferenciado do pulmão | 99,39% | L5 | Sem racional mecanístico evidente |
| Blastoma pulmonar | 99,37% | L5 | Sem estudos |
| Leucemia linfoblástica aguda | 99,25% | L4 | Apenas relatos de caso e estudos de resistência |
| Carcinoma de pulmão de pequenas células | 99,24% | L4 | Estudos históricos antigos e um estudo pré-clínico de 2026 |

---

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados.

---

## Evidências da Literatura

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [12577769](https://pubmed.ncbi.nlm.nih.gov/12577769/) | 2003 | Revisão | Nederlands Tijdschrift voor Geneeskunde | A LLC de células B é a leucemia mais comum no mundo ocidental e não é tão indolente quanto se pensava; descreve dois subtipos (pré-centro germinativo, com genes de imunoglobulina não mutados, e pós-centro germinativo) e defende uma abordagem adaptada ao risco |

---

## Informações de Comercialização no Brasil

| Número de Registro | Nome Comercial | Forma Farmacêutica | Indicação Aprovada |
|---------|------|------|-----------|
| Registro nº 137640148 (cancelado) | Leukeran | Não informada | Outros antineoplásicos |

---

## Citotoxicidade

| Item | Conteúdo |
|------|------|
| Classificação de Citotoxicidade | Citotóxico convencional (agente alquilante, classe das mostardas nitrogenadas) |
| Risco de Mielossupressão | Alto (dose-dependente; a mielossupressão é um efeito conhecido do fármaco, e a base compilada aponta neutropenia, trombocitopenia, leucopenia, linfopenia e anemia como contraindicações no grafo de conhecimento) |
| Classificação de Emetogenicidade | Baixa a média (formulação oral) |
| Itens de Monitoramento | Hemograma completo com diferencial, função hepática e renal; atenção a sinais neurológicos (convulsões) e pulmonares |
| Proteção no Manuseio | Necessário seguir os regulamentos de manuseio de citotóxicos |

---

## Considerações de Segurança

Os dados de advertências e contraindicações da bula não estão disponíveis na base compilada. Consulte a bula para esses itens.

- **Contraindicações/condições de risco segundo o grafo de conhecimento do TxGNN (PrimeKG; não são texto de bula):** epilepsia; trombocitopenia; síndrome nefrótica (incluindo as formas familiar e lipoide); neutropenia; agranulocitose; anemia (incluindo macrocítica); leucopenia; linfopenia; doença pulmonar intersticial; fibrose pulmonar (incluindo pós-inflamatória); lesão hepática induzida por fármacos; leucemias agudas (incluindo bilineal, de linhagem ambígua, indiferenciada, bifenotípica e de fenótipo misto).
- **Interações medicamentosas:** foram identificadas 167 interações no total. As de maior gravidade entre as listadas são:
  - **Maior:** deferiprona; samário (153Sm) lexidronam.
  - **Moderada:** anfotericina B (e formulações lipídica, com sulfato de colesterila e lipossomal), palifermina, cloranfenicol (inclusive oftálmico), mercaptopurina, roflumilaste, cloreto de estrôncio Sr-89.
  - **Menor:** levofloxacino.
  - Gravidade não classificada: mesalazina, omeprazol, prednisona, prednisolona, sinvastatina, varfarina, levotiroxina.
- **Segurança a longo prazo (literatura do indicador de linfoma pulmonar):** estudos de coorte e caso-controle em doença de Hodgkin apontam risco aumentado de segundas neoplasias (inclusive leucemia aguda e câncer de pulmão) após quimioterapia que inclui agentes alquilantes.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
- A clorambucila já é um agente consolidado em LLC/LLPC, então a previsão não representa um reposicionamento genuíno. Para o subtipo específico previsto, há apenas uma revisão de 2003 e nenhum ensaio clínico, o que corresponde a evidência de nível L4. Além disso, o único registro brasileiro está cancelado e faltam dados de bula e de mecanismo de ação.

**Para prosseguir, é necessário:**
- Obter e analisar a bula na ANVISA (advertências e contraindicações), pois esta lacuna impede a triagem de segurança.
- Obter os dados de mecanismo de ação no DrugBank.
- Confirmar a situação regulatória atual no Brasil (registro cancelado; verificar se há outro registro vigente ou alternativa disponível).
- Buscar estudos subtipo-específicos (por exemplo, status do IGHV) e comparações com os tratamentos atuais da LLC, como inibidores de BTK (o ensaio RESONATE-2 já mostrou superioridade do ibrutinibe frente à clorambucila).
- Entre as demais indicações, priorizar como questão de pesquisa o linfoma pulmonar primário (linfoma MALT), que tem evidência indireta (L3), com revisão sistemática de dados de clorambucila em linfoma MALT.
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

