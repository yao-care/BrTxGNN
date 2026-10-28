---
layout: default
title: Sotatercept
parent: Apenas Predição do Modelo (L5)
nav_order: 597
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-28
description: "Sotatercept: nova indicação prevista, leucemia linfoblástica aguda (nível de evidência L5). Indicação original: Anti-hipertensivos para hipertensão arterial pulmonar"
monitor_inn: "sotatercept"
predicted_indications: ["acute lymphoblastic leukemia (disease)", "severe nonproliferative diabetic retinopathy", "diabetic retinopathy", "drug-induced osteoporosis", "diabetic cataract", "HER2 positive breast carcinoma", "transitional cell carcinoma", "prostatic urethra urothelial carcinoma", "kidney pelvis sarcomatoid transitional cell carcinoma", "infiltrating bladder urothelial carcinoma sarcomatoid variant"]
---

# Sotatercept
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

## Sotatercepte: Da hipertensão arterial pulmonar à leucemia linfoblástica aguda
{: .text-alpha }

## Resumo em Uma Frase

Sotatercepte (WINREVAIR) foi originalmente registrado na ANVISA como anti-hipertensivo para o tratamento da hipertensão arterial pulmonar.
O modelo TxGNN prevê que pode ser eficaz para **Leucemia Linfoblástica Aguda (acute lymphoblastic leukemia)**,
mas atualmente há **0 ensaios clínicos** e **0 publicações** nos dados compilados para este relatório apoiando esta direção. Trata-se de uma previsão exclusivamente computacional.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Anti-hipertensivos para hipertensão arterial pulmonar |
| Nova Indicação Prevista | Leucemia Linfoblástica Aguda (acute lymphoblastic leukemia) |
| Pontuação de Previsão TxGNN | 0,9978 |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | Comercializado (registros ativos: 1 de 1) |
| Número de Registros | 1 (ativos: 1) |
| Decisão Recomendada | Hold |

## Por que Esta Previsão é Razoável?

Não há dados detalhados sobre o mecanismo de ação nos dados compilados. Segundo informações conhecidas, o sotatercepte é uma proteína de fusão do receptor de activina tipo IIA com Fc (ActRIIA-Fc). Ele captura activinas e fatores de diferenciação de crescimento (GDFs), reequilibrando a sinalização BMP/activina, o que sustenta seu uso na hipertensão arterial pulmonar.

A ligação com a leucemia linfoblástica aguda é **especulativa**. A sinalização da família activina/TGF-beta pode influenciar a hematopoese, mas não há mecanismo direto estabelecido. A pontuação alta (0,9978) é apenas uma previsão do modelo, sem respaldo em ensaios ou publicações. Como o fármaco modula a diferenciação hematopoética, um sinal em neoplasia hematológica também precisaria ser avaliado quanto a possível **dano**, e não apenas benefício.

### Outras previsões do modelo (todas L5, Hold)

Todas as previsões abaixo têm pontuação do modelo TxGNN (deep learning) entre 0,9934 e 0,9978, sem ensaios clínicos nem literatura nos dados compilados:

| Posição | Doença prevista | Pontuação | Observação sobre plausibilidade |
|------|------|------|------|
| 2 | Retinopatia diabética não proliferativa grave | 0,9977 | Plausível, porém indireta (remodelação vascular mediada por activina/BMP); preocupação com sangramento e telangiectasias |
| 3 | Retinopatia diabética | 0,9972 | Categoria mais ampla, sobreposta à anterior; não é evidência independente |
| 4 | Osteoporose induzida por fármacos | 0,9965 | Biologicamente a mais coerente (activina regula a remodelação óssea; armadilhas de ligantes ActRIIA-Fc mostraram efeitos anabólicos ósseos em estudos pré-clínicos e iniciais); precisa ser verificada por busca dedicada |
| 5 | Catarata diabética | 0,9949 | Sem conexão mecanística clara; a pontuação vem do modelo TxGNN (deep learning) e pode refletir semelhanças aprendidas pelo modelo entre doenças relacionadas, não evidência biológica |
| 6 | Carcinoma de mama HER2 positivo | 0,9943 | Papel da sinalização de activina/TGF-beta é dependente de contexto; terapia-padrão anti-HER2 já bem estabelecida |
| 7–10 | Carcinoma urotelial e variantes (células transicionais, uretra prostática, pelve renal sarcomatoide, bexiga sarcomatoide) | 99,34–0,9939 | Sem mecanismo conhecido; previsões correlacionadas entre si, não independentes |

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados.

## Evidências da Literatura

Atualmente não há literatura relacionada.

## Informações de Comercialização no Brasil

| Número de Registro | Nome Comercial | Forma Farmacêutica | Indicação Aprovada |
|---------|------|------|-----------|
| Registro nº 101710238 (cancelado) | WINREVAIR | Não informada | Anti-hipertensivos para hipertensão arterial pulmonar |

## Considerações de Segurança

- **Interações Medicamentosas**: a consulta não retornou interações registradas.
- Não há dados de advertências nem de contraindicações nos dados compilados. Consulte a bula para informações de segurança.
- Sinais de atenção teóricos, de acordo com o mecanismo: possível risco de sangramento e telangiectasias (relevante em contexto retiniano) e efeitos sobre a diferenciação hematopoética (relevante em neoplasias hematológicas). Estes pontos não foram confirmados por dados de bula.

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
Todas as previsões estão no nível L5 (apenas previsão do modelo), sem ensaios clínicos nem publicações. O registro brasileiro está cancelado e não há dados de segurança da bula, o que impede avançar para a triagem de segurança. Para leucemia linfoblástica aguda, há ainda a possibilidade de dano, além de ausência de mecanismo estabelecido.

**Para prosseguir, é necessário:**
- Obter e analisar a bula na ANVISA (advertências e contraindicações), lacuna que bloqueia a triagem de segurança.
- Obter dados do mecanismo de ação no DrugBank.
- Esclarecer o motivo e a situação do cancelamento do registro no Brasil.
- Realizar busca dedicada de literatura e ensaios, priorizando osteoporose induzida por fármacos (mais coerente biologicamente), com possível reclassificação para L3–L4 se confirmada.
- Avaliar a compatibilidade de vias de administração (por exemplo, para indicações oculares) e a similaridade com a indicação original.
- Tratar as previsões de carcinoma urotelial e de retinopatia diabética como grupos correlacionados, e não como evidências independentes.
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

