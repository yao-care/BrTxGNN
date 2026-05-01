---
layout: default
title: Oxaliplatin
parent: 僅模型預測 (L5)
nav_order: 376
evidence_level: L5
indication_count: 10
---

# Oxaliplatin
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

# Oxaliplatin: Do câncer colorretal ao mesotelioma pleural maligno

## Resumo em Uma Frase

Oxaliplatin é um agente quimioterápico de terceira geração à base de platina, amplamente estabelecido no tratamento do câncer colorretal como componente central dos regimes FOLFOX e XELOX.
O modelo TxGNN prevê que pode ser eficaz para **Mesotelioma Pleural Maligno (Malignant Pleural Mesothelioma)**,
atualmente com **5 ensaios clínicos** e **20 publicações** apoiando esta direção.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Câncer colorretal (uso clínico estabelecido; regime FOLFOX/XELOX) |
| Nova Indicação Prevista | Mesotelioma Pleural Maligno (Malignant Pleural Mesothelioma) |
| Pontuação de Previsão TxGNN | 99,68% |
| Nível de Evidência | L2 |
| Situação no Mercado Brasileiro | ✓ Comercializado |
| Número de Registros | 20 |
| Decisão Recomendada | Proceed with Guardrails |

---

## Por que Esta Previsão é Razoável?

Embora os dados detalhados de mecanismo de ação não estejam disponíveis neste Evidence Pack, o oxaliplatin é reconhecidamente um agente alquilante de DNA pertencente à classe das platinas de terceira geração. Ele forma adutos intrafita do tipo 1,2-d(GpG) entre guaninas adjacentes da dupla-hélice, bloqueando a replicação e a transcrição do DNA nas células tumorais. Ao contrário da cisplatina, os adutos volumosos formados pelo oxaliplatin apresentam geometria tridimensional distinta, dificultando o reconhecimento pelos sistemas de reparo nucleotídico (NER) em alguns contextos.

O mesotelioma pleural maligno (MPM) é um tumor altamente quimioresistente que superexpressa enzimas do complexo de reparo ERCC1/XPF — o mesmo sistema que confere resistência à cisplatina. A estrutura diferenciada dos adutos do oxaliplatin permite contornar parcialmente essa resistência cruzada, tornando o oxaliplatin uma opção biologicamente plausível para pacientes com MPM, especialmente em segunda linha após falha a pemetrexed + cisplatina. Adicionalmente, estudos translacionais demonstraram que o oxaliplatin induz morte celular imunogênica (ICD) com liberação de DAMPs (como calreticulina e HMGB1), abrindo perspectiva de sinergia com inibidores de checkpoint imunológico no MPM.

Esta hipótese foi validada por múltiplos ensaios clínicos prospectivos de Fase 2, com destaque para os regimes GEMOX (gemcitabina + oxaliplatin) e raltitrexed + oxaliplatin, todos testados diretamente em pacientes com MPM difuso. Os resultados são mistos — o regime GEMOX demonstrou atividade como primeira e segunda linhas, enquanto raltitrexed + oxaliplatin mostrou eficácia em primeira linha (JCO, 2003) mas ausência de resposta em segunda linha (Lung Cancer, 2005) —, sublinhando a importância do contexto de uso.

---

## Evidências de Ensaios Clínicos

