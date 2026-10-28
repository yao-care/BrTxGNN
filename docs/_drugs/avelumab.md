---
layout: default
title: Avelumab
parent: Apenas Predição do Modelo (L5)
nav_order: 93
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-13
description: "Avelumab: nova indicação prevista, Tumor relacionado ao herpesvírus humano 8 (human herpesvirus 8-relate… (nível de evidência L5). Indicação original: Antineoplásico"
monitor_inn: "avelumab"
predicted_indications: ["human herpesvirus 8-related tumor", "middle ear neuroendocrine tumor", "malignant cutaneous granular cell skin tumor", "ectomesenchymoma", "adenosine deaminase deficiency", "reticular dysgenesis", "Immunoerythromyeloid hypoplasia", "non-severe combined immunodeficiency", "kidney pelvis sarcomatoid transitional cell carcinoma"]
---

# Avelumab
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

## Avelumabe: De antineoplásico (indicação genérica) para tumor relacionado ao herpesvírus humano 8
{: .text-alpha }

## Resumo em Uma Frase

Avelumabe (nome comercial BAVENCIO) é um anticorpo anti-PD-L1, originalmente registrado na ANVISA com a indicação genérica de "antineoplásico".
O modelo TxGNN prevê que pode ser eficaz para **tumor relacionado ao herpesvírus humano 8 (human herpesvirus 8-related tumor)**,
mas atualmente há **0 ensaios clínicos** e **0 publicações** nos dados compilados para este relatório apoiando esta direção. A previsão se baseia apenas no modelo.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Antineoplásico |
| Nova Indicação Prevista | Tumor relacionado ao herpesvírus humano 8 (human herpesvirus 8-related tumor) |
| Pontuação de Previsão TxGNN | 0,9997 |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | Comercializado (registros ativos: 1 de 1) |
| Número de Registros | 1 (ativos: 1) |
| Decisão Recomendada | Hold |

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação na base consultada. Segundo informações conhecidas, o avelumabe é um anticorpo monoclonal anti-PD-L1 (inibidor de checkpoint imunológico), que bloqueia a ligação entre PD-L1 e PD-1 e, assim, pode restaurar a resposta imune contra células tumorais.

Os tumores causados pelo HHV-8 (como o sarcoma de Kaposi e o linfoma primário de efusão) utilizam a via PD-1/PD-L1 para escapar do sistema imune, o que torna biologicamente plausível o uso do bloqueio de checkpoint. Outros inibidores da via PD-1 já mostraram atividade no sarcoma de Kaposi. Além disso, o avelumabe é aprovado em outros países para o carcinoma de células de Merkel, também um tumor associado a vírus, o que oferece apenas apoio conceitual indireto.

É importante ressaltar que nenhum ensaio clínico ou publicação sobre o avelumabe nesta indicação foi encontrado nos dados compilados. A previsão repousa unicamente na pontuação do TxGNN.

## Outras Indicações Previstas

Além da principal, o modelo previu outras indicações. Todas permanecem sem ensaios clínicos ou literatura nos dados compilados.

| Posição | Indicação Prevista | Pontuação TxGNN | Nível | Recomendação | Comentário |
|---------|------|------|------|------|------|
| 2 | Tumor neuroendócrino da orelha média | 0,9997 | L5 | Hold | Vínculo plausível com o carcinoma de Merkel, mas tumor raro e geralmente indolente, com pouca evidência de dependência de PD-L1 |
| 3 | Tumor cutâneo maligno de células granulares | 0,9997 | L5 | Hold | Sem justificativa mecanística PD-L1 identificada; evidência mínima |
| 4 | Ectomesenquimoma | 0,9997 | L5 | Hold | Tumor pediátrico extremamente raro; sem evidência de expressão de PD-L1 |
| 5 | Deficiência de adenosina desaminase | 0,9995 | L5 | Hold | Sem conexão terapêutica lógica; a pontuação vem do modelo TxGNN (aprendizado profundo) e pode refletir semelhanças aprendidas entre doenças relacionadas, não evidência biológica; risco de ativação imune |
| 6 | Disgenesia reticular | 0,9994 | L5 | Hold | Imunodeficiência combinada grave; a pontuação vem do modelo TxGNN (aprendizado profundo) e pode refletir semelhanças aprendidas entre doenças relacionadas, não evidência biológica |
| 7 | Hipoplasia imunoeritromieloide | 0,9994 | L5 | Hold | Sem mecanismo plausível para restaurar a hematopoese |
| 8 | Imunodeficiência não combinada grave | 0,9992 | L5 | Hold | Bloqueio de PD-L1 não é tratamento reconhecido; risco de ativação imune |
| 9 | Carcinoma urotelial da uretra prostática | 0,9992 | L4 | Research Question | Subtipo de carcinoma urotelial, no qual o avelumabe tem evidência de Fase 3 (JAVELIN Bladder 100); evidência indireta |
| 10 | Carcinoma sarcomatoide de células transicionais da pelve renal | 0,9991 | L4 | Research Question | Mesma família do carcinoma urotelial; histologia agressiva, mas sub-representada nos estudos pivotais |

A indicação urotelial (posição 9) é a que tem maior respaldo indireto. As pontuações das indicações de imunodeficiência (posições 5 a 8) vêm do modelo TxGNN (aprendizado profundo) e podem refletir semelhanças aprendidas entre doenças relacionadas, não evidência biológica, e podem representar risco.

## Informações de Comercialização no Brasil

| Número de Registro | Nome Comercial | Forma Farmacêutica | Indicação Aprovada |
|---------|------|------|-----------|
| Registro nº 100890403 (cancelado) | BAVENCIO | Não informada | Antineoplásico |

## Citotoxicidade

| Item | Conteúdo |
|------|------|
| Classificação de Citotoxicidade | Imunoterapia (anticorpo monoclonal anti-PD-L1), não é citotóxico convencional |
| Risco de Mielossupressão | Baixo (não é quimioterápico citotóxico); consulte a bula |
| Classificação de Emetogenicidade | Baixa |
| Itens de Monitoramento | Hemograma, função hepática, renal e tireoidiana, glicemia (para eventos adversos imunomediados) |
| Proteção no Manuseio | Consulte as advertências e precauções na bula |

## Considerações de Segurança

- **Interações Medicamentosas** (3 interações de nível Major):
  - Lenalidomida
  - Pomalidomida
  - Talidomida

Para advertências e contraindicações, consulte a bula.

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
Para a indicação principal (tumor relacionado ao HHV-8), a previsão está no nível L5, sem nenhum ensaio clínico ou publicação, e o registro brasileiro está cancelado. Embora o mecanismo seja biologicamente plausível, a evidência é insuficiente para avançar.

**Para prosseguir, é necessário:**
- Realizar busca sistemática de ensaios e literatura sobre avelumabe em sarcoma de Kaposi e outros tumores associados ao HHV-8
- Obter e analisar a bula na ANVISA (advertências e contraindicações), uma lacuna bloqueante para a triagem de segurança
- Completar os dados de mecanismo de ação no DrugBank
- Esclarecer a situação regulatória, já que o único registro está cancelado
- Se houver interesse em oncologia, considerar priorizar as indicações uroteliais (posições 9 e 10), que têm evidência indireta mais robusta
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

