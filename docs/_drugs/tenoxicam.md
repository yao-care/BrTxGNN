---
layout: default
title: Tenoxicam
parent: 僅模型預測 (L5)
nav_order: 460
evidence_level: L5
indication_count: 10
---

# Tenoxicam
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

Usando o skill `txgnn-pipeline` para verificar contexto do projeto — confirmado que se trata de um relatório para o pipeline BrTxGNN. Prossigo com a geração do relatório.

---

# Tenoxicam: De Analgésico Anti-inflamatório ao Tratamento da Artrite Reumatoide

## Resumo em Uma Frase

Tenoxicam é um anti-inflamatório não esteroidal (AINE) da classe oxicam, utilizado como agente analgésico e anti-inflamatório no controle da dor musculoesquelética e inflamação. O modelo TxGNN prevê que pode ser eficaz para **Artrite Reumatoide (Rheumatoid Arthritis)**, atualmente com **1 ensaio clínico registrado** e **20 publicações científicas** — incluindo múltiplos RCTs de grande porte — apoiando esta direção.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Analgésico e anti-inflamatório (AINE, classe oxicam) |
| Nova Indicação Prevista | Artrite Reumatoide (Rheumatoid Arthritis) |
| Pontuação de Previsão TxGNN | 99.90% |
| Nível de Evidência | L1 |
| Situação no Mercado Brasileiro | ✓ Comercializado |
| Número de Registros ANVISA | 20 |
| Decisão Recomendada | Proceed with Guardrails |

---

## Por que Esta Previsão é Razoável?

Embora os dados detalhados de mecanismo de ação (MOA) não estejam disponíveis neste Evidence Pack, Tenoxicam pertence à classe dos AINEs oxicam — a mesma família do piroxicam — e é reconhecido por inibir de forma não seletiva as enzimas ciclooxigenase 1 e 2 (COX-1/COX-2). Essa inibição reduz a síntese de prostaglandinas inflamatórias, especialmente a prostaglandina E2 (PGE2), principal mediadora do processo inflamatório articular. Sua meia-vida longa (aproximadamente 60–75 horas) permite administração em dose única diária, o que favorece a adesão ao tratamento crônico típico da AR.

A artrite reumatoide é uma doença inflamatória autoimune crônica na qual a inflamação sinovial — mediada predominantemente por PGE2 e citocinas — é responsável pela dor, edema articular e progressão do dano estrutural. A inibição de COX por Tenoxicam atua diretamente nesse mecanismo. Estudos farmacocinéticos realizados em pacientes com AR demonstraram excelente penetração do fármaco no líquido sinovial, com razão fluido sinovial/plasma próxima de 1,0 (PMID 3262939), evidenciando biodisponibilidade local adequada para o tratamento de inflamações intra-articulares.

É importante contextualizar que a artrite reumatoide não representa uma indicação estritamente "nova" para Tenoxicam: múltiplos ensaios clínicos randomizados publicados entre 1985 e 1996 — incluindo estudos com centenas a milhares de pacientes — já confirmaram sua eficácia e tolerabilidade comparável à de outros AINEs de referência como piroxicam, naproxeno e diclofenaco. O modelo TxGNN está, portanto, reconhecendo e validando uma indicação com fundamento biológico sólido e substancial suporte empírico acumulado ao longo de décadas.

---

## Evidências de Ensaios Clínicos

