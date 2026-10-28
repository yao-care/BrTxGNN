---
layout: default
title: Phenylalanine
parent: Apenas Predição do Modelo (L5)
nav_order: 522
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-28
description: "Phenylalanine: nova indicação prevista, Colangite esclerosante (sclerosing cholangitis) (nível de evidência L5). Indicação original: Nutrientes parenterais"
monitor_inn: "PHENYLALANINE"
predicted_indications: ["sclerosing cholangitis", "congenital prothrombin deficiency"]
---

# Phenylalanine
{: .fs-9 }

Nível de evidência: **L5** | Indicações previstas: **2** 
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

## Fenilalanina: De nutriente parenteral para colangite esclerosante
{: .text-alpha }

## Resumo em Uma Frase

Fenilalanina é um aminoácido essencial, usado originalmente como componente de soluções de nutrição parenteral e de reposição hidroeletrolítica.
O modelo TxGNN prevê que pode ser eficaz para **colangite esclerosante (sclerosing cholangitis)**, mas atualmente há **0 ensaios clínicos** e apenas **3 publicações** de caráter observacional, sem demonstração de efeito terapêutico.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Nutrientes parenterais |
| Nova Indicação Prevista | Colangite esclerosante (sclerosing cholangitis) |
| Pontuação de Previsão TxGNN | 0,9943 |
| Nível de Evidência | L5 (apenas previsão do modelo; a literatura encontrada é observacional e não avalia efeito terapêutico) |
| Situação no Mercado Brasileiro | Comercializado (registros ativos: 15 de 15) |
| Número de Registros | 15 (ativos: 15) |
| Decisão Recomendada | Hold |

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação. Segundo informações conhecidas, a fenilalanina é um aminoácido aromático essencial, precursor da tirosina e das catecolaminas, e faz parte das formulações de nutrição parenteral. Seu uso como nutriente está estabelecido, mas isso não implica efeito terapêutico em doenças hepatobiliares.

A relação entre a indicação original e a nova indicação é fraca. A literatura encontrada associa o metabolismo de aminoácidos aromáticos (tirosina plasmática) à fadiga na cirrose biliar primária e na colangite esclerosante primária. Trata-se de uma associação observacional com sintomas da doença, e não de evidência de benefício terapêutico.

Portanto, a pontuação elevada do TxGNN (0,9943) é apenas uma previsão computacional do modelo TxGNN (deep learning), que pode refletir semelhanças aprendidas pelo modelo entre doenças relacionadas, e não evidência biológica. Não há racional mecanístico direto que justifique o uso da fenilalanina para tratar a colangite esclerosante.

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados.

## Evidências da Literatura

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [15790420](https://pubmed.ncbi.nlm.nih.gov/15790420/) | 2005 | Coorte | BMC Gastroenterology | Investigou a relação entre a concentração plasmática de tirosina, padrões de aminoácidos e fadiga em pacientes com cirrose biliar primária e colangite esclerosante primária |
| [32025163](https://pubmed.ncbi.nlm.nih.gov/32025163/) | 2020 | Coorte | Journal of Clinical and Experimental Hepatology | Caracterizou o perfil metabolômico sérico de colangiocarcinoma em comparação com doenças hepatobiliares benignas, buscando biomarcadores precoces |
| [2103382](https://pubmed.ncbi.nlm.nih.gov/2103382/) | 1990 | Outro | Journal of Gastroenterology and Hepatology | Radioimunoensaio de peptídeo quimiotático bacteriano (formil-metionil-leucil-fenilalanina) e circulação êntero-hepática; relevância indireta |

## Informações de Comercialização no Brasil

Os 15 registros estão válidos. São listados os 5 principais:

| Número de Registro | Nome Comercial | Forma Farmacêutica | Indicação Aprovada |
|---------|------|------|-----------|
| Registro 100410131 | Nephrotect | — | Nutrientes parenterais |
| Registro 100410159 | Aminoven 10% Infant | — | Nutrientes parenterais |
| Registro 100850145 | Amixal | — | Nutrientes parenterais |
| Registro 100850109 | Nutriflex Plus | — | Nutrientes parenterais |
| Registro 100410149 | SmofKabiven livre de eletrólitos | — | Nutrientes parenterais |

## Considerações de Segurança

- **Contraindicações (segundo o grafo de conhecimento, não a bula)**: o grafo de conhecimento do TxGNN aponta associação de contraindicação com fenilcetonúria e outros distúrbios do metabolismo da fenilalanina, doença renal (incluindo doença renal crônica e insuficiência renal terminal), nefrolitíase, nefrocalcinose, hipercalcemia (incluindo hipercalcemia humoral da malignidade), sarcoidose, doenças do metabolismo do fósforo, doença cardíaca e cardiovascular, nefropatia aguda por urato, intoxicação digitálica, fibrilação ventricular e piureter.
- **Interações Medicamentosas**: não foram encontradas interações registradas nos dados compilados.

Consulte a bula para as advertências e contraindicações oficiais.

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
- Não há ensaios clínicos nem evidência de efeito terapêutico; a literatura é apenas observacional, e a pontuação do TxGNN é uma previsão computacional sem racional mecanístico estabelecido. O medicamento é comercializado no Brasil, com 15 registros válidos de 15.

**Para prosseguir, é necessário:**
- Obter e analisar a bula na ANVISA (advertências e contraindicações), etapa que bloqueia a triagem de segurança
- Complementar os dados de mecanismo de ação via DrugBank
- Gerar evidência pré-clínica ou mecanística que relacione a fenilalanina à fisiopatologia da colangite esclerosante
- Avaliar o risco das contraindicações apontadas no grafo de conhecimento (renais, cardiovasculares e do metabolismo da fenilalanina) em pacientes com doença hepatobiliar
- Definir a via de administração e a viabilidade regulatória, dado que não há produto comercializado no país
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

