---
layout: default
title: Exemestane
parent: Apenas Predição do Modelo (L5)
nav_order: 309
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Exemestane: nova indicação prevista, Deficiência de antitrombina tipo 2 (antithrombin deficiency type 2) (nível de evidência L5). Indicação original: Antineoplásico"
monitor_inn: "Exemestane"
predicted_indications: ["antithrombin deficiency type 2", "amenorrhea (disease)", "factor 5 excess with spontaneous thrombosis", "heparin cofactor 2 deficiency", "thrombophilia", "migraine disorder", "migraine with brainstem aura", "acne (disease)", "migraine with or without aura, susceptibility to", "breast fibrocystic disease"]
---

# Exemestane
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

# Exemestano: Do câncer (antineoplásico) a deficiência de antitrombina tipo 2

## Resumo em Uma Frase

Exemestano é um inibidor da aromatase esteroidal, registrado na ANVISA como antineoplásico (usado no câncer de mama hormônio-dependente).
O modelo TxGNN prevê que possa ser eficaz para **deficiência de antitrombina tipo 2 (antithrombin deficiency type 2)**, mas **não há ensaios clínicos nem publicações** apoiando esta direção; trata-se apenas de uma previsão computacional.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Antineoplásico |
| Nova Indicação Prevista | Deficiência de antitrombina tipo 2 (antithrombin deficiency type 2) |
| Pontuação de Previsão TxGNN | 99,83% |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | ✗ Somente registros cancelados |
| Número de Registros | 5 (todos cancelados) |
| Decisão Recomendada | Hold |

---

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação nos dados compilados para este relatório. Segundo informações conhecidas, o exemestano é um inibidor irreversível da aromatase, de estrutura esteroidal, que reduz os níveis de estrogênio. Sua eficácia como antineoplásico, no câncer de mama dependente de hormônio, é a base do seu uso original.

**Na prática, esta previsão não tem uma justificativa mecanística plausível.** A deficiência de antitrombina tipo 2 é um defeito hereditário do gene SERPINC1, e a inibição da aromatase não corrige essa alteração. Não se conhece nenhum efeito de agentes que reduzem estrogênio sobre a função da antitrombina. A pontuação alta (0,998) reflete apenas a proximidade no grafo de conhecimento, sem respaldo clínico ou na literatura.

Previsões vizinhas (fator V, cofator II da heparina, trombofilia) formam um agrupamento que provavelmente decorre de características compartilhadas do grafo, e não de biologia real. Além disso, inibidores da aromatase têm suas próprias considerações de segurança cardiovascular e tromboembólica.

### Outras indicações previstas (para contexto)

| Posição | Doença prevista | Pontuação TxGNN | Evidência | Observação |
|------|------|------|------|------|
| 2 | Amenorreia | 99,82% | L4 | Efeito esperado do fármaco (supressão de estrogênio), não alvo terapêutico; a literatura é indireta |
| 3 | Excesso de fator 5 com trombose espontânea | 99,82% | L5 | Sem mecanismo claro |
| 4 | Deficiência de cofator 2 da heparina | 99,82% | L5 | Sem mecanismo plausível |
| 5 | Trombofilia | 99,67% | L5 | Vínculo apenas especulativo |
| 6 | Enxaqueca | 99,02% | L5 | A redução de estrogênio pode piorar a enxaqueca; cefaleia é efeito adverso relatado |
| 7 | Enxaqueca com aura do tronco encefálico | 99,01% | L5 | Provável propagação do nó de enxaqueca geral |
| 8 | Acne | 97,25% | L5 | Atividade androgênica fraca do exemestano pode agravar a acne |
| 9 | Suscetibilidade a enxaqueca com ou sem aura | 96,63% | L5 | Fenótipo genético, redundante com as demais enxaquecas |
| 10 | Doença fibrocística da mama | 95,66% | L5 | Plausibilidade biológica (resposta a estrogênio), porém sem evidência |

---

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados.

---

## Evidências da Literatura

Para a indicação principal (deficiência de antitrombina tipo 2), atualmente não há literatura relacionada.

