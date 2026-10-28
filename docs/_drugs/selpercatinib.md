---
layout: default
title: Selpercatinib
parent: Apenas Predição do Modelo (L5)
nav_order: 582
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-13
description: "Selpercatinib: nova indicação prevista, Hipertensão Pulmonar (Pulmonary Hypertension) (nível de evidência L5). Indicação original: Inibidores da proteína quinase"
monitor_inn: "selpercatinib"
predicted_indications: ["pulmonary hypertension", "migraine disorder", "migraine with brainstem aura"]
---

# Selpercatinib
{: .fs-9 }

Nível de evidência: **L5** | Indicações previstas: **3** 
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

## Selpercatinibe: De inibidor de proteína quinase para hipertensão pulmonar
{: .text-alpha }

## Resumo em Uma Frase

Selpercatinibe (RETSEVMO) é um inibidor de proteína quinase, classe registrada na ANVISA como indicação original; sabe-se que atua como inibidor seletivo da quinase RET.
O modelo TxGNN prevê que pode ser eficaz para **Hipertensão Pulmonar (Pulmonary Hypertension)**, mas atualmente há **0 ensaios clínicos** e **nenhuma publicação** que trate dessa indicação; a previsão é puramente computacional.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Inibidores da proteína quinase |
| Nova Indicação Prevista | Hipertensão Pulmonar (Pulmonary Hypertension) |
| Pontuação de Previsão TxGNN | 0,9918 |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | Comercializado (registros ativos: 1 de 1) |
| Número de Registros | 1 (ativos: 1) |
| Decisão Recomendada | Hold |

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação nos dados compilados para este relatório. Segundo informações conhecidas, o selpercatinibe é um inibidor seletivo da quinase RET, pertencente à classe dos inibidores de proteína quinase. Não há, porém, vínculo mecanístico estabelecido entre a inibição de RET e a hipertensão pulmonar.

Alguns inibidores de quinase de outros alvos (por exemplo, o imatinibe, que atua sobre PDGFR) já foram explorados na hipertensão arterial pulmonar. Para a inibição específica de RET, no entanto, não há evidência de apoio. As publicações recuperadas tratam de cânceres dependentes de RET e de eventos adversos, não do tratamento de hipertensão pulmonar.

A pontuação elevada do TxGNN (0,9918) é apenas uma previsão computacional e deve ser interpretada com cautela. As previsões seguintes do modelo (enxaqueca, com 0,9917, e enxaqueca com aura do tronco encefálico, com 0,9905) também carecem de qualquer evidência clínica ou da literatura; a segunda está provavelmente correlacionada à primeira, não constituindo evidência independente.

## Evidências da Literatura

As publicações abaixo foram recuperadas na busca, mas não tratam de hipertensão pulmonar; servem apenas como contexto sobre o fármaco.

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [39372206](https://pubmed.ncbi.nlm.nih.gov/39372206/) | 2024 | Coorte | Frontiers in Pharmacology | Estudo de mundo real (FAERS) comparando eventos adversos de pralsetinibe e selpercatinibe |
| [34178121](https://pubmed.ncbi.nlm.nih.gov/34178121/) | 2021 | Coorte | Therapeutic Advances in Medical Oncology | Análise retrospectiva (SIREN) de selpercatinibe em câncer de pulmão de não pequenas células com fusão de RET, tratados por programa de acesso |
| [41918669](https://pubmed.ncbi.nlm.nih.gov/41918669/) | 2026 | Relato de caso | Cureus | Carcinoma medular de tireoide metastático em NEM 2B com mutação RET M918T: desafios do manejo de longo prazo e da terapia-alvo |

Atualmente não há ensaios clínicos relacionados registrados.

## Informações de Comercialização no Brasil

| Número de Registro | Nome Comercial | Forma Farmacêutica | Indicação Aprovada |
|---------|------|------|-----------|
| Registro nº 112600204 (cancelado) | RETSEVMO | Não informada | Inibidores da proteína quinase |

## Citotoxicidade

| Item | Conteúdo |
|------|------|
| Classificação de Citotoxicidade | Terapia alvo (inibidor seletivo de quinase RET) |
| Risco de Mielossupressão | Consulte as advertências e precauções na bula |
| Classificação de Emetogenicidade | Consulte as advertências e precauções na bula |
| Itens de Monitoramento | Consulte a bula; o perfil de segurança conhecido inclui hipertensão, prolongamento do intervalo QT e hepatotoxicidade, sugerindo monitorar pressão arterial, ECG e função hepática |
| Proteção no Manuseio | Consulte as advertências e precauções na bula |

## Considerações de Segurança

- **Interações Medicamentosas**: foram registradas 249 interações no total. Entre as exemplificadas nos dados compilados:
  - **Gravidade maior**: famotidina, ranitidina, cimetidina, omeprazol, rabeprazol, dexlansoprazol (redutores de acidez gástrica), aprepitanto, claritromicina, dexametasona e óxido de magnésio.
  - **Gravidade moderada**: hidrocortisona, triancinolona, betametasona, budesonida, pioglitazona, saxagliptina, loperamida, bisacodil e polietilenoglicol com eletrólitos.
- **Perfil de segurança conhecido** (fora da bula brasileira, que não foi obtida): hipertensão, prolongamento do intervalo QT e hepatotoxicidade, o que pesa contra o uso em indicação crônica não oncológica.

Consulte a bula para advertências e contraindicações, pois estas não estavam disponíveis nos dados compilados.

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
- A previsão para hipertensão pulmonar baseia-se somente no modelo (nível L5), sem ensaios clínicos, sem literatura sobre a indicação e sem vínculo mecanístico plausível. Além disso, o único registro brasileiro está cancelado.

**Para prosseguir, é necessário:**
- Obter e analisar a bula da ANVISA (advertências e contraindicações), etapa que bloqueia a triagem de segurança.
- Complementar os dados de mecanismo de ação (por exemplo, via DrugBank).
- Buscar evidência pré-clínica que ligue a via RET à fisiopatologia da hipertensão pulmonar.
- Avaliar o impacto das interações medicamentosas e do perfil de segurança (pressão arterial, QT, fígado) em um contexto não oncológico.
- Esclarecer a situação regulatória no Brasil (registro cancelado).
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

