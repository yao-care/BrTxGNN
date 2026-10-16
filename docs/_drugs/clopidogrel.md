---
layout: default
title: Clopidogrel
parent: Apenas Predição do Modelo (L5)
nav_order: 235
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Clopidogrel: nova indicação prevista, Enxaqueca com aura de tronco encefálico (migraine with brainstem aura) (nível de evidência L5). Indicação original: Síndrome coronariana aguda (embolia intracran…"
---

# Clopidogrel
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

# Clopidogrel: Da síndrome coronariana aguda à enxaqueca

## Resumo em Uma Frase

Clopidogrel é um antiagregante plaquetário (inibidor do receptor P2Y12), originalmente usado em **síndrome coronariana aguda**, embolia intracraniana e infarto do miocárdio com supradesnivelamento do segmento ST.
O modelo TxGNN prevê que pode ser eficaz para **enxaqueca com aura de tronco encefálico (migraine with brainstem aura)**, mas essa previsão específica não tem ensaios clínicos e conta com **15 publicações** de apoio, em sua maioria indiretas. A evidência mais consistente refere-se à **enxaqueca em geral (migraine disorder)**, a segunda previsão, com **6 ensaios clínicos** registrados e **22 publicações**, sobretudo em pacientes com forame oval patente (FOP) ou após fechamento de comunicação interatrial.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Síndrome coronariana aguda (embolia intracraniana e infarto do miocárdio com supra de ST também constam no grafo de conhecimento) |
| Nova Indicação Prevista | Enxaqueca com aura de tronco encefálico (migraine with brainstem aura) |
| Pontuação de Previsão TxGNN | 99,44% |
| Nível de Evidência | L2 (L5 se considerada estritamente a aura de tronco encefálico; a evidência de L2 vem da enxaqueca em geral/FOP) |
| Situação no Mercado Brasileiro | ✗ Não comercializado (segundo os dados compilados) |
| Número de Registros | 0 |
| Decisão Recomendada | Hold (previsão de aura de tronco encefálico); Proceed with Guardrails seria adequado apenas para a enxaqueca associada a FOP |

---

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação nos dados compilados. Segundo informações conhecidas, o clopidogrel é um pró-fármaco que bloqueia o receptor plaquetário P2Y12, reduzindo a agregação plaquetária. Sua eficácia na prevenção de eventos trombóticos em síndrome coronariana aguda e doença cerebrovascular está estabelecida.

A hipótese para a enxaqueca é que a ativação plaquetária e microêmbolos paradoxais (principalmente em pacientes com shunt direita-esquerda, como o FOP) liberariam mediadores vasoativos e serotoninérgicos capazes de desencadear a aura. Bloquear o P2Y12 poderia, portanto, reduzir esses eventos. Estudos pré-clínicos também sugerem participação do receptor P2Y12 em modelos de enxaqueca em camundongos.

Há um limite importante: a evidência concentra-se em enxaqueca com aura em populações com FOP ou após fechamento de comunicação interatrial. Nada específico foi estudado para a aura de tronco encefálico, e os dados não permitem afirmar eficácia na enxaqueca em geral.

---

## Evidências de Ensaios Clínicos

Não há ensaios registrados para a aura de tronco encefálico. Os ensaios abaixo referem-se à segunda previsão, **enxaqueca (migraine disorder)**, e são os mais relevantes para a direção terapêutica.

| Número do Ensaio | Fase | Status | Participantes | Principais Achados |
|---------|------|------|------|---------|
| [NCT05546320](https://clinicaltrials.gov/study/NCT05546320) | Phase 2 | Concluído | 1000 | COMPETE: compara anticoagulação, antiagregante plaquetário e medicação convencional para enxaqueca com FOP; resultados publicados (PMID 42526943) |
| [NCT00799045](https://clinicaltrials.gov/study/NCT00799045) | Phase 4 | Concluído | 220 | CANOA: clopidogrel somado à aspirina para prevenir enxaqueca de início recente após fechamento de comunicação interatrial |
| [NCT02938182](https://clinicaltrials.gov/study/NCT02938182) | Phase 4 | Desconhecido | 50 | Eficácia profilática do clopidogrel em enxaqueca com shunt direita-esquerda; pequeno e com situação incerta |
| [NCT04946734](https://clinicaltrials.gov/study/NCT04946734) | Phase 3 | Ativo, sem recrutamento | 440 | SPRING: fechamento de FOP versus medicação para enxaqueca; o dispositivo é a intervenção (relevância indireta) |
| [NCT00562289](https://clinicaltrials.gov/study/NCT00562289) | Phase 3 | Concluído | 664 | CLOSE: fechamento de FOP versus anticoagulantes versus antiagregantes na recorrência de AVC; enxaqueca não é o desfecho principal (indireto) |
| [NCT04100135](https://clinicaltrials.gov/study/NCT04100135) | NA | Encerrado | 7 | Estudo de dispositivo (oclusor GORE) para enxaqueca; encerrado com 7 participantes, sem dados úteis |

---

## Evidências da Literatura

Publicações mais relevantes (enxaqueca com aura/FOP e enxaqueca em geral):

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [42526943](https://pubmed.ncbi.nlm.nih.gov/42526943/) | 2026 | RCT | BMJ | Ensaio multicêntrico, randomizado e aberto sobre tratamento antitrombótico na prevenção de enxaqueca em pacientes com FOP (COMPETE) |
| [26551304](https://pubmed.ncbi.nlm.nih.gov/26551304/) | 2015 | RCT | JAMA | CANOA: clopidogrel + aspirina versus aspirina isolada após fechamento de comunicação interatrial |
| [32965476](https://pubmed.ncbi.nlm.nih.gov/32965476/) | 2021 | RCT | JAMA Cardiology | Resultados de 1 ano do CANOA, após a suspensão do clopidogrel aos 3 meses |
| [24836213](https://pubmed.ncbi.nlm.nih.gov/24836213/) | 2014 | RCT (piloto) | Cephalalgia | Estudo piloto randomizado do clopidogrel como profilaxia da enxaqueca |
| [39989443](https://pubmed.ncbi.nlm.nih.gov/39989443/) | 2025 | Revisão sistemática | Headache | Avalia o papel dos antitrombóticos na prevenção da enxaqueca |
| [40144614](https://pubmed.ncbi.nlm.nih.gov/40144614/) | 2025 | Revisão sistemática | Indian J Thorac Cardiovasc Surg | Incidência e manejo da cefaleia/enxaqueca de início recente após fechamento de comunicação interatrial |
| [32848048](https://pubmed.ncbi.nlm.nih.gov/32848048/) | 2020 | Coorte/observacional | J Investig Med | Clopidogrel 75 mg/dia como profilaxia complementar em enxaqueca refratária com FOP |
| [16103551](https://pubmed.ncbi.nlm.nih.gov/16103551/) | 2005 | Coorte/observacional | Heart | Clopidogrel reduziu enxaqueca com aura após fechamento de FOP e comunicação interatrial |
| [30478066](https://pubmed.ncbi.nlm.nih.gov/30478066/) | 2018 | Revisão retrospectiva | Neurology | Uso off-label de tienopiridinas em pacientes com enxaqueca e FOP |
| [30478067](https://pubmed.ncbi.nlm.nih.gov/30478067/) | 2018 | Piloto aberto | Neurology | Ticagrelor (mesma classe de inibidores P2Y12) em enxaqueca refratária com FOP |

---

## Informações de Comercialização no Brasil

Segundo os dados compilados, o clopidogrel consta como **não comercializado** e sem registros listados. Essa informação deve ser confirmada diretamente na ANVISA antes de qualquer decisão, pois contraria o esperado para um medicamento amplamente utilizado.

---

## Considerações de Segurança

- **Contraindicações (segundo o grafo de conhecimento, não a bula)**: insuficiência hepática aguda, hepatite, doenças da coagulação, lesões/traumatismos, púrpura trombocitopênica, úlcera péptica ativa e hemorragia intracraniana.
- **Interações medicamentosas**: foram identificadas 100 interações, sendo as principais de gravidade **maior**: omeprazol, esomeprazol, rabeprazol (inibição da ativação via CYP2C19), pioglitazona, repaglinida e loperamida. Entre as de gravidade moderada estão ácido acetilsalicílico (risco de sangramento), clopidogrel com cimetidina, claritromicina, bupropiona, morfina, lansoprazol e pantoprazol.
- **Riscos observados na literatura**: sangramento, inclusive hemorragia intracerebral com uso concomitante de AINEs, e hemartrose espontânea com a associação clopidogrel-aspirina.

As advertências e contraindicações da bula não estavam disponíveis nos dados compilados; consulte a bula aprovada pela ANVISA.

---

## Conclusão e Próximos Passos

**Decisão: Hold** (para a enxaqueca com aura de tronco encefálico)

**Justificativa:**
- A previsão específica tem pontuação alta (99,44%), mas não conta com ensaios clínicos nem com estudos dirigidos ao subtipo; a evidência vem de enxaqueca com aura/FOP e é extrapolada.
- Para a enxaqueca associada a FOP ou pós-fechamento de comunicação interatrial, há ensaios Phase 2/4 e o RCT do BMJ, o que sustentaria uma pergunta de pesquisa (nível L2). O nível L1 não é atribuído porque os ensaios Phase 3 tratam do fechamento de FOP, não do clopidogrel.

**Para prosseguir, é necessário:**
- Ler integralmente o RCT COMPETE (PMID 42526943) e os resultados do CANOA para avaliar a magnitude do efeito e a segurança.
- Obter o mecanismo de ação detalhado e as advertências/contraindicações da bula na ANVISA.
- Confirmar a situação regulatória no Brasil (registros e indicações aprovadas).
- Definir a população-alvo (enxaqueca com aura e shunt direita-esquerda) e avaliar o balanço risco-sangramento.
- Considerar um ensaio dirigido ao subtipo com aura de tronco encefálico, caso haja interesse nessa indicação específica.
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

