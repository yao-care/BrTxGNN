---
layout: default
title: Milrinone
parent: Apenas Predição do Modelo (L5)
nav_order: 460
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-29
description: "Milrinone: nova indicação prevista, Alopecia (Alopecia) (nível de evidência L5). Indicação original: Vasodilatadores"
monitor_inn: "milrinone"
predicted_indications: ["alopecia", "hypotrichosis simplex of the scalp", "congenital hypotrichosis milia", "diffuse alopecia areata", "headache disorder", "migraine disorder", "migraine with brainstem aura", "trigeminal autonomic cephalalgia", "acute pulmonary heart disease"]
---

# Milrinone
{: .fs-9 }

Nível de evidência: **L5** | Indicações previstas: **9** 
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

## Milrinona: De vasodilatador à alopecia (previsão principal do modelo)
{: .text-alpha }

## Resumo em Uma Frase

Milrinona (lactato de milrinona) é um inibidor da fosfodiesterase 3 (PDE3), registrado na ANVISA na categoria de vasodilatadores e usado clinicamente na insuficiência cardíaca.
O modelo TxGNN prevê, como indicação de maior pontuação, que possa ser eficaz para **alopecia (Alopecia)**, mas **sem nenhum ensaio clínico ou publicação** que apoie essa direção.
Entre as demais previsões, a mais sustentada por evidências é **cor pulmonale agudo** (1 ensaio clínico e 20 publicações), muito próxima da indicação original.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Vasodilatadores |
| Nova Indicação Prevista | Alopecia (Alopecia) |
| Pontuação de Previsão TxGNN | 0,9991 |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | Comercializado (registros ativos: 2 de 3) |
| Número de Registros | 3 (ativos: 2) |
| Decisão Recomendada | Hold |

> **Observação:** a previsão de maior pontuação (alopecia) não tem nenhuma evidência real. As previsões com respaldo de evidências (insuficiência cardíaca congestiva e cor pulmonale agudo) estão descritas nas seções seguintes, pois ajudam a orientar a decisão.

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação nos registros compilados. Segundo informações conhecidas, a milrinona é um inibidor de PDE3 (também com afinidade registrada por PDE2A, PDE3B e PDE5A), com efeito inotrópico positivo e vasodilatador ("inodilatador"). Isso ocorre pelo aumento do AMPc em cardiomiócitos e na musculatura lisa vascular.

Para a **alopecia**, o vínculo é apenas teórico: o aumento da sinalização por AMPc e uma possível melhora da microcirculação do couro cabeludo, de forma semelhante ao vasodilatador minoxidil. Não há ensaios nem literatura que sustentem essa hipótese. Para as formas genéticas (hipotricose simples do couro cabeludo, hipotricose congênita com milia), a pontuação alta provavelmente reflete a proximidade na rede de conhecimento com outros termos de perda de cabelo, e não uma ligação biológica. Na alopecia areata difusa, que é autoimune, a inibição de PDE tem papel imunomodulador teórico, mas mais relacionado à PDE4 do que à PDE3.

Já para **insuficiência cardíaca congestiva** e **cor pulmonale agudo**, o vínculo é direto: a inibição de PDE3 reduz pós-carga e pulmonar vascular resistência, além de melhorar a função ventricular. O uso inalatório pode dar efeito pulmonar mais seletivo, com menos hipotensão sistêmica. Na cefaleia, a literatura trata da síndrome de vasoconstrição cerebral reversível (SVCR), uma entidade distinta, e o vínculo é indireto.

## Evidências de Ensaios Clínicos

