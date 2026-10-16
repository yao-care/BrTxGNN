---
layout: default
title: Acetic Acid
parent: Apenas Predição do Modelo (L5)
nav_order: 20
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-13
description: "Acetic Acid: nova indicação prevista, Transtorno pós-bacteriano (post-bacterial disorder) (nível de evidência L5). Indicação original: Produtos para hemodiálise"
---

# Acetic Acid
{: .fs-9 }

Nível de evidência: **L5** | Indicações previstas: **9** 
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

# Ácido acético: De produtos para hemodiálise a transtorno pós-bacteriano

## Resumo em Uma Frase

O ácido acético é um componente de concentrados ácidos para hemodiálise, registrados na ANVISA como "produtos para hemodiálise".
O modelo TxGNN prevê que pode ser eficaz para **transtorno pós-bacteriano (post-bacterial disorder)**,
mas atualmente há **0 ensaios clínicos** e **0 publicações** apoiando esta direção específica. Trata-se apenas de uma previsão computacional.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Produtos para hemodiálise |
| Nova Indicação Prevista | Transtorno pós-bacteriano (post-bacterial disorder) |
| Pontuação de Previsão TxGNN | 99,98% |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | Somente registros cancelados |
| Número de Registros | 4 (todos cancelados) |
| Decisão Recomendada | Hold |

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação. Segundo informações conhecidas, o ácido acético faz parte de concentrados ácidos para hemodiálise, nos quais atua como acidificante/tampão do dialisato. Isso é muito diferente de qualquer uso anti-infeccioso ou imunomodulador.

O ácido acético possui atividade antibacteriana geral, o que poderia sugerir alguma relação com condições "pós-bacterianas". Porém, com os dados compilados para este relatório, não é possível estabelecer um vínculo mecanístico específico entre o fármaco e as sequelas pós-bacterianas. A similaridade com a indicação original ainda está pendente de análise.

As demais previsões do modelo (todas com pontuação acima de 99%) também não têm respaldo clínico, com uma exceção parcial: a **tinea corporis**, que tem plausibilidade como antifúngico tópico (veja abaixo).

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados.

## Evidências da Literatura

Para a indicação principal (transtorno pós-bacteriano), atualmente não há literatura relacionada.

### Outras indicações previstas com alguma literatura

**Síndrome pós-infecciosa (post-infectious syndrome)** – pontuação 99,98%, nível L5

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [20848144](https://pubmed.ncbi.nlm.nih.gov/20848144/) | 2011 | Revisão sistemática | J Gastroenterol | Revisa modelos animais de síndrome do intestino irritável pós-infecciosa; trata da modelagem da doença, não do tratamento com ácido acético |

**Tinea corporis** – pontuação 99,25%, nível L4 (Pergunta de pesquisa)

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [20996178](https://pubmed.ncbi.nlm.nih.gov/20996178/) | 1946 | Relato clínico histórico | JAMA | Tratamento de tinea capitis com iodo especial e ácido acético diluído |
| [20983383](https://pubmed.ncbi.nlm.nih.gov/20983383/) | 1946 | Relato clínico histórico | Arch Dermatol Syphilol | Mesmo tema: tinea capitis com iodo e ácido acético diluído |
| [20256868](https://pubmed.ncbi.nlm.nih.gov/20256868/) | 1947 | Série de casos histórica | Urol Cutaneous Rev | Resultados em série maior de pacientes com tinea capitis |
| [13616002](https://pubmed.ncbi.nlm.nih.gov/13616002/) | 1958 | Relato clínico histórico | Vestn Dermatol Venerol | Epidermofitose do pé tratada com concentrações crescentes de ácido acético |
| [26857689](https://pubmed.ncbi.nlm.nih.gov/26857689/) | 2016 | Estudo in vitro | Mycoses | Avaliação de produtos antifúngicos tópicos em modelo de onicomicose |
| [31049344](https://pubmed.ncbi.nlm.nih.gov/31049344/) | 2019 | Relato clínico | Skin Appendage Disord | Peeling químico como alternativa aos antifúngicos orais em onicomicose |
| [37256034](https://pubmed.ncbi.nlm.nih.gov/37256034/) | 2023 | Série de casos (sinal de segurança) | Arch Plast Surg | Queimaduras causadas por remédios populares coreanos, sinalizando risco do uso tópico não controlado |

Observação: as demais referências levantadas para tinea corporis (estudos com *Lactobacillus*, produtos de fermentação e método analítico do tolnaftato) são indiretas ou não relevantes e não foram listadas.

## Informações de Comercialização no Brasil

| Número de Registro | Nome Comercial | Forma Farmacêutica | Indicação Aprovada | Situação |
|---------|------|------|-----------|------|
| 116880014 | CPHD - Concentrado Ácido para Hemodiálise sem Glicose | Não informada | Produtos para hemodiálise | Cancelado |
| 110850045 | Fração Ácida Ca++ 3,0 mEq/L 1:44 | Não informada | Produtos para hemodiálise | Cancelado |
| 110850041 | Farmace CPHD - Fração Ácida com Cálcio 2,5 mEq/L | Não informada | Produtos para hemodiálise | Cancelado |
| 116880004 | Farmarin CPHD | Não informada | Produtos para hemodiálise | Cancelado |

## Considerações de Segurança

- **Contraindicações segundo o grafo de conhecimento (não da bula)**: porfiria hereditária, doença do metabolismo da porfirina, porfiria, infecção por herpes simples e herpes zóster geniculado. Esses dados vêm de relações do grafo de conhecimento e precisam ser confirmados em fontes regulatórias.
- **Sinal de segurança na literatura**: queimaduras por uso tópico não controlado de remédios populares (PMID 37256034), relevante caso se considere uso tópico em tinea corporis.
- **Interações medicamentosas**: nenhuma interação encontrada nos dados consultados.

Consulte a bula para as demais informações de segurança.

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
- A previsão principal (transtorno pós-bacteriano) e as demais previsões de maior pontuação carecem de ensaios clínicos e literatura (nível L5), e não há mecanismo plausível identificado. Além disso, todos os registros brasileiros estão cancelados.
- A única linha com algum respaldo é o uso tópico em tinea corporis (L4, "Pergunta de pesquisa"), baseado em relatos históricos e estudos in vitro, mas sem estudos controlados modernos.

**Para prosseguir, é necessário:**
- Obter a bula na ANVISA (advertências e contraindicações), pois esta lacuna impede a triagem de segurança.
- Obter o mecanismo de ação na DrugBank para analisar o vínculo mecanístico.
- Avaliar a compatibilidade de via de administração (hoje pendente), especialmente a via tópica para tinea corporis, já que o produto original é um concentrado para diálise e não de uso direto no paciente.
- Se for priorizada a tinea corporis: revisar a literatura de forma sistemática e definir concentração, formulação e perfil de segurança cutânea (risco de queimaduras) antes de qualquer estudo clínico.
- Esclarecer a situação regulatória, dado que não há registro válido no Brasil.
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

