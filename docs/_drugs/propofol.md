---
layout: default
title: Propofol
parent: Evidência Alta (L1-L2)
nav_order: 554
evidence_level: L2
indication_count: 10
last_modified_at: 2026-10-13
description: "Propofol: nova indicação prevista, Enxaqueca (Migraine Disorder) (nível de evidência L2). Indicação original: Não disponível nos dados de registro da ANVISA (uso conhecido: aneste…"
monitor_inn: "Propofol"
predicted_indications: ["migraine disorder", "migraine with brainstem aura", "Prinzmetal angina", "nephrogenic syndrome of inappropriate antidiuresis", "Tourette syndrome", "tendinitis", "idiopathic granulomatous myositis", "myositis fibrosa", "fibromyalgia", "atrophoderma vermiculata"]
---

# Propofol
{: .fs-9 }

Nível de evidência: **L2** | Indicações previstas: **10** 
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

## Propofol: De anestésico geral para enxaqueca
{: .text-alpha }

## Resumo em Uma Frase

Propofol é um anestésico geral intravenoso, usado para indução e manutenção de anestesia e para sedação. Não há indicação original registrada na ANVISA nos dados compilados para este relatório.
O modelo TxGNN prevê que pode ser eficaz para **Enxaqueca (Migraine Disorder)**, atualmente com **3 ensaios clínicos** e **20 publicações** apoiando esta direção.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Não disponível nos dados de registro da ANVISA (uso conhecido: anestesia geral e sedação) |
| Nova Indicação Prevista | Enxaqueca (Migraine Disorder) |
| Pontuação de Previsão TxGNN | 99,69% |
| Nível de Evidência | L2 |
| Situação no Mercado Brasileiro | Não comercializado (nos dados compilados) |
| Número de Registros | 0 |
| Decisão Recomendada | Proceed with Guardrails |

## Por que Esta Previsão é Razoável?

Não há dados detalhados sobre o mecanismo de ação originalmente registrados. Segundo o conhecimento farmacológico, o propofol é um modulador alostérico positivo do receptor GABA-A, o que intensifica a inibição GABAérgica no sistema nervoso central. Essa é a base de sua ação anestésica e sedativa.

A inibição GABAérgica reforçada pode atenuar a sinalização nociceptiva trigeminovascular e a hiperexcitabilidade cortical, que participam da fisiopatologia da enxaqueca. Um estudo pré-clínico com hemissuccinato de propofol indicou supressão da depressão alastrante cortical, considerada o substrato da aura migranosa. Isso oferece uma base plausível para o uso em doses subanestésicas como terapia abortiva em enxaqueca refratária, o que combina com a pontuação muito alta do modelo.

Outras previsões do modelo (por exemplo, angina de Prinzmetal, tendinite, fibromialgia, síndrome de Tourette) não têm respaldo de benefício terapêutico. A literatura nesses casos trata o propofol como anestésico de uso procedimental ou como possível gatilho de eventos adversos. Por isso, este relatório se concentra na enxaqueca, a previsão mais bem apoiada.

## Evidências de Ensaios Clínicos

