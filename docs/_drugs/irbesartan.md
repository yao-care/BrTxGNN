---
layout: default
title: Irbesartan
parent: Apenas Predição do Modelo (L5)
nav_order: 373
evidence_level: L5
indication_count: 4
last_modified_at: 2026-10-13
description: "Irbesartan: nova indicação prevista, Hipertensão renovascular maligna (Malignant Renovascular Hypertension) (nível de evidência L5). Indicação original: Hipertensão arterial e nefropatia diabética"
monitor_inn: "IRBESARTAN"
predicted_indications: ["malignant renovascular hypertension", "malignant hypertensive renal disease", "pulmonary hypertension owing to lung disease and/or hypoxia", "pulmonary hypertension with unclear multifactorial mechanism"]
---

# Irbesartan
{: .fs-9 }

Nível de evidência: **L5** | Indicações previstas: **4** 
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

# Irbesartana: Da hipertensão e nefropatia diabética à hipertensão renovascular maligna

## Resumo em Uma Frase

Irbesartana é um bloqueador do receptor de angiotensina II (AT1), originalmente usado no tratamento da hipertensão arterial e da nefropatia diabética.
O modelo TxGNN prevê que pode ser eficaz para **Hipertensão Renovascular Maligna (Malignant Renovascular Hypertension)**,
mas atualmente há **0 ensaios clínicos** e **0 publicações** apoiando diretamente esta previsão específica; a evidência é apenas computacional.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Hipertensão arterial e nefropatia diabética (segundo o grafo de conhecimento; não há registros no Brasil com texto de indicação) |
| Nova Indicação Prevista | Hipertensão renovascular maligna (Malignant Renovascular Hypertension) |
| Pontuação de Previsão TxGNN | 99,31% |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | Não comercializado (segundo os dados compilados para este relatório) |
| Número de Registros | 0 |
| Decisão Recomendada | Hold |

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação nos dados compilados. Segundo informações conhecidas, a irbesartana é um antagonista do receptor AT1 da angiotensina II, com eficácia estabelecida em hipertensão e nefropatia diabética. Mecanisticamente, pode ser aplicável à hipertensão renovascular, que é dirigida pela ativação do sistema renina-angiotensina.

A relação com a indicação original é direta: ambas envolvem a hiperatividade do sistema renina-angiotensina-aldosterona e a elevação da pressão. Bloquear o receptor AT1 reduz a pressão arterial e a pressão intraglomerular.

Há, porém, uma ressalva de segurança importante: os bloqueadores do receptor de angiotensina (BRAs) têm risco conhecido de queda aguda da função renal em estenose bilateral de artéria renal, e o grafo de conhecimento registra "obstrução da artéria renal" entre as contraindicações. O alto escore (0,993) é uma previsão computacional, sem estudos que a sustentem.

**Outras previsões do modelo (todas com a mesma limitação):**

| Indicação Prevista | Pontuação TxGNN | Nível | Observação |
|------|------|------|------|
| Doença renal hipertensiva maligna | 99,31% | L5 | Sobrepõe-se às indicações já aprovadas; é mais uma extensão do que um reposicionamento verdadeiro. Sem estudos para o fenótipo maligno (acelerado). |
| Hipertensão pulmonar por doença pulmonar e/ou hipóxia | 99,25% | L4 | Apenas evidência pré-clínica e indireta (ver abaixo). É a previsão com mais suporte na literatura. |
| Hipertensão pulmonar de mecanismo multifatorial não esclarecido | 99,25% | L5 | Indicação heterogênea e mal definida; sem estudos. |

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados.

## Evidências da Literatura

