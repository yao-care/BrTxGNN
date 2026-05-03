---
layout: default
title: Minoxidil
parent: 僅模型預測 (L5)
nav_order: 352
evidence_level: L5
indication_count: 10
---

# Minoxidil
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

O skill txgnn-pipeline orienta o fluxo técnico do pipeline, mas não sobrepõe o formato de relatório definido no prompt principal. Prosseguindo com a geração do relatório conforme o Evidence Pack fornecido.

---

# Minoxidil: Da alopecia androgenética à hipotricose simples do couro cabeludo

## Resumo em Uma Frase

Minoxidil é um medicamento aprovado no Brasil para o tratamento da alopecia androgenética (queda de cabelo de padrão hereditário) em sua formulação tópica, e para hipertensão arterial grave em sua formulação oral.
O modelo TxGNN prevê que pode ser eficaz para a **Hipotricose Simples do Couro Cabeludo (Hypotrichosis Simplex of the Scalp)**, uma rara condição genética autossômica dominante que causa perda progressiva de cabelo.
Atualmente, há **0 ensaios clínicos** e **3 publicações** (todos relatos de caso) apoiando esta direção.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|----------|
| Indicação Original | Alopecia androgenética (formulação tópica) / Hipertensão arterial grave (formulação oral) |
| Nova Indicação Prevista | Hipotricose Simples do Couro Cabeludo (Hypotrichosis Simplex of the Scalp) |
| Pontuação de Previsão TxGNN | 99.99999% |
| Nível de Evidência | L4 |
| Situação no Mercado Brasileiro | ✓ Comercializado |
| Número de Registros | 20 |
| Decisão Recomendada | Hold |

---

## Por que Esta Previsão é Razoável?

Atualmente não há dados detalhados sobre o mecanismo de ação disponíveis neste pacote de evidências. Com base na literatura consolidada, Minoxidil atua como ativador de canais de potássio dependentes de ATP (K_ATP), promovendo vasodilatação perifollicular e estimulação direta das células da papila dérmica — o que prolonga a fase anágena do ciclo capilar e aumenta o diâmetro e a densidade dos fios. Esta ação já é bem estabelecida na alopecia androgenética.

A hipotricose simples do couro cabeludo (HSS) é uma condição monogênica rara, causada principalmente por mutações no gene CDSN (que codifica a corneodesmosin, uma proteína desmossômica), levando ao desenvolvimento folicular deficiente e queda progressiva de cabelo. A conexão teórica com Minoxidil reside na sua capacidade de compensar funcionalmente a insuficiência folicular por meio de estímulo microvascular e de proliferação celular, potencialmente independente da causa genética subjacente — uma lógica de "resgate funcional".

No entanto, existe uma limitação mecanística importante: ao contrário da AGA (onde os folículos estão miniaturizados, mas presentes), na HSS os folículos podem apresentar defeitos estruturais congênitos mais profundos. A eficácia de Minoxidil depende, portanto, do grau de preservação folicular residual em cada paciente. Os três relatos de caso disponíveis são encorajadores, mas insuficientes para estabelecer benefício clínico geral. Investigação prospectiva mais estruturada é necessária.

---

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados.

---

## Evidências da Literatura

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|-----------|-------------------|
| [39902296](https://pubmed.ncbi.nlm.nih.gov/39902296/) | 2024 | Relato de Caso | Frontiers in Genetics | Criança de 8 anos com HSS causada por mutação no CDSN tratada com combinação de extratos botânicos e Minoxidil, com melhora clínica relatada |
| [36651821](https://pubmed.ncbi.nlm.nih.gov/36651821/) | 2023 | Relato de Caso | J Dermatological Treatment | Paciente de 14 anos com hipotricose simples hereditária: tratamento combinado de plasma rico em plaquetas (PRP) intralesional + Minoxidil tópico 2% resultou em crescimento capilar observável |
| [35761391](https://pubmed.ncbi.nlm.nih.gov/35761391/) | 2022 | Série de Casos | Dermatologic Therapy | Hipotricose simples hereditária tratada com Minoxidil oral associado a fatores de crescimento; achados clínicos favoráveis relatados |

---

## Informações de Comercialização no Brasil

Há **20 registros** ativos na ANVISA para produtos contendo Minoxidil. Os detalhes individuais (número de registro, nome comercial, forma farmacêutica e indicação aprovada) não estão disponíveis nos dados fornecidos neste pacote. Com base no perfil regulatório consolidado do fármaco, os registros incluem tipicamente:

| Forma Farmacêutica | Concentração | Indicação Conhecida |
|--------------------|-------------|---------------------|
| Solução tópica | 2% / 5% | Alopecia androgenética feminina e masculina |
| Espuma tópica | 5% | Alopecia androgenética masculina |
| Comprimido oral | 2,5 mg / 10 mg | Hipertensão arterial grave / uso off-label para alopecia |

> Para detalhes completos de cada registro, consultar diretamente o sistema CONSULTAS da ANVISA.

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
As evidências disponíveis para o uso de Minoxidil em hipotricose simples do couro cabeludo restringem-se a três relatos de caso (nível L4), sem nenhum ensaio clínico controlado registrado. Embora o mecanismo seja biologicamente plausível e os relatos sejam favoráveis, a natureza genética e estrutural da HSS impõe limitações que exigem investigação mais robusta antes de qualquer avanço clínico formal.

**Para prosseguir, é necessário:**
- Obter dados completos de mecanismo de ação (MOA) do DrugBank para aprofundar a análise de compatibilidade com a fisiopatologia da HSS
- Recuperar advertências, contraindicações e interações medicamentosas da bula ANVISA (atualmente com data gap bloqueante)
- Conduzir um estudo-piloto prospectivo ou observacional com número adequado de pacientes diagnosticados geneticamente com HSS (mínimo recomendado: N ≥ 20)
- Definir endpoint primário objetivável (ex.: densidade capilar por tricoscopia digital, contagem de fios/cm²)
- Avaliar se a via tópica ou oral é mais adequada para esta indicação, considerando biodisponibilidade folicular e perfil de segurança em população pediátrica (casos relatados incluem crianças)
- Registrar protocolo no ClinicalTrials.gov para garantir rastreabilidade e viabilizar futuras meta-análises sobre esta condição rara
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

