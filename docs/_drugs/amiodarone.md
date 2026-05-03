---
layout: default
title: Amiodarone
parent: 僅模型預測 (L5)
nav_order: 50
evidence_level: L5
indication_count: 10
---

# Amiodarone
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

# Amiodarone: Das Arritmias Ventriculares à Taquicardia Ventricular Polimórfica Catecolaminérgica

## Resumo em Uma Frase

Amiodarone é um antiarrítmico de amplo espectro (Vaughan Williams Classe III), amplamente utilizado no manejo de fibrilação ventricular e taquiarritmias ventriculares graves e refratárias.
O modelo TxGNN prevê que pode ser eficaz para **Taquicardia Ventricular Polimórfica Catecolaminérgica (catecholaminergic polymorphic ventricular tachycardia, CPVT)**,
atualmente com **0 ensaios clínicos** e **10 publicações** apoiando esta direção, com nível de evidência L4.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Fibrilação ventricular e taquiarritmias ventriculares graves (uso estabelecido internacionalmente; sem registro ANVISA) |
| Nova Indicação Prevista | Taquicardia Ventricular Polimórfica Catecolaminérgica (CPVT) |
| Pontuação de Previsão TxGNN | 99,78% |
| Nível de Evidência | L4 |
| Situação no Mercado Brasileiro | ✗ Não comercializado (sem registro ANVISA) |
| Número de Registros | 0 |
| Decisão Recomendada | Hold |

---

## Por que Esta Previsão é Razoável?

Amiodarone é um antiarrítmico de perfil farmacológico único e multiclasse: além de bloquear canais de K⁺ prolongando o período refratário (Classe III), atua como bloqueador de canais de Na⁺ (Classe I), agente β-bloqueador não competitivo (Classe II) e bloqueador de Ca²⁺ (Classe IV). Esse mecanismo de quatro classes o torna eficaz em uma ampla variedade de taquiarritmias supraventriculares e ventriculares. Os dados detalhados de mecanismo de ação (MOA) não estão disponíveis no presente pack de evidências, mas sua atividade farmacológica multicanal é amplamente documentada na literatura clínica e farmacológica.

A CPVT é uma canalopatia cardíaca hereditária rara, causada principalmente por mutações no receptor de rianodina tipo 2 (RYR2) ou na calsequestrina cardíaca (CASQ2). Essas mutações provocam liberação excessiva e descontrolada de Ca²⁺ intracelular durante estimulação adrenérgica — exercício físico ou estresse emocional —, gerando despolarizações tardias (DAD) e taquicardia ventricular bidirecional ou polimórfica potencialmente fatal em corações estruturalmente normais. O padrão de tratamento atual consiste em beta-bloqueadores (nadolol ou propranolol) e flecainide como agentes de primeira linha.

A conexão mecanística com amiodarone assenta-se em dois pilares: (1) seu componente β-bloqueador não competitivo pode suprimir a estimulação catecolaminérgica que deflagra os episódios de CPVT; (2) seu bloqueio de Na⁺ pode inibir as atividades deflagradas geradas por DAD. Contudo, o amiodarone não possui ação direta sobre o canal RYR2 — alvo do flecainide, que demonstrou superioridade em estudos controlados. Na prática clínica, o amiodarone é considerado apenas como opção de resgate quando beta-bloqueadores, flecainide e CDI falharam simultaneamente, com suporte baseado exclusivamente em relatos e séries de casos individuais. A alta pontuação do TxGNN reflete a sobreposição mecanística no grafo de conhecimento, mas não equivale a eficácia clínica comprovada nesta indicação específica.

---

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados para amiodarone em taquicardia ventricular polimórfica catecolaminérgica.

---

