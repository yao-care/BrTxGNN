---
layout: default
title: Pregabalin
parent: Apenas Predição do Modelo (L5)
nav_order: 548
evidence_level: L5
indication_count: 6
last_modified_at: 2026-11-13
monitor_inn: "PREGABALIN"
predicted_indications: ["tendinitis", "myositis fibrosa", "idiopathic granulomatous myositis", "inclusion body myositis", "migraine disorder", "migraine with brainstem aura"]
description: "Pregabalin: nova indicação prevista, Tendinite (tendinitis) (nível de evidência L5). Indicação original: Não consta nos dados locais"
---

# Pregabalin
{: .fs-9 }

Nível de evidência: **L5** | Indicações previstas: **6** 
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

## Pregabalin: Tendinite (tendinitis)
{: .text-alpha }

## Resumo em Uma Frase

A pregabalina é um ligante da subunidade alfa-2-delta dos canais de cálcio, usado originalmente em transtorno de ansiedade, fibromialgia, síndrome de dor miofascial e neuralgia pós-herpética.
O modelo TxGNN prevê que pode ser eficaz para **tendinite (tendinitis)**, mas, para essa indicação, **não há ensaios clínicos** e a literatura recuperada é **indireta** (6 publicações, nenhuma tratando a tendinite em si).

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Não consta nos dados locais |
| Nova Indicação Prevista | Tendinite (tendinitis) |
| Pontuação de Previsão TxGNN | 0.9971 |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | Comercializado (registros ativos: 60 de 86) |
| Número de Registros | 86 (ativos: 60) |
| Decisão Recomendada | Hold |

## Por que Esta Previsão é Razoável?

A pregabalina liga-se à subunidade alfa-2-delta dos canais de cálcio dependentes de voltagem e reduz a liberação de neurotransmissores excitatórios. Isso pode aliviar componentes de dor neuropática ou de sensibilização central que acompanham doenças tendíneas crônicas. Os dados compilados não trazem uma descrição formal do mecanismo de ação; a explicação acima é uma interpretação mecanística plausível.

A relação com as indicações originais está na dor crônica: fibromialgia e dor miofascial envolvem o sistema musculoesquelético e a sensibilização central, o que aproxima o fármaco de condições dolorosas dos tendões. A ligação, porém, é indireta.

É preciso cautela. A literatura recuperada trata de analgesia pós-operatória (reparo artroscópico do manguito rotador), relatos de caso de compressão nervosa e incapacidade associada a fluoroquinolonas. Nada disso mostra tratamento da tendinite em si. A pontuação muito alta do TxGNN é uma previsão computacional, sem confirmação clínica.

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados para a tendinite.