| Número do Ensaio | Fase | Status | Participantes | Principais Achados |
|---------|------|------|------|---------|
| [NCT00859469](https://clinicaltrials.gov/study/NCT00859469) | Phase 2 | Concluído | 29 | Avalia diretamente a taxa de resposta do regime GEMOX (oxaliplatin + gemcitabina) como quimioterapia de 1ª ou 2ª linha em pacientes com mesotelioma pleural ou peritoneal maligno — evidência central para esta indicação |
| [NCT00996385](https://clinicaltrials.gov/study/NCT00996385) | Phase 2 | Desconhecido | 29 | VELCADE (bortezomibe) + ELOXATIN (oxaliplatin) em pacientes previamente tratados com mesotelioma pleural ou peritoneal maligno; delineamento de 2ª linha, resultados finais não confirmados |
| [NCT03210298](https://clinicaltrials.gov/study/NCT03210298) | Observacional | Desconhecido | 1.000 | Registro multicêntrico internacional de PIPAC (quimioterapia em aerossol intraperitoneal pressurizado) para doenças pleurais e peritoneais malignas; oxaliplatin é um dos principais agentes utilizados nessa abordagem |
| [NCT06310473](https://clinicaltrials.gov/study/NCT06310473) | Phase 2 | Não iniciado | 30 | Cadonilimab (anticorpo bispecífico anti-PD-1/CTLA-4) + quimioterapia neoadjuvante para câncer gástrico e da junção esofagogástrica; oxaliplatin provável componente do esquema, sem relevância direta para MPM |

---

## Evidências da Literatura

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [12525529](https://pubmed.ncbi.nlm.nih.gov/12525529/) | 2003 | Phase II Clinical Trial | J Clin Oncol | Raltitrexed + oxaliplatin em 70 pacientes com MPM difuso (15 pré-tratados, 55 naive); régime ativo, especialmente em 1ª linha; estudo prospectivo aberto de referência para esta combinação |
| [14609447](https://pubmed.ncbi.nlm.nih.gov/14609447/) | 2003 | Phase II Clinical Trial | Clin Lung Cancer | Fase II multicêntrico de gemcitabina + oxaliplatin em MPM: 25 pacientes, máximo 6 ciclos de 21 dias; avaliação de atividade antitumoral e perfil de segurança |
| [19091133](https://pubmed.ncbi.nlm.nih.gov/19091133/) | 2008 | Phase II Clinical Trial | J Occup Med Toxicol | Gemcitabina ± oxaliplatin em pacientes com MPM difuso pré-tratados com pemetrexed; investiga eficácia do GEMOX como alternativa de resgate após primeira linha |
| [11989592](https://pubmed.ncbi.nlm.nih.gov/11989592/) | 2001 | Phase II Clinical Trial | Tumori | Estudo-piloto de oxaliplatin + raltitrexed em MPM inoperável; primeira demonstração clínica de atividade desta combinação em doença inoperável |
| [15639727](https://pubmed.ncbi.nlm.nih.gov/15639727/) | 2005 | Phase II Clinical Trial | Lung Cancer | Vinorelbina + oxaliplatin (VO) em 1ª linha para MPM não tratado; avaliação de resposta, sobrevida e toxicidade em população sem tratamento prévio |
| [15893013](https://pubmed.ncbi.nlm.nih.gov/15893013/) | 2005 | Phase II Clinical Trial | Lung Cancer | Raltitrexed + oxaliplatin como 2ª linha em MPM: nenhuma resposta objetiva em 14 pacientes avaliáveis (melhor resposta: estabilização em 28,6%); resultado negativo importante para delimitar o contexto de uso |
| [31455014](https://pubmed.ncbi.nlm.nih.gov/31455014/) | 2019 | Review/Translacional | Int J Mol Sci | Cisplatina, oxaliplatin e pemetrexed modulam a expressão de checkpoints imunológicos em MPM; oxaliplatin identificado como candidato racional para combinação com imunoterapia |
| [12610498](https://pubmed.ncbi.nlm.nih.gov/12610498/) | 2003 | Review | Br J Cancer | Revisão abrangente de ensaios de quimioterapia em MPM; novas combinações com antifolatos e platina (incluindo oxaliplatin) emergem como mais promissoras que agentes convencionais isolados |
| [10930799](https://pubmed.ncbi.nlm.nih.gov/10930799/) | 2000 | Phase II/Retrospectivo | Eur J Cancer | Experiência do Institut Gustave Roussy em 163 pacientes com mesotelioma ao longo de 9 anos; combinação raltitrexed + oxaliplatin apresentada como avanço potencial na armamentária terapêutica |
| [12601280](https://pubmed.ncbi.nlm.nih.gov/12601280/) | 2003 | Review | Curr Opin Oncol | Síntese de dados de Fase 2/3 em MPM; pemetrexed + platina alcança resposta de até 45%; raltitrexed + oxaliplatin discutida como alternativa emergente com perfil favorável |

---

## Informações de Comercialização no Brasil

O oxaliplatin possui **20 registros ativos** junto à ANVISA, com status de **comercialização confirmado**. Os dados detalhados de cada registro (número ANVISA, nome comercial, forma farmacêutica e texto de indicação aprovada) não estão disponíveis neste Evidence Pack.

> Para consultar os registros individuais, acesse o portal da ANVISA: [https://consultas.anvisa.gov.br/](https://consultas.anvisa.gov.br/) e busque por "oxaliplatina".

---

## Citotoxicidade

| Item | Conteúdo |
|------|------|
| Classificação de Citotoxicidade | Citotóxico convencional — platina de 3ª geração (agente alquilante de DNA, formador de adutos intrafita) |
| Risco de Mielossupressão | Médio — neutropenia e trombocitopenia são efeitos descritos, geralmente menos severos que cisplatina; monitoramento regular necessário |
| Classificação de Emetogenicidade | Moderada a alta (em doses ≥ 75 mg/m²) — profilaxia antiemética com antagonistas 5-HT3 + dexametasona recomendada |
| Itens de Monitoramento | Hemograma completo com diferencial (CBC); creatinina sérica e clearance de creatinina (toxicidade renal); transaminases hepáticas (ALT, AST); avaliação clínica de neuropatia periférica sensitiva (dose-limitante cumulativa) |
| Proteção no Manuseio | Obrigatório seguir normas para agentes citotóxicos: luvas de nitrila duplas, avental impermeável de manga longa, proteção ocular e máscara FFP2 durante preparo; descarte em recipientes para resíduos quimioterápicos |

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Proceed with Guardrails**

**Justificativa:**
O nível de evidência L2 é sustentado por pelo menos um ensaio de Fase 2 concluído (NCT00859469) e múltiplas publicações prospectivas de Fase 2 em MPM com oxaliplatin em combinação, demonstrando sinal de atividade antitumoral. O mecanismo de diferenciação parcial em relação à resistência cruzada à cisplatina confere plausibilidade biológica adicional. Contudo, a ausência de dados de Fase 3 e os resultados negativos em segunda linha (PMID 15893013) exigem que qualquer avanço seja acompanhado de critérios rigorosos de seleção de pacientes.

**Para prosseguir, é necessário:**
- Obter dados completos de mecanismo de ação (MOA) via DrugBank API (DG002 — severidade alta)
- Recuperar os textos de indicação aprovada dos 20 registros ANVISA para verificar se MPM já está contemplado (DG001 — severidade bloqueante)
- Obter advertências, contraindicações e interações medicamentosas da bula ANVISA (DG001)
- Definir o contexto preciso de uso: 1ª linha (GEMOX) vs. 2ª linha pós-pemetrexed, e selecionar subpopulação com maior probabilidade de benefício
- Avaliar viabilidade de combinação com imunoterapia (anti-PD-1/PD-L1) dado o potencial de indução de ICD pelo oxaliplatin
- Considerar a via de administração HIPEC/PIPAC para subtipos peritoneais, dado o perfil farmacocinético favorável nessa abordagem
---

