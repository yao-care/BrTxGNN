---
layout: default
title: Nitazoxanide
parent: 僅模型預測 (L5)
nav_order: 359
evidence_level: L5
indication_count: 10
---

# Nitazoxanide
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

Skill carregada. Agora gero o relatório com base no Evidence Pack.

---

# Nitazoxanide: Da antiparasitária à Hiperamilasemia

## Resumo em Uma Frase

Nitazoxanide é um agente antiparasitário/antiprotozoário utilizado internacionalmente para o tratamento de giardíase e criptosporidiose, porém **não registrado no Brasil** pela ANVISA.
O modelo TxGNN prevê que pode ser eficaz para **Hiperamilasemia (Hyperamylasemia)**,
contudo esta previsão conta atualmente com **0 ensaios clínicos** e **0 publicações** de suporte direto, representando exclusivamente uma hipótese computacional.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Antiparasitária (giardíase, criptosporidiose) — uso internacional; sem registro no Brasil |
| Nova Indicação Prevista | Hiperamilasemia (Hyperamylasemia) |
| Pontuação de Previsão TxGNN | 97,82% |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | ✗ Não comercializado (0 registros ANVISA) |
| Número de Registros | 0 |
| Decisão Recomendada | Hold |

---

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação disponíveis neste Evidence Pack. Com base em informações conhecidas da literatura farmacológica, Nitazoxanide pertence à classe das tiazolidas, atuando principalmente por inibição da enzima piruvato:ferredoxina oxidorredutase (PFOR), essencial ao metabolismo energético anaeróbico de parasitas. Há também evidências de que o fármaco modula a via mTOR e induz autofagia celular, o que despertou interesse em pesquisa oncológica e antiviral.

A hiperamilasemia é uma alteração laboratorial (elevação da amilase sérica) de origem pancreática ou salivar, e não uma doença com mecanismo patogênico único. A conexão entre a inibição de PFOR/mTOR e a regulação da secreção ou metabolismo de amilase é biologicamente pouco plausível, conforme indicado na própria análise mecanística do modelo.

Em termos práticos, **a previsão do TxGNN para esta indicação deve ser interpretada com cautela**. O score elevado (97,82%) reflete o posicionamento no espaço do grafo de conhecimento, mas a ausência total de estudos clínicos, dados pré-clínicos direcionados e suporte literário torna a hipótese exclusivamente especulativa neste momento.

---

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados para Nitazoxanide em hiperamilasemia.

---

## Evidências da Literatura

Atualmente não há literatura relacionada para Nitazoxanide em hiperamilasemia.

---

## Informações de Comercialização no Brasil

Nitazoxanide **não possui nenhum registro ativo na ANVISA** e não é comercializado no Brasil. Não há dados de licenciamento a apresentar.

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
A previsão do TxGNN para hiperamilasemia em Nitazoxanide não é suportada por nenhum ensaio clínico, estudo pré-clínico direcionado ou publicação científica específica. A análise mecanística indica conexão fraca entre o perfil farmacológico do fármaco e a fisiopatologia da hiperamilasemia, tornando prematura qualquer iniciativa de desenvolvimento nesta direção.

**Para prosseguir, seria necessário:**
- Dados de MOA completos (DrugBank API) para análise de conectividade mecanística aprofundada
- Estudos in vitro ou in vivo demonstrando efeito de Nitazoxanide sobre vias de secreção/metabolismo de amilase
- Hipótese biológica plausível que justifique o vínculo entre PFOR/mTOR e regulação amilásica
- Registro na ANVISA (processo regulatório local) como pré-requisito para qualquer uso clínico no Brasil
- Informações de segurança completas (advertências, contraindicações) via bula ANVISA/TFDA
---

