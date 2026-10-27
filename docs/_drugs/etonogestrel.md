---
layout: default
title: Etonogestrel
parent: Apenas Predição do Modelo (L5)
nav_order: 304
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Etonogestrel: nova indicação prevista, Amenorreia (amenorrhea) (nível de evidência L5). Indicação original: Não há dados de indicação aprovada na ANVISA"
monitor_inn: "Etonogestrel"
predicted_indications: ["amenorrhea (disease)", "breast fibrocystic disease", "apocrine adenosis of breast", "blunt duct adenosis of breast", "benign mammary dysplasia", "fat necrosis of breast", "breast abscess", "lactation disease", "breast adenosis", "acne (disease)"]
---

# Etonogestrel
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

## Etonogestrel: Da contracepção à amenorreia (previsão computacional, sem evidência clínica direta)
{: .text-alpha }

## Resumo em Uma Frase

Etonogestrel é um progestágeno usado em contracepção hormonal (por exemplo, em implantes). Não há indicação original registrada no Brasil nos dados compilados para este relatório.
O modelo TxGNN prevê que pode ser eficaz para **amenorreia (amenorrhea)**, mas atualmente há **0 ensaios clínicos** e apenas **1 publicação** associada, sem relação direta com a indicação. A previsão é, portanto, essencialmente computacional.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Não há dados de indicação aprovada na ANVISA (o uso contraceptivo é conhecimento geral do fármaco, não dado de registro) |
| Nova Indicação Prevista | Amenorreia (amenorrhea) |
| Pontuação de Previsão TxGNN | 99,84% |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | Não comercializado |
| Número de Registros | 0 |
| Decisão Recomendada | Hold |

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação nos dados compilados. Segundo informações conhecidas, o etonogestrel é um progestágeno que suprime a ovulação e afina o endométrio.

A relação com a nova indicação é, na prática, **invertida**: a amenorreia é um efeito esperado do uso do implante (um padrão de sangramento comum), e não uma condição que ele trate. Usar um progestágeno para tratar amenorreia patológica seria mecanisticamente contraintuitivo, pois a exposição ao progestágeno induz, e não resolve, a amenorreia. A pontuação alta do TxGNN provavelmente reflete a associação fármaco-doença no grafo de conhecimento, e não um sinal terapêutico.

### Outras previsões avaliadas

As demais previsões do modelo também permanecem em **Hold**:

| Doença prevista | Pontuação TxGNN | Nível | Observação |
|------|------|------|------|
| Doença fibrocística da mama | 99,61% | L5 | Racional hormonal plausível, mas sem estudos |
| Adenose apócrina da mama | 99,29% | L5 | Apenas previsão baseada em grafo |
| Adenose de ductos obtusos da mama | 99,29% | L5 | Mesma pontuação da anterior, sugerindo sinal compartilhado do grafo |
| Displasia mamária benigna | 99,21% | L5 | Apenas previsão |
| Necrose gordurosa da mama | 98,99% | L5 | Sem mecanismo hormonal crível (causa traumática/cirúrgica) |
| Abscesso mamário | 98,99% | L5 | Condição infecciosa, sem mecanismo plausível |
| Doença da lactação | 98,93% | L4 | Evidência indireta sobre contracepção na lactação, não tratamento |
| Adenose mamária | 98,86% | L5 | Sem evidência clínica |
| Acne | 98,69% | L4 | A acne é um evento adverso documentado do implante; sinal oposto ao benefício |

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados.

## Evidências da Literatura

Para amenorreia, a única publicação associada não tem relação com a indicação. Para outras previsões, há duas publicações relevantes, apresentadas separadamente.

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [33430924](https://pubmed.ncbi.nlm.nih.gov/33430924/) | 2021 | Protocolo de RCT (não relacionado) | Trials | Protocolo do estudo COVA (BIO101 na deterioração respiratória em COVID-19). Sem relação com etonogestrel ou amenorreia |
| [26410174](https://pubmed.ncbi.nlm.nih.gov/26410174/) | 2016 | Revisão sistemática | Contraception | Uso de contraceptivos somente com progestágeno em mulheres que amamentam; evidência indireta sobre segurança e lactação (previsão: doença da lactação) |
| [11861056](https://pubmed.ncbi.nlm.nih.gov/11861056/) | 2002 | Dados agrupados de ensaios clínicos (segurança) | Contraception | Eventos adversos não menstruais com implantes contraceptivos; a acne aparece como evento adverso, não como benefício (previsão: acne) |

## Considerações de Segurança

- **Contraindicações (derivadas do grafo de conhecimento, não do texto da bula):** hipertensão, epilepsia, transtornos de ansiedade e neuróticos, distimia, porfirias, doença renal, doença hepática, doença da vesícula biliar, lúpus eritematoso sistêmico, asma, diabetes mellitus e cetoacidose diabética, hipertrigliceridemia, hiperlipidemia, carcinoma de mama feminino, tromboflebite, enxaqueca, doença arterial coronariana e obesidade.
- **Interações Medicamentosas:** foram identificadas 100 interações no total; entre as listadas, todas de gravidade **moderada**, destacam-se antidiabéticos (acarbose, metformina, glimepiride, clorpropamida), inibidores de SGLT2 (canagliflozina, dapagliflozina, empagliflozina), inibidores de DPP-4 (alogliptina, saxagliptina), agonistas de GLP-1 (albiglutida, dulaglutida, semaglutida), insulinas (asparte, degludeca, detemir, glargina, glulisina), além de aprepitanto, claritromicina e linaclotida.

Consulte a bula para advertências e contraindicações oficiais, pois não foram obtidos dados da bula da ANVISA.

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
- A previsão principal (amenorreia) é apenas computacional (L5) e mecanisticamente contraditória, já que a amenorreia é um efeito esperado do fármaco. Não há ensaios clínicos, o fármaco não está comercializado no Brasil e as demais previsões também carecem de evidência direta.

**Para prosseguir, é necessário:**
- Obter e analisar a bula da ANVISA (advertências e contraindicações), etapa que bloqueia a triagem de segurança
- Complementar os dados de mecanismo de ação (consulta ao DrugBank)
- Reavaliar a relevância das previsões com revisão da literatura dirigida, priorizando indicações com racional plausível (por exemplo, doenças benignas da mama)
- Confirmar a situação regulatória e as vias de administração disponíveis no Brasil
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

