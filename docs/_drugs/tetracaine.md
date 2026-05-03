---
layout: default
title: Tetracaine
parent: 僅模型預測 (L5)
nav_order: 470
evidence_level: L5
indication_count: 9
---

# Tetracaine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **9** 個
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

# Tetracaine: De Anestésico Local para Acne Keloid

## Resumo em Uma Frase

Tetracaine é um anestésico local de tipo éster, amplamente utilizado para anestesia de superfície em procedimentos oftalmológicos, otorrinolaringológicos e dermatológicos, agindo pelo bloqueio dos canais de sódio voltagem-dependentes (Nav).
Entre as 9 indicações previstas pelo modelo TxGNN, a de **melhor evidência clínica** é **Acne Keloid (Cicatriz Queloide por Acne)** — especificamente como adjuvante anestésico em procedimentos de laser dermatológico —, apoiada por **1 ensaio clínico Phase 4 concluído** e **1 publicação RCT** no British Journal of Dermatology.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Anestesia local e superficial (oftalmológica, dermatológica, otorrinolaringológica) |
| Nova Indicação Prevista | Acne Keloid — anestesia tópica pré-procedimental para laser (Acne Keloidalis Nuchae) |
| Pontuação de Previsão TxGNN | 99.91% (rank geral #779) |
| Nível de Evidência | L2 |
| Situação no Mercado Brasileiro | ✗ Não comercializado |
| Número de Registros | 0 |
| Decisão Recomendada | Proceed with Guardrails *(apenas para acne keloid)* |

---

## Por que Esta Previsão é Razoável?

Tetracaine é um anestésico local da classe dos ésteres que exerce seu efeito pelo bloqueio reversível dos canais de sódio voltagem-dependentes (Nav) na membrana neuronal, impedindo a despolarização e a condução do impulso doloroso. Embora os dados detalhados de MOA não estejam disponíveis no Evidence Pack consultado, Tetracaine é farmacologicamente bem caracterizado na literatura científica. É utilizado classicamente em preparações tópicas (colírio, spray, gel, creme) e para raquianestesia.

A acne keloidalis nuchae (AKN) é uma dermatose inflamatória crônica que forma pápulas e placas queloideanas na região da nuca e couro cabeludo posterior. Seu tratamento de primeira linha inclui procedimentos físicos dolorosos como laser Nd:YAG, laser de diodo, criocirurgia ou excisão cirúrgica. Para reduzir a dor associada a esses procedimentos, a formulação em creme de 7% Lidocaína / 7% Tetracaína é aplicada topicamente de forma prévia como anestésico de superfície de ação profunda e prolongada — superando formulações convencionais como EMLA (2,5% Lid/2,5% Pril) em eficácia analgésica para procedimentos dérmicos profundos.

Portanto, o papel de Tetracaine neste contexto não é como terapia modificadora da fibrose ou da inflamação subjacente à AKN, mas sim como **adjuvante anestésico procedimental** — um uso clinicamente direto, mecanisticamente coerente com o perfil farmacológico do fármaco, e respaldado por evidência clínica formal. O RCT duplo-cego de Phase 4 identificado confirma especificamente a eficácia e a segurança desta aplicação.

---

## Visão Geral das 9 Indicações Previstas

| Rank | Doença Prevista | Score TxGNN | Evidência | Recomendação | Interpretação |
|------|-----------------|-------------|-----------|--------------|---------------|
| 1 | Acrodermatitis chronica atrophicans | 99.93% | L5 | Hold | Falso positivo — doença bacteriana (Borrelia); Nav sem papel terapêutico |
| 2 | Neonatal dermatomyositis | 99.92% | L5 | Hold | Doença autoimune (IFN/complemento); sem mecanismo relevante |
| 3 | Bronchitis | 99.92% | L4 | Hold | Uso procedimental em broncoscopia, não tratamento da bronquite em si |
| 4 | ILD pediátrica + doença do tecido conjuntivo | 99.92% | L5 | Hold | Falso positivo — doença pulmonar autoimune fibrótica |
| **5** | **Acne Keloid** | **99.91%** | **L2** | **Proceed with Guardrails** | **Melhor evidência: RCT Phase 4 completo (n=30)** |
| 6 | Hydroa vacciniforme, familiar | 99.91% | L5 | Hold | Doença EBV-relacionada (NK/T); sem mecanismo com Nav |
| 7 | Amyopathic dermatomyositis | 99.90% | L5 | Hold | Autoimune (anti-MDA5); completamente sem relação com Nav |
| 8 | Cauda equina syndrome | 99.55% | L4 | Hold | ⚠️ **ALERTA**: Tetracaine é causa conhecida de CES iatrogênica — sinal invertido |
| 9 | Irritable bowel syndrome | 99.41% | L5 | Hold | Sem biodisponibilidade oral; inviável para alcance sistêmico intestinal |

---

## Evidências de Ensaios Clínicos

*(Indicação com evidência: Acne Keloid — rank #5)*

| Número do Ensaio | Fase | Status | Participantes | Principais Achados |
|---------|------|------|------|---------|
| [NCT02372786](https://clinicaltrials.gov/study/NCT02372786) | Phase 4 | Concluído | 30 | Ensaio duplo-cego randomizado comparando creme 7% Lidocaína/7% Tetracaína vs. 2,5% Lidocaína/2,5% Prilocaína para anestesia local durante laser em acne keloidalis nuchae e remoção de tatuagem. Desfecho primário: redução da dor autorreferida durante o procedimento. Design rigoroso; amostra pequena (n=30). |

---

## Evidências da Literatura

*(Indicação com evidência: Acne Keloid — rank #5)*

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [27377616](https://pubmed.ncbi.nlm.nih.gov/27377616/) | 2017 | RCT | British Journal of Dermatology | Resultados de dois ensaios clínicos randomizados comparando lidocaína/tetracaína vs. lidocaína/prilocaína em creme para anestesia tópica em laser para acne keloidalis nuchae e remoção de tatuagens. Confirma eficácia da formulação com Tetracaína para procedimentos dérmicos profundos; alta correspondência com NCT02372786 (possível publicação do mesmo estudo). |

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

> **⚠️ Alerta Especial — Causalidade Reversa (Rank #8, Cauda Equina Syndrome):**
> A previsão TxGNN para síndrome da cauda equina deve ser interpretada como **sinal falso positivo por associação inversa**: Tetracaine em raquianestesia — especialmente em altas concentrações ou com formulações hipobáricas/hiperbáricas inadequadas — é uma **causa conhecida** de lesão neurológica iatrogênica, incluindo síndrome da cauda equina. Há múltiplos relatos de caso na literatura descrevendo este dano neurológico após injeção intratecal de Tetracaine. Este fármaco **não deve** ser considerado para tratamento desta condição.

---

## Conclusão e Próximos Passos

**Decisão: Proceed with Guardrails** *(indicação: Acne Keloid como anestésico tópico pré-procedimental para laser)*

**Justificativa:**
Um RCT duplo-cego de Phase 4 (NCT02372786, n=30) avaliou diretamente a formulação 7% Lidocaína/7% Tetracaína para redução de dor durante laser em acne keloidalis nuchae, com publicação formal no British Journal of Dermatology (2017). O uso é mecanisticamente coerente com o perfil farmacológico de Tetracaine como bloqueador Nav, porém restringe-se ao papel de **anestésico procedimental** — não representa terapia modificadora da doença queloide subjacente.

**Para prosseguir, é necessário:**
- Registrar a formulação 7% Lidocaína / 7% Tetracaína em creme junto à ANVISA (atualmente sem registro no Brasil)
- Obter dados completos de advertências, contraindicações e MOA via consulta ao DrugBank e à bula oficial
- Avaliar viabilidade regulatória: registro de formulação composta, importação ou manipulação em farmácia de manipulação com laudo de equivalência
- Delimitar claramente o contexto de uso: anestesia tópica pré-procedimento de laser/criocirurgia — não como tratamento da fibrose ou inflamação da AKN
- Para as demais **8 indicações previstas**: recomendação **Hold** universal, por ausência de mecanismo plausível (ranks 1, 2, 4, 6, 7, 9), natureza procedimental sem benefício terapêutico real (ranks 3, 5), ou risco de interpretação de causalidade inversa (**rank 8 — contraindicado investigar**)
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

