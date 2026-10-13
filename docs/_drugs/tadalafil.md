---
layout: default
title: Tadalafil
parent: Apenas Predição do Modelo (L5)
nav_order: 603
evidence_level: L5
indication_count: 8
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

<div id="pharmacist">

## Relatório de avaliação farmacêutica

</div>

# Tadalafila: Da hiperplasia prostática benigna à hipertricose congênita universal tipo Ambras

## Resumo em Uma Frase

Tadalafila é um inibidor da fosfodiesterase tipo 5 (PDE5), originalmente usado em hiperplasia prostática benigna, hipertensão pulmonar e disfunção erétil, entre outras condições.
O modelo TxGNN prevê que pode ser eficaz para **Hipertricose universal congênita tipo Ambras (Ambras type hypertrichosis universalis congenita)**, mas há **0 ensaios clínicos** e **0 publicações** apoiando esta direção. Trata-se de uma previsão puramente computacional.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Hiperplasia prostática benigna (as indicações originais vêm do grafo de conhecimento; não há texto de indicação de registro no Brasil) |
| Nova Indicação Prevista | Hipertricose universal congênita tipo Ambras (Ambras type hypertrichosis universalis congenita) |
| Pontuação de Previsão TxGNN | 99,98% |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | ✗ Não comercializado (nos dados compilados) |
| Número de Registros | 0 |
| Decisão Recomendada | Hold |

---

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação no material compilado. Segundo informações conhecidas, a tadalafila é um inibidor da PDE5: aumenta o GMPc (monofosfato de guanosina cíclico) e provoca vasodilatação, o que sustenta seu uso em disfunção erétil, hipertensão pulmonar e hiperplasia prostática benigna.

**Na prática, esta previsão não tem respaldo mecanístico.** A síndrome de Ambras é um distúrbio genético raro do desenvolvimento do folículo piloso (rearranjos cromossômicos que afetam a regulação do gene TRPS1). Não há relação demonstrada entre a inibição da PDE5 e a correção desse defeito. Além disso, a hipertricose é um efeito adverso conhecido de outros vasodilatadores, como o minoxidil. Assim, um mecanismo baseado em vasodilatação mediada por GMPc tenderia, de forma plausível, a piorar a condição, e não a tratá-la.

A pontuação alta (0,9998; posição 228 no ranking do modelo) reflete apenas a estrutura do grafo de conhecimento, sem sustentação clínica ou na literatura.

---

## Outras Previsões do Modelo (Todas sem Respaldo)

| Posição | Doença prevista | Pontuação | Nível | Observação |
|------|------|------|------|------|
| 2 | Hipertricose | 99,98% | L5 | Direção farmacológica possivelmente oposta (hipertricose induzida por vasodilatadores) |
| 3 | Síndrome de malformação com componente dentário/periodontal | 99,97% | L5 | Sem vínculo mecanístico plausível |
| 4 | Síndrome com malformação de Dandy-Walker como característica principal | 99,97% | L5 | Malformação estrutural congênita; sem vínculo plausível |
| 5 | Anormalidade genética isolada da haste do cabelo | 99,96% | L5 | Defeito estrutural determinado geneticamente |
| 6 | Tricomegalia isolada familiar | 99,65% | L5 | Sem mecanismo demonstrado |
| 7 | Cardiopatia cifoescoliótica | 99,43% | L5 | Racional indireto fraco (hipertensão pulmonar e sobrecarga do coração direito); apenas hipótese |
| 8 | Enxaqueca com aura de tronco encefálico | 99,08% | L4 | Único registro é um relato de caso de **efeito adverso**, sinal de dano e não de benefício |

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

