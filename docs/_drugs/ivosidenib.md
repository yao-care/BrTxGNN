---
layout: default
title: Ivosidenib
parent: Apenas Predição do Modelo (L5)
nav_order: 381
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-28
description: "Ivosidenib: nova indicação prevista, Poliomielite bulbar (bulbar polio) (nível de evidência L5). Indicação original: Agentes antineoplásicos"
monitor_inn: "ivosidenib"
predicted_indications: ["bulbar polio"]
---

# Ivosidenib
{: .fs-9 }

Nível de evidência: **L5** | Indicações previstas: **1** 
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

## Ivosidenibe: De agente antineoplásico para poliomielite bulbar
{: .text-alpha }

## Resumo em Uma Frase

Ivosidenibe (TIBSOVO) é um inibidor da isocitrato desidrogenase 1 mutante (IDH1), registrado na ANVISA na classe dos agentes antineoplásicos.
O modelo TxGNN prevê que pode ser eficaz para **poliomielite bulbar (bulbar polio)**, mas atualmente há **0 ensaios clínicos** e **0 publicações** apoiando esta direção. A previsão é apenas computacional.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Agentes antineoplásicos |
| Nova Indicação Prevista | Poliomielite bulbar (bulbar polio) |
| Pontuação de Previsão TxGNN | 0,9931 |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | Comercializado (registros ativos: 1 de 1) |
| Número de Registros | 1 (ativos: 1) |
| Decisão Recomendada | Hold |

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação nos dados compilados para este relatório. Segundo informações conhecidas, o ivosidenibe é um inibidor da enzima IDH1 mutante: reduz a produção de 2-hidroxiglutarato e alivia o bloqueio de diferenciação celular em cânceres com mutação em IDH1, como a leucemia mieloide aguda (LMA).

Para a poliomielite bulbar, **não há vínculo mecanístico crível**. Trata-se de uma infecção viral dos neurônios motores causada pelo poliovírus, e não se conhece nenhuma via dependente de IDH1 envolvida. A pontuação alta do TxGNN (0,9931) vem do modelo TxGNN (deep learning) e pode refletir semelhanças que o modelo aprendeu entre doenças relacionadas, não evidência biológica.

### Outras previsões do modelo (para contexto)

Duas previsões seguintes têm plausibilidade biológica maior, embora também sem evidência direta:

| Posição | Indicação prevista | Pontuação TxGNN | Nível |
|------|------|------|------|

O ivosidenibe é aprovado para LMA com mutação em IDH1 e tem atividade em SMD com essa mutação. O benefício nessas formas relacionadas a terapia dependeria da presença da mutação em IDH1, e não da origem etiológica. As pontuações idênticas sugerem que ambas derivam de um mesmo nó pai (LMA/SMD relacionada a terapia), de modo que **não são sinais independentes**.

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados.

## Evidências da Literatura

Atualmente não há literatura relacionada.

## Informações de Comercialização no Brasil

| Número de Registro | Nome Comercial | Forma Farmacêutica | Indicação Aprovada |
|---------|------|------|-----------|
| Registro nº 112780089 (cancelado) | TIBSOVO | Não informada | Agentes antineoplásicos |

## Citotoxicidade

| Item | Conteúdo |
|------|------|
| Classificação de Citotoxicidade | Terapia alvo (inibidor de IDH1 mutante), não citotóxico convencional |
| Risco de Mielossupressão | Consulte as advertências e precauções na bula |
| Classificação de Emetogenicidade | Consulte as advertências e precauções na bula |
| Itens de Monitoramento | Consulte a bula; em geral, hemograma completo, função hepática e renal, eletrólitos e ECG (risco de prolongamento do intervalo QT) |
| Proteção no Manuseio | Consulte as advertências e precauções na bula |

## Considerações de Segurança

- **Interações Medicamentosas**: foram identificadas **413 interações** no total. Entre as 20 listadas nos dados compilados:
  - **Gravidade maior**: aprepitanto, claritromicina, dolasetrona, palonossetrona, cisaprida, granissetrona, levofloxacino. Vários desses fármacos estão associados a prolongamento do intervalo QT ou a metabolismo via CYP3A4.
  - **Gravidade moderada**: famotidina, loperamida, bisacodil, ácido picossulfúrico, polietilenoglicol 3350 com eletrólitos, saxagliptina, eliglustate, linagliptina, sulfato de sódio, óleo de rícino, glicerina, lactitol e lactulose.

Para advertências e contraindicações, consulte a bula.

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
- Para poliomielite bulbar, não há ensaios, literatura nem mecanismo plausível (nível L5). A pontuação alta vem do modelo TxGNN (deep learning) e pode refletir semelhanças que o modelo aprendeu entre doenças relacionadas, não evidência biológica. Além disso, o medicamento é comercializado no Brasil, com 1 registro válido de 1.

**Para prosseguir, é necessário:**
- Obter os dados de mecanismo de ação (MOA) do DrugBank.
- Baixar e analisar a bula na ANVISA (advertências e contraindicações), etapa que bloqueia a triagem de segurança.
- Confirmar a situação regulatória atual do ivosidenibe no Brasil.
- Priorizar a investigação de subgrupos de LMA/SMD relacionadas a terapia com mutação em IDH1 em ensaios já existentes de ivosidenibe, o que poderia elevar o nível de evidência dessas indicações.
- Descartar ou redirecionar a hipótese de poliomielite bulbar, salvo surgimento de evidência biológica nova.
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