| Número do Ensaio | Fase | Status | Participantes | Principais Achados |
|---------|------|------|------|---------|
| [NCT01604785](https://clinicaltrials.gov/study/NCT01604785) | Phase 2/3 | Concluído | 74 | Propofol em dose baixa como terapia abortiva da enxaqueca pediátrica no pronto-socorro; dados retrospectivos prévios sugeriam segurança e eficácia possivelmente superior aos tratamentos padrão |
| [NCT02485418](https://clinicaltrials.gov/study/NCT02485418) | NA | Concluído | 40 | Infusão de propofol em dose baixa como abortivo da enxaqueca pediátrica; avalia eficácia, limites seguros de dose e duração do efeito |
| [NCT02492295](https://clinicaltrials.gov/study/NCT02492295) | NA | Encerrado precocemente | 12 | Propofol em dose baixa para enxaqueca refratária grave no pronto-socorro; término antecipado limita a interpretação |

## Evidências da Literatura

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [29456086](https://pubmed.ncbi.nlm.nih.gov/29456086/) | 2018 | RCT | J Emerg Med | Estudo randomizado e prospectivo de propofol em dose baixa na enxaqueca pediátrica, com possível menor tempo de permanência |
| [33070469](https://pubmed.ncbi.nlm.nih.gov/33070469/) | 2021 | RCT | Emerg Med Australas | Propofol versus placebo (duplo-cego) na resolução precoce da enxaqueca aguda em adultos no pronto-socorro |
| [32705801](https://pubmed.ncbi.nlm.nih.gov/32705801/) | 2020 | RCT (piloto) | Emerg Med Australas | Propofol em dose de sedação procedural versus terapia padrão no tratamento inicial da enxaqueca |
| [35573713](https://pubmed.ncbi.nlm.nih.gov/35573713/) | 2022 | RCT | Arch Acad Emerg Med | Sumatriptano associado a propofol versus sumatriptano isolado na enxaqueca aguda |
| [35402989](https://pubmed.ncbi.nlm.nih.gov/35402989/) | 2022 | RCT | Arch Acad Emerg Med | Propofol + granisetrona versus propofol + metoclopramida no controle dos sintomas da enxaqueca aguda |
| [31621134](https://pubmed.ncbi.nlm.nih.gov/31621134/) | 2020 | Revisão sistemática | Acad Emerg Med | Avalia segurança e eficácia do propofol na enxaqueca aguda no pronto-socorro; evidência limitada |
| [26790849](https://pubmed.ncbi.nlm.nih.gov/26790849/) | 2016 | Revisão sistemática | Headache | Revisão qualitativa dos tratamentos agudos da enxaqueca pediátrica |
| [41321235](https://pubmed.ncbi.nlm.nih.gov/41321235/) | 2026 | Diretriz | Headache | Atualização da diretriz da Sociedade Americana de Cefaleia sobre terapias parenterais para enxaqueca aguda no pronto-socorro |
| [27454834](https://pubmed.ncbi.nlm.nih.gov/27454834/) | 2016 | Revisão | Expert Rev Neurother | Perfil do propofol em doses subanestésicas na enxaqueca refratária |
| [10759925](https://pubmed.ncbi.nlm.nih.gov/10759925/) | 2000 | Série clínica | Headache | Efetividade do propofol intravenoso em enxaqueca intratável em centro ambulatorial de cefaleia |

## Citotoxicidade

Não aplicável: o propofol não é antineoplásico, portanto esta seção foi omitida.

## Considerações de Segurança

- **Contraindicações segundo o grafo de conhecimento (não extraídas da bula)**: o grafo de conhecimento do TxGNN associa o propofol a contraindicação em epilepsia, distúrbio hipotensivo, insuficiência respiratória, arteriosclerose intracraniana, distúrbio hereditário do metabolismo lipídico e hiperlipidemia familiar.
- **Interações medicamentosas**: foram identificadas 100 interações, e as principais listadas foram, em sua maioria, de nível moderado. Entre elas: morfina (inclusive lipossomal) e ópio (depressão do sistema nervoso central e respiratória, em princípio aditiva), antieméticos como ondansetrona, granisetrona e dolasetrona, e antibióticos como claritromicina e levofloxacino (possível prolongamento do intervalo QT, a confirmar na fonte), além de cisaprida, famotidina, loperamida, laxantes e antiácidos (bisacodil, lactulose, lactitol, glicerina, citrato e hidróxido de magnésio, óleo mineral e óleo de rícino). Metronidazol tem interação de nível leve. Os mecanismos de cada par não constam nos dados compilados.
- **Sinal de alerta adicional**: a literatura sobre angina de Prinzmetal descreve a anestesia com propofol como possível gatilho de vasoespasmo coronariano, o que exige cautela em pacientes com doença coronariana.

As advertências e contraindicações da bula da ANVISA não estavam disponíveis nos dados compilados. Consulte a bula para informações de segurança completas.

## Conclusão e Próximos Passos

**Decisão: Proceed with Guardrails**

**Justificativa:**
Há um ensaio de Phase 2/3 concluído (n=74) e vários ensaios randomizados publicados em enxaqueca, com plausibilidade mecanística (modulação GABA-A e supressão da depressão alastrante cortical). Porém, o conjunto de evidências é pequeno, heterogêneo (população pediátrica e adulta, desenhos variados) e uma revisão sistemática descreve a evidência como limitada, o que justifica nível L2 e não L1.

**Para prosseguir, é necessário:**
- Obter e analisar a bula da ANVISA (advertências e contraindicações), lacuna considerada bloqueante para a triagem de segurança.
- Confirmar a situação regulatória no Brasil, pois os dados compilados indicam ausência de registros ativos.
- Confirmar o mecanismo de ação em fonte oficial (por exemplo, DrugBank).
- Realizar ensaios randomizados maiores e controlados, com definição de dose subanestésica, desfechos de recidiva e segurança.
- Definir protocolo restrito a ambiente hospitalar/pronto-socorro com monitorização cardiorrespiratória e hemodinâmica, dada a via intravenosa e o risco de depressão respiratória e hipotensão.
- Avaliar o risco em pacientes com as condições apontadas pelo grafo de conhecimento (epilepsia, hipotensão, insuficiência respiratória, distúrbios lipídicos) e em doença coronariana.
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

