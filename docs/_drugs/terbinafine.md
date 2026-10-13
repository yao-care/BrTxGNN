---
layout: default
title: Terbinafine
parent: Apenas Predição do Modelo (L5)
nav_order: 614
evidence_level: L5
indication_count: 10
---

# Terbinafine
{: .fs-9 }

Nível de evidência: **L5** | Indicações previstas: **10** 
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

# Terbinafina: De antimicótico a furunculose miiásica (previsão do modelo, com ressalvas importantes)

## Resumo em Uma Frase

Terbinafina é um antifúngico (antimicótico), originalmente registrado no Brasil como antimicótico, inclusive para uso tópico.
A primeira previsão do modelo TxGNN é **miíase furuncular (furuncular myiasis)**, mas **não há ensaios clínicos** e a única publicação associada é **um relato de caso** que não demonstra eficácia do fármaco. Essa previsão parece ser um artefato do grafo de conhecimento. As previsões mais plausíveis (tinea manuum e micose superficial) estão dentro do uso antifúngico já estabelecido.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Antimicótico |
| Nova Indicação Prevista | Miíase furuncular (Furuncular Myiasis) |
| Pontuação de Previsão TxGNN | 96,74% |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | ✗ Somente registros cancelados |
| Número de Registros | 17 (todos cancelados) |
| Decisão Recomendada | Hold |

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação nos dados compilados para este relatório. Segundo informações conhecidas, a terbinafina é um antifúngico da classe das alilaminas, que inibe a enzima esqualeno epoxidase do fungo, reduzindo o ergosterol da membrana fúngica e acumulando esqualeno. Sua eficácia em infecções fúngicas superficiais é consolidada.

**Esta previsão, porém, não tem fundamento mecanístico.** A miíase é uma infestação por larvas de moscas, e a terbinafina não tem atividade larvicida ou antiparasitária conhecida. A pontuação alta parece derivar de proximidade no grafo de conhecimento com outros termos de miíase. O único artigo ligado (PMID 25016125) descreve um menino com furúnculo que não respondeu a antibióticos e outros fármacos, entre eles a terbinafina, sem sucesso. Ou seja, o artigo não apoia o uso do fármaco.

As previsões seguintes do modelo (miíase de ferida, miíase rastejante, miíase, toxoplasmose e equinococose) também carecem de plausibilidade mecanística. Já **tinea manuum** e **micose superficial** são coerentes com o mecanismo, mas coincidem com o uso antifúngico original, portanto não são reposicionamento propriamente dito.

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados.

## Evidências da Literatura

Para a indicação principal (miíase furuncular), existe apenas uma publicação:

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [25016125](https://pubmed.ncbi.nlm.nih.gov/25016125/) | 2014 | Relato de caso | Turkiye Parazitolojii Dergisi | Menino de 12 anos com miíase cutânea furuncular, tratado por 2 meses com penicilina, claritromicina, terbinafina e ibuprofeno, sem sucesso. Não há evidência de eficácia da terbinafina. |

**Indicações alternativas com melhor respaldo (referência):**

| Indicação | Nível | Evidência principal | Decisão do modelo |
|------|-----|---------|------|
| Tinea manuum | L3 | [PMID 1911319](https://pubmed.ncbi.nlm.nih.gov/1911319/) (1991): estudo clínico não controlado com terbinafina por 2 semanas em tinea pedis e tinea manuum; [PMID 15679673](https://pubmed.ncbi.nlm.nih.gov/15679673/) (2005): caso de tinea manuum bolhosa curado com terbinafina; revisões e estudos de resistência | Proceed with Guardrails |
| Micose superficial | L3 | Revisões sobre dermatofitoses e terapia antifúngica sistêmica (por exemplo, [PMID 11155585](https://pubmed.ncbi.nlm.nih.gov/11155585/)); vigilância de resistência (*T. indotineae*) | Proceed with Guardrails |
| Candidíase cutânea | L4 | Revisões e estudos in vitro (por exemplo, [PMID 9593126](https://pubmed.ncbi.nlm.nih.gov/9593126/)); atividade contra *Candida* variável e geralmente fungistática | Research Question |
| Blastomicose | L4 | Relato de caso de paracoccidioidomicose tratada com terbinafina ([PMID 10886159](https://pubmed.ncbi.nlm.nih.gov/10886159/)); sem evidência direta para *Blastomyces dermatitidis* | Research Question |

## Informações de Comercialização no Brasil

Todos os 17 registros encontrados estão **cancelados**; não há registro válido atualmente. Principais registros:

| Número de Registro | Nome Comercial | Forma Farmacêutica | Indicação Aprovada |
|---------|------|------|-----------|
| Registro nº 105830521 | Cloridrato de terbinafina | Não informada | Antimicótico |
| Registro nº 103700707 | Cloridrato de terbinafina | Não informada | Antimicótico |
| Registro nº 125680065 | Cloridrato de terbinafina | Não informada | Antimicóticos para uso tópico |
| Registro nº 144930073 | Lakesiapes | Não informada | Antimicótico |
| Registro nº 102980297 | Funtyl | Não informada | Antimicótico |

Entre os demais registros cancelados constam também as marcas Micosil e Ternasil.

## Considerações de Segurança

- **Contraindicações sugeridas pelo grafo de conhecimento** (relações fármaco-doença do TxGNN/PrimeKG, não texto de bula): doença renal, piureter, doença hepática, doença da vesícula biliar, lúpus eritematoso sistêmico (inclusive pediátrico) e abuso/dependência de substâncias.
- **Interações medicamentosas** (100 interações registradas; principais): 
  - **Maior gravidade:** eliglustat.
  - **Moderada:** morfina, naltrexona, ondansetrona, dexfenfluramina e fenfluramina.
  - **Leve:** cimetidina.
  - Outras (nível não classificado): fentermina, pantoprazol, glimepirida, doxiciclina, clotrimazol, metformina, omeprazol, lansoprazol, prednisona, hidrocortisona, cloreto de potássio, loperamida e rosiglitazona.

Para advertências e contraindicações formais, consulte a bula.

## Conclusão e Próximos Passos

**Decisão: Hold** (para a indicação principal, miíase furuncular)

**Justificativa:**
- A previsão é apenas do modelo (L5), sem ensaios e com um único relato de caso que não demonstra benefício. A terbinafina não tem mecanismo plausível contra larvas de mosca, e a pontuação alta parece ser um artefato do grafo.
- Se houver interesse em algo viável, as indicações dentro do espectro antifúngico (tinea manuum e micose superficial, ambas L3, Proceed with Guardrails) são mais promissoras, mas não representam reposicionamento novo.

**Para prosseguir, é necessário:**
- Dados do mecanismo de ação e da bula, com advertências e contraindicações.
- Não investir na indicação de miíase sem estudos pré-clínicos que demonstrem atividade contra larvas.
- Para as indicações antifúngicas, considerar testes de suscetibilidade e estratégia de uso racional, dada a resistência crescente (*T. indotineae*, *T. rubrum*).
- Verificar a situação regulatória no Brasil, pois todos os 17 registros estão cancelados e seria necessário confirmar se existe outro registro vigente do fármaco.
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

