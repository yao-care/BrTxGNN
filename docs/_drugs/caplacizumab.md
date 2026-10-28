---
layout: default
title: Caplacizumab
parent: Apenas Predição do Modelo (L5)
nav_order: 187
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-13
description: "Caplacizumab: nova indicação prevista, Transtorno primário de liberação plaquetária (primary release disorde… (nível de evidência L5). Indicação original: Antitrombótico"
monitor_inn: "caplacizumab"
predicted_indications: ["primary release disorder of platelets", "pseudo-von Willebrand disease", "Glanzmann thrombasthenia", "Scott syndrome", "bleeding diathesis due to a collagen receptor defect", "hemorrhagic disorder due to a constitutional thrombocytopenia", "fetal and neonatal alloimmune thrombocytopenia", "hemophilia", "platelet-type bleeding disorder"]
---

# Caplacizumab
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

## Caplacizumabe: De antitrombótico a transtorno primário de liberação plaquetária
{: .text-alpha }

## Resumo em Uma Frase

Caplacizumabe é um nanocorpo anti-fator de von Willebrand (vWF), registrado no Brasil com a indicação genérica de antitrombótico.
O modelo TxGNN prevê que pode ser eficaz para **transtorno primário de liberação plaquetária (primary release disorder of platelets)**, mas há **0 ensaios clínicos** e **0 publicações** apoiando esta direção. A previsão é puramente computacional e, mecanisticamente, o fármaco tenderia a piorar esse quadro hemorrágico.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Antitrombótico |
| Nova Indicação Prevista | Transtorno primário de liberação plaquetária (primary release disorder of platelets) |
| Pontuação de Previsão TxGNN | 1,0000 |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | Comercializado (registros ativos: 1 de 1) |
| Número de Registros | 1 (ativos: 1) |
| Decisão Recomendada | Hold |

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação nas informações compiladas. Segundo o conhecimento disponível, caplacizumabe é um nanocorpo dirigido ao domínio A1 do vWF. Ele bloqueia a ligação do vWF à glicoproteína Ib (GPIb) plaquetária e, assim, impede a adesão das plaquetas e a formação de microtrombos. Esse é o motivo de sua classificação como antitrombótico.

A relação com a nova indicação é fraca. Nos transtornos primários de liberação plaquetária, o problema é a secreção deficiente dos grânulos das plaquetas, um processo que não depende da interação vWF-GPIb. Bloquear a adesão plaquetária num distúrbio hemorrágico deveria, em princípio, agravar o quadro e não tratá-lo.

A pontuação muito alta do TxGNN reflete, provavelmente, associações genéricas entre doenças plaquetárias e não um vínculo mecanístico real. Sem estudos clínicos ou literatura, a previsão não é acionável neste momento.

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados.

## Evidências da Literatura

Atualmente não há literatura relacionada.

## Informações de Comercialização no Brasil

| Número de Registro | Nome Comercial | Forma Farmacêutica | Indicação Aprovada |
|---------|------|------|-----------|
| Registro nº 183260480 (cancelado) | CABLIVI | — | Antitrombótico |

## Considerações de Segurança

- **Interações Medicamentosas**: foram identificadas 139 interações. As de gravidade **maior** incluem:
  - ácido acetilsalicílico
  - abciximabe
  - alteplase
  - fondaparinux
  - anagrelida
  - acalabrutinibe
  - deferasirox
  - trastuzumabe entansina
  - ibritumomabe tiuxetano
  - tositumomabe

  Em geral, o risco principal é o aumento do sangramento. Também há interações de gravidade moderada, por exemplo com ibuprofeno, cetorolaco, celecoxibe, fluvoxamina, fenfluramina, dexfenfluramina e sibutramina.
- Como se trata de um fármaco que reduz a adesão plaquetária, o risco hemorrágico é a principal preocupação em pacientes que já têm distúrbio de sangramento.

Para advertências e contraindicações, consulte a bula.

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
- Não há ensaios clínicos nem publicações para esta indicação (nível L5).
- O mecanismo de ação (inibição da adesão plaquetária mediada por vWF) sugere possível piora de um distúrbio hemorrágico, o que contraria a previsão do modelo.
- O único registro brasileiro está cancelado.

**Para prosseguir, é necessário:**
- Dados detalhados do mecanismo de ação e uma justificativa biológica que explique como bloquear vWF-GPIb poderia beneficiar um defeito de secreção plaquetária.
- Estudos pré-clínicos que mostrem benefício e não piora do fenótipo hemorrágico.
- Avaliação de segurança, com análise específica do risco de sangramento, e consulta à bula para advertências e contraindicações.
- Esclarecimento do status regulatório no Brasil (registro cancelado).

**Observação:** na mesma lista de previsões, a **púrpura trombocitopênica trombótica (PTT)** aparece como o 5º alvo, com 8 ensaios clínicos (incluindo os Phase 3 HERCULES e Post-HERCULES) e 20 publicações, nível de evidência L1 e recomendação *Proceed with Guardrails*. Trata-se, porém, da indicação já aprovada do fármaco e não de um reposicionamento propriamente dito. Se o objetivo é avaliar o potencial real de caplacizumabe, vale analisar o relatório dessa indicação, com atenção ao risco hemorrágico, ao uso concomitante de troca plasmática e imunossupressão e à duração guiada pela atividade de ADAMTS13.
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

