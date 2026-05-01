---
layout: default
title: Ioversol
parent: 僅模型預測 (L5)
nav_order: 285
evidence_level: L5
indication_count: 10
---

# Ioversol
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

Usando o skill `txgnn-pipeline` para orientação sobre o pipeline TxGNN, e o prompt do sistema para o formato de relatório de reposicionamento.

---

# Ioversol: De Agente de Contraste Iodado para Suscetibilidade à Osteoartrite

## Resumo em Uma Frase

Ioversol é um agente de contraste iodado não-iônico de baixa osmolaridade, utilizado em procedimentos de imagem diagnóstica (angiografia, urografia e tomografia computadorizada com contraste).
O modelo TxGNN prevê que pode ser eficaz para **Suscetibilidade à Osteoartrite (Osteoarthritis Susceptibility)**,
porém esta previsão **não é apoiada por nenhum ensaio clínico ou publicação científica** — apenas pela estrutura do grafo de conhecimento (KG).

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|----------|
| Indicação Original | Agente de contraste para procedimentos de imagem diagnóstica |
| Nova Indicação Prevista | Suscetibilidade à Osteoartrite (Osteoarthritis Susceptibility) |
| Pontuação de Previsão TxGNN | 99.67% |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | ✓ Comercializado |
| Número de Registros | 3 |
| Decisão Recomendada | Hold |

---

## Por que Esta Previsão é Razoável?

Ioversol é um agente de contraste iodado não-iônico administrado por via intravascular. Sua função é aumentar a densidade radiológica de vasos sanguíneos e estruturas anatômicas durante exames de imagem, como angiografia, urografia excretora e tomografia computadorizada. A indicação original é estritamente diagnóstica — Ioversol não possui atividade farmacológica terapêutica clássica (não atua em receptores, enzimas ou vias de sinalização celular com intenção de modificar doenças).

Atualmente, não há dados detalhados sobre o mecanismo de ação disponíveis no Evidence Pack. A "suscetibilidade à osteoartrite" representa um fenótipo genético e de risco — ou seja, a predisposição do indivíduo a desenvolver OA —, e não uma condição clínica diretamente modificável por um agente de contraste. Agentes de contraste iodados não possuem mecanismo conhecido de modulação de cartilagem articular, inflamação sinovial ou vias genéticas associadas à OA (como genes COL2A1, GDF5 ou ALDH1A2).

A previsão do TxGNN é gerada por propagação em grafo de conhecimento (Knowledge Graph) e pode refletir conexões indiretas: o uso de Ioversol em exames de imagem de pacientes com patologias osteomusculares pode ter criado associações topológicas no KG sem implicação causal ou terapêutica. Sem qualquer evidência de ensaio clínico ou literatura que suporte a hipótese, esta previsão deve ser tratada com cautela extrema e interpretada como artefato do modelo.

---

## Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados para Ioversol e suscetibilidade à osteoartrite.

---

## Evidências da Literatura

Atualmente não há literatura relacionada para Ioversol e suscetibilidade à osteoartrite.

---

## Informações de Comercialização no Brasil

Ioversol possui **3 registros ativos** no Brasil (✓ Comercializado). Os dados detalhados de número de registro, nome comercial, forma farmacêutica e indicação aprovada não estão disponíveis no Evidence Pack atual e precisam ser obtidos diretamente na base da ANVISA.

| Situação | Detalhe |
|----------|---------|
| Status de comercialização | ✓ Comercializado |
| Total de registros ativos | 3 |

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
A previsão do TxGNN para suscetibilidade à osteoartrite é classificada como L5 (ausência total de evidências reais), sem nenhum ensaio clínico ou publicação científica que apoie o uso terapêutico de Ioversol nesta indicação. Adicionalmente, "suscetibilidade" é um fenótipo de risco genético — não uma indicação terapêutica convencional —, e agentes de contraste iodados não possuem hipótese mecanicista plausível para modificação de OA, tornando o reposicionamento biologicamente implausível com base nos dados atuais.

**Para prosseguir, seria necessário:**
- Dados completos de MOA do Ioversol via DrugBank API (remediar DG002)
- Dados completos dos registros ANVISA com indicações aprovadas (remediar ausência nos `licenses`)
- Hipótese mecanicista publicada e plausível conectando agentes de contraste iodados à fisiopatologia da OA
- Estudos pré-clínicos em modelos animais de osteoartrite como mínimo de evidência inicial (para sair do nível L5)
---

