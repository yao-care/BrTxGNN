---
layout: default
title: Domperidone
parent: 僅模型預測 (L5)
nav_order: 227
evidence_level: L5
indication_count: 1
---

# Domperidone
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

# Domperidona: De antiemético/procinético à Síndrome Nefrogênica de Antidiurese Inapropriada

## Resumo em Uma Frase

Domperidona é um antagonista periférico dos receptores de dopamina D2/D3, amplamente utilizado como agente procinético no tratamento de náuseas, vômitos e gastroparesia.
O modelo TxGNN prevê potencial eficácia para a **Síndrome Nefrogênica de Antidiurese Inapropriada (Nephrogenic Syndrome of Inappropriate Antidiuresis — NSIAD)**, porém sem **nenhum ensaio clínico** nem **publicação científica** apoiando diretamente esta direção, e com forte indicativo de falso-positivo pela análise mecanística.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Náuseas, vômitos e distúrbios de motilidade gastrointestinal (procinético) |
| Nova Indicação Prevista | Síndrome Nefrogênica de Antidiurese Inapropriada (NSIAD) |
| Pontuação de Previsão TxGNN | 99,08% |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | Não comercializado |
| Número de Registros | 0 |
| Decisão Recomendada | Hold |

---

## Por que Esta Previsão é Razoável?

Domperidona atua como antagonista dos receptores de dopamina D2 e D3 periféricos. Sua principal ação se dá no trato gastrointestinal e na zona de gatilho quimiorreceptora, acelerando o esvaziamento gástrico e suprimindo náuseas e vômitos. Por não cruzar significativamente a barreira hematoencefálica, seus efeitos extrapiramidais são raros — característica que a diferencia de antieméticos de ação central como a metoclopramida.

A NSIAD é uma doença genética rara causada por mutações de ganho de função no gene *AVPR2* (que codifica o receptor V2 da vasopressina). Essas mutações levam à ativação constitutiva do V2R, elevação persistente do AMPc intracelular, superexpressão da aquaporina-2 (AQP2) nas células do ducto coletor renal e retenção crônica de água, resultando em hiponatremia dilucional grave mesmo na ausência de vasopressina circulante.

O TxGNN identificou conectividade topológica entre os nós D2R → AQP2 → regulação hídrica no grafo de conhecimento e gerou uma pontuação elevada (99,08%). Contudo, a análise mecanística revela uma contradição crítica: os receptores D2R renais exercem normalmente uma influência inibitória sobre a via do AMPc. O bloqueio desses receptores pela domperidona **removeria essa inibição tônica**, podendo **agravar** a superativação do AMPc e o acúmulo de AQP2 — efeito diametralmente oposto ao objetivo terapêutico na NSIAD. O modelo capturou a conectividade estrutural, mas não a **direcionalidade funcional** do efeito, configurando alta probabilidade de falso-positivo. Soma-se ainda o risco conhecido de prolongamento do intervalo QTc associado à domperidona, o que introduziria complexidade adicional no manejo de pacientes com NSIAD.

---

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados.

---

## Evidências da Literatura

Atualmente não há literatura relacionada.

---

## Informações de Comercialização no Brasil

Domperidona não possui registros ativos na ANVISA. Nenhum produto foi identificado nas bases consultadas para o mercado brasileiro.

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
A previsão TxGNN é classificada como nível **L5** — sem qualquer ensaio clínico ou publicação de suporte —, e a análise mecanística indica que o bloqueio do D2R renal provavelmente **agrava**, e não trata, a fisiopatologia da NSIAD. A ausência de registro regulatório no Brasil e os dados de segurança incompletos reforçam a recomendação de não avançar com esta hipótese nas condições atuais.

**Para reconsiderar esta indicação, seria necessário:**
- Estudos pré-clínicos em modelos animais de NSIAD demonstrando direção de efeito farmacológico favorável
- Revisão mecanística aprofundada da interação D2R/AMPc/AQP2 no contexto de mutações *AVPR2* com ganho de função
- Dados completos de segurança (advertências, contraindicações e interações medicamentosas da domperidona)
- Avaliação do risco de prolongamento de QTc na população-alvo antes de qualquer protocolo clínico
---

