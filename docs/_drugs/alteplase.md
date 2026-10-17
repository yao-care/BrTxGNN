---
layout: default
title: Alteplase
parent: Apenas Predição do Modelo (L5)
nav_order: 45
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-13
description: "Alteplase: nova indicação prevista, Infarto do miocárdio posterolateral (posterolateral myocardial infarc… (nível de evidência L5). Indicação original: Embolia pulmonar, AVC, infarto do miocárdio, tr…"
monitor_inn: "ALTEPLASE"
predicted_indications: ["heparin cofactor 2 deficiency", "congenital coronary artery anomaly", "factor 5 excess with spontaneous thrombosis", "antithrombin deficiency type 2", "thrombophilia", "coronary stenosis"]
---

# Alteplase
{: .fs-9 }

Nível de evidência: **L5** | Indicações previstas: **9** 
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

# Alteplase: Do infarto do miocárdio e AVC à trombofilia

## Resumo em Uma Frase

Alteplase é um ativador do plasminogênio tecidual recombinante, originalmente usado no tratamento de eventos trombóticos agudos, como infarto do miocárdio, embolia pulmonar e AVC isquêmico.
O modelo TxGNN prevê que pode ser eficaz para **infarto do miocárdio posterolateral (posterolateral myocardial infarction)**, a previsão de maior pontuação, mas sem nenhum ensaio clínico ou publicação específica. Entre as previsões analisadas, a **trombofilia (thrombophilia)** tem o maior volume de evidências: **1 ensaio clínico** de Fase 2 em andamento e **19 publicações**, quase todas relatos de caso.

> Observação: a previsão de maior pontuação é, na prática, um subtipo anatômico de uma indicação já existente (infarto do miocárdio), e não um reposicionamento genuíno. Por isso, este relatório destaca também as previsões com mais evidências.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Embolia pulmonar, AVC, infarto do miocárdio, trombose coronariana (indicações originais segundo o grafo de conhecimento; não há registro no Brasil com texto de indicação) |
| Nova Indicação Prevista (maior pontuação) | Infarto do miocárdio posterolateral (posterolateral myocardial infarction) |
| Pontuação de Previsão TxGNN | 99,79% |
| Nível de Evidência | L5 (previsão de maior pontuação); L3 para trombofilia; L2 para estenose coronariana |
| Situação no Mercado Brasileiro | Não comercializado |
| Número de Registros | 0 |
| Decisão Recomendada | Hold |

### Outras previsões analisadas

| Posição | Indicação prevista | Pontuação | Nível | Decisão |
|------|------|------|------|------|
| 1 | Infarto do miocárdio posterolateral | 99,79% | L5 | Hold |
| 2 | Infarto do miocárdio posteroinferior | 99,79% | L5 | Hold |
| 3 | Infarto do miocárdio septal | 99,77% | L4 | Hold |
| 4 | Deficiência de cofator 2 da heparina | 99,72% | L5 | Hold |
| 5 | Anomalia coronariana congênita | 99,64% | L5 | Hold |
| 6 | Excesso de fator V com trombose espontânea | 99,56% | L5 | Hold |
| 7 | Deficiência de antitrombina tipo 2 | 99,56% | L5 | Hold |
| 8 | Trombofilia | 99,43% | L3 | Questão de pesquisa |
| 9 | Estenose coronariana | 99,14% | L2 | Questão de pesquisa |

---

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação compilados para este relatório. Segundo informações conhecidas, a alteplase é um ativador do plasminogênio tecidual recombinante que converte plasminogênio em plasmina, dissolvendo a fibrina dos coágulos. Sua eficácia em eventos trombóticos agudos (infarto, embolia pulmonar, AVC isquêmico) é bem estabelecida.

Para os subtipos de infarto (posterolateral, posteroinferior, septal), o mecanismo é exatamente o mesmo da indicação já existente: lise do trombo oclusivo coronariano. A pontuação alta provavelmente reflete a proximidade no grafo com o infarto do miocárdio em geral, e não uma descoberta nova. Esses casos não representam reposicionamento verdadeiro.

Nas trombofilias (deficiência de antitrombina, de cofator 2 da heparina, excesso de fator V), a alteplase poderia dissolver trombos agudos, mas **não corrige o estado pró-trombótico subjacente**. Já a estenose coronariana é plausível quando há trombo sobreposto, como na angina instável, embora a angioplastia primária tenha substituído em grande parte a terapia fibrinolítica nesse cenário. Na anomalia coronariana congênita, o vínculo é apenas indireto.

---

## Evidências de Ensaios Clínicos

Para a previsão de maior pontuação (infarto do miocárdio posterolateral) não há ensaios clínicos registrados. O único ensaio clínico encontrado refere-se à trombofilia:

