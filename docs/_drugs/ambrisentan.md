---
layout: default
title: Ambrisentan
parent: Apenas Predição do Modelo (L5)
nav_order: 47
evidence_level: L5
indication_count: 5
monitor_inn: "ambrisentan"
predicted_indications: ["pulmonary arteriovenous malformation (disease)", "malformation syndrome with odontal and/or periodontal component", "hypotrichosis simplex of the scalp", "hypertrichosis (disease)", "syndrome with a Dandy-Walker malformation as major feature"]
last_modified_at: 2026-10-31
description: "Ambrisentan: nova indicação prevista, Malformação arteriovenosa pulmonar (pulmonary arteriovenous malformation (disease)) (nível de evidência L5). Indicação original: ANTI-HIPERTENSIVOS"
---

# Ambrisentan
{: .fs-9 }

Nível de evidência: **L5** | Indicações previstas: **5** 
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

## Ambrisentana: antagonista do receptor de endotelina → Malformação arteriovenosa pulmonar (pulmonary arteriovenous malformation (disease))
{: .text-alpha }

## Resumo em Uma Frase

Ambrisentana é um antagonista do receptor de endotelina tipo A, usado como anti-hipertensivo.
O modelo TxGNN prevê que pode ser eficaz para **Malformação arteriovenosa pulmonar (pulmonary arteriovenous malformation (disease))**, mas há apenas **1 publicação** (um relato de caso) relacionada, e **nenhum ensaio clínico** registrado.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | ANTI-HIPERTENSIVOS |
| Nova Indicação Prevista | Malformação arteriovenosa pulmonar (pulmonary arteriovenous malformation (disease)) |
| Pontuação de Previsão TxGNN | 0,9941 |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | Comercializado (registros ativos: 1 de 1) |
| Número de Registros | 1 (ativos: 1) |
| Decisão Recomendada | Hold |

## Por que Esta Previsão é Razoável?

Segundo a seção “Mechanism of Action” da bula aprovada pela FDA dos EUA (Prescribing Information) para Ambrisentan (tradução não oficial): “A endotelina-1 (ET-1) é um potente peptídeo autócrino e parácrino. Dois subtipos de receptores, ET A e ET B, medeiam os efeitos da ET-1 no músculo liso vascular e no endotélio. […] A ambrisentana é um antagonista do receptor ET A de alta afinidade (K i =0,011 nM), com alta seletividade pelo receptor ET A em relação ao receptor ET B (>4000 vezes).” Texto original em inglês: "Endothelin-1 (ET-1) is a potent autocrine and paracrine peptide. Two receptor subtypes, ET A and ET B, mediate the effects of ET-1 in the vascular smooth muscle and endothelium. […] Ambrisentan is a high-affinity (K i =0.011 nM) ET A receptor antagonist with a high selectivity for the ET A versus ET B receptor (>4000-fold)." ([DailyMed: Letairis (ambrisentan) prescribing information, Gilead Sciences, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=725d4e73-6c83-477a-adc6-0ae4a133a844), versão de 2026-06-22; acessado em 2026-11-19). Segundo informações conhecidas, a ambrisentana é um antagonista seletivo do receptor de endotelina tipo A, que reduz a resistência vascular pulmonar.

A única publicação associada descreve hipertensão arterial pulmonar em uma paciente com telangiectasia hemorrágica hereditária. Trata-se de uma complicação hipertensiva e não do tratamento da malformação arteriovenosa pulmonar em si. A pontuação alta provavelmente reflete a proximidade da rede de relações com a hipertensão arterial pulmonar.

Mecanisticamente, o bloqueio da endotelina não deve fechar nem tratar os shunts das malformações, e a vasodilatação poderia, em teoria, piorar o shunt direita-esquerda. A previsão deve ser vista com cautela. Como nenhum estudo avalia diretamente a doença prevista como alvo de tratamento, o nível de evidência é L5.

## Evidências da Literatura

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [33969094](https://pubmed.ncbi.nlm.nih.gov/33969094/) | 2021 | Relato de caso | World J Clin Cases | Paciente com telangiectasia hemorrágica hereditária e hipertensão arterial pulmonar; revisão do quadro clínico, tratamento e análise genética familiar |

Atualmente não há ensaios clínicos relacionados registrados.

## Informações de Comercialização no Brasil

| Registro | Produto | Empresa detentora | Situação |
|------|------|------|------|
| 101070281 | VOLIBRIS | GLAXOSMITHKLINE BRASIL LTDA | Ativo |

## Considerações de Segurança

- **Contraindicações**: não há texto de bula disponível nos dados compilados para este relatório.
- **Teratogenicidade**: a ambrisentana é teratogênica, o que exige cautela em contextos de malformações do desenvolvimento.
- **Interações Medicamentosas**: foram identificadas 112 interações. Entre as de nível moderado estão canagliflozina, dapagliflozina, empagliflozina, ertugliflozina, eliglustate e naltrexona. Entre as de nível menor estão claritromicina, miconazol e omeprazol.

Consulte a bula para as demais informações de segurança.

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
- A previsão se apoia somente no modelo e em um relato de caso sobre hipertensão pulmonar, sem estudo que avalie diretamente a malformação arteriovenosa pulmonar. Há ainda risco teórico de piora do shunt.

**Para prosseguir, é necessário:**
- Estudos que avaliem diretamente o efeito da ambrisentana em malformações arteriovenosas pulmonares
- Dados de mecanismo de ação e análise do risco de piora do shunt direita-esquerda
- Texto de bula da ANVISA com advertências e contraindicações
- Plano de monitoramento de segurança, incluindo contracepção, dada a teratogenicidade

<!-- review:begin log -->

## Registro de verificação

Abaixo, o registro de verificação desta página. A frase que dizia não haver dados sobre o mecanismo de ação foi substituída por um trecho da bula oficial citada (com tradução não oficial); as previsões do modelo, os níveis de evidência e as conclusões não foram reescritos.

| Data da verificação | Item | Ação | Fonte |
|------|------|------|------|
| 2026-11-19 | Frase “não há dados sobre o mecanismo de ação” substituída por trecho da bula dos EUA | Frase sobre a falta de dados do mecanismo de ação substituída por um trecho com fonte | [DailyMed: Letairis (ambrisentan) prescribing information, Gilead Sciences, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=725d4e73-6c83-477a-adc6-0ae4a133a844) |

<!-- review:end log -->

## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

