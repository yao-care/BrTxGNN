---
layout: default
title: Prasugrel
parent: Apenas Predição do Modelo (L5)
nav_order: 543
evidence_level: L5
indication_count: 10
---

# Prasugrel
{: .fs-9 }

Nível de evidência: **L5** | Indicações previstas: **10** 
{: .fs-6 .fw-300 }

---

## Índice
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Relatório de avaliação farmacêutica

</div>

# Prasugrel: Da síndrome coronariana aguda à hipertensão pulmonar

## Resumo em Uma Frase

Prasugrel é um antiagregante plaquetário (antagonista do receptor P2Y12), originalmente usado no tratamento da síndrome coronariana aguda.
O modelo TxGNN prevê que pode ser eficaz para **Hipertensão Pulmonar (Pulmonary Hypertension)**, mas atualmente há **0 ensaios clínicos** e **2 publicações** (que não tratam diretamente dessa doença) associados a esta previsão. A indicação com maior respaldo na literatura entre as previstas é a **enxaqueca**, discutida adiante.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Síndrome coronariana aguda (segundo o grafo de conhecimento do TxGNN; não há texto de indicação aprovado no Brasil) |
| Nova Indicação Prevista | Hipertensão Pulmonar (Pulmonary Hypertension) |
| Pontuação de Previsão TxGNN | 99,88% |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | Não comercializado |
| Número de Registros | 0 |
| Decisão Recomendada | Hold |

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação nos dados compilados. Segundo informações conhecidas, o prasugrel é um antagonista do receptor P2Y12 que inibe a agregação plaquetária, e sua eficácia na síndrome coronariana aguda é estabelecida.

Na hipertensão pulmonar, a ativação plaquetária e a trombose *in situ* contribuem para o remodelamento vascular pulmonar. Existe, portanto, um elo plausível, porém não comprovado, entre a ação antiplaquetária e a nova indicação.

A pontuação elevada do TxGNN é apenas uma previsão computacional. Os dois artigos recuperados tratam da adesão ao clopidogrel na síndrome coronariana aguda e do efeito de terapias prévias sobre a mortalidade por COVID-19; nenhum aborda a hipertensão pulmonar.

### Outras indicações previstas de interesse

- **Enxaqueca (rank 2, pontuação 99,88%, nível L3):** é a previsão com mais respaldo. A hipótese é que microêmbolos paradoxais ou mediadores derivados de plaquetas, em pessoas com forame oval patente (FOP), desencadeiem crises, e que inibidores de P2Y12 reduzam esses gatilhos. Há uma revisão retrospectiva de tienopiridinas em pacientes com enxaqueca e FOP e um piloto aberto com ticagrelor (mesma classe, não prasugrel). Os ensaios listados avaliam fechamento de FOP, não o prasugrel.
- **Enxaqueca com aura do tronco encefálico** (99,83%, L4) e **suscetibilidade à enxaqueca com ou sem aura** (99,67%, L4): apoio apenas indireto, por extrapolação dos estudos de enxaqueca com FOP. Para o segundo, há ainda um estudo pré-clínico de 2026 em camundongos (epilepsia induzida por pentilenotetrazol), que não modela enxaqueca.
- **Cardiopatia cifoescoliótica, artrite reumatoide, hipercolesterolemia familiar homozigótica, hipoalfalipoproteinemia, síndrome braquidactilia-sindactilia e hanseníase:** sem ensaios ou literatura, e sem mecanismo plausível ou com mecanismo muito frágil. São previsões puramente computacionais (L5).

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados para hipertensão pulmonar.

Para a enxaqueca (indicação alternativa), os registros encontrados foram:

