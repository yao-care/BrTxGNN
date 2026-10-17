---
layout: default
title: Cobalamin
parent: Apenas Predição do Modelo (L5)
nav_order: 238
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-13
description: "Cobalamin: nova indicação prevista, Hiperfosfatemia (hyperphosphatemia) (nível de evidência L5). Indicação original: Monovitaminas, exceto vitamina K"
monitor_inn: "cobalamin"
predicted_indications: ["hyperphosphatemia (disease)", "cystinosis"]
---

# Cobalamin
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

# Cobalamina: De monovitamina (exceto vitamina K) para hiperfosfatemia

## Resumo em Uma Frase

Cobalamina (vitamina B12) foi registrada na ANVISA como monovitamina (exceto vitamina K), sob o nome comercial CRONOBÊ.
O modelo TxGNN prevê que pode ser eficaz para **hiperfosfatemia (hyperphosphatemia)**, mas **não há ensaios clínicos nem publicações** que apoiem essa direção. A previsão é puramente computacional.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Monovitaminas, exceto vitamina K |
| Nova Indicação Prevista | Hiperfosfatemia (hyperphosphatemia) |
| Pontuação de Previsão TxGNN | 99,66% |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | ✗ Apenas registro cancelado |
| Número de Registros | 1 |
| Decisão Recomendada | Hold |

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação nos dados compilados para este relatório. Segundo informações conhecidas, a cobalamina atua como cofator da metionina sintase e da metilmalonil-CoA mutase, e sua função está estabelecida na reposição vitamínica.

Não há relação mecanística conhecida entre a cobalamina e a homeostase do fósforo. A pontuação TxGNN é muito alta (0,997), mas, sem ensaios clínicos ou literatura, deve ser tratada apenas como um sinal gerador de hipóteses, e não como evidência de eficácia.

Vale mencionar a segunda previsão do modelo, a **cistinose** (pontuação de 99,04%). A ligação é indireta e fraca: ambas envolvem o processamento e o transporte lisossômico, mas a literatura recuperada não demonstra efeito terapêutico da cobalamina nessa doença. A pontuação elevada provavelmente reflete proximidade na rede de conhecimento, e não evidência clínica.

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados para hiperfosfatemia.

## Evidências da Literatura

Para a indicação principal (hiperfosfatemia), atualmente não há literatura relacionada. A tabela abaixo refere-se à segunda previsão (cistinose), apenas como contexto:

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [19146888](https://pubmed.ncbi.nlm.nih.gov/19146888/) | 2009 | Revisão | Biochimica et Biophysica Acta | Revisão dos mecanismos moleculares de doenças lisossômicas causadas por defeito no transporte através da membrana lisossômica, incluindo a cistinose. Não avalia a cobalamina como tratamento. |
| [39294696](https://pubmed.ncbi.nlm.nih.gov/39294696/) | 2024 | Relato de caso | Italian Journal of Pediatrics | Pancitopenia grave na apresentação da síndrome de Imerslund-Gräsbeck (má absorção de cobalamina) em um menino de 23 meses. Trata de deficiência de cobalamina, não de tratamento da cistinose. |

## Informações de Comercialização no Brasil

| Número de Registro | Nome Comercial | Forma Farmacêutica | Indicação Aprovada |
|---------|------|------|-----------|
| Registro 109740008 (cancelado) | CRONOBÊ | Não informada | Monovitaminas, exceto vitamina K |

## Considerações de Segurança

- **Contraindicações segundo o grafo de conhecimento (PrimeKG, não derivadas da bula)**: doença hipertensiva, hipertensão, deficiência de potássio, gastrite atrófica crônica e neuropatia óptica hereditária de Leber.
- **Interações medicamentosas**: nenhuma interação encontrada na consulta realizada.

Para advertências e contraindicações formais, consulte a bula.

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
A previsão para hiperfosfatemia tem pontuação alta, porém sem nenhum ensaio clínico, sem literatura e sem relação mecanística plausível (nível L5). Além disso, o único registro brasileiro está cancelado.

**Para prosseguir, é necessário:**
- Obter e analisar a bula na ANVISA (advertências e contraindicações), pendência que bloqueia a triagem de segurança
- Obter dados do mecanismo de ação via DrugBank
- Realizar revisão de literatura e estudos pré-clínicos que testem uma possível ligação entre a cobalamina e o metabolismo do fosfato
- Avaliar a relevância das contraindicações do grafo de conhecimento (p. ex., hipertensão e deficiência de potássio)
- Esclarecer a situação regulatória e as formas farmacêuticas disponíveis, dado que o registro está cancelado
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

