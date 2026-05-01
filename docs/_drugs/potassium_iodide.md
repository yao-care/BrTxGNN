---
layout: default
title: Potassium Iodide
parent: 僅模型預測 (L5)
nav_order: 408
evidence_level: L5
indication_count: 10
---

# Potassium Iodide
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

Using **txgnn-pipeline** como contexto de projeto. Gerando relatório conforme o formato especificado.

---

# Iodeto de Potássio: Do tratamento de micoses à doença da cavidade nasal

## Resumo em Uma Frase

Iodeto de potássio (KI) é um composto mineral com uso histórico como antifúngico e expectorante, especialmente na forma de solução saturada (SSKI), empregado no tratamento de micoses cutâneas como esporotricose e pitiose em humanos e animais.
O modelo TxGNN prevê que pode ser eficaz para **Doença da Cavidade Nasal (Nasal Cavity Disease)**, atualmente com **0 ensaios clínicos** e **4 publicações** apoiando esta direção.
As evidências disponíveis provêm quase exclusivamente de relatos de casos veterinários, com um único caso humano documentado — zigomicose nasofacial tratada com KI no Estado do Pará, Brasil (PMID 7997795).

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Sem registro no Brasil; uso histórico como antifúngico e expectorante (SSKI) |
| Nova Indicação Prevista | Doença da Cavidade Nasal (Nasal Cavity Disease) |
| Pontuação de Previsão TxGNN | 99.95% |
| Nível de Evidência | L4 |
| Situação no Mercado Brasileiro | ✗ Não comercializado |
| Número de Registros | 0 |
| Decisão Recomendada | Hold |

---

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação no registro disponível. Com base no conhecimento farmacológico estabelecido, o iodeto de potássio apresenta múltiplas ações: atividade antifúngica direta (especialmente na forma de SSKI — Solução Saturada de Iodeto de Potássio), efeito expectorante por estimulação da secreção mucoserosa das vias aéreas, e possível ação imunomoduladora ainda parcialmente elucidada. O SSKI é utilizado há décadas no tratamento de infecções fúngicas cutâneas e subcutâneas como esporotricose e pitiose, tanto em humanos quanto em medicina veterinária.

A relação entre o uso antifúngico do KI e a doença da cavidade nasal é biologicamente plausível. A cavidade nasal é sítio frequente de infecções fúngicas como aspergilose rinosinusal, zigomicose nasofacial e pitiose rinonasal — todas causadas por patógenos sobre os quais o KI demonstrou atividade na literatura. A literatura veterinária documenta consistentemente o uso de KI oral para rinite micótica em ovinos e equinos no Brasil. Ainda mais relevante, um caso humano brasileiro (Barcarena, Pará, 1994) de zigomicose nasofacial com envolvimento da mucosa nasal apresentou resposta rápida ao tratamento com KI, fornecendo o único precedente humano direto para esta indicação.

No entanto, as limitações são substanciais: o único caso humano é histórico (1994) e não controlado; a grande maioria das evidências é veterinária (Tier 3); e o mecanismo exato do KI sobre os patógenos da cavidade nasal humana permanece incompletamente caracterizado. Estudos clínicos controlados em humanos são indispensáveis antes de qualquer aplicação clínica sistemática.

---

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados para a indicação de doença da cavidade nasal.

---

## Evidências da Literatura

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [7997795](https://pubmed.ncbi.nlm.nih.gov/7997795/) | 1994 | Human Case Report | Rev Inst Med Trop São Paulo | Zigomicose nasofacial em paciente do Pará, Brasil (2.º caso no Norte do Brasil); resposta rápida ao tratamento com iodeto de potássio, confirmado por achados micológicos e histopatológicos |
| [34902797](https://pubmed.ncbi.nlm.nih.gov/34902797/) | 2022 | Veterinary Case Series | Journal de mycologie médicale | Pitiose rinonasal em ovinos no Brasil causada por *Pythium insidiosum*; tratamento bem-sucedido com KI; massas necroproliferativas ocupavam a cavidade nasal rostral e palato duro |
| [39576399](https://pubmed.ncbi.nlm.nih.gov/39576399/) | 2024 | Veterinary Case Report | Veterinary Research Communications | Rinite micótica por *Aspergillus fumigatus* em égua Quarter Horse; KI oral combinado com clotrimazol tópico; achados incluíam erosão e cicatrizes da mucosa nasal, secreção purulenta e sanguinolenta |
| [10976304](https://pubmed.ncbi.nlm.nih.gov/10976304/) | 2000 | Veterinary Case Report | J Am Vet Med Assoc | Infecção por *Pseudallescheria boydii* em cavidade nasal equina; tratamento com miconazol intranasal + iodeto de **sódio** IV (composto estruturalmente relacionado ao KI, mas farmacologicamente distinto) |

---

## Informações de Comercialização no Brasil

Iodeto de potássio não possui registro na ANVISA e não está comercializado no Brasil. Nenhuma licença foi identificada na base de dados regulatória.

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
As evidências disponíveis para doença da cavidade nasal são inteiramente compostas por relatos de casos (Tier 3), com apenas um caso humano histórico documentado, sem ensaios clínicos controlados em humanos. O nível de evidência L4 é insuficiente para suportar uma decisão de avanço imediato.

**Para prosseguir, é necessário:**
- Levantamento sistemático de todos os casos humanos documentados de infecções fúngicas da cavidade nasal tratadas com KI ou SSKI (revisão narrativa ou scoping review)
- Obtenção e análise completa dos dados de segurança do KI: perfil de iodismo, risco de disfunção tireoidiana (hiper e hipotireoidismo), e risco de urticária induzida por iodeto (iodide-induced urticaria / iododerma), que representam contraindicações relativas importantes
- Atenção ao **sinal de segurança invertido**: o TxGNN prevê KI para urticária alérgica (Rank 5), mas KI é um **indutor conhecido de urticária** — esse dado sugere cautela no perfil de segurança do fármaco e deve ser incluído na avaliação de risco
- Definição de subpopulação-alvo para estudo clínico: pacientes com rinite fúngica confirmada por zigomicose ou pitiose em regiões tropicais do Brasil, onde esses patógenos são endêmicos
- Revisão dos resultados do ensaio NCT03980132 (Phase 4, n=184, concluído em 2023) sobre a solução de Lugol (contendo KI) em preparo cirúrgico tireoidiano, que pode fornecer dados de segurança sistêmica úteis para formulação de dose e monitoramento
- Delineamento de estudo clínico piloto (Phase 1/2) em humanos com infecções fúngicas da cavidade nasal confirmadas microbiologicamente
---