| Número do Ensaio | Fase | Status | Participantes | Principais Achados |
|---------|------|------|------|---------|
| [NCT05540834](https://clinicaltrials.gov/study/NCT05540834) | Phase 2 | Recrutando | 70 | Estudo de segurança, determinação de dose e eficácia do tratamento com tPA guiado por testes viscoelásticos em insuficiência respiratória aguda pró-trombótica (COVID e não COVID). Sem resultados ainda; previsão de término em dez/2026. A correspondência com trombofilia é inferida. |

---

## Evidências da Literatura

Seleção das publicações mais relevantes (prioridade: ensaios randomizados, revisões e depois relatos de caso).

### Estenose coronariana

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [8299637](https://pubmed.ncbi.nlm.nih.gov/8299637/) | 1993 | RCT | European Heart Journal | Estudo duplo-cego com 80 pacientes com dor torácica em repouso e depressão de ST: alteplase 100 mg em 3 h versus placebo |
| [1782951](https://pubmed.ncbi.nlm.nih.gov/1782951/) | 1991 | RCT | European Heart Journal | Alteplase versus placebo em 36 pacientes com angina instável refratária submetidos a angioplastia subsequente |
| [8721695](https://pubmed.ncbi.nlm.nih.gov/8721695/) | 1996 | Estudo clínico | Cathet Cardiovasc Diagn | Alteplase intracoronária dirigida à lesão com heparina em 45 pacientes com angina instável e trombo coronariano |
| [19069338](https://pubmed.ncbi.nlm.nih.gov/19069338/) | 2008 | Estudo comparativo | Srp Arh Celok Lek | Comparação entre estreptoquinase e alteplase nos sinais de reperfusão em IAM com supradesnivelamento de ST |
| [22094974](https://pubmed.ncbi.nlm.nih.gov/22094974/) | 2012 | Estudo piloto | J Thromb Thrombolysis | Viabilidade e segurança de ICP precoce após alteplase em meia dose em população chinesa com IAMCSST |
| [2118432](https://pubmed.ncbi.nlm.nih.gov/2118432/) | 1990 | Revisão | Circulation | Revisão da terapia trombolítica no infarto agudo do miocárdio |

### Infarto do miocárdio septal

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [8763515](https://pubmed.ncbi.nlm.nih.gov/8763515/) | 1996 | Estudo clínico | Rev Port Cardiol | Efeito da trombólise tardia com alteplase sobre a função ventricular esquerda no infarto |
| [37754803](https://pubmed.ncbi.nlm.nih.gov/37754803/) | 2023 | Relato de caso | J Cardiovasc Dev Dis | Embolia pulmonar simulando IAMCSST, tratada com trombectomia por aspiração e trombólise dirigida por cateter |

### Trombofilia

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [41876387](https://pubmed.ncbi.nlm.nih.gov/41876387/) | 2026 | Relato de caso | Catheter Cardiovasc Interv | Resistência à trombólise sistêmica na deficiência de antitrombina III, resolvida com trombólise dirigida por cateter |
| [26588446](https://pubmed.ncbi.nlm.nih.gov/26588446/) | 2016 | Relato de caso | Blood Coagul Fibrinolysis | Deficiência hereditária de antitrombina e esteroides anabolizantes; embolia pulmonar submaciça tratada com trombólise dirigida por cateter (não é evidência direta de benefício da trombólise) |
| [36163059](https://pubmed.ncbi.nlm.nih.gov/36163059/) | 2022 | Relato de caso | J Natl Med Assoc | Trombólise sistêmica na oclusão aguda da artéria central da retina em doença falciforme |
| [19006032](https://pubmed.ncbi.nlm.nih.gov/19006032/) | 2008 | Relato de caso | Kardiol Pol | Embolia pulmonar grave após apendicectomia em usuária de anticoncepcional, tratada com infusão de alteplase |
| [29196364](https://pubmed.ncbi.nlm.nih.gov/29196364/) | 2017 | Relato de caso/Revisão | Clin Med (London) | Trombólise com alteplase em AVC isquêmico na gravidez |
| [19260122](https://pubmed.ncbi.nlm.nih.gov/19260122/) | 2009 | Relato de caso | Am J Hematol | Argatroban e trombólise dirigida por cateter com alteplase em paciente com histórico de trombocitopenia induzida por heparina |

---

## Considerações de Segurança

- **Interações Medicamentosas**: foram identificadas 100 interações no total; entre as listadas, destacam-se as de gravidade **maior** (risco aumentado de sangramento por efeito aditivo sobre a hemostasia): abciximabe, apixabana, fondaparinux, anisindiona, acalabrutinibe, deferasirox, ibritumomabe tiuxetana e tositumomabe (incluindo a forma I-131). Interações de gravidade **moderada** incluem ácido acetilsalicílico, ibuprofeno, cetorolaco (inclusive oftálmico), fluvoxamina, fosinopril, ácido aminocaproico, aprotinina, fenfluramina, dexfenfluramina e sibutramina.
- **Risco de sangramento**: na população com trombofilia, o risco hemorrágico precisa ser avaliado com cuidado. Um relato de caso também descreve resistência à trombólise sistêmica na deficiência de antitrombina III.

Consulte a bula para as demais informações de segurança, como advertências e contraindicações.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
- As previsões de maior pontuação são subtipos de indicações já aprovadas (infarto do miocárdio) e não têm ensaios nem literatura específicos; portanto, não configuram reposicionamento real.
- Para trombofilia (L3) e estenose coronariana (L2), as evidências são sobretudo relatos de caso e estudos antigos, sem benefício claro estabelecido, e o fármaco não está registrado no Brasil. Ambas permanecem como questões de pesquisa.

**Para prosseguir, é necessário:**
- Obter a bula da ANVISA e confirmar o status regulatório (atualmente sem registros no Brasil), incluindo advertências e contraindicações
- Complementar os dados do mecanismo de ação a partir do DrugBank
- Aguardar os resultados do ensaio NCT05540834 e confirmar sua população e desenho
- Realizar revisão sistemática ou estudos controlados em trombofilia, com avaliação específica do risco de sangramento
- Definir se subtipos de infarto devem ser tratados como indicações já cobertas, em vez de novas indicações
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

