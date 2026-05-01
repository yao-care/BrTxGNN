---
layout: default
title: Flunitrazepam
parent: 僅模型預測 (L5)
nav_order: 255
evidence_level: L5
indication_count: 10
---

# Flunitrazepam
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

# Flunitrazepam: Do Sedativo-Hipnótico à Insônia

## Resumo em Uma Frase

Flunitrazepam é um benzodiazepínico de alta potência da classe dos agonistas do receptor GABA-A, historicamente utilizado para sedação e indução anestésica, com aprovação para insônia em múltiplos países europeus e asiáticos — embora os dados regulatórios brasileiros estejam incompletos no sistema atual. O modelo TxGNN prevê que pode ser eficaz para **Insônia (Insomnia Disease)** como indicação de maior pontuação (rank 1), com **1 ensaio clínico observacional** identificado. Nota clínica relevante: dentre todas as indicações previstas, o **Delirium por Abstinência Alcoólica (rank 6)** apresenta as evidências clínicas mais diretas e robustas neste pack.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Sedação / hipnótico (dados de indicação aprovada indisponíveis nos registros ANVISA do sistema) |
| Nova Indicação Prevista | Insônia (Insomnia Disease) |
| Pontuação de Previsão TxGNN | 99,89% |
| Nível de Evidência | L3 |
| Situação no Mercado Brasileiro | ✓ Comercializado |
| Número de Registros | 6 |
| Decisão Recomendada | Hold |

---

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados de mecanismo de ação disponíveis no sistema para o Flunitrazepam (Data Gap confirmado). Com base no conhecimento farmacológico estabelecido, o Flunitrazepam é um benzodiazepínico de alta potência (10× mais potente que o diazepam) que atua como modulador alostérico positivo do receptor GABA-A, aumentando a frequência de abertura dos canais de cloreto em resposta ao GABA. Isto resulta em hiperpolarização neuronal e efeitos sedativos, hipnóticos, ansiolíticos, anticonvulsivantes e relaxantes musculares pronunciados.

A relação entre este mecanismo e o tratamento da insônia é direta: a potenciação dos receptores GABA-A encurta a latência do sono, aumenta o sono de ondas lentas (NREM fase 2) e reduz o sono REM — alterações documentadas por estudos polisomnográficos em pacientes com insônia (evidências nos PMIDs 9681586 e 17559 da lista de literatura). A indicação de insônia é, inclusive, a aprovação histórica do fármaco em múltiplos países europeus e asiáticos, o que torna esta previsão do TxGNN mecanisticamente coerente, embora clinicamente já conhecida.

A principal barreira para o avanço desta indicação **não é o mecanismo farmacológico**, mas o perfil de segurança e o contexto regulatório: o Flunitrazepam apresenta potencial de abuso documentado, foi associado a crimes de violência sexual facilitada ("date rape drug"), tem forte potencial de dependência e já foi alvo de restrições severas ou retirada do mercado em países como os Estados Unidos. Para reposicionamento formal no Brasil, a avaliação regulatória e de segurança é o obstáculo prioritário.

---

## Evidências de Ensaios Clínicos

| Número do Ensaio | Fase | Status | Participantes | Principais Achados |
|---------|------|------|------|---------|
| [NCT02648776](https://clinicaltrials.gov/study/NCT02648776) | N/A | Desconhecido | 1.400 | Coorte prospectiva avaliando padrões de uso de hipnóticos em idosos com distúrbios do sono em centro universitário de Taiwan — inclui análise de eficácia, segurança, farmacocinética e farmacogenética; fornece dados de mundo real sobre hipnóticos (incluindo benzodiazepínicos), mas não é ensaio interventivo para Flunitrazepam em insônia |

---

## Informações de Comercialização no Brasil

O Flunitrazepam possui **6 registros ativos** na ANVISA. Os campos de nome comercial, forma farmacêutica, fabricante e texto de indicação aprovada não estão disponíveis no sistema neste momento — todos os registros retornaram com dados em branco. Consulte diretamente o portal de consulta de medicamentos da ANVISA (https://consultas.anvisa.gov.br/) para verificar os detalhes completos de cada registro.

---

## Considerações de Segurança

Consulte a bula para informações de segurança. Com base no conhecimento farmacológico público disponível, destacam-se os seguintes pontos de atenção:

- **Potencial de abuso e dependência**: O Flunitrazepam é um dos benzodiazepínicos com maior potencial de abuso documentado, estando associado a dependência física e síndrome de abstinência grave.
- **Efeitos amnésicos**: Produz amnésia anterógrada significativa dose-dependente, o que contribuiu para seu uso indevido como facilitador de crimes.
- **Reações paradoxais**: A literatura documenta ocorrência de agitação, desinibição, agressividade e comportamento violento, especialmente em altas doses (PMID 16087304).
- **Interações com álcool e depressores do SNC**: A combinação com álcool potencializa efeitos depressores do SNC com risco de depressão respiratória grave (PMID 38676788).
- **Comprometimento de condução de veículos**: Estudos farmacológicos documentam prejuízo significativo da habilidade de condução (PMID 15365913).

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
Embora o mecanismo GABA-A do Flunitrazepam seja farmacologicamente compatível com o tratamento de insônia e a previsão TxGNN seja de alta pontuação (99,89%), as evidências clínicas diretas para esta indicação são escassas (apenas 1 estudo observacional, sem literatura específica de eficácia para insônia neste pack), e o perfil de segurança/abuso do fármaco representa uma barreira regulatória de alto risco que supera o benefício potencial frente às alternativas disponíveis no mercado.

**Para prosseguir, é necessário:**
- Recuperar os dados completos de indicação aprovada dos 6 registros ANVISA (download e análise das bulas em PDF)
- Verificar o status atual de controle especial do Flunitrazepam no Brasil (Portaria SVS/MS nº 344 — portaria de psicotrópicos)
- Obter dados de mecanismo de ação via DrugBank API (remediation do Data Gap DG002)
- **Prioridade alternativa recomendada**: Avaliar formalmente a indicação **Delirium por Abstinência Alcoólica (rank 6, score 99,50%)**, que possui o suporte clínico mais robusto neste evidence pack — com estudos clínicos diretos de Flunitrazepam IV em UTI (PMID 8214408: série de 25 casos; PMID 14557857: coorte em UTI cirúrgica; PMID 42267 e PMID 6123125: estudos clínicos piloto de 1979 e 1981), tornando-a a candidatura de reposicionamento com melhor relação evidência/mecanismo neste conjunto de dados.
---

