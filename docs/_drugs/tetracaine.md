---
layout: default
title: Tetracaine
parent: Apenas Predição do Modelo (L5)
nav_order: 624
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-28
description: "Tetracaine: nova indicação prevista, Acrodermatite crônica atrófica (acrodermatitis chronica atrophicans) (nível de evidência L5). Indicação original: Anestésicos locais"
monitor_inn: "TETRACAINE"
predicted_indications: ["acrodermatitis chronica atrophicans", "neonatal dermatomyositis", "bronchitis", "secondary interstitial lung disease specific to childhood associated with a connective tissue disease", "acne keloid", "hydroa vacciniforme, familial", "amyopathic dermatomyositis", "cauda equina syndrome", "irritable bowel syndrome"]
---

# Tetracaine
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

## Tetracaína: Do anestésico local à Acrodermatite Crônica Atrófica? (previsão sem respaldo)
{: .text-alpha }

> Observação: o relatório avalia a previsão de maior pontuação do TxGNN (acrodermatite crônica atrófica). Também comenta a única indicação com estudos relacionados (acne queloidiana) e o caso de segurança da síndrome da cauda equina.

## Resumo em Uma Frase

Tetracaína é um anestésico local do tipo éster, originalmente usado em anestesia local, em antissépticos tópicos para orofaringe e em associações com glicocorticoides tópicos.
O modelo TxGNN prevê que pode ser eficaz para **acrodermatite crônica atrófica (acrodermatitis chronica atrophicans)**, mas **não há ensaios clínicos nem publicações** que apoiem essa previsão. Trata-se de uma previsão puramente computacional.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Anestésicos locais |
| Nova Indicação Prevista | Acrodermatite crônica atrófica (acrodermatitis chronica atrophicans) |
| Pontuação de Previsão TxGNN | 0,9993 |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | Comercializado (registros ativos: 5 de 5) |
| Número de Registros | 5 (ativos: 5) |
| Decisão Recomendada | Hold |

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação nos dados compilados para este relatório. Segundo informações conhecidas, a tetracaína é um anestésico local do tipo éster que bloqueia canais de sódio dependentes de voltagem, e sua eficácia como anestésico local está estabelecida.

A acrodermatite crônica atrófica é uma manifestação dermatológica tardia da infecção por *Borrelia* (doença de Lyme). O bloqueio de canais de sódio não tem papel antimicrobiano nem modificador da doença. **Não foi identificado vínculo mecanístico plausível**: a pontuação alta vem do modelo TxGNN (deep learning) e pode refletir semelhanças que o modelo aprendeu entre doenças relacionadas, não evidência biológica.

As demais previsões de topo seguem o mesmo padrão e não têm respaldo clínico:

- **Dermatomiosite neonatal e dermatomiosite amiopática**: doenças autoimunes que a tetracaína não trata. Além disso, o uso em neonatos levanta preocupações de segurança.
- **Bronquite**: vínculo fraco e indireto. Anestésicos tópicos suprimem a tosse (sintoma), mas não tratam a doença.
- **Doença pulmonar intersticial secundária da infância associada a doença do tecido conjuntivo**: sem vínculo plausível.
- **Hidroa vaciniforme familiar**: sem atividade fotoprotetora, antiviral ou imunomoduladora.
- **Síndrome do intestino irritável**: hipótese especulativa (hipersensibilidade visceral), sem estudos.

## Evidências de Ensaios Clínicos

Para a indicação principal (acrodermatite crônica atrófica), atualmente não há ensaios clínicos relacionados registrados.

Entre as outras previsões, há um ensaio relacionado à acne queloidiana (rank 5), de relevância apenas indireta:

