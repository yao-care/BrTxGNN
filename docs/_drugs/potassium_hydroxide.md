---
layout: default
title: Potassium Hydroxide
parent: 僅模型預測 (L5)
nav_order: 407
evidence_level: L5
indication_count: 10
---

# Potassium Hydroxide
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

Usando o skill `txgnn-pipeline` como contexto para geração de relatório de reposicionamento. Vou agora gerar o relatório completo seguindo o formato especificado.

---

# Hidróxido de Potássio (KOH): De Reagente Diagnóstico para Hiperplasia Prostática Benigna

## Resumo em Uma Frase

O hidróxido de potássio (KOH) é um álcali forte sem indicação terapêutica aprovada, utilizado na medicina principalmente como reagente diagnóstico — a preparação KOH para identificação microscópica de fungos em pele e cabelo.
O modelo TxGNN prevê que pode ser eficaz para **Hiperplasia Prostática Benigna (Benign Prostatic Hyperplasia)**, porém com **0 ensaios clínicos** e **0 publicações** apoiando especificamente esta direção.
A pontuação elevada (97.99%) é considerada um artefato do grafo de conhecimento, sem bioplausibilidade biológica que sustente o reposicionamento.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Nenhuma indicação terapêutica aprovada (uso como reagente diagnóstico laboratorial) |
| Nova Indicação Prevista | Hiperplasia Prostática Benigna (Benign Prostatic Hyperplasia) |
| Pontuação de Previsão TxGNN | 97.99% |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | ✗ Não comercializado (0 registros ANVISA) |
| Número de Registros | 0 |
| Decisão Recomendada | Hold |

---

## Por que Esta Previsão é Razoável?

O hidróxido de potássio (KOH) é uma base forte inorgânica (fórmula: KOH), amplamente utilizada como reagente industrial e laboratorial. No contexto clínico, seu único uso reconhecido é o **exame de KOH** (KOH mount ou KOH prep): uma solução diluída a 10–20% aplicada sobre raspados de pele, unhas ou cabelo para dissolver queratina e permitir a visualização de hifas ou esporos fúngicos ao microscópio. Trata-se inteiramente de uma ferramenta **diagnóstica**, não terapêutica.

Não há dados sobre mecanismo de ação terapêutico porque o KOH não possui indicação farmacológica reconhecida por nenhum órgão regulatório. Sua atividade química — dissolução alcalina de proteínas e lipídios — é útil no laboratório diagnóstico, mas representa risco de lesão tecidual severa em qualquer aplicação clínica sistêmica ou tópica com finalidade de tratamento.

A previsão do TxGNN para hiperplasia prostática benigna (BPH) obteve pontuação de 97.99%, provavelmente devido a conexões indiretas no grafo de conhecimento envolvendo metabolismo de potássio ou vias de sinalização iónica compartilhadas. No entanto, **não há bioplausibilidade para o uso de KOH no tratamento de BPH**: a fisiopatologia da BPH envolve hiperplasia do epitélio prostático e estroma mediada por andrógenos (DHT via 5α-redutase) e fatores de crescimento (IGF, EGF), mecanismos completamente distintos das propriedades cáusticas do KOH. Esta previsão é classificada como **falso positivo de alto risco** no contexto do grafo de conhecimento.

---

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados ao uso de Potassium hydroxide em Hiperplasia Prostática Benigna registrados.

---

## Evidências da Literatura

Atualmente não há literatura relacionada ao uso terapêutico de Potassium hydroxide em Hiperplasia Prostática Benigna.

---

## Informações de Comercialização no Brasil

O hidróxido de potássio não possui nenhum registro de medicamento ativo junto à ANVISA. É comercializado exclusivamente como reagente químico de laboratório (produto industrial/diagnóstico), sem qualquer registro farmacêutico.

---

## Considerações de Segurança

Não há bula farmacêutica registrada para o Potassium hydroxide no Brasil. Do ponto de vista da segurança química, o KOH é classificado como substância corrosiva (GHS05), capaz de causar queimaduras graves em pele, mucosas e trato gastrointestinal. Qualquer desenvolvimento para uso terapêutico exigiria avaliação toxicológica completa desde a fase pré-clínica.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
O hidróxido de potássio é um reagente químico cáustico sem indicação terapêutica, sem registro regulatório no Brasil e sem qualquer mecanismo biológico plausível para o tratamento de hiperplasia prostática benigna. A pontuação elevada do TxGNN (97.99%) é interpretada como artefato de propagação indireta no grafo de conhecimento — não reflete utilidade clínica real e representa um falso positivo estrutural do modelo para esta classe de substâncias.

**Para prosseguir com qualquer investigação futura, seria necessário:**
- Investigar a origem do alto score no grafo de conhecimento do TxGNN (identificar o caminho de propagação que gerou o falso positivo)
- Avaliar se existem derivados ou formas galênicas diluídas de compostos de potássio com perfil de segurança adequado para investigação farmacológica
- Estabelecer bioplausibilidade biológica básica antes de qualquer consideração clínica
- Considerar a exclusão de reagentes laboratoriais cáusticos da base de candidatos do pipeline de reposicionamento para evitar falsos positivos sistemáticos

> ⚠️ **Aviso**: Os resultados deste relatório são de natureza exploratória e gerados por modelo computacional. Não constituem recomendação terapêutica nem substituem avaliação clínica especializada. O hidróxido de potássio é uma substância cáustica — qualquer uso experimental requer supervisão regulatória e toxicológica rigorosa.
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