Para a indicação principal (hipertensão renovascular maligna) não há literatura. A tabela abaixo reúne os estudos recuperados para a previsão de hipertensão pulmonar associada à hipóxia, a mais bem sustentada entre as previsões. Todos são pré-clínicos ou indiretos.

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [35288835](https://pubmed.ncbi.nlm.nih.gov/35288835/) | 2022 | Revisão | Inflammopharmacology | Efeitos pleiotrópicos dos antagonistas AT1 na hipóxia induzida por isquemia cardíaca, no contexto do sistema renina-angiotensina |
| [34147903](https://pubmed.ncbi.nlm.nih.gov/34147903/) | 2021 | Pré-clínico (animal) | Biomed Pharmacother | Irbesartana melhorou lesões da artéria pulmonar em modelo de ratos com doença crônica de montanha |
| [34286497](https://pubmed.ncbi.nlm.nih.gov/34286497/) | 2021 | Tipo não classificado | Eur Rev Med Pharmacol Sci | Irbesartana e melhora do estresse oxidativo em ratos com hipertensão pulmonar de altitude, via flora intestinal |
| [34626328](https://pubmed.ncbi.nlm.nih.gov/34626328/) | 2022 | Pré-clínico (animal) | Sleep Breath | Irbesartana atenuou a apoptose cardíaca induzida por apneia do sono e aumentou a expressão de Sirtuína 1 |
| [30356256](https://pubmed.ncbi.nlm.nih.gov/30356256/) | 2018 | Pré-clínico (in vitro) | PLoS One | Efeito protetor da irbesartana em cardiomiócitos sob estresse hipóxico |
| [17142340](https://pubmed.ncbi.nlm.nih.gov/17142340/) | 2007 | Pré-clínico (animal) | Am J Physiol Heart Circ Physiol | Irbesartana inibiu a angiogênese coronariana estimulada por hipóxia intermitente em ratos neonatos |
| [15526904](https://pubmed.ncbi.nlm.nih.gov/15526904/) | 2004 | Pré-clínico (animal) | Ren Fail | Irbesartana atenuou a nefrotoxicidade da ciclosporina (relevância indireta) |

Outros registros recuperados (extratos de ervas, um relato de caso de sobredosagem de roxadustate e um estudo de células-tronco após infarto) não são específicos para irbesartana na indicação prevista e foram omitidos. Nenhum estudo avalia hipertensão pulmonar em pacientes.

## Considerações de Segurança

- **Contraindicações e condições de alerta (segundo o grafo de conhecimento, não o texto da bula):** angioedema (incluindo hereditário, adquirido e induzido por bloqueadores do sistema renina-angiotensina-aldosterona), lúpus eritematoso sistêmico, pancreatite, miopatia e rabdomiólise, anúria, obstrução da artéria renal, doenças hipotensivas, diabetes mellitus e cetoacidose diabética, gota e hiperuricemia, hiperparatireoidismo, hipercalcemia e nefrocalcinose, encefalopatia/coma hepático, deficiência de potássio e paralisia periódica familiar, icterícia neonatal, entre outras.
- **Interações medicamentosas (100 registradas; exemplos principais):**
  - **Graves:** citrato de potássio e bicarbonato de potássio (risco de hipercalemia).
  - **Moderadas:** corticosteroides (hidrocortisona, dexametasona, betametasona, budesonida, triancinolona), inibidores de SGLT2 (canagliflozina, dapagliflozina, empagliflozina), ácido acetilsalicílico, bupropiona, aprepitanto, morfina, dronabinol, insulinas (asparte, degludeca) e preparos de limpeza intestinal (picossulfato, polietilenoglicol, sulfato de sódio).

Consulte a bula para as advertências formais, pois os dados de bula não estavam disponíveis.

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
- A previsão principal tem apenas respaldo computacional (nível L5), sem ensaios nem literatura. A irbesartana não tem registro ativo no Brasil, e o risco renal em estenose de artéria renal exige cautela. Entre as previsões, a hipertensão pulmonar associada à hipóxia (L4) pode ser tratada como questão de pesquisa, não como candidata a uso clínico.

**Para prosseguir, é necessário:**
- Obter e analisar a bula na ANVISA (advertências e contraindicações), pois a triagem de segurança não pode avançar sem ela.
- Complementar os dados de mecanismo de ação a partir do DrugBank.
- Realizar revisão da literatura clínica sobre BRAs em hipertensão renovascular e maligna, com atenção à estenose da artéria renal.
- Para hipertensão pulmonar, buscar estudos clínicos em humanos além dos modelos animais.
- Avaliar a viabilidade regulatória e comercial, dado que o fármaco não tem registro vigente no país.
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