| Número do Ensaio | Fase | Status | Participantes | Principais Achados |
|---------|------|------|------|---------|
| [NCT02372786](https://clinicaltrials.gov/study/NCT02372786) | Phase 4 | Concluído | 30 | Creme de lidocaína 7%/tetracaína 7% vs. lidocaína 2,5%/prilocaína 2,5% para dor durante laser em acne queloidiana da nuca e remoção de tatuagem. Avalia analgesia do procedimento, não tratamento da doença. |

## Evidências da Literatura

Para a indicação principal, atualmente não há literatura relacionada.

Literatura das outras previsões (selecionada, priorizando RCT, depois revisões e relatos de caso):

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [27377616](https://pubmed.ncbi.nlm.nih.gov/27377616/) | 2017 | RCT | Br J Dermatol | Comparação de creme lidocaína/tetracaína vs. lidocaína/prilocaína para anestesia em laser de acne queloidiana da nuca e remoção de tatuagem (anestesia do procedimento) |
| [9033758](https://pubmed.ncbi.nlm.nih.gov/9033758/) | 1996 | Revisão | Ann Fr Anesth Reanim | Neurotoxicidade de agentes administrados por via intratecal |
| [10876464](https://pubmed.ncbi.nlm.nih.gov/10876464/) | 2000 | Revisão | AANA J | Sintomas neurológicos transitórios e raquianestesia |
| [30625770](https://pubmed.ncbi.nlm.nih.gov/30625770/) | 2009 | Relato de caso | Korean J Anesthesiol | Síndrome da cauda equina após raquianestesia com tetracaína hiperbárica 0,5% com epinefrina |
| [11685003](https://pubmed.ncbi.nlm.nih.gov/11685003/) | 2001 | Relato de caso | Anesthesiology | Síndrome da cauda equina após tetracaína espinhal, com acompanhamento eletromiográfico de 20 anos |
| [8982894](https://pubmed.ncbi.nlm.nih.gov/8982894/) | 1996 | Relato de caso | J Clin Anesth | Lesão do cone medular após raquianestesia com tetracaína e lidocaína |
| [20739341](https://pubmed.ncbi.nlm.nih.gov/20739341/) | 2010 | Relato de caso | Br J Radiol | Realce da cauda equina por gadolínio após anestesia combinada raquidiana-peridural |
| [8017646](https://pubmed.ncbi.nlm.nih.gov/8017646/) | 1994 | Pré-clínico | Anesthesiology | Bloqueio de condução irreversível em nervo isolado por altas concentrações de anestésicos locais |
| [8024139](https://pubmed.ncbi.nlm.nih.gov/8024139/) | 1994 | Pré-clínico (animal) | Anesthesiology | Déficit sensorial sacral persistente após infusão intratecal de anestésico local em ratos |

**Atenção:** a literatura sobre síndrome da cauda equina descreve a tetracaína como **causa** (neurotoxicidade após uso espinhal/intratecal), não como tratamento. A pontuação alta do modelo provavelmente reflete essa relação de evento adverso e não é um sinal de reposicionamento. Essa direção seria contraindicada por segurança.

## Informações de Comercialização no Brasil

Os 5 registros estão válidos; o medicamento é comercializado.

| Número de Registro | Nome Comercial | Forma Farmacêutica | Indicação Aprovada |
|---------|------|------|-----------|
| Registro 101430075 | Pliaglis | Não informada | Anestésicos locais |
| Registro 102980565 | Skincaine | Não informada | Anestésicos locais |
| Registro 178170933 | Hexomedine | Não informada | Antiinfecciosos e antissépticos tópicos para orofaringe |
| Registro 102980552 | Lidocaína + Tetracaína | Não informada | Anestésicos locais |
| Registro 103900162 | Oto Betnovate | Não informada | Glicocorticoides tópicos – associação medicamentosa |

## Considerações de Segurança

- **Contraindicações previstas pelo grafo de conhecimento** (relações do grafo TxGNN/PrimeKG, não texto de bula): epilepsia, doença renal, doença hepática, doença da vesícula biliar, doença cardíaca e cardiovascular, parada cardíaca súbita, doença do sistema de condução cardíaco, insuficiência respiratória, miastenia gravis (inclusive de início na idade adulta), doença da junção neuromuscular, deficiência de butirilcolinesterase, hipertireoidismo, doença de Graves, tireotoxicose, uveíte, doenças da íris e do corpo ciliar, panuveíte, doenças infecciosas oculares e conjuntivite.
- **Interações medicamentosas** (32 registradas; principais):
  - **Maior gravidade:** ácido nitroso e bupivacaína lipossomal.
  - **Moderada:** sulfassalazina e sulfametoxazol; outros anestésicos (lidocaína tópica e oftálmica, benzocaína, cocaína tópica e nasal, proparacaína, oxibuprocaína, cinchocaína); benzodiazepínicos (alprazolam, clordiazepóxido, clobazam, clonazepam, ácido clorazépico, diazepam, estazolam).
  - **Menor:** hialuronidase.
- **Risco neurológico:** casos de síndrome da cauda equina e lesão do cone medular após uso espinhal/intratecal.
- **Neonatos:** o uso de anestésico tópico ou espinhal em neonatos exige cautela (relevante para a previsão de dermatomiosite neonatal).

As advertências e contraindicações da bula da ANVISA não estavam disponíveis nos dados compilados; consulte a bula para informações completas de segurança.

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
- A previsão principal tem pontuação alta (0,9993), mas está no nível L5: não há ensaios, literatura nem vínculo mecanístico plausível. O único estudo relacionado (acne queloidiana) avalia analgesia de procedimento, já alinhada à indicação original, e não configura reposicionamento. Os 5 registros brasileiros estão válidos e o medicamento é comercializado.

**Para prosseguir, é necessário:**
- Obter e analisar a bula da ANVISA (advertências e contraindicações), pois a ausência desses dados bloqueia a triagem de segurança.
- Consultar o mecanismo de ação detalhado no DrugBank.
- Apresentar uma hipótese mecanística plausível e evidência pré-clínica antes de qualquer investimento clínico.
- Definir a via de administração compatível com a nova indicação e avaliar sua viabilidade regulatória, já que não há registro válido no Brasil.
- Descartar a síndrome da cauda equina como alvo terapêutico, por refletir um evento adverso.
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

