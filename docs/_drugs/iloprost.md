---
layout: default
title: Iloprost
parent: Apenas Predição do Modelo (L5)
nav_order: 361
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-13
description: "Iloprost: nova indicação prevista, Hipotricose simples do couro cabeludo (hypotrichosis simplex of the s… (nível de evidência L5). Indicação original: PROSTAGLANDINAS"
monitor_inn: "iloprost"
predicted_indications: ["hypotrichosis simplex of the scalp", "congenital hypotrichosis milia", "pulmonary arteriovenous malformation (disease)", "diffuse alopecia areata"]
---

# Iloprost
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

# Iloprosta: De prostaglandinas para hipotricose simples do couro cabeludo

## Resumo em Uma Frase

Iloprosta (iloprost) é um análogo estável da prostaciclina, registrado no Brasil como VENTAVIS, com a indicação original descrita como "PROSTAGLANDINAS".
O modelo TxGNN prevê que pode ser eficaz para **hipotricose simples do couro cabeludo (hypotrichosis simplex of the scalp)**, porém **sem nenhum ensaio clínico e sem nenhuma publicação** apoiando esta direção específica; trata-se de uma previsão puramente computacional.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | PROSTAGLANDINAS |
| Nova Indicação Prevista | Hipotricose simples do couro cabeludo (hypotrichosis simplex of the scalp) |
| Pontuação de Previsão TxGNN | 99,45% |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | Apenas registros cancelados |
| Número de Registros | 1 |
| Decisão Recomendada | Hold |

---

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação nos dados compilados para este relatório. Segundo informações conhecidas, a iloprosta é um análogo da prostaciclina: ativa os receptores IP, eleva o AMPc, causa vasodilatação e inibe a agregação plaquetária e o remodelamento vascular. É esse o mecanismo que sustenta seu uso aprovado na hipertensão arterial pulmonar (HAP).

A relação com a nova indicação é frágil. A hipotricose simples é um distúrbio genético de perda de cabelo (por exemplo, variantes em CDSN, APCDD1 e RPL21). Um efeito vasodilatador na microcirculação do couro cabeludo é apenas especulativo. A pontuação alta do TxGNN é uma previsão computacional, sem respaldo clínico.

Em resumo, **não há vínculo mecanístico sustentado pelos dados** entre a prostaciclina e esta doença.

---

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados.

---

## Evidências da Literatura

Atualmente não há literatura relacionada.

---

## Informações de Comercialização no Brasil

| Número de Registro | Nome Comercial | Forma Farmacêutica | Indicação Aprovada |
|---------|------|------|-----------|
| Registro 170560076 (cancelado) | VENTAVIS | Não informada | PROSTAGLANDINAS |

---

## Considerações de Segurança

- **Contraindicações (associações do grafo de conhecimento, não texto de bula)**: insuficiência hepática, doença pulmonar obstrutiva crônica (DPOC), DPOC grave de início precoce, distúrbios hipotensivos, edema pulmonar e doença brônquica.
- **Interações Medicamentosas**: foram identificadas 353 interações. Entre as de nível moderado estão: epinefrina, ácido acetilsalicílico, inibidores de SGLT2 (canagliflozina, dapagliflozina, empagliflozina, ertugliflozina), insulina humana inalada, manitol, efedrina, fenfluramina, dexfenfluramina, glicerina, papaverina e sibutramina. Também constam interações de nível desconhecido com calcitriol, pantoprazol, morfina, metformina e omeprazol.

Consulte a bula para as advertências e contraindicações oficiais, que não estavam disponíveis nos dados compilados.

---

## Outras Previsões do Modelo (Contexto)

Entre as demais indicações previstas, as que apresentam alguma evidência são subgrupos da HAP, condição em que a iloprosta já é estabelecida:

| Indicação prevista | Pontuação TxGNN | Nível de Evidência | Observação |
|------|------|------|------|
| HAP associada a cardiopatia congênita | 99,32% | L3 | Estudos de coorte, séries de casos (síndrome de Eisenmenger) e estudos pediátricos; um estudo cruzado piloto controlado por placebo (PMID 31371115). Sem ensaio randomizado específico. |
| HAP associada a doença do tecido conjuntivo | 99,21% | L3 | Coortes e revisões, incluindo desfechos de longo prazo com iloprosta intravenosa domiciliar (PMID 27651181). Evidência predominantemente observacional. |
| HAP associada ao HIV | 99,21% | L4 | Apenas revisões gerais e um registro nacional; sem dados específicos da iloprosta. |
| HAP associada à esquistossomose | 99,21% | L4 | Evidência indireta. |
| HAP associada a anemia hemolítica crônica | 99,21% | L5 | Sem evidências. |
| Malformação arteriovenosa pulmonar | 99,31% | L5 | Sem racional terapêutico; a vasodilatação poderia, em teoria, piorar o shunt ou a hipoxemia. |
| Hipotricose congênita com milia | 99,33% | L5 | Sem evidências. |
| Alopecia areata difusa | 99,10% | L5 | Vínculo especulativo. |

A HAP associada a cardiopatia congênita e a HAP associada a doença do tecido conjuntivo são, na prática, subgrupos de uma indicação já estabelecida, e não reposicionamentos genuinamente novos.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
- Para a indicação principal prevista (hipotricose simples do couro cabeludo), não há ensaios, literatura nem vínculo mecanístico plausível; a previsão é exclusivamente computacional (nível L5).
- O único registro brasileiro da iloprosta (VENTAVIS) está cancelado, e os dados de bula (advertências e contraindicações) não estavam disponíveis, o que impede a triagem de segurança.

**Para prosseguir, é necessário:**
- Obter e analisar a bula na ANVISA (advertências e contraindicações).
- Complementar os dados de mecanismo de ação no DrugBank.
- Verificar a situação regulatória atual da iloprosta no Brasil, já que o único registro está cancelado.
- Considerar priorizar os subgrupos de HAP (cardiopatia congênita e doença do tecido conjuntivo) como questões de pesquisa, por terem maior suporte (L3).
- Para hipotricose simples, gerar evidência pré-clínica de mecanismo antes de qualquer avanço.
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

