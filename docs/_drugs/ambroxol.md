---
layout: default
title: Ambroxol
parent: Apenas Predição do Modelo (L5)
nav_order: 48
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Ambroxol: nova indicação prevista, Doença da Cavidade Nasal (Nasal Cavity Disease) (nível de evidência L5). Indicação original: Faringite (segundo as relações de indicação do grafo de conhecimento…"
monitor_inn: "Ambroxol"
predicted_indications: ["nasal cavity disease", "acute laryngopharyngitis", "vulvovaginal candidiasis", "faucial diphtheria", "cervical disc degenerative disorder", "vulvitis", "postmenopausal atrophic vaginitis", "ulceration of vulva", "vulvar neoplasm", "vulvovaginitis"]
---

# Ambroxol
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

## Ambroxol: Da faringite à doença da cavidade nasal
{: .text-alpha }

## Resumo em Uma Frase

Ambroxol é um agente mucolítico/secretolítico, originalmente associado ao tratamento da faringite.
O modelo TxGNN prevê que pode ser eficaz para **Doença da Cavidade Nasal (Nasal Cavity Disease)**,
atualmente com **nenhum ensaio clínico** e **1 publicação** (revisão narrativa sobre tosse aguda) apoiando esta direção.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Faringite (segundo as relações de indicação do grafo de conhecimento TxGNN; não há texto de indicação aprovada no Brasil) |
| Nova Indicação Prevista | Doença da Cavidade Nasal (Nasal Cavity Disease) |
| Pontuação de Previsão TxGNN | 99,91% |
| Nível de Evidência | L5 (apenas previsão do modelo; a única publicação disponível é uma revisão narrativa sem verificação do desenho, o que não alcança o nível L3) |
| Situação no Mercado Brasileiro | Não comercializado |
| Número de Registros | 0 |
| Decisão Recomendada | Hold |

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação nos dados compilados para este relatório. Segundo informações conhecidas de farmacologia geral, o ambroxol é um agente mucolítico e secretolítico que aumenta a depuração das secreções das vias aéreas. Também apresenta atividade anestésica local (bloqueio de canais de sódio) e propriedades anti-inflamatórias.

A faringite e as doenças da cavidade nasal são ambas afecções das vias aéreas superiores, com hipersecreção de muco e irritação da mucosa. Por isso, é plausível que o efeito sobre as secreções e o efeito anestésico/anti-inflamatório local possam aliviar sintomas nasais. Trata-se, porém, de uma inferência baseada em farmacologia geral, não confirmada pelos dados compilados.

Vale notar que o ambroxol também atua como chaperona da enzima glucosilceramidase beta (GBA1) e está sendo estudado para doenças neurodegenerativas, como Parkinson e esclerose lateral amiotrófica. Isso não tem relação direta com a indicação nasal prevista.

## Evidências da Literatura

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [26525480](https://pubmed.ncbi.nlm.nih.gov/26525480/) | 2015 | Revisão narrativa (desenho não verificável) | Vestnik otorinolaringologii | Discute o tratamento da tosse aguda associada a gripe e infecções respiratórias virais agudas, em que a tosse pode ser produtiva, com expectoração evidente |

Não há ensaios clínicos registrados relacionados a esta indicação.

## Considerações de Segurança

- **Interações Medicamentosas**: foi identificada 1 interação farmacológica, com a glucosilceramidase beta (GBA1). O ambroxol atua como chaperona inibitória da enzima em pH neutro, mas aumenta a atividade intracelular da enzima nos lisossomos ácidos. Trata-se de uma interação de alvo farmacológico, sem nível de gravidade classificado.

Para advertências e contraindicações, consulte a bula.

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
A pontuação do modelo é muito alta (99,91%), mas não há ensaios clínicos e a única publicação é uma revisão narrativa sobre tosse aguda, não específica para doença da cavidade nasal. Além disso, o fármaco não é comercializado no Brasil e os dados de segurança e de mecanismo estão incompletos.

**Para prosseguir, é necessário:**
- Obter a bula na ANVISA para avaliar advertências e contraindicações (lacuna bloqueante para a triagem de segurança)
- Complementar os dados do mecanismo de ação (por exemplo, via DrugBank)
- Buscar estudos clínicos ou observacionais específicos de ambroxol em doenças da cavidade nasal
- Esclarecer a via de administração necessária (a compatibilidade de vias ainda está pendente) e a viabilidade regulatória, dado que não há registro no Brasil
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

