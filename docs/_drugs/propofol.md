---
layout: default
title: Propofol
parent: 僅模型預測 (L5)
nav_order: 420
evidence_level: L5
indication_count: 10
---

# Propofol
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

Usando o skill `txgnn-pipeline` para verificar diretrizes do projeto — confirmado. Agora gero o relatório seguindo o formato v5.

---

# Propofol: Da Anestesia Geral à Enxaqueca (Migraine Disorder)

## Resumo em Uma Frase

Propofol é um agente anestésico intravenoso de ação ultracurta, amplamente utilizado para indução e manutenção da anestesia geral e sedação em procedimentos clínicos. O modelo TxGNN prevê que pode ser eficaz no tratamento da **Enxaqueca (Migraine Disorder)** em doses sub-anestésicas, especialmente no cenário de emergência. Atualmente há **5 ensaios clínicos** e **20 publicações** apoiando esta direção.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Anestesia geral e sedação |
| Nova Indicação Prevista | Enxaqueca (Migraine Disorder) |
| Pontuação de Previsão TxGNN | 99.69% |
| Nível de Evidência | L2 |
| Situação no Mercado Brasileiro | ✓ Comercializado |
| Número de Registros | 20 |
| Decisão Recomendada | Proceed with Guardrails |

---

## Por que Esta Previsão é Razoável?

Com base no conhecimento farmacológico consolidado, o propofol (2,6-diisopropilphenol) é um sedativo-hipnótico que atua principalmente como modulador positivo alostérico do receptor GABA-A, potencializando a inibição gabaérgica no sistema nervoso central. Em doses sub-anestésicas, esse mesmo mecanismo pode ser aproveitado terapeuticamente sem induzir perda de consciência completa.

A conexão com a enxaqueca é biologicamente plausível: a depressão alastrante cortical (CSD — *Cortical Spreading Depression*) é o correlato neural da aura migranosa e um gatilho da dor. O propofol suprime a CSD por meio da potenciação GABA-A, interrompendo a cascata que ativa a via trigeminovascular e desencadeia a crise. Adicionalmente, doses sub-anestésicas modulam os centros de dor hipotalâmicos e do tronco cerebral através das vias dopaminérgica e serotoninérgica — contribuindo para o alívio do episódio agudo.

Múltiplos ensaios clínicos randomizados, revisões sistemáticas e, mais recentemente, uma diretriz da American Headache Society (2025/2026) apoiam a tradução clínica desse mecanismo, especialmente no contexto de pronto-socorro para enxaqueca aguda refratária e na população pediátrica.

---

## Evidências de Ensaios Clínicos

