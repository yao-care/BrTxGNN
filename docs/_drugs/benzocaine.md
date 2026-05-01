---
layout: default
title: Benzocaine
parent: 僅模型預測 (L5)
nav_order: 107
evidence_level: L5
indication_count: 1
---

# Benzocaine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# Benzocaine: Da Anestesia Local à Conjuntivite Papilar

## Resumo em Uma Frase

Benzocaine é um anestésico local do tipo éster, amplamente utilizado para o alívio temporário de dor e prurido em mucosas e tecidos superficiais.
O modelo TxGNN prevê que pode ser eficaz para **Conjuntivite Papilar (Papillary Conjunctivitis)**,
porém atualmente há **0 ensaios clínicos** e **0 publicações** apoiando diretamente esta direção.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Anestesia local de mucosas e superfícies teciduais |
| Nova Indicação Prevista | Conjuntivite Papilar (Papillary Conjunctivitis) |
| Pontuação de Previsão TxGNN | 99,38% |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | ✗ Não comercializado |
| Número de Registros | 0 |
| Decisão Recomendada | Hold |

---

## Por que Esta Previsão é Razoável?

Benzocaine é um anestésico local do tipo éster que atua bloqueando canais de sódio voltagem-dependentes (Nav1.x), inibindo a condução de sinais nervosos sensoriais. Teoricamente, essa ação poderia proporcionar alívio sintomático temporário do prurido e da sensação de corpo estranho associados à conjuntivite papilar.

No entanto, a fisiopatologia central da conjuntivite papilar envolve ativação de mastócitos mediada por IgE e inflamação crônica conduzida por linfócitos T — mecanismos tipicamente desencadeados por lentes de contato ou próteses oculares. Um anestésico local age apenas no sintoma e não alcança os mecanismos imunológicos subjacentes.

A pontuação elevada do TxGNN provavelmente reflete uma inferência indireta pelo caminho "anestésico local → tecido mucoso → alívio de sintomas conjuntivais" dentro do grafo de conhecimento. Trata-se de uma extrapolação do modelo sem validação biológica direta. Adicionalmente, o uso oftálmico de benzocaína levanta preocupações de toxicidade epitelial corneal e risco de meta-hemoglobinemia em caso de absorção sistêmica, elevando o risco translacional.

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
A previsão do TxGNN apresenta pontuação elevada (99,38%), porém não há qualquer ensaio clínico ou publicação científica apoiando o uso de benzocaína em conjuntivite papilar. O mecanismo de ação anestésico local não aborda a patogênese imunológica da doença, e há riscos de segurança oftálmica não negligenciáveis. O nível de evidência L5 (apenas previsão do modelo) é insuficiente para avançar.

**Para prosseguir, é necessário:**
- Obter dados completos de mecanismo de ação (MOA) via DrugBank para fundamentar a plausibilidade biológica
- Levantar dados de segurança oftálmica em modelos pré-clínicos (estudos de toxicidade corneal)
- Verificar se existem formulações oftálmicas de benzocaína registradas em outros países e seus perfis de segurança
- Registrar o fármaco na ANVISA antes de qualquer desenvolvimento clínico no Brasil
- Considerar se a indicação-alvo justifica priorização frente a candidatos com evidência de nível L3 ou superior
---

