---
layout: default
title: Oxacillin
parent: Apenas Predição do Modelo (L5)
nav_order: 496
evidence_level: L5
indication_count: 4
last_modified_at: 2026-10-13
description: "Oxacillin: nova indicação prevista, Epiglotite (Epiglottitis) (nível de evidência L5). Indicação original: Penicilinas resistentes à penicilinase"
monitor_inn: "oxacillin"
predicted_indications: ["epiglottitis", "laryngitis", "bacterial arthritis", "urinary tract infection (disease)"]
---

# Oxacillin
{: .fs-9 }

Nível de evidência: **L5** | Indicações previstas: **4** 
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

## Oxacilina: Da terapia antibacteriana sistêmica à epiglotite
{: .text-alpha }

## Resumo em Uma Frase

A oxacilina é uma penicilina resistente à penicilinase, originalmente usada como antibiótico sistêmico.
O modelo TxGNN prevê que ela pode ser eficaz para **Epiglotite (Epiglottitis)**, mas atualmente há **0 ensaios clínicos** e **0 publicações** apoiando esta direção específica.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Penicilinas resistentes à penicilinase |
| Nova Indicação Prevista | Epiglotite (Epiglottitis) |
| Pontuação de Previsão TxGNN | 0,9990 |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | Comercializado (registros ativos: 6 de 6) |
| Número de Registros | 6 (ativos: 6) |
| Decisão Recomendada | Hold |

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação. Segundo informações conhecidas, a oxacilina faz parte da classe das penicilinas resistentes à penicilinase (beta-lactâmicos), com atividade contra *Staphylococcus aureus* sensível à meticilina (MSSA).

A epiglotite é uma infecção bacteriana aguda, na qual o *S. aureus* pode ser um dos agentes causadores. Por isso, existe uma lógica antibacteriana para a previsão. No entanto, o tratamento empírico padrão costuma priorizar agentes com cobertura para *H. influenzae* e estreptococos, e a cobertura de *S. aureus* geralmente é feita com outros fármacos.

A pontuação alta do TxGNN (0,9990) não é sustentada por nenhum ensaio clínico ou publicação recuperados. Trata-se, portanto, de uma previsão do modelo sem confirmação por dados reais.

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados.

## Evidências da Literatura

Atualmente não há literatura relacionada.

## Informações de Comercialização no Brasil

Os 6 registros no Brasil estão válidos; o medicamento é comercializado.

| Número de Registro | Nome Comercial | Forma Farmacêutica | Indicação Aprovada |
|---------|------|------|-----------|
| Registro nº 116370111 | OXANON | Não informada | Penicilinas penicilinase-resistentes |
| Registro nº 103700282 | Oxacilina Sódica | Não informada | Antibióticos sistêmicos simples |
| Registro nº 174200007 | Oxacilina Sódica | Não informada | Penicilinas penicilinase-resistentes |
| Registro nº 116370141 | Oxacilina Sódica | Não informada | Penicilinas penicilinase-resistentes |
| Registro nº 100410179 | Oxacilil | Não informada | Antibióticos sistêmicos simples |

## Considerações de Segurança

- **Contraindicações (grafo de conhecimento, não texto de bula)**: doença renal, piureter, colite por *Clostridium difficile*, enterocolite necrosante perinatal, mononucleose infecciosa e síndrome de infecção crônica pelo vírus Epstein-Barr.
- **Interações Medicamentosas**: foram identificadas 41 interações no total. As de gravidade moderada incluem:
  - Doxiciclina
  - Tetraciclina
  - Minociclina
  - Ácido picossulfúrico
  - Iodeto I-131

  A claritromicina tem interação de gravidade leve. Outras (por exemplo, morfina, omeprazol, vancomicina e metronidazol) têm gravidade não classificada.

Consulte a bula para advertências e contraindicações formais, que não estavam disponíveis nos dados compilados para este relatório.

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
- A previsão para epiglotite tem pontuação alta no modelo (TxGNN, deep learning), mas não conta com ensaios clínicos nem literatura (nível L5). O uso estaria, além disso, dentro do espectro antibacteriano já conhecido, e não seria um reposicionamento claramente novo. O medicamento é comercializado no Brasil, com 6 registros válidos de 6.

**Para prosseguir, é necessário:**
- Obter e analisar a bula na ANVISA para advertências e contraindicações formais.
- Complementar os dados de mecanismo de ação (DrugBank).
- Realizar revisão da literatura clínica sobre o papel de antiestafilocócicos na epiglotite.
- Verificar a disponibilidade comercial atual, dado que não há registro válido no Brasil.
- Avaliar a via de administração e a forma farmacêutica necessárias.

**Observação sobre outras indicações previstas:** "artrite bacteriana" (pontuação 0,9950, nível L4) tem plausibilidade mecanística maior, pois a oxacilina é tratamento estabelecido para infecções osteoarticulares por MSSA. Contudo, a literatura recuperada é majoritariamente descritiva (revisões, séries de casos, epidemiologia), sem ensaios diretos de eficácia, e trata-se de uso já dentro da indicação antibacteriana existente. "Laringite" (0,9973, L5) e "infecção do trato urinário" (0,9903, L4) são pouco plausíveis clinicamente: a laringite é majoritariamente viral, e a oxacilina não cobre as enterobactérias, principais causadoras de ITU. Ambas permanecem em Hold.
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

