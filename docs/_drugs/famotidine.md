---
layout: default
title: Famotidine
parent: 僅模型預測 (L5)
nav_order: 249
evidence_level: L5
indication_count: 10
---

# Famotidine
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

# Famotidine: Da doença ulcerosa péptica ao refluxo duodenogástrico

## Resumo em Uma Frase

Famotidine é um antagonista seletivo dos receptores H2 de histamina, amplamente utilizado globalmente no tratamento de úlceras gástricas e duodenais e de condições de hipersecreção ácida, porém **sem registro vigente no Brasil**.
O modelo TxGNN prevê que pode ser eficaz para o **Refluxo Duodenogástrico (Duodenogastric reflux)**, com pontuação de 99,99%, indicação atualmente apoiada por apenas **0 ensaios clínicos** e **2 publicações** científicas específicas.
A força da previsão reflete associações no grafo de conhecimento, mas as evidências clínicas diretas para esta indicação específica são ainda incipientes.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Doença ulcerosa péptica / supressão da acidez gástrica (uso global; sem indicação registrada no Brasil) |
| Nova Indicação Prevista | Refluxo Duodenogástrico (Duodenogastric reflux) |
| Pontuação de Previsão TxGNN | 99,99% |
| Nível de Evidência | L4 |
| Situação no Mercado Brasileiro | ✗ Não comercializado |
| Número de Registros | 0 |
| Decisão Recomendada | Hold |

---

## Por que Esta Previsão é Razoável?

Famotidine pertence à classe dos antagonistas seletivos dos receptores H2 de histamina. Internacionalmente reconhecido, o fármaco bloqueia os receptores H2 nas células parietais do estômago, inibindo potentemente a secreção de ácido clorídrico — tanto a basal quanto a estimulada por histamina, gastrina e acetilcolina. Em termos de potência, é aproximadamente 20 vezes mais ativo que a cimetidina e 7,5 vezes mais potente que a ranitidina na supressão ácida. Embora os dados formais de mecanismo de ação não estejam disponíveis no sistema regulatório brasileiro, este perfil farmacológico é amplamente documentado na literatura científica.

O refluxo duodenogástrico é uma condição em que o conteúdo duodenal — bile, suco pancreático e enzimas — retorna ao estômago. Ao contrário do refluxo gastroesofágico, cuja fisiopatologia é fortemente dependente do ácido, o refluxo duodenogástrico é primariamente biliar. A supressão ácida pelo famotidine pode teoricamente reduzir a lesão combinada da mucosa gástrica quando o ambiente ácido potencializa o dano dos ácidos biliares refluxados, e pode aliviar sintomas dispépticos associados. No entanto, o fármaco não controla o refluxo biliar em si.

Desta forma, a plausibilidade biológica existe — especialmente em quadros mistos de refluxo ácido e biliar —, mas é limitada. A pontuação TxGNN elevada (99,99%) decorre das relações no grafo de conhecimento entre o mecanismo de supressão ácida e doenças do trato gastrointestinal superior, e não deve ser interpretada como equivalente à robustez das evidências clínicas, que permanecem escassas para esta indicação específica.

---

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados para famotidine em refluxo duodenogástrico.

---

## Evidências da Literatura

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [12532466](https://pubmed.ncbi.nlm.nih.gov/12532466/) | 2003 | Clinical Study | World Journal of Gastroenterology | Investigação do efeito do famotidine sobre o refluxo gastroesofágico (GER) e o refluxo duodeno-gastro-esofágico (DGER) em pacientes críticos hospitalizados, explorando possíveis mecanismos subjacentes e fatores associados ao refluxo |
| [16259441](https://pubmed.ncbi.nlm.nih.gov/16259441/) | 2004 | Review | Experimental & Clinical Gastroenterology | Avaliação clínica e endoscópica da eficácia do famotidine 20 mg 2x/dia nos estágios iniciais da doença por refluxo gastroduodenal, com base na escala de Savary-Miller modificada (graus 0 e 1) |

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
As evidências específicas para refluxo duodenogástrico são insuficientes — zero ensaios clínicos registrados e apenas 2 publicações de qualidade moderada —, e o mecanismo de supressão ácida do famotidine possui papel fisiopatológico limitado em um refluxo de natureza predominantemente biliar.

**Para prosseguir, é necessário:**
- Obter dados formais de mecanismo de ação (MOA) via consulta ao DrugBank API
- Baixar e analisar bula oficial (FDA, EMA ou ANVISA equivalente) para preenchimento de advertências, contraindicações e interações medicamentosas relevantes
- Iniciar processo de registro na ANVISA, já que o fármaco não possui comercialização no Brasil — pré-requisito para qualquer desenvolvimento clínico local
- Avaliar as indicações com evidências significativamente mais robustas já identificadas pelo TxGNN, em especial **Doença Ulcerosa Péptica (Rank 8 — Nível L1**, com 14 ensaios clínicos concluídos e 20 publicações), que representa o uso clínico estabelecido do famotidine no mundo e o candidato mais promissor para registro no Brasil
- Realizar revisão sistemática focada no papel específico dos antagonistas H2 no refluxo duodenogástrico primário (biliar), diferenciando-o do refluxo gastroesofágico
---