## Evidências da Literatura

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [34052386](https://pubmed.ncbi.nlm.nih.gov/34052386/) | 2022 | RCT | Arthroscopy | Pregabalina oral perioperatória comparada ao bloqueio do plexo braquial interescalênico após reparo artroscópico do manguito rotador, com foco em dor pós-operatória, consumo de opioides e satisfação do paciente |
| [32839073](https://pubmed.ncbi.nlm.nih.gov/32839073/) | 2021 | Coorte retrospectiva | J Orthop Sci | Avaliação do efeito analgésico e poupador de opioides da pregabalina após reparo do manguito rotador; os estudos prévios têm resultados conflitantes |
| [41017607](https://pubmed.ncbi.nlm.nih.gov/41017607/) | 2025 | Relato de caso/Revisão | Praxis | Incapacidade associada a fluoroquinolonas (ciprofloxacino), incluindo tendinopatias; sem relação direta com o tratamento por pregabalina |
| [40818536](https://pubmed.ncbi.nlm.nih.gov/40818536/) | 2025 | Editorial | Arthroscopy | Síndrome do piriforme e compressão do nervo ciático; sem relação direta com a pregabalina |
| [37051935](https://pubmed.ncbi.nlm.nih.gov/37051935/) | 2023 | Relato de caso | Pain Pract | Lesão do nervo cutâneo femoral posterior após maratona, associada a tendinite dos isquiotibiais |
| [39703364](https://pubmed.ncbi.nlm.nih.gov/39703364/) | 2024 | Pré-clínico (animal) | Adv Pharmacol Pharm Sci | Extrato de *Cissus quadrangularis* na neuropatia induzida por vincristina em ratos; sem relação direta com a pregabalina |

## Considerações de Segurança

- **Contraindicações segundo o grafo de conhecimento (não é texto de bula):** transtorno de ansiedade, transtorno neurótico, transtorno distímico, trombocitopenia, angioedema (incluindo as formas adquirida, hereditária, não histaminérgica e induzida por bloqueadores do sistema renina-angiotensina-aldosterona), miopatia, doença muscular, doença do músculo esquelético, paralisia periódica familiar, rabdomiólise, fasciite nodular, insuficiência renal e bloqueio atrioventricular.
- **Interações medicamentosas** (100 interações registradas; as principais):
  - **Maior gravidade:** morfina e morfina lipossomal.
  - **Gravidade moderada:** pioglitazona, rosiglitazona, troglitazona, difenoxina, difenoxilato, dronabinol, nabilona, metoclopramida, ópio e sibutramina.
  - **Gravidade desconhecida:** calcitriol, vitamina A, fentermina, pantoprazol, glimepirida, sucralfato, palonosetrona e nistatina.

Para advertências e contraindicações oficiais, consulte a bula.

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
- Não há ensaios clínicos nem literatura direta sobre pregabalina na tendinite. A pontuação alta do TxGNN reflete apenas uma previsão computacional (nível L4).

<!-- review:begin br-lic-20261106-pregabalin-1 -->

> **Correção de verificação (2026-11-06)**: Texto original: “A pontuação alta do TxGNN reflete apenas uma previsão computacional (nível L4), e a ausência de registro no Brasil limita o acesso.” Removido: a afirmação de que os registros estariam cancelados, vencidos ou inválidos não correspondia aos dados de registro (dados abertos de medicamentos da ANVISA, em 2026-11-06). Nos dados (dados abertos de medicamentos da ANVISA) constam 86 registros para este medicamento, 61 válidos; os números atualizados estão no resumo rápido e nas informações de comercialização. Fonte: [ANVISA – Dados abertos de medicamentos](https://dados.anvisa.gov.br/dados/DADOS_ABERTOS_MEDICAMENTOS.csv).

<!-- review:end br-lic-20261106-pregabalin-1 -->

**Para prosseguir, é necessário:**
- Estudos clínicos ou pré-clínicos que testem diretamente a pregabalina na tendinite, e não apenas na dor pós-operatória.
- Dados detalhados do mecanismo de ação e análise da ligação mecanística com a doença tendínea.
- Advertências e contraindicações oficiais obtidas da bula (ANVISA), pendência que bloqueia a triagem de segurança.
- Avaliação da viabilidade regulatória.

<!-- review:begin br-lic-20261106-pregabalin-2 -->

> **Correção de verificação (2026-11-06)**: Texto original: “Avaliação da viabilidade regulatória, já que o fármaco não tem registro no Brasil.” Removido: a afirmação de que os registros estariam cancelados, vencidos ou inválidos não correspondia aos dados de registro (dados abertos de medicamentos da ANVISA, em 2026-11-06). Nos dados (dados abertos de medicamentos da ANVISA) constam 86 registros para este medicamento, 61 válidos; os números atualizados estão no resumo rápido e nas informações de comercialização. Fonte: [ANVISA – Dados abertos de medicamentos](https://dados.anvisa.gov.br/dados/DADOS_ABERTOS_MEDICAMENTOS.csv).

<!-- review:end br-lic-20261106-pregabalin-2 -->

### Outras indicações previstas (resumo)

Os dados compilados incluem outras indicações previstas. A mais avançada é a **enxaqueca (migraine disorder)**, com pontuação de 0,9947 e nível L2. Há um ensaio de Fase 3 retirado (NCT00447369) e ensaios randomizados pediátricos pequenos, comparando a pregabalina com valproato e propranolol. A recomendação é tratá-la como **questão de pesquisa**, pois não há evidência confirmatória de Fase 3. As demais indicações (miosite granulomatosa idiopática, miosite fibrosa, miosite por corpos de inclusão e enxaqueca com aura do tronco encefálico) têm apenas previsão do modelo ou estudos pré-clínicos (L4–L5) e permanecem em **Hold**.

<!-- review:begin log -->

## Registro de verificação

Abaixo está o registro de verificação desta página: afirmações conferidas com os dados oficiais de registro (dados abertos de medicamentos da ANVISA). As correções se limitam a fatos básicos; as previsões do modelo, os níveis de evidência e as conclusões não foram reescritos.

| Data da verificação | Item | Ação | Fonte |
|------|------|------|------|
| 2026-11-06 | Removido: “e a ausência de registro no Brasil limita o acesso” | Corrigido | [ANVISA – Dados abertos de medicamentos](https://dados.anvisa.gov.br/dados/DADOS_ABERTOS_MEDICAMENTOS.csv) |
| 2026-11-06 | Removido: “já que o fármaco não tem registro no Brasil” | Corrigido | [ANVISA – Dados abertos de medicamentos](https://dados.anvisa.gov.br/dados/DADOS_ABERTOS_MEDICAMENTOS.csv) |

<!-- review:end log -->

## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

