---
layout: default
title: Minoxidil
parent: Evidência Moderada (L3-L4)
nav_order: 461
evidence_level: L3
indication_count: 10
last_modified_at: 2026-10-13
description: "Minoxidil: nova indicação prevista, Hipotricose simples do couro cabeludo (Hypotrichosis simplex of the s… (nível de evidência L3). Indicação original: Hipertensão arterial e alopecia"
monitor_inn: "Minoxidil"
predicted_indications: ["congenital hypotrichosis milia", "pulmonary arterial hypertension", "pulmonary arteriovenous malformation (disease)", "pulmonary arterial hypertension associated with congenital heart disease", "primary hereditary glaucoma", "pulmonary arterial hypertension associated with connective tissue disease", "pulmonary arterial hypertension associated with HIV infection"]
---

# Minoxidil
{: .fs-9 }

Nível de evidência: **L3** | Indicações previstas: **10** 
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

# Minoxidil: Da hipertensão e alopecia à hipotricose simples do couro cabeludo

## Resumo em Uma Frase

Minoxidil é um vasodilatador originalmente usado no tratamento da hipertensão arterial e da alopecia.
O modelo TxGNN prevê que pode ser eficaz para **hipotricose simples do couro cabeludo (Hypotrichosis simplex of the scalp)**,
atualmente com **nenhum ensaio clínico registrado** e **3 publicações** (séries e relatos de caso) apoiando esta direção.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Hipertensão arterial e alopecia (conforme o grafo de conhecimento; não há texto de indicação de registro no Brasil) |
| Nova Indicação Prevista | Hipotricose simples do couro cabeludo (Hypotrichosis simplex of the scalp) |
| Pontuação de Previsão TxGNN | 99,99% |
| Nível de Evidência | L3 |
| Situação no Mercado Brasileiro | Não comercializado (nos dados compilados) |
| Número de Registros | 0 |
| Decisão Recomendada | Proceed with Guardrails |

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação nos dados compilados. Segundo informações conhecidas, o minoxidil é um estimulante do crescimento capilar consolidado: abre canais de potássio, prolonga a fase anágena do folículo e aumenta o fluxo sanguíneo folicular. Também é um vasodilatador usado em hipertensão grave.

A hipotricose simples do couro cabeludo é uma doença hereditária rara, de herança autossômica dominante, associada a variantes do gene *CDSN* (corneodesmosina), com crescimento insuficiente de cabelo. Como o minoxidil já é usado em outras formas de perda capilar, o mecanismo é plausivelmente aplicável.

Há, porém, uma limitação importante: as três publicações (2022–2024) descrevem minoxidil oral ou tópico quase sempre combinado com fatores de crescimento, extratos botânicos ou plasma rico em plaquetas (PRP). Esses desenhos impedem atribuir o efeito ao minoxidil isolado.

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados.

## Evidências da Literatura

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [35761391](https://pubmed.ncbi.nlm.nih.gov/35761391/) | 2022 | Série de casos / estudo clínico pequeno | Dermatologic Therapy | Tratamento da hipotricose simples hereditária do couro cabeludo com minoxidil oral e fatores de crescimento |
| [39902296](https://pubmed.ncbi.nlm.nih.gov/39902296/) | 2024 | Relato de caso | Frontiers in Genetics | Criança de 8 anos com HSS por mutação em *CDSN*, tratada com extratos botânicos e minoxidil |
| [36651821](https://pubmed.ncbi.nlm.nih.gov/36651821/) | 2023 | Relato de caso | J Dermatol Treat | Paciente de 14 anos tratada com injeção de PRP e minoxidil tópico 2%, com resposta relatada como bem-sucedida |

## Considerações de Segurança

- **Contraindicações descritas no grafo de conhecimento** (não são texto de bula): hipotensão ortostática, atrofia de múltiplos sistemas, síndrome de taquicardia postural ortostática, doença renal, acidente vascular cerebral e doenças cerebrovasculares, infarto do miocárdio, doenças cardiovasculares e cardíacas, feocromocitoma e paraganglioma simpático, pericardite, derrame pericárdico e tamponamento cardíaco, hemoglobinopatias e dermatoses do couro cabeludo.
- **Interações medicamentosas**: foram identificadas 100 interações no total. As listadas são, em sua maioria, de nível moderado: corticosteroides (hidrocortisona, triamcinolona, dexametasona, betametasona, budesonida, prednisolona, prednisona), bupropiona, morfina, ópio, inibidores de SGLT2 (canagliflozina, dapagliflozina, empagliflozina, ertugliflozina), dronabinol, nabilona e sapropterina. Calcitriol, clotrimazol e metformina têm nível desconhecido.

Consulte a bula para as advertências formais de segurança.

## Outras Indicações Previstas (Visão Resumida)

| Indicação Prevista | Evidência | Recomendação | Comentário |
|------|------|------|------|
| Alopecia areata difusa | L3 | Questão de pesquisa | Minoxidil não trata a causa autoimune; é usado como adjuvante. Diretrizes favorecem inibidores de JAK e corticosteroides. |
| Pseudopelade de Brocq | L4 | Hold | Alopecia cicatricial com destruição folicular; a literatura é toda sobre alopecia androgenética (indireta). |
| Hipertensão arterial pulmonar | L4 | Hold | Dados antigos (1976–1977) em hipertensão sistêmica; retenção de líquidos e derrame pericárdico preocupam. |
| Hipotricose congênita com milia, malformação arteriovenosa pulmonar, HAP associada a cardiopatia congênita, a doença do tecido conjuntivo e a HIV, glaucoma hereditário primário | L5 | Hold | Apenas previsão computacional, sem ensaios nem literatura. Vasodilatação pode ser desfavorável em vários desses cenários. |

## Conclusão e Próximos Passos

**Decisão: Proceed with Guardrails**

**Justificativa:**
- A hipotricose simples do couro cabeludo tem três publicações de casos que apoiam a direção, com mecanismo plausível. Porém, não há ensaios registrados, o efeito do minoxidil isolado não é separável e o fármaco não está comercializado no Brasil.

**Para prosseguir, é necessário:**
- Obter a bula e as informações de segurança aprovadas pela ANVISA (advertências e contraindicações), hoje ausentes.
- Complementar os dados de mecanismo de ação.
- Gerar evidência com minoxidil em monoterapia (série de casos maiores ou ensaio controlado).
- Definir via e dose (oral em baixa dose ou tópica) e plano de monitoramento cardiovascular, incluindo pressão arterial, frequência cardíaca, edema e derrame pericárdico.
- Esclarecer a situação regulatória do minoxidil no Brasil, já que os dados compilados indicam 0 registros.
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

