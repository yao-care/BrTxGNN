---
layout: default
title: Biotin
parent: 僅模型預測 (L5)
nav_order: 123
evidence_level: L5
indication_count: 10
---

# Biotin
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

# Biotin: De suplemento vitamínico à dispepsia

## Resumo em Uma Frase

Biotin (Vitamina B7/H) é uma vitamina hidrossolúvel do complexo B, amplamente utilizada como suplemento nutricional e no tratamento de estados de deficiência vitamínica, incluindo defeitos enzimáticos ligados à biotinidase.
O modelo TxGNN prevê que pode ser eficaz para **Dispepsia (Dyspepsia)**, com pontuação de 99,43%,
atualmente sem **ensaios clínicos** ou **publicações** apoiando diretamente esta direção.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Suplementação vitamínica (Vitamina B7/H); deficiência de biotinidase |
| Nova Indicação Prevista | Dispepsia (Dyspepsia) |
| Pontuação de Previsão TxGNN | 99,43% |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | ✓ Comercializado |
| Número de Registros | 20 |
| Decisão Recomendada | Hold |

---

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação disponíveis neste pacote de evidências. Segundo informações conhecidas, Biotin (Vitamina B7/H) é uma vitamina hidrossolúvel essencial que atua como cofator obrigatório para quatro carboxilases mitocondriais — piruvato carboxilase, acetil-CoA carboxilase, propionil-CoA carboxilase e 3-metilcrotonil-CoA carboxilase. Essas enzimas participam de reações fundamentais de carboxilação envolvendo síntese de ácidos graxos, gliconeogênese e catabolismo de aminoácidos de cadeia ramificada. Sua deficiência causa comprometimento metabólico sistêmico, com manifestações neurológicas, cutâneas e imunológicas.

A relação entre Biotin e dispepsia — síndrome gastrointestinal funcional caracterizada por desconforto epigástrico, plenitude pós-prandial e saciedade precoce — não é evidente do ponto de vista mecanístico direto. Não há evidências moleculares conhecidas de que Biotin regule a secreção ácida gástrica, a motilidade gastroduodenal, a proteção da mucosa gastrointestinal ou a neurotransmissão no sistema nervoso entérico. A fisiopatologia da dispepsia envolve hipersensibilidade visceral, dismotilidade gástrica e alterações no eixo cérebro-intestino — nenhuma dessas vias tem conexão estabelecida com a atividade de cofator de carboxilase do Biotin.

A alta pontuação TxGNN (99,43%) provavelmente reflete conexões indiretas dentro dos nós de redes metabólicas no grafo de conhecimento — como a rede geral de metabolismo energético —, e não uma interação farmacológica específica para dispepsia. Este padrão é consistente com o alto risco de falso positivo descrito para candidatos de nível L5, onde a previsão não é sustentada por evidências clínicas ou pré-clínicas independentes.

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
Nível de evidência L5 — a previsão baseia-se exclusivamente no modelo TxGNN sem respaldo de ensaios clínicos ou literatura científica. A ligação mecanística entre Biotin e dispepsia é biologicamente pouco plausível, com alto risco de falso positivo no grafo de conhecimento decorrente de conexões indiretas em nós de metabolismo energético.

**Para prosseguir, é necessário:**
- Identificação de mecanismo molecular plausível ligando Biotin à fisiologia gástrica (secreção ácida, motilidade ou microbiota intestinal)
- Estudos pré-clínicos (in vitro/in vivo) explorando o efeito de Biotin em modelos de dispepsia funcional
- Dados epidemiológicos associando status sérico de Biotin à prevalência ou gravidade de sintomas dispépticos
- Investigação de possíveis mediadores indiretos (ex.: papel do Biotin no metabolismo energético da mucosa gástrica ou na regulação do microbioma intestinal)
- **Nota clínica:** Indicações com evidências mais robustas estão disponíveis em rankings inferiores deste pacote: Rank 7 — Distúrbio por deficiência vitamínica (L3, *Proceed with Guardrails*, 10 ensaios clínicos e 19 publicações) e Rank 8 — Doença metabólica por Biotin (L3, *Proceed with Guardrails*, com ensaio Phase 1/2 direto em pacientes com deficiência de biotinidase — NCT03269045)
---