## Evidências da Literatura

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [26513538](https://pubmed.ncbi.nlm.nih.gov/26513538/) | 2015 | Review | Expert Opin Pharmacother | Revisão sobre avanços no tratamento farmacológico de arritmias ventriculares; discute papel de antiarrítmicos — incluindo amiodarone — no espectro das VT herdadas como CPVT, reconhecendo-o como opção de resgate |
| [35892906](https://pubmed.ncbi.nlm.nih.gov/35892906/) | 2022 | Observational Cohort | Life (Basel) | Revisão sistemática de características clínicas, base genética (RYR2) e desfechos arrítmicos de pacientes com CPVT na China; base para comparação epidemiológica entre populações asiáticas e ocidentais |
| [39076628](https://pubmed.ncbi.nlm.nih.gov/39076628/) | 2022 | Observational Cohort | Rev Cardiovasc Med | Coorte retrospectiva descrevendo características clínicas, genéticas, utilização de recursos de saúde e custos em pacientes com CPVT; documenta padrões de tratamento no mundo real |
| [22553997](https://pubmed.ncbi.nlm.nih.gov/22553997/) | 2012 | Case Series | Pacing Clin Electrophysiol | Flecainide suprimiu tempestade arrítmica induzida por CDI em adolescente com CPVT por mutação de calsequestrina-2, após falha de outros agentes; amiodarone citado no contexto de manejo multimodal de resgate |
| [39735866](https://pubmed.ncbi.nlm.nih.gov/39735866/) | 2024 | Case Report | Front Cardiovasc Med | Adolescente com CPVT refratária resolvida por desnervação simpática cardíaca direita após falha da esquerda; ilustra a complexidade e os limites das opções farmacológicas de resgate |
| [37852665](https://pubmed.ncbi.nlm.nih.gov/37852665/) | 2023 | Case Report | BMJ Case Reports | Criança com parada cardíaca extra-hospitalar e 40 desfibrilações; amiodarone integrou a terapia farmacológica multimodal de emergência em contexto de VT polimórfica refratária |
| [22218697](https://pubmed.ncbi.nlm.nih.gov/22218697/) | 2012 | Case Report | Anesth Analg | Neonato com síndrome do QT longo e VT refratária tratado com lidocaína, esmolol e amiodarone; documenta uso de amiodarone como componente de terapia combinada em arritmia neonatal grave |
| [29668588](https://pubmed.ncbi.nlm.nih.gov/29668588/) | 2018 | Case Report | Medicine | Diagnóstico tardio de 6 anos de CPVT com mutação RYR2 c.7580T>G em criança de 9 anos; destaca atraso diagnóstico em regiões com acesso limitado a testes genéticos |
| [30116135](https://pubmed.ncbi.nlm.nih.gov/30116135/) | 2018 | Case Report | Türk Pediatri Arşivi | CPVT como causa rara de parada cardíaca súbita em criança de 2 anos sem cardiopatia estrutural; enfatiza a necessidade de reconhecimento precoce da síndrome em pediatria |
| [17125720](https://pubmed.ncbi.nlm.nih.gov/17125720/) | 2006 | Case Report | Rev Española Cardiol | Tempestade arrítmica induzida por descarga de CDI em paciente com CPVT; amiodarone utilizado na estabilização de emergência aguda |

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
A CPVT já dispõe de terapias de primeira linha clinicamente estabelecidas (beta-bloqueadores e flecainide), e o amiodarone é reconhecido apenas como opção de último recurso neste contexto — sem nenhum ensaio clínico dedicado e com evidências restritas a relatos e séries de casos (nível L4). Adicionalmente, o fármaco não possui registro na ANVISA, o que inviabiliza seu uso regular no Brasil como produto específico para esta indicação.

**Para prosseguir, é necessário:**
- Obtenção ou submissão de registro na ANVISA para viabilizar acesso clínico no Brasil
- Levantamento detalhado do mecanismo de ação (MOA), especialmente interação com canais RYR2, para fortalecer a plausibilidade mecanística
- Evidências clínicas prospectivas em pacientes com CPVT documentadamente refratária a beta-bloqueadores + flecainide + CDI
- Dados de segurança completos da bula de referência (FDA/EMA), incluindo advertências, contraindicações e perfil de toxicidade orgânica (pulmonar, hepática, tireoidiana, ocular)
- Avaliação comparativa formal com nadolol e flecainide, que possuem maior suporte clínico específico para CPVT
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

