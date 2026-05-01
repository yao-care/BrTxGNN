---
layout: default
title: Iopamidol
parent: 僅模型預測 (L5)
nav_order: 284
evidence_level: L5
indication_count: 10
---

# Iopamidol
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

O skill `txgnn-pipeline` cobre gestão do pipeline de ML — não se aplica diretamente à tarefa de escrita de relatório. Prossigo com a análise do Evidence Pack e geração do relatório conforme o formato especificado.

---

# Iopamidol: Do meio de contraste iodado para a angina de Prinzmetal

## Resumo em Uma Frase

Iopamidol é um meio de contraste iodado não iônico amplamente utilizado em procedimentos de diagnóstico por imagem, incluindo tomografia computadorizada, angiografia coronariana e urografia.
O modelo TxGNN prevê que pode ser eficaz para **Angina de Prinzmetal (Prinzmetal Angina)**,
porém atualmente **sem ensaios clínicos** e **sem publicações** apoiando esta direção terapêutica — a previsão reflete uma co-ocorrência diagnóstica no Knowledge Graph, não uma relação de tratamento.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Meio de contraste iodado para diagnóstico por imagem (TC, angiografia, urografia, mielografia) |
| Nova Indicação Prevista | Angina de Prinzmetal (Prinzmetal Angina) |
| Pontuação de Previsão TxGNN | 98,57% |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | ✓ Comercializado |
| Número de Registros | 4 |
| Decisão Recomendada | Hold |

---

## Por que Esta Previsão é Razoável?

A angina de Prinzmetal (angina variante) é caracterizada por espasmo transitório da artéria coronariana, causando isquemia miocárdica episódica. Seu diagnóstico definitivo frequentemente requer coronariografia — e é justamente neste procedimento que Iopamidol, como agente de contraste iodado não iônico de baixa osmolaridade, é rotineiramente empregado. Este ponto de convergência clínica foi capturado pelo Knowledge Graph (KG) como uma associação entre o fármaco e a doença, gerando a previsão.

No entanto, a análise do mecanismo revela que a associação no KG é **diagnóstica, não terapêutica**. O caminho inferido é: espasmo coronariano → coronariografia diagnóstica → Iopamidol como meio de contraste. Não há dados de MOA disponíveis para Iopamidol (Data Gap), e não existe hipótese biológica plausível pela qual um meio de contraste iodado pudesse modificar ou tratar o espasmo vascular coronariano subjacente.

É digno de nota que estudos comparativos já demonstraram que agentes não iônicos como Iopamidol causam menor perturbação hemodinâmica durante a coronariografia do que meios iônicos — o que representa uma **vantagem de segurança diagnóstica**, não uma ação farmacológica sobre a fisiopatologia da angina variante. Esta previsão TxGNN deve ser interpretada como um **artefato de topologia do KG por co-ocorrência diagnóstica**.

---

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados.

---

## Evidências da Literatura

Atualmente não há literatura relacionada.

---

## Informações de Comercialização no Brasil

O sistema identificou **4 registros** de Iopamidol no Brasil com situação de mercado ativa. Os detalhes individuais dos registros (número, nome comercial, forma farmacêutica e indicação aprovada) não foram capturados neste ciclo de coleta de dados. Para consulta completa, acesse o banco de dados de produtos registrados da ANVISA em [consultas.anvisa.gov.br](https://consultas.anvisa.gov.br/).

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
A previsão TxGNN de Iopamidol para angina de Prinzmetal é classificada como L5 (exclusivamente baseada em previsão computacional, sem estudos clínicos ou pré-clínicos de suporte) e representa um artefato de co-ocorrência diagnóstica no Knowledge Graph. Não existe mecanismo terapêutico biologicamente plausível, e nenhuma evidência empírica — nem ensaio clínico nem publicação científica — apoia esta indicação.

**Para prosseguir com a análise de Iopamidol, é necessário:**
- Completar os dados regulatórios da ANVISA: recuperar os detalhes dos 4 registros (nome comercial, forma farmacêutica, indicação aprovada)
- Obter informações de segurança da bula oficial: advertências, contraindicações e interações relevantes para populações de risco (insuficiência renal, alergia a iodo, disfunção tireoidiana)
- **Priorizar a análise da indicação de Rank 2 — carcinoma de mama feminina (L4, "Research Question")**: esta previsão possui 1 ensaio clínico registrado e 20 publicações explorando aplicações inovadoras de Iopamidol como agente de CT-linfografia para biópsia de linfonodo sentinela e como marcador de pH tumoral por acidoCEST MRI — configurando um potencial theranostic genuinamente distinto da indicação Rank 1
---

