---
layout: default
title: Lopinavir
parent: Evidência Moderada (L3-L4)
nav_order: 424
evidence_level: L4
indication_count: 3
monitor_inn: "LOPINAVIR"
predicted_indications: ["simian immunodeficiency virus infection", "feline acquired immunodeficiency syndrome", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter"]
last_modified_at: 2026-10-31
description: "Lopinavir: nova indicação prevista, Infecção pelo vírus da imunodeficiência símia (nível de evidência L4). Indicação original: Infecção por HIV e AIDS"
---

# Lopinavir
{: .fs-9 }

Nível de evidência: **L4** | Indicações previstas: **3** 
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

## Lopinavir: Da infecção por HIV/AIDS à infecção pelo vírus da imunodeficiência símia
{: .text-alpha }

## Resumo em Uma Frase

Lopinavir é um inibidor da protease do HIV, originalmente usado no tratamento da infecção por HIV e da AIDS.
O modelo TxGNN prevê que pode ser eficaz para **infecção pelo vírus da imunodeficiência símia (simian immunodeficiency virus infection)**, mas as evidências se limitam a **3 publicações** de estudos pré-clínicos em macacos e **nenhum ensaio clínico**.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Infecção por HIV e AIDS (relação registrada no grafo de conhecimento; os registros brasileiros não trazem texto de indicação) |
| Nova Indicação Prevista | Infecção pelo vírus da imunodeficiência símia |
| Pontuação de Previsão TxGNN | 0,9990 |
| Nível de Evidência | L4 |
| Situação no Mercado Brasileiro | Comercializado (registros ativos: 2 de 4) |
| Número de Registros | 4 (ativos: 2) |
| Decisão Recomendada | Hold |

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação neste conjunto de dados. Segundo o conhecimento farmacológico geral, o lopinavir é um inibidor da protease do HIV-1, enzima necessária para a maturação das partículas virais. A predição para este medicamento vem do modelo TxGNN (deep learning) e pode refletir semelhanças que o modelo aprendeu entre doenças relacionadas, não evidência biológica.

O vírus da imunodeficiência símia (SIV) é um lentivírus muito próximo do HIV, com protease homóloga. Por isso, é biologicamente plausível que a inibição da maturação viral também funcione nesse vírus. Os três estudos encontrados usam regimes antirretrovirais contendo lopinavir em macacos, ou modelos de SHIV com protease derivada do HIV-1.

É importante notar que o SIV infecta primatas não humanos. Essa indicação representa, sobretudo, um uso do fármaco em modelos pré-clínicos, e não uma oportunidade real de reposicionamento para humanos. O vínculo mecanístico é inferido, não demonstrado com dados do fármaco.

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados.

## Evidências da Literatura

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [16973590](https://pubmed.ncbi.nlm.nih.gov/16973590/) | 2006 | Estudo pré-clínico em animais | Journal of Virology | Macacos cynomolgus infectados com SIVmac251 receberam 7 dias de terapia antirretroviral quádrupla, para estudar a dinâmica de queda da carga viral |
| [17350308](https://pubmed.ncbi.nlm.nih.gov/17350308/) | 2007 | Estudo pré-clínico em animais | Microbes and Infection | Construção de um SHIV com gene da protease do HIV-1, replicado em macacos rhesus; proposto como ferramenta para testar inibidores de protease in vivo |
| [12951220](https://pubmed.ncbi.nlm.nih.gov/12951220/) | 2003 | Estudo pré-clínico em animais | Journal of Virological Methods | Macacos infectados com SHIV 89.6P tratados por via oral com AZT, 3TC e lopinavir/ritonavir por 28 dias; avaliação do efeito sobre o subtipo de células CD8 |

## Informações de Comercialização no Brasil

| Registro | Produto | Empresa detentora | Situação |
|------|------|------|------|
| 102980436 | LOPINAVIR + RITONAVIR | CRISTÁLIA PRODUTOS QUÍMICOS FARMACÊUTICOS LTDA. | Ativo |
| 198600010 | KALETRA | ABBVIE FARMACÊUTICA LTDA. | Ativo |
| 105530242 | KALETRA | ABBOTT LABORATÓRIOS DO BRASIL LTDA | Cancelado |
| 110390223 | LOPINAVIR + RITONAVIR | FUNDAÇÃO PARA O REMÉDIO POPULAR - FURP | Cancelado |

## Considerações de Segurança

- **Contraindicações registradas no grafo de conhecimento** (não provêm do texto da bula): síndrome do QT longo (inclusive familiar), torsades de pointes, parada cardíaca súbita, doença do sistema de condução cardíaco, bloqueio atrioventricular, pancreatite, doenças hepáticas (incluindo cirrose e hepatites B e C crônicas), doença da vesícula biliar, hiperglicemia, diabetes mellitus, cetoacidose diabética, hipertrigliceridemia, hiperlipidemia familiar combinada, hiperbilirrubinemia (incluindo síndrome de Gilbert), deficiência de potássio, isquemia miocárdica, doença arterial coronariana, cardiomiopatias e hemofilia.
- **Interações medicamentosas**: foram registradas 65 interações. Entre as listadas, as de gravidade **maior** são com **dolasetrona** e **papaverina**. Há interações de gravidade moderada com acarbose, dapagliflozina, metformina, levofloxacino, ondansetrona, palonosetrona, famotidina e vários laxantes (bisacodil, óleo de rícino, glicerina, lactitol, lactulose, citrato e hidróxido de magnésio, óleo mineral, fenolftaleína). Cimetidina e clotrimazol têm interação leve.
- O lopinavir é usado em coformulação com ritonavir, forte inibidor da CYP3A4, o que aumenta a complexidade das interações.

Para advertências e contraindicações oficiais, consulte a bula.

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
- Os únicos estudos são pré-clínicos em macacos, sem ensaios clínicos. O SIV é uma infecção de primatas não humanos, portanto a previsão tem pouco valor como reposicionamento para humanos, apesar da pontuação alta do TxGNN.
- As outras duas previsões do modelo (AIDS felina e um transtorno do neurodesenvolvimento raro) não têm nenhuma evidência de apoio. A segunda não tem vínculo mecanístico plausível.

**Para prosseguir, é necessário:**
- Definir se há interesse real nessa indicação (por exemplo, uso do fármaco como ferramenta em modelos animais) ou se ela deve ser descartada para uso humano.
- Obter os dados de mecanismo de ação no DrugBank.
- Baixar e analisar a bula na ANVISA (advertências, contraindicações e indicações aprovadas), pois isso bloqueia a triagem de segurança.
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

