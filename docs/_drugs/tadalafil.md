---
layout: default
title: Tadalafil
parent: Apenas Predição do Modelo (L5)
nav_order: 603
evidence_level: L5
indication_count: 8
last_modified_at: 2026-10-28
monitor_inn: "TADALAFIL"
predicted_indications: ["Ambras type hypertrichosis universalis congenita", "hypertrichosis (disease)", "malformation syndrome with odontal and/or periodontal component", "syndrome with a Dandy-Walker malformation as major feature", "isolated genetic hair shaft abnormality", "familial isolated trichomegaly", "kyphoscoliotic heart disease", "migraine with brainstem aura"]
description: "Tadalafil: nova indicação prevista, Hipertricose universal congênita tipo Ambras (Ambras type hypertrichosis universalis congenita) (nível de evidência L5). Indicação original: Não consta nos dados l…"
---

# Tadalafil
{: .fs-9 }

Nível de evidência: **L5** | Indicações previstas: **8** 
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

## Tadalafil: Hipertricose universal congênita tipo Ambras (Ambras type hypertrichosis universalis congenita)
{: .text-alpha }

## Resumo em Uma Frase

Tadalafila é um inibidor da fosfodiesterase tipo 5 (PDE5), originalmente usado em hiperplasia prostática benigna, hipertensão pulmonar e disfunção erétil, entre outras condições.
O modelo TxGNN prevê que pode ser eficaz para **Hipertricose universal congênita tipo Ambras (Ambras type hypertrichosis universalis congenita)**, mas há **0 ensaios clínicos** e **0 publicações** apoiando esta direção. Trata-se de uma previsão puramente computacional.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Não consta nos dados locais |
| Nova Indicação Prevista | Hipertricose universal congênita tipo Ambras (Ambras type hypertrichosis universalis congenita) |
| Pontuação de Previsão TxGNN | 0.9998 |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | Comercializado (registros ativos: pelo menos 11) |
| Número de Registros | 0 |
| Decisão Recomendada | Hold |

---

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação no material compilado. Segundo informações conhecidas, a tadalafila é um inibidor da PDE5: aumenta o GMPc (monofosfato de guanosina cíclico) e provoca vasodilatação, o que sustenta seu uso em disfunção erétil, hipertensão pulmonar e hiperplasia prostática benigna.

**Na prática, esta previsão não tem respaldo mecanístico.** A síndrome de Ambras é um distúrbio genético raro do desenvolvimento do folículo piloso (rearranjos cromossômicos que afetam a regulação do gene TRPS1). Não há relação demonstrada entre a inibição da PDE5 e a correção desse defeito. Além disso, a hipertricose é um efeito adverso conhecido de outros vasodilatadores, como o minoxidil. Assim, um mecanismo baseado em vasodilatação mediada por GMPc tenderia, de forma plausível, a piorar a condição, e não a tratá-la.

A pontuação alta (0.9998) vem do modelo TxGNN (deep learning) e pode refletir semelhanças que o modelo aprendeu entre doenças relacionadas, não evidência biológica.

---

## Outras Previsões do Modelo (Todas sem Respaldo)

| Posição | Doença prevista | Pontuação | Nível | Observação |
|------|------|------|------|------|
| 2 | Hipertricose | 0,9998 | L5 | Direção farmacológica possivelmente oposta (hipertricose induzida por vasodilatadores) |
| 3 | Síndrome de malformação com componente dentário/periodontal | 0,9997 | L5 | Sem vínculo mecanístico plausível |
| 4 | Síndrome com malformação de Dandy-Walker como característica principal | 0,9997 | L5 | Malformação estrutural congênita; sem vínculo plausível |
| 5 | Anormalidade genética isolada da haste do cabelo | 0,9996 | L5 | Defeito estrutural determinado geneticamente |
| 6 | Tricomegalia isolada familiar | 0,9965 | L5 | Sem mecanismo demonstrado |
| 7 | Cardiopatia cifoescoliótica | 0,9943 | L5 | Racional indireto fraco (hipertensão pulmonar e sobrecarga do coração direito); apenas hipótese |
| 8 | Enxaqueca com aura de tronco encefálico | 0,9908 | L4 | Único registro é um relato de caso de **efeito adverso**, sinal de dano e não de benefício |

---

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados.

---

## Evidências da Literatura

Para a indicação principal (hipertricose universal congênita tipo Ambras), atualmente não há literatura relacionada.

Entre as demais previsões, a única publicação identificada refere-se à enxaqueca com aura de tronco encefálico:

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [17059442](https://pubmed.ncbi.nlm.nih.gov/17059442/) | 2006 | Relato de caso | Cephalalgia | Tadalafila associada a aura migranosa típica sem cefaleia, ou seja, um evento adverso e não um efeito terapêutico (resumo não disponível) |

---

## Considerações de Segurança

- **Contraindicações segundo o grafo de conhecimento (não é texto de bula):** o grafo associa a tadalafila a contraindicação em diversas condições, entre elas:
  - Cardiovasculares: estenose aórtica e doenças da valva aórtica, infarto do miocárdio, síndrome coronariana aguda, trombose coronariana, cardiomiopatia hipertrófica (inclusive familiar) e distúrbios hipotensivos.
  - Cerebrovasculares: acidente vascular cerebral, doença cerebrovascular e infarto cerebral.
  - Hematológicas: anemia falciforme, hemoglobinopatias, persistência hereditária de hemoglobina fetal, doenças da coagulação, mieloma de plasmócitos e leucemia.
  - Penianas: priapismo, doença de Peyronie, fibromatose peniana e balanite xerótica obliterante.
  - Outras: insuficiência hepática, epilepsia, perda auditiva (inclusive surdez mista ligada ao X com gusher perilinfático) e perda visual funcional.
- **Interações medicamentosas:** foram identificadas 100 interações no total; entre as listadas, a maioria é de gravidade moderada.
  - Moderadas: aprepitanto, dexametasona, lorcasserina, claritromicina, cimetidina, miconazol, clotrimazol, sapropterina, troglitazona e os inibidores de SGLT2 (canagliflozina, dapagliflozina, empagliflozina, ertugliflozina).
  - Leve: papaverina.
  - Gravidade não classificada: pantoprazol, glimepirida, doxiciclina, morfina, metformina e omeprazol.
- Para advertências e contraindicações em bula, consulte a bula aprovada pela ANVISA.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
- A previsão baseia-se apenas na pontuação do modelo (nível L5), sem ensaios clínicos nem literatura. O racional farmacológico sugere inclusive direção oposta à terapêutica, já que vasodilatadores podem causar hipertricose.
- A tadalafila não tem registro comercializado no Brasil nos dados compilados, e há contraindicações extensas segundo o grafo de conhecimento.

**Para prosseguir, é necessário:**
- Dados do mecanismo de ação (MOA) a partir do DrugBank, para permitir análise mecanística formal.
- Advertências e contraindicações da bula na ANVISA (lacuna bloqueante para a triagem de segurança).
- Evidência pré-clínica que demonstre plausibilidade biológica da inibição de PDE5 em distúrbios do folículo piloso, o que hoje não existe.
- Avaliar a priorização de outras previsões com racional mais plausível, como a cardiopatia cifoescoliótica (via hipertensão pulmonar), antes de qualquer investimento nesta indicação.
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