| Número do Ensaio | Fase | Status | Participantes | Principais Achados |
|---------|------|------|------|---------|
| [NCT05508451](https://clinicaltrials.gov/study/NCT05508451) | NA | Concluído | 80 | Comparação de Tenoxicam, Paracetamol e combinação no controle da dor pós-operatória em cirurgia bimaxilar; confirma as propriedades analgésicas e anti-inflamatórias do fármaco, com relevância mecanística para condições inflamatórias como AR |

---

## Evidências da Literatura

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [8894360](https://pubmed.ncbi.nlm.nih.gov/8894360/) | 1996 | RCT | Clinical Rheumatology | Ensaio multicêntrico, paralelo, duplo-cego com 292 pacientes com AR (3 meses): Tenoxicam demonstrou eficácia e segurança equivalentes ao aceclofenaco, com melhora significativa e contínua dos parâmetros clínicos a partir de 15 dias |
| [2695152](https://pubmed.ncbi.nlm.nih.gov/2695152/) | 1989 | RCT | British Journal of Clinical Practice | Estudo duplo-cego paralelo com 1.328 pacientes com OA e AR: Tenoxicam mostrou eficácia ligeiramente superior ao piroxicam na avaliação global do paciente, com melhora da dor noturna, ao movimento e da rigidez articular |
| [2292331](https://pubmed.ncbi.nlm.nih.gov/2292331/) | 1990 | RCT Multicêntrico | Journal of International Medical Research | 2.963 pacientes de 252 clínicas gerais com OA e AR tratados por 12 semanas: redução expressiva de dor e rigidez; 31% mantiveram tratamento além de 52 semanas, indicando eficácia e tolerabilidade no uso prolongado |
| [1593574](https://pubmed.ncbi.nlm.nih.gov/1593574/) | 1992 | RCT | Journal of Rheumatology | Tenoxicam 20mg/dia vs Piroxicam 20mg/dia em 102 pacientes com AR (5 centros): eficácia equivalente nas variáveis primárias; taxa similar de descontinuações por intolerância gastrointestinal |
| [3915885](https://pubmed.ncbi.nlm.nih.gov/3915885/) | 1985 | Ensaio Clínico Múltiplas Indicações | European Journal of Rheumatology | Série de estudos duplo-cego em OA, AR e espondilite anquilosante: Tenoxicam 20mg/dia mostrou eficácia ao menos equivalente ao piroxicam em todas as indicações, incluindo em doses relativamente altas |
| [3915889](https://pubmed.ncbi.nlm.nih.gov/3915889/) | 1985 | Ensaio Clínico | European Journal of Rheumatology | 79 pacientes com AR (n=39) e artrose (n=40) tratados com Tenoxicam 20mg/dia via retal por 6 semanas: melhora clínica significativa em ambos os grupos, validando a eficácia por via não oral |
| [2512637](https://pubmed.ncbi.nlm.nih.gov/2512637/) | 1989 | Ensaio Clínico de Longa Duração | Scandinavian Journal of Rheumatology | Ensaio de 4 anos com 20 pacientes com AR em terapia combinada (Tenoxicam + sais de ouro ou D-penicilamina): melhora analgésica e anti-inflamatória sustentada ao longo de todo o período de acompanhamento |
| [1711963](https://pubmed.ncbi.nlm.nih.gov/1711963/) | 1991 | Review | Drugs | Revisão abrangente: Tenoxicam oral, retal ou parenteral é eficaz no tratamento sintomático de AR, OA, espondilite anquilosante e condições reumáticas extra-articulares; tolerabilidade ao menos equivalente ao piroxicam e provavelmente superior ao diclofenaco e indometacina |
| [1778090](https://pubmed.ncbi.nlm.nih.gov/1778090/) | 1991 | Estudo Aberto | Current Medical Research and Opinion | 736 pacientes africanos ambulatoriais com distúrbios reumáticos e inflamatórios (incluindo AR, OA e tendinite): Tenoxicam 20mg/dia por 15–30 dias demonstrou eficácia e tolerabilidade satisfatórias em população diversificada |
| [3262939](https://pubmed.ncbi.nlm.nih.gov/3262939/) | 1988 | Estudo Farmacocinético | Therapeutic Drug Monitoring | Dose única de 40mg em pacientes com AR e OA: Tenoxicam apresentou razão fluido sinovial/plasma próxima de 1,0, confirmando excelente penetração intra-articular — base farmacocinética que fundamenta a eficácia local na AR |

---

## Informações de Comercialização no Brasil

Tenoxicam está registrado na ANVISA com **20 registros ativos**, confirmando ampla disponibilidade no mercado brasileiro. Os detalhes individuais dos registros (nome comercial, forma farmacêutica e indicações aprovadas) não estão disponíveis neste Evidence Pack e devem ser consultados diretamente no [portal ANVISA](https://consultas.anvisa.gov.br/).

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Proceed with Guardrails**

**Justificativa:**
A evidência científica para uso de Tenoxicam em artrite reumatoide é excepcionalmente robusta, com múltiplos RCTs de grande porte — incluindo estudos com mais de 1.000 pacientes — publicados entre 1985 e 1996, confirmando eficácia comparável à de AINEs de referência. O nível de evidência L1 reflete essa solidez histórica. Com 20 registros ativos na ANVISA, as barreiras regulatórias no Brasil são substancialmente reduzidas.

**Para prosseguir, é necessário:**
- Obter e revisar os dados completos de segurança da bula ANVISA (advertências, contraindicações e interações medicamentosas), atualmente identificados como lacuna de dados bloqueante
- Verificar se a indicação de artrite reumatoide já consta nos registros ANVISA existentes ou se requer solicitação de extensão de indicação
- Confirmar o mecanismo de ação detalhado via DrugBank API (lacuna de dados de alta prioridade)
- Avaliar o perfil de risco gastrointestinal e cardiovascular para uso crônico em pacientes com AR, especialmente em comparação com inibidores seletivos de COX-2 disponíveis no mercado brasileiro
---