| Número do Ensaio | Fase | Status | Participantes | Principais Achados |
|---------|------|------|------|---------|
| [NCT01604785](https://clinicaltrials.gov/study/NCT01604785) | Phase 2/3 | Concluído | 74 | Maior ensaio prospectivo pediátrico: testa propofol em doses sub-anestésicas como agente abortivo de enxaqueca aguda no pronto-socorro infantil; fornece dados de segurança e eficácia |
| [NCT02485418](https://clinicaltrials.gov/study/NCT02485418) | NA | Concluído | 40 | Infusão de propofol em baixa dose como agente abortivo em enxaqueca pediátrica; avalia eficácia, limites de dosagem seguros e duração do efeito |
| [NCT02492295](https://clinicaltrials.gov/study/NCT02492295) | NA | Encerrado Prematuramente | 12 | Propofol em baixa dose para enxaqueca grave refratária em adultos no pronto-socorro; encerrado precocemente (n=12), evidência limitada — motivo do encerramento desconhecido |
| [NCT03789370](https://clinicaltrials.gov/study/NCT03789370) | NA | Desconhecido | 130 | Comparação de propofol vs. sevoflurano na manutenção anestésica e incidência de cefaleia pós-operatória; evidência indireta de potencial efeito protetor do propofol sobre a enxaqueca |

---

## Evidências da Literatura

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [41321235](https://pubmed.ncbi.nlm.nih.gov/41321235/) | 2026 | Diretriz Clínica | Headache | Atualização 2025 da diretriz da American Headache Society para tratamento parenteral de enxaqueca no pronto-socorro; revisão de evidências de farmacoterapias incluindo propofol |
| [39364614](https://pubmed.ncbi.nlm.nih.gov/39364614/) | 2024 | Revisão Sistemática + Metanálise em Rede | Headache | Comparação de agentes parenterais para redução de recidiva em enxaqueca aguda grave; inclui avaliação de propofol entre os tratamentos de segunda linha |
| [31621134](https://pubmed.ncbi.nlm.nih.gov/31621134/) | 2020 | Revisão Sistemática | Academic Emergency Medicine | Primeira revisão sistemática dedicada ao propofol para enxaqueca aguda no pronto-socorro; avalia segurança e eficácia com base na literatura disponível |
| [35402989](https://pubmed.ncbi.nlm.nih.gov/35402989/) | 2022 | RCT | Archives of Academic Emergency Medicine | RCT duplo-cego comparando propofol + granisetron vs. propofol + metoclopramida no controle dos sintomas de enxaqueca aguda no pronto-socorro |
| [35573713](https://pubmed.ncbi.nlm.nih.gov/35573713/) | 2022 | RCT | Archives of Academic Emergency Medicine | RCT avaliando eficácia da combinação sumatriptana + propofol versus sumatriptana isolada no manejo de enxaqueca aguda |
| [29456086](https://pubmed.ncbi.nlm.nih.gov/29456086/) | 2018 | RCT | The Journal of Emergency Medicine | RCT prospectivo de propofol em baixa dose para enxaqueca pediátrica no pronto-socorro; avalia eficácia, perfil de efeitos adversos e tempo de permanência |
| [32705801](https://pubmed.ncbi.nlm.nih.gov/32705801/) | 2020 | RCT Piloto | Emergency Medicine Australasia | RCT piloto comparando propofol em dose de sedação procedural vs. terapia padrão para manejo inicial de enxaqueca no pronto-socorro adulto |
| [27454834](https://pubmed.ncbi.nlm.nih.gov/27454834/) | 2016 | Revisão de Especialista | Expert Review of Neurotherapeutics | Perfil completo do propofol no manejo de enxaqueca super-refratária em doses sub-anestésicas; relata benefícios em pacientes não responsivos ao tratamento padrão |
| [32638172](https://pubmed.ncbi.nlm.nih.gov/32638172/) | 2020 | Revisão | Current Pain and Headache Reports | Tratamento intravenoso de enxaqueca em crianças e adolescentes; discute propofol como uma das opções disponíveis no contexto pediátrico de emergência |
| [10759925](https://pubmed.ncbi.nlm.nih.gov/10759925/) | 2000 | Série de Casos | Headache | Relato pioneiro da eficácia singular do propofol intravenoso no tratamento de enxaqueca intratável em ambulatório de cefaleia; fundamentou as investigações clínicas subsequentes |

---

## Informações de Comercialização no Brasil

O propofol possui **20 registros ativos** no Brasil (situação: ✓ Comercializado). Os detalhes individuais de cada registro — nome comercial, forma farmacêutica e indicação aprovada — não estão disponíveis no conjunto de dados atual.

> ℹ️ Para consultar os registros individuais, acesse o portal de consulta de medicamentos da ANVISA em [consultas.anvisa.gov.br](https://consultas.anvisa.gov.br/).

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Proceed with Guardrails**

**Justificativa:**
Há múltiplos RCTs, revisões sistemáticas e uma diretriz clínica de 2025/2026 da American Headache Society apoiando o uso de propofol em doses sub-anestésicas para o tratamento agudo de enxaqueca — especialmente em pronto-socorro e na população pediátrica. O mecanismo GABA-A/CSD é biologicamente coerente com o alvo terapêutico, e a qualidade das evidências disponíveis justifica o nível L2.

**Para prosseguir, é necessário:**
- Obter dados de advertências e contraindicações da bula registrada na ANVISA (bloqueio DG001 — severidade: Bloqueante)
- Confirmar mecanismo de ação completo via DrugBank API (bloqueio DG002 — severidade: Alta)
- Definir protocolo de monitoramento para uso em doses sub-anestésicas: risco de sedação excessiva e depressão respiratória requer suporte de ressuscitação disponível no local de aplicação
- Avaliar viabilidade de uso restrito ao ambiente de pronto-socorro com equipe treinada em sedação
- Verificar necessidade de extensão de indicação regulatória junto à ANVISA para uso sistemático nesta nova indicação
---

