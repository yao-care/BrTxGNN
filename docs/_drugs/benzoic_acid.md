---
layout: default
title: Benzoic Acid
parent: Apenas Predição do Modelo (L5)
nav_order: 123
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-28
description: "Benzoic Acid: nova indicação prevista, Bronquite (bronchitis) (nível de evidência L5). Indicação original: Expectorantes balsâmicos e mucolítico"
monitor_inn: "benzoic acid"
predicted_indications: ["bronchitis", "severe nonproliferative diabetic retinopathy", "diabetic retinopathy", "dry eye syndrome", "palmar fibromatosis", "Ledderhose disease", "infantile digital fibromatosis", "hereditary angioedema with C1Inh deficiency", "posterior leukoencephalopathy syndrome", "C1 inhibitor deficiency"]
---

# Benzoic Acid
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

## Ácido benzoico: De expectorante balsâmico e mucolítico para bronquite
{: .text-alpha }

## Resumo em Uma Frase

O ácido benzoico (benzoic acid) foi originalmente registrado na ANVISA como componente de um produto expectorante balsâmico e mucolítico (PENETRO).
O modelo TxGNN prevê que pode ser eficaz para **bronquite (bronchitis)**,
mas atualmente há **0 ensaios clínicos** e **2 publicações** recuperadas, nenhuma delas estudando o ácido benzoico diretamente. A previsão se apoia apenas no modelo computacional.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Expectorantes balsâmicos e mucolítico |
| Nova Indicação Prevista | Bronquite (bronchitis) |
| Pontuação de Previsão TxGNN | 0,9998 |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | Comercializado (registros ativos: 1 de 1) |
| Número de Registros | 1 (ativos: 1) |
| Decisão Recomendada | Hold |

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação. Segundo as informações conhecidas, o ácido benzoico foi comercializado no Brasil como expectorante balsâmico e mucolítico (produto PENETRO). Isso sugere uma ligação conceitual com o alívio de sintomas respiratórios.

A bronquite é uma inflamação das vias aéreas associada a tosse e excesso de secreção. Um fármaco usado para fluidificar ou eliminar secreções brônquicas tem, em tese, relação com o alívio sintomático dessa condição. Essa proximidade entre a indicação original e a nova é a principal razão pela qual a previsão parece plausível.

É importante ser cauteloso: a pontuação elevada do TxGNN é apenas uma previsão computacional. As duas publicações recuperadas (uma revisão sobre repaglinida no diabetes tipo 2 e um estudo animal sobre inibidor de epóxido hidrolase solúvel na DPOC induzida por fumaça) não avaliam o ácido benzoico e, portanto, não oferecem suporte direto.

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados.

## Evidências da Literatura

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [11577798](https://pubmed.ncbi.nlm.nih.gov/11577798/) | 2001 | Revisão | Drugs | Revisão do uso terapêutico da repaglinida (derivado do ácido benzoico) no diabetes tipo 2; não trata de bronquite nem do ácido benzoico como fármaco |
| [22180869](https://pubmed.ncbi.nlm.nih.gov/22180869/) | 2012 | Estudo pré-clínico/animal | Am J Respir Cell Mol Biol | Inibidor de epóxido hidrolase solúvel na DPOC induzida por fumaça de tabaco; não envolve o ácido benzoico |

## Informações de Comercialização no Brasil

| Número de Registro | Nome Comercial | Forma Farmacêutica | Indicação Aprovada |
|---------|------|------|-----------|
| Registro nº 101430027 (cancelado) | PENETRO | Não informada | Expectorantes balsâmicos e mucolítico |

## Considerações de Segurança

Os dados de bula (advertências e contraindicações) e de interações medicamentosas não estavam disponíveis. Consulte a bula para informações de segurança.

Nota complementar: o grafo de conhecimento utilizado pelo TxGNN (PrimeKG) registra associações de contraindicação entre o ácido benzoico e diversas condições. Não se trata de texto de bula, e devem ser confirmadas em fontes oficiais. Entre elas:

- **Cardiovasculares:** hipertensão, doença arterial coronariana, parada cardíaca súbita, doenças da condução cardíaca, doença cardiovascular
- **Hepáticas, renais e biliares:** insuficiência hepática, doença hepática, doença renal, doença da vesícula biliar
- **Metabólicas:** diabetes mellitus, cetoacidose diabética, doenças de depósito de glicogênio, cistinúria, galactosemia
- **Hematológicas:** distúrbios da coagulação, hemofilia, anemia (incluindo macrocítica), deficiência de G6PD
- **Neuromusculares:** miastenia gravis, doenças da junção neuromuscular
- **Gastrointestinais e outras:** gastrite, acalasia, megaesôfago, anorexia nervosa, hiperplasia prostática benigna, piureter

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
- A previsão para bronquite tem pontuação alta no TxGNN, mas é sustentada apenas pelo modelo (nível L5), sem ensaios clínicos e sem literatura que avalie o ácido benzoico. Além disso, o único registro na ANVISA está cancelado e faltam dados de segurança de bula.

**Para prosseguir, é necessário:**
- Obter a bula na ANVISA e analisar advertências e contraindicações, etapa que bloqueia a triagem de segurança
- Obter dados do mecanismo de ação (por exemplo, via DrugBank)
- Realizar busca de literatura específica sobre ácido benzoico e bronquite/expectoração, além de verificar ensaios clínicos
- Avaliar o motivo do cancelamento do registro PENETRO e a viabilidade regulatória de uma nova indicação
- Esclarecer a forma farmacêutica e a via de administração compatíveis com a nova indicação
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

