---
layout: default
title: Loperamide
parent: Apenas Predição do Modelo (L5)
nav_order: 423
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Loperamide: nova indicação prevista, Conjuntivite contagiosa aguda (acute contagious conjunctivitis) (nível de evidência L5). Indicação original: Antidiarreicos simples sem ação antimicrobiana"
monitor_inn: "Loperamide"
predicted_indications: ["acute contagious conjunctivitis", "amebic dysentery", "conjunctivitis", "gastroduodenitis", "pseudomembranous conjunctivitis", "parasitic conjunctivitis", "serous conjunctivitis except viral", "chronic follicular conjunctivitis", "conjunctival folliculosis", "Angelucci syndrome"]
---

# Loperamide
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

## Loperamida: De antidiarreico a conjuntivite contagiosa aguda (previsão sem respaldo)
{: .text-alpha }

## Resumo em Uma Frase

A loperamida é um antidiarreico simples, sem ação antimicrobiana, originalmente usado para controlar a diarreia.
O modelo TxGNN prevê que poderia ser eficaz para **conjuntivite contagiosa aguda (acute contagious conjunctivitis)**, mas **não há nenhum ensaio clínico nem publicação** que sustente essa previsão.
A pontuação alta vem do modelo TxGNN (deep learning) e pode refletir semelhanças que o modelo aprendeu entre doenças relacionadas, não evidência biológica.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Antidiarreicos simples sem ação antimicrobiana |
| Nova Indicação Prevista | Conjuntivite contagiosa aguda (acute contagious conjunctivitis) |
| Pontuação de Previsão TxGNN | 0,9997 |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | Comercializado (registros ativos: 8 de 8) |
| Número de Registros | 8 (ativos: 8) |
| Decisão Recomendada | Hold |

---

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação nos dados compilados para este relatório. Segundo informações conhecidas, a loperamida é um agonista dos receptores opioides mu periféricos, que age nos neurônios mioentéricos do intestino e reduz a motilidade intestinal. É essa ação que explica seu uso no alívio sintomático da diarreia.

**Na prática, a previsão não é razoável.** Não foi identificado nenhum vínculo mecanístico plausível entre a inibição da motilidade intestinal mediada por opioides e a conjuntivite infecciosa. O papel da loperamida no olho não tem respaldo. A pontuação elevada (0,9997) vem do modelo TxGNN (deep learning) e pode refletir semelhanças que o modelo aprendeu entre doenças relacionadas, não justificativa biológica.

O mesmo padrão aparece nas demais previsões do modelo. Das 10 principais, 7 são variações de conjuntivite ou condições oculares correlatas (com pontuações idênticas em vários casos, sinal de artefato compartilhado), e nenhuma tem ensaio clínico. As duas previsões com alguma literatura, **disenteria amebiana** e **gastroduodenite**, apontam para **risco**, não para benefício (ver "Evidências da Literatura").

---

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados.

---

## Evidências da Literatura

Para a indicação principal (conjuntivite contagiosa aguda) não há literatura. A tabela abaixo reúne os estudos encontrados para outras previsões do modelo, que servem principalmente como alerta de segurança.

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [17241255](https://pubmed.ncbi.nlm.nih.gov/17241255/) | 2007 | Relato de caso | Journal of Travel Medicine | Colite amebiana fulminante (megacólon tóxico) após uso intenso de loperamida; antimotilidade pode agravar a infecção |
| [41924411](https://pubmed.ncbi.nlm.nih.gov/41924411/) | 2026 | Relato de caso | Cureus | Depressão respiratória por loperamida em inflamação gastrointestinal grave pós-quimioterapia, com maior absorção sistêmica |
| [3893119](https://pubmed.ncbi.nlm.nih.gov/3893119/) | 1985 | Revisão | The American Journal of Medicine | Terapias não líquidas e quimioprofilaxia da diarreia aguda; a hidratação oral é a base do tratamento |

---

## Informações de Comercialização no Brasil

Os 8 registros estão válidos (8 de 8); o medicamento está comercializado atualmente.

| Número de Registro | Nome Comercial | Forma Farmacêutica | Indicação Aprovada |
|---------|------|------|-----------|
| Registro nº 117170085 | Cloridrato de Loperamida | Não informada | Antidiarreicos simples sem ação antimicrobiana |
| Registro nº 157211211 | Imosec | Não informada | Antidiarreicos adsorventes e antiflatulentos |
| Registro nº 100470318 | Diasec | Não informada | Antidiarreicos adsorventes e antiflatulentos |
| Registro nº 155840142 | Magnostase | Não informada | Antidiarreicos simples sem ação antimicrobiana |
| Registro nº 105350159 | Cloridrato de Loperamida | Não informada | Antidiarreicos simples sem ação antimicrobiana |

Há outros 3 registros cancelados (nº 100470525, 105350156 e 117170026), não listados por limite de 5 registros.

---

## Considerações de Segurança

- **Contraindicações (segundo o grafo de conhecimento, não texto de bula)**: doença hepática, doença da vesícula biliar, íleo paralítico, obstrução intestinal, miopatia visceral familiar, disenteria, doenças diarreicas, diarreia infecciosa e doenças infecciosas intestinais.
- **Interações medicamentosas**: foram identificadas 100 interações no total. Entre as principais, de gravidade **maior**: abiraterona, ranitidina, fosamprenavir e genfibrozila. De gravidade **moderada**: outros opioides (codeína, di-hidrocodeína, tramadol), anti-histamínicos (clorfeniramina, cetirizina, acrivastina), etanol, salbutamol, alfuzosina, galantamina, foscarnet, fostamatinibe, fostemsavir, gemifloxacino e gilteritinibe.
- **Sinais da literatura**: risco de megacólon tóxico em infecções invasivas (como amebíase) e de depressão respiratória com maior exposição sistêmica em inflamação intestinal grave.

Consulte a bula para as demais informações de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
- A previsão não tem ensaios clínicos, literatura nem mecanismo plausível (nível L5), e a pontuação alta vem do modelo TxGNN (deep learning) e pode refletir semelhanças aprendidas entre doenças relacionadas, não evidência biológica. O medicamento está comercializado no Brasil, com 8 registros válidos de 8.
- Os únicos sinais da literatura nas previsões relacionadas indicam risco, não benefício.

**Para prosseguir, seria necessário:**
- Dados de mecanismo de ação (MOA) confirmados, por exemplo via DrugBank.
- Obter e analisar as bulas na ANVISA (advertências e contraindicações), pendência que bloqueia a triagem de segurança.
- Algum indício biológico ou pré-clínico que ligue a loperamida à superfície ocular; sem isso, não se recomenda investimento adicional.
- Reavaliar a rota de administração, pois a loperamida é de uso oral e a indicação ocular exigiria via tópica, ainda não avaliada.
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

