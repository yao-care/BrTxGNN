---
layout: default
title: Lopinavir
parent: Apenas Predição do Modelo (L5)
nav_order: 424
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-13
description: "Lopinavir: nova indicação prevista, Síndrome da imunodeficiência adquirida felina (Feline Acquired Immuno… (nível de evidência L5). Indicação original: Infecção por HIV e AIDS"
monitor_inn: "LOPINAVIR"
predicted_indications: ["feline acquired immunodeficiency syndrome", "simian immunodeficiency virus infection", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter"]
---

# Lopinavir
{: .fs-9 }

Nível de evidência: **L5** | Indicações previstas: **3** 
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

# Lopinavir: Da infecção por HIV/AIDS à síndrome da imunodeficiência adquirida felina

## Resumo em Uma Frase

Lopinavir é um inibidor de protease do HIV-1, originalmente usado no tratamento da infecção por HIV e da AIDS.
O modelo TxGNN prevê que pode ser eficaz para **síndrome da imunodeficiência adquirida felina (Feline Acquired Immunodeficiency Syndrome)**,
atualmente com **0 ensaios clínicos** e **0 publicações** apoiando esta direção específica (a segunda previsão, a infecção por vírus da imunodeficiência símia, conta com 3 estudos pré-clínicos em primatas não humanos).

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Infecção por HIV e AIDS (conforme o grafo de conhecimento; não há texto de indicação em registro brasileiro) |
| Nova Indicação Prevista | Síndrome da imunodeficiência adquirida felina (Feline Acquired Immunodeficiency Syndrome) |
| Pontuação de Previsão TxGNN | 99,90% |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | Não comercializado (segundo os dados compilados) |
| Número de Registros | 0 |
| Decisão Recomendada | Hold |

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação nos dados compilados. Segundo informações conhecidas, o lopinavir é um inibidor da protease do HIV-1, e sua eficácia em HIV/AIDS está estabelecida (geralmente usado em associação com ritonavir). Mecanisticamente, poderia ser aplicável a outros lentivírus que dependam de uma protease viral.

O vírus da imunodeficiência felina (FIV) é um lentivírus aparentado ao HIV-1 e codifica sua própria protease, o que torna a previsão biologicamente plausível. Porém, a protease do FIV difere da do HIV-1 quanto à especificidade de substrato e à sensibilidade a inibidores, e alguns inibidores de protease do HIV-1 têm atividade reduzida contra ela. A pontuação elevada (0,999) provavelmente reflete a semelhança da doença com as indicações originais no grafo de conhecimento, e não evidência experimental. Trata-se ainda de uma indicação veterinária, com relevância limitada para o reposicionamento em humanos.

**Outras previsões do modelo:**
- **Infecção por vírus da imunodeficiência símia (SIV)** (pontuação 99,90%, nível L4, Hold): o SIV é um lentivírus de primatas próximo ao HIV, e o macaco é um modelo pré-clínico padrão. Há três estudos em animais (veja abaixo), que sustentam atividade farmacológica em primatas não humanos, mas não constituem evidência clínica em humanos.
- **Transtorno do neurodesenvolvimento com marcha atáxica, ausência de fala e redução da substância branca cortical** (pontuação 99,90%, nível L5, Hold): não foi identificado vínculo mecanístico claro. Trata-se de doença genética rara sem dependência aparente de protease viral, e a penetração limitada do lopinavir no sistema nervoso central é um obstáculo adicional. Provavelmente é um falso positivo do modelo.

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados.

## Evidências da Literatura

Para a indicação principal (síndrome da imunodeficiência adquirida felina) não há literatura relacionada. Para a segunda previsão (infecção por SIV), foram encontrados os estudos pré-clínicos abaixo:

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [16973590](https://pubmed.ncbi.nlm.nih.gov/16973590/) | 2006 | Estudo pré-clínico em animais (macacos) | Journal of Virology | Declínio viral rápido em macacos cynomolgus infectados com SIVmac251 que receberam terapia antirretroviral quádrupla por 7 dias |
| [17350308](https://pubmed.ncbi.nlm.nih.gov/17350308/) | 2007 | Estudo pré-clínico em animais (construção de SHIV em macacos rhesus) | Microbes and Infection | Construção de um SHIV com gene da protease do HIV-1, útil como ferramenta para testar in vivo inibidores de protease |
| [12951220](https://pubmed.ncbi.nlm.nih.gov/12951220/) | 2003 | Estudo pré-clínico em animais (macacos) | Journal of Virological Methods | Avaliou o efeito da HAART oral (AZT, 3TC e lopinavir/ritonavir) sobre o subconjunto CD8 em macacos cronicamente infectados com SHIV 89.6P |

## Considerações de Segurança

Os dados abaixo vêm do grafo de conhecimento (relações fármaco-doença de contraindicação), e não do texto da bula:

- **Contraindicações segundo o grafo de conhecimento**: síndrome do QT longo (inclusive familiar), torsades de pointes, parada cardíaca súbita, doenças de condução cardíaca, bloqueio atrioventricular, isquemia miocárdica, doença arterial coronariana, cardiomiopatias, pancreatite, doença hepática, cirrose, hepatite B e C crônicas, doença da vesícula biliar, hiperglicemia, diabetes mellitus, cetoacidose diabética, hipertrigliceridemia, hiperlipidemia familiar combinada, hiperbilirrubinemia (incluindo síndrome de Gilbert), deficiência de potássio e hemofilia.
- **Interações medicamentosas**: foram identificadas 65 interações; entre as 20 listadas, destacam-se as de gravidade **maior** com **dolasetrona** e **papaverina** (sinal de risco cardíaco, coerente com as contraindicações de QT). Há interações moderadas com acarbose, dapagliflozina, metformina, famotidina, levofloxacino, ondansetrona, palonosetrona, laxantes (bisacodil, óleo de rícino, glicerina, lactitol, lactulose, citrato e hidróxido de magnésio, óleo mineral, fenolftaleína) e interações leves com cimetidina e clotrimazol.

Para advertências e contraindicações da bula, consulte a bula aprovada.

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
- A previsão principal tem apenas suporte do modelo (L5), sem ensaios clínicos nem literatura, trata-se de indicação veterinária, e a protease do FIV pode ser pouco sensível ao lopinavir. O fármaco não está comercializado no Brasil, segundo os dados compilados.

**Para prosseguir, é necessário:**
- Dados do mecanismo de ação (MOA) do fármaco, para analisar o vínculo mecanístico
- Advertências e contraindicações da bula aprovada pela ANVISA, para triagem de segurança
- Dados de atividade do lopinavir contra a protease do FIV (estudos enzimáticos e in vitro)
- Para a previsão relacionada ao SIV, avaliar se serve apenas como modelo translacional
- Para a terceira previsão, investigar a biologia do gene e das vias envolvidas antes de qualquer consideração
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