| Número do Ensaio | Fase | Status | Participantes | Principais Achados |
|---------|------|------|------|---------|
| [NCT07629635](https://clinicaltrials.gov/study/NCT07629635) | Phase 3 | Recrutando | 32 | Terapia dirigida ao FOP para cessação de enxaqueca; o texto cita o prasugrel como medicamento antiplaquetário que reduziu crises em alguns pacientes. Não é evidência direta do fármaco; é preciso verificar se há braço antiplaquetário |
| [NCT04100135](https://clinicaltrials.gov/study/NCT04100135) | Não se aplica | Encerrado | 7 | Estudo de dispositivo (oclusor septal GORE® CARDIOFORM) para alívio da enxaqueca; não avalia prasugrel e traz evidência mínima |

## Evidências da Literatura

Para hipertensão pulmonar (artigos recuperados, sem relação direta com a doença):

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [21241206](https://pubmed.ncbi.nlm.nih.gov/21241206/) | 2011 | Coorte | Current Medical Research and Opinion | Fatores associados ao uso e à adesão ao clopidogrel em pacientes com síndrome coronariana aguda submetidos a ICP |
| [34713782](https://pubmed.ncbi.nlm.nih.gov/34713782/) | 2021 | Coorte | Kardiologiia | Influência da terapia prévia para comorbidades sobre o risco de morte por COVID-19 (registro ACTIV) |

Para enxaqueca (indicação alternativa):

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [30478066](https://pubmed.ncbi.nlm.nih.gov/30478066/) | 2018 | Coorte retrospectiva | Neurology | Revisão da experiência clínica com tienopiridinas (uso off-label) em pacientes com enxaqueca e FOP |
| [30478067](https://pubmed.ncbi.nlm.nih.gov/30478067/) | 2018 | Piloto aberto | Neurology | Ticagrelor em enxaqueca refratária com FOP; motivado pela redução dos sintomas com clopidogrel e prasugrel em alguns pacientes |
| [42722054](https://pubmed.ncbi.nlm.nih.gov/42722054/) | 2026 | Pré-clínico (camundongo) | European Journal of Pharmacology | Prasugrel com efeito neuroprotetor no modelo de epilepsia por pentilenotetrazol; não modela enxaqueca |

## Considerações de Segurança

- **Contraindicações segundo o grafo de conhecimento (não é texto de bula):** insuficiência hepática, distúrbios hipotensivos, doenças da coagulação, AVC e doenças cerebrovasculares, suscetibilidade a AVC isquêmico, infarto cerebral, lesões/traumatismos, púrpura trombocitopênica, hemorragia intracraniana, ataque isquêmico transitório e insuficiência vertebrobasilar.
- **Interações medicamentosas** (100 registradas; principais exemplos):
  - **Maior gravidade:** deferasirox e ibritumomabe tiuxetana.
  - **Moderada:** ácido acetilsalicílico, morfina, ópio, fenfluramina, dexfenfluramina e sibutramina.
  - **Leve:** inibidores de bomba de prótons (omeprazol, esomeprazol, pantoprazol, lansoprazol, dexlansoprazol, rabeprazol), antagonistas H2 (famotidina, ranitidina, cimetidina, nizatidina) e bupropiona.

Consulte a bula para advertências e contraindicações oficiais; o risco hemorrágico inerente a um antiplaquetário potente deve ser considerado em qualquer nova indicação.

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
- Para hipertensão pulmonar, a previsão é apenas computacional (L5), sem ensaios e com literatura não relacionada. O prasugrel não tem registro no Brasil, e a bula da ANVISA não foi obtida. A enxaqueca associada ao FOP é a direção mais promissora (L3), mas o apoio vem de estudos de classe, retrospectivos e pequenos, e pode ser tratada como pergunta de pesquisa.

**Para prosseguir, é necessário:**
- Obter e analisar a bula da ANVISA (advertências e contraindicações) e confirmar a situação regulatória do prasugrel no Brasil.
- Complementar os dados de mecanismo de ação (por exemplo, via DrugBank).
- Para hipertensão pulmonar: estudos pré-clínicos ou observacionais que sustentem o elo entre antagonismo de P2Y12 e remodelamento vascular pulmonar.
- Para enxaqueca: verificar se o NCT07629635 inclui braço antiplaquetário e extrair dados específicos do prasugrel na revisão retrospectiva (PMID 30478066).
- Avaliação do equilíbrio entre risco hemorrágico e benefício em populações sem doença coronariana.
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