Para contexto, a segunda previsão (amenorreia) tem literatura indireta, que trata de supressão e recuperação da função ovariana em câncer de mama, e não do tratamento da amenorreia com exemestano:

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [23108951](https://pubmed.ncbi.nlm.nih.gov/23108951/) | 2013 | Coorte | Annals of Oncology | Incidência e preditores de recuperação da função ovariana em pacientes com câncer de mama e amenorreia induzida por quimioterapia que trocaram tamoxifeno por exemestano |
| [28118723](https://pubmed.ncbi.nlm.nih.gov/28118723/) | 2016 | Revisão | Klinicka Onkologie | Inibidores da aromatase (anastrozol, letrozol, exemestano) como tratamento endócrino padrão em mulheres na pós-menopausa com câncer de mama; manejo de efeitos adversos |
| [26178334](https://pubmed.ncbi.nlm.nih.gov/26178334/) | 2015 | Revisão | Oncology (Williston Park) | Papel da supressão ovariana em mulheres na pré-menopausa com câncer de mama inicial positivo para receptor hormonal |
| [31379370](https://pubmed.ncbi.nlm.nih.gov/31379370/) | 2019 | Revisão | Recenti Progressi in Medicina | Papel atual dos análogos de LHRH no câncer de mama em pacientes na pré-menopausa |
| [26951320](https://pubmed.ncbi.nlm.nih.gov/26951320/) | 2016 | Revisão/Comentário | Journal of Clinical Oncology | Necessidade de monitorar estradiol em mulheres com supressão ovariana por câncer de mama |

---

## Informações de Comercialização no Brasil

Todos os registros encontrados estão cancelados; atualmente não há produto com registro válido.

| Número de Registro | Nome Comercial | Forma Farmacêutica | Indicação Aprovada |
|---------|------|------|-----------|
| Registro nº 146820072 | EMAH | — | Antineoplásico |
| Registro nº 121100397 | AROMASIN | — | Antineoplásico |
| Registro nº 155370048 | EXEMESTANO | — | Antineoplásico |
| Registro nº 100431336 | PROEXTY | — | Agentes antineoplásicos |
| Registro nº 146820066 | EXEMESTANO | — | Antineoplásico |

---

## Citotoxicidade

| Item | Conteúdo |
|------|------|
| Classificação de Citotoxicidade | Terapia hormonal (inibidor da aromatase), não é citotóxico convencional |
| Risco de Mielossupressão | Baixo (não é característico desta classe) |
| Classificação de Emetogenicidade | Baixa |
| Itens de Monitoramento | Consulte as advertências e precauções na bula; em geral, considerar função hepática, densidade óssea e perfil lipídico |
| Proteção no Manuseio | Consulte as advertências e precauções na bula |

---

## Considerações de Segurança

- **Interações Medicamentosas**: foram identificadas 100 possíveis interações. As de nível moderado são com **dexametasona** e **troglitazona**. Outras interações listadas (por exemplo, pantoprazol, omeprazol, metformina, sinvastatina, morfina, ondansetrona, ácido acetilsalicílico, rosuvastatina) não têm gravidade classificada.
- **Aspectos relacionados às indicações previstas**: inibidores da aromatase carregam suas próprias considerações cardiovasculares e tromboembólicas, relevantes para as previsões de trombofilia; cefaleia é efeito adverso relatado, relevante para as previsões de enxaqueca; perda óssea e sintomas do tipo menopausa são esperados em mulheres na pré-menopausa.

Para advertências e contraindicações, consulte a bula.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
- A previsão para deficiência de antitrombina tipo 2 baseia-se apenas na pontuação do grafo (nível L5), sem ensaios, sem literatura e sem mecanismo plausível. Nenhuma das 10 indicações previstas apresenta evidência que sustente o reposicionamento, e todas permanecem em Hold. Além disso, todos os registros no Brasil estão cancelados.

**Para prosseguir, é necessário:**
- Dados do mecanismo de ação do exemestano (DrugBank) para permitir análise de vínculo mecanístico
- Bula da ANVISA com advertências e contraindicações (lacuna que bloqueia a triagem de segurança)
- Uma hipótese biológica justificável que ligue a redução de estrogênio ao defeito da antitrombina (SERPINC1), com estudos pré-clínicos
- Se houver interesse em outra indicação, priorizar a doença fibrocística da mama (plausibilidade hormonal), com pergunta de pesquisa dedicada e avaliação de risco-benefício
- Verificar a situação regulatória atual (registros cancelados) caso se pretenda uma via de reposicionamento no Brasil
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