Não há ensaios clínicos registrados para alopecia nem para as demais indicações capilares. Os ensaios abaixo se referem a **insuficiência cardíaca congestiva** (previsão #6) e **cor pulmonale agudo** (previsão #10), e são apresentados como contexto.

| Número do Ensaio | Fase | Status | Participantes | Principais Achados |
|---------|------|------|------|---------|
| [NCT01849094](https://clinicaltrials.gov/study/NCT01849094) | Phase 1/2 | Concluído | 9 | Formulação oral de liberação lenta de milrinona: farmacocinética estável e efeito hemodinâmico em insuficiência cardíaca |
| [NCT01956006](https://clinicaltrials.gov/study/NCT01956006) | Phase 1/2 | Concluído | 26 | Estudo piloto de milrinona oral de liberação lenta em insuficiência cardíaca avançada |
| [NCT07186062](https://clinicaltrials.gov/study/NCT07186062) | Phase 4 | Concluído | 60 | Levosimendana vs dobutamina vs milrinona em insuficiência cardíaca aguda descompensada com disfunção renal |
| [NCT03207165](https://clinicaltrials.gov/study/NCT03207165) | Phase 4 | Concluído | 192 | Milrinona vs dobutamina em pacientes críticos na unidade coronariana |
| [NCT04718350](https://clinicaltrials.gov/study/NCT04718350) | NA | Concluído | 40 | Levosimendana IV vs milrinona inalatória em cirurgia cardíaca com hipertensão pulmonar |
| [NCT02077010](https://clinicaltrials.gov/study/NCT02077010) | Phase 1 | Concluído | 10 | Milrinona nebulizada em insuficiência cardíaca avançada hospitalizada |
| [NCT05450328](https://clinicaltrials.gov/study/NCT05450328) | Phase 2 | Recrutando | 141 | Milrinona inalatória e epoprostenol para prevenir dificuldade de saída da circulação extracorpórea |
| [NCT02408003](https://clinicaltrials.gov/study/NCT02408003) | NA | Concluído | 30 | Levosimendana vs milrinona: deformação cardíaca e hemodinâmica |
| [NCT00338455](https://clinicaltrials.gov/study/NCT00338455) | Phase 2 | Encerrado | 16 | Nesiritida em candidatos a transplante, com milrinona como terapia de base; baixa relevância |
| [NCT02644057](https://clinicaltrials.gov/study/NCT02644057) | Phase 2 | Retirado | 0 | Dobutamina vs milrinona em síndrome cardiorrenal; nenhum participante incluído |

## Evidências da Literatura

Não há literatura para alopecia. As publicações abaixo se referem a cefaleia (SVCR), insuficiência cardíaca congestiva e cor pulmonale agudo.

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [25625413](https://pubmed.ncbi.nlm.nih.gov/25625413/) | 2015 | Revisão sistemática/meta-análise | Basic Clin Pharmacol Toxicol | Segurança e eficácia da milrinona na insuficiência cardíaca aguda após infarto agudo do miocárdio |
| [37999764](https://pubmed.ncbi.nlm.nih.gov/37999764/) | 2024 | Revisão sistemática/meta-análise | Eur J Pediatr | Papel da milrinona na insuficiência cardíaca e hipertensão pulmonar em neonatos e crianças |
| [2035427](https://pubmed.ncbi.nlm.nih.gov/2035427/) | 1991 | Estudo multicêntrico de fase III | Am Heart J | Benefícios hemodinâmicos e clínicos da milrinona IV em 189 pacientes com insuficiência cardíaca crônica grave |
| [3591689](https://pubmed.ncbi.nlm.nih.gov/3591689/) | 1987 | Ensaio randomizado | Am J Cardiol | Milrinona IV vs dobutamina em 79 pacientes com insuficiência cardíaca classe III/IV |
| [8903534](https://pubmed.ncbi.nlm.nih.gov/8903534/) | 1996 | Ensaio comparativo | Clin Cardiol | Milrinona vs dobutamina em insuficiência cardíaca após infarto agudo (33 pacientes) |
| [31865433](https://pubmed.ncbi.nlm.nih.gov/31865433/) | 2020 | Estudo comparativo retrospectivo | Heart Vessels | Milrinona vs olprinona em 288 pacientes com insuficiência cardíaca |
| [41296998](https://pubmed.ncbi.nlm.nih.gov/41296998/) | 2025 | Revisão | Cardiol Rev | Evidências atuais e perspectivas da milrinona na insuficiência cardíaca avançada |
| [18647181](https://pubmed.ncbi.nlm.nih.gov/18647181/) | 2009 | Relato de caso | Headache | Milrinona intra-arterial em um caso de SVCR com deterioração neurológica |
| [34784343](https://pubmed.ncbi.nlm.nih.gov/34784343/) | 2021 | Relato de caso | Am J Case Rep | SVCR em contexto de eclâmpsia com resposta à infusão de milrinona |
| [11792300](https://pubmed.ncbi.nlm.nih.gov/11792300/) | 2001 | Estudo clínico | Rev Esp Anestesiol Reanim | Efeito vasodilatador pulmonar de prostaciclina e milrinona inaladas na hipertensão pulmonar |

## Informações de Comercialização no Brasil

Os 3 registros (3 de 3) estão **válidos**; o medicamento está comercializado.

| Número de Registro | Nome Comercial | Forma Farmacêutica | Indicação Aprovada |
|---------|------|------|-----------|
| Registro 100410234 | Lactato de Milrinona | Não informada | Vasodilatadores |
| Registro 183260321 | Primacor | Não informada | Vasodilatadores |
| Registro 174650017 | Lactato de Milrinona | Não informada | Vasodilatadores |

## Considerações de Segurança

- **Contraindicações (segundo a rede de conhecimento do TxGNN, e não o texto da bula):** doença renal, piureter, distúrbio hipotensivo, infarto do miocárdio, trombose coronária, hemoglobinopatia, parada cardíaca súbita, doença do sistema de condução cardíaco, estenose da válvula pulmonar (incluindo a forma valvar), cardiomiopatia hipertrófica (incluindo a familiar).
- **Interações Medicamentosas (9 registradas):** interações de nível moderado com amifostina, diatrizoato, anagrelida, ozanimode e procarbazina. Há ainda afinidade farmacológica com PDE2A, PDE3A, PDE3B e PDE5A.
- **Observação clínica:** o uso oral prolongado foi associado a aumento de mortalidade, e o uso deve se restringir a contextos de curto prazo ou paliativos, com monitoramento hemodinâmico. Há cautela quanto a hipotensão e arritmia.

Consulte a bula para as advertências e contraindicações oficiais, que não estavam disponíveis nos dados compilados.

## Conclusão e Próximos Passos

**Decisão: Hold** (para a indicação principal, alopecia)

**Justificativa:**
- A previsão de alopecia (0,9991) é apenas do modelo (L5): não há ensaios, literatura nem mecanismo estabelecido, e a pontuação alta parece refletir proximidade na rede com termos de perda de cabelo. Todas as indicações capilares, bem como enxaqueca e cefaleias relacionadas, permanecem em Hold.
- Para fins de contexto, cor pulmonale agudo alcança nível L2 (Proceed with Guardrails), mas é uma indicação muito próxima do uso cardiovascular já conhecido e, portanto, pouco "nova". Além disso, os 3 registros brasileiros (3 de 3) estão válidos e o medicamento está comercializado.

**Para prosseguir, é necessário:**
- Obter da ANVISA a bula com advertências e contraindicações oficiais (lacuna bloqueante para a triagem de segurança).
- Complementar os dados de mecanismo de ação (consulta ao DrugBank).
- Para alopecia: estudos pré-clínicos (por exemplo, modelos de folículo piloso) que testem o efeito da inibição de PDE3, e avaliação de viabilidade de via tópica, já que o uso atual é intravenoso.
- Definir a situação regulatória: como não há registro válido no Brasil, seria necessário novo registro ou reativação.
- Se o interesse for cardiovascular, priorizar a análise de insuficiência cardíaca aguda e cor pulmonale, com monitoramento hemodinâmico e restrição a uso de curto prazo.
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

