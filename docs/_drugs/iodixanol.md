---
layout: default
title: Iodixanol
parent: 僅模型預測 (L5)
nav_order: 283
evidence_level: L5
indication_count: 10
---

# Iodixanol
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

Usando o skill `txgnn-pipeline` para contexto de projeto. Agora vou gerar o relatório com base no Evidence Pack fornecido.

---

# Iodixanol: De meio de contraste radiológico à suscetibilidade à osteoartrite

## Resumo em Uma Frase

Iodixanol é um agente de contraste iodado iso-osmolar utilizado em procedimentos de imagem diagnóstica como angiografia, tomografia computadorizada e artroscopia.
O modelo TxGNN prevê que pode ser eficaz para **Suscetibilidade à Osteoartrite (Osteoarthritis Susceptibility)**, porém atualmente **não há ensaios clínicos nem publicações** apoiando esta direção terapêutica.
A análise de plausibilidade indica que esta previsão provavelmente decorre de uma associação diagnóstica no grafo de conhecimento (uso de contraste em artroscopia de OA) e não de potencial terapêutico real.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|----------|
| Indicação Original | Agente de contraste iodado para procedimentos de imagem (angiografia, TC, artroscopia diagnóstica) |
| Nova Indicação Prevista | Suscetibilidade à Osteoartrite (Osteoarthritis Susceptibility) |
| Pontuação de Previsão TxGNN | 99.16% |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | ✓ Comercializado |
| Número de Registros | 5 |
| Decisão Recomendada | **Hold** |

---

## Por que Esta Previsão é Razoável?

Iodixanol (comercializado como Visipaque®) é um agente de contraste iodado não-iônico de iso-osmolaridade (≈ 290 mOsm/kg), desenvolvido para reduzir reações adversas em comparação com contrastes hiperosmolares mais antigos. Seu "mecanismo de ação" é essencialmente **físico-químico**: o iodo possui alta densidade eletrônica, atenuando a radiação X e tornando visíveis estruturas vasculares, articulações e cavidades corporais. Ao contrário de fármacos terapêuticos, o Iodixanol não age em receptores, enzimas ou vias de sinalização biológica — seu propósito é exclusivamente diagnóstico.

A associação entre Iodixanol e osteoartrite existe no grafo de conhecimento, mas é de natureza **diagnóstica, não terapêutica**: Iodixanol é frequentemente utilizado em artroscopia de contraste (arthrography) para avaliação radiológica de articulações acometidas por OA. Essa co-ocorrência droga-doença no banco de dados foi provavelmente interpretada pelo modelo TxGNN como sinal de potencial terapêutico, gerando uma previsão que carece de base mecanística real.

Não existe hipótese terapêutica plausível para o uso de Iodixanol no tratamento de OA. A doença é mediada por degradação da cartilagem articular, inflamação sinovial e remodelação óssea subcondral — processos sem nenhuma interação conhecida com agentes de contraste iodados. A pontuação TxGNN de 99,16%, neste caso, reflete provavelmente um artefato de viés de associação diagnóstica no grafo, e não uma relação terapêutica genuína.

---

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados.

---

## Evidências da Literatura

Atualmente não há literatura relacionada.

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
A previsão TxGNN de nível L5 para suscetibilidade à osteoartrite não possui qualquer suporte de evidência terapêutica — a associação no grafo de conhecimento reflete uso diagnóstico (artroscopia de contraste) e não potencial de reposicionamento. Não há fundamento farmacológico identificável para avançar com investigação terapêutica.

**Para reconsiderar esta decisão, seria necessário:**
- Identificação de hipótese mecanística terapêutica viável (atualmente inexistente para Iodixanol em OA)
- Preenchimento dos dados de registro ANVISA (os 5 registros constam com campos vazios no Evidence Pack — necessário acesso direto ao sistema ANVISA)
- Resolução dos Data Gaps de segurança:
  - **DG001** (Bloqueante): Advertências e contraindicações da bula ANVISA — baixar PDF da bula no site TFDA/ANVISA
  - **DG002** (Alto): Mecanismo de ação detalhado — consultar DrugBank API para `DB01249`
- Reavaliação do pipeline TxGNN para filtrar associações diagnósticas vs. terapêuticas no KG, evitando que o uso de contrastes em procedimentos diagnósticos gere candidatos de reposicionamento espúrios
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

