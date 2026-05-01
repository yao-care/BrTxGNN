---
layout: default
title: Levothyroxine
parent: 僅模型預測 (L5)
nav_order: 321
evidence_level: L5
indication_count: 10
---

# Levothyroxine
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

# Levothyroxine: Da Hipotireoidismo ao Bócio Endêmico

## Resumo em Uma Frase

Levothyroxine (L-tiroxina sintética, T4) é amplamente utilizado no tratamento da hipotireoidismo como terapia de reposição hormonal tireoidiana, bem como na supressão pós-operatória do TSH em neoplasias tireoidanas.
O modelo TxGNN prevê que pode ser eficaz para **Bócio Endêmico (Endemic Goiter)**, atualmente com **1 ensaio clínico** e **20 publicações** apoiando esta direção.
O mecanismo de supressão do TSH pelo T4 exógeno é biologicamente plausível para reduzir o estímulo proliferativo sobre o tecido tireoidiano hipertrofiado por deficiência crônica de iodo.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Hipotireoidismo (reposição de hormônio tireoidiano) |
| Nova Indicação Prevista | Bócio Endêmico (Endemic Goiter) |
| Pontuação de Previsão TxGNN | 99.81% |
| Nível de Evidência | L3 |
| Situação no Mercado Brasileiro | ✗ Não Comercializado (0 registros identificados) |
| Número de Registros | 0 |
| Decisão Recomendada | Proceed with Guardrails |

---

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação disponíveis neste pacote de evidências. Com base em conhecimento farmacológico estabelecido, Levothyroxine é a forma sintética do hormônio T4, que após absorção oral é convertido perifericamente em T3 (forma biologicamente ativa), exercendo efeitos metabólicos sistêmicos sobre múltiplos tecidos. A característica central do seu uso clínico é a capacidade de modular o eixo hipotálamo-hipófise-tireoide por retroalimentação negativa.

O bócio endêmico tem como principal causa a deficiência crônica de iodo: sem substrato suficiente para sintetizar T4 e T3, os níveis hormonais caem, o que desencadeia elevação compensatória do TSH (hormônio estimulante da tireoide). O TSH elevado estimula continuamente a proliferação das células foliculares tireoidanas, resultando no aumento progressivo da glândula. A **terapia supressiva com Levothyroxine** interrompe esse ciclo: ao fornecer T4 exógeno, ativa o feedback negativo hipofisário, suprime a secreção de TSH e elimina o principal sinal de crescimento sobre o parênquima aumentado.

Um estudo multicêntrico alemão (Pfannenstiel, 1988 — PMID 3278876) documentou diretamente essa eficácia: 74 pacientes com bócio difuso endêmico eutireoidiano foram tratados por 6 meses com 150 µg/dia de Levothyroxine (isolado ou combinado com iodeto de potássio), obtendo redução volumétrica significativa do bócio em ambos os grupos. É importante destacar que as diretrizes internacionais posicionam a **suplementação de iodo como intervenção de primeira linha** no bócio endêmico; o Levothyroxine é indicado como tratamento adjuvante ou alternativa em contextos onde a reposição de iodo é insuficiente, inviável ou já foi realizada sem resposta completa.

---

## Evidências de Ensaios Clínicos

| Número do Ensaio | Fase | Status | Participantes | Principais Achados |
|---------|------|------|------|---------|
| [NCT04482907](https://clinicaltrials.gov/study/NCT04482907) | N/A | Concluído | 68 | Estudo placebo-controlado de Anethum graveolens (endro) em pacientes com tireoidite e bócio nodular, avaliando níveis hormonais e tamanho de nódulos por ultrassonografia ao longo de 90 dias. Levothyroxine não é o fármaco investigado — oferece contexto sobre a população-alvo com bócio nodular/endêmico, mas sem contribuição direta à eficácia do LT4. |

---

## Evidências da Literatura

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [3278876](https://pubmed.ncbi.nlm.nih.gov/3278876/) | 1988 | Estudo Multicêntrico (Intervenção) | Deutsche Med. Wochenschrift | 74 pacientes com bócio difuso endêmico eutireoidiano tratados por 6 meses com 150 µg/dia Levothyroxine (grupo I, n=35) ou combinação LT4+KI (grupo II, n=39); ambos obtiveram redução volumétrica significativa do bócio, com seguimento profilático adicional de 3 meses com iodeto |
| [2031356](https://pubmed.ncbi.nlm.nih.gov/2031356/) | 1991 | Review | World Journal of Surgery | Revisão abrangente sobre bócio endêmico; confirma papel central da deficiência de iodo, discute estratégias de suplementação e papel da terapia supressiva com hormônio tireoidiano em áreas onde a profilaxia com iodo enfrenta barreiras técnicas e socioeconômicas |
| [6304776](https://pubmed.ncbi.nlm.nih.gov/6304776/) | 1983 | Observacional/Fisiopatológico | Prog Clin Biol Res | TSH basal significativamente elevado (31 ± 8 µU/mL) em pacientes de área endêmica vs. controles normais (10 ± 4 µU/mL); correlação inversa entre ingestão de iodo e TSH sérico — embasamento fisiopatológico direto para a lógica da supressão de TSH com LT4 |
| [3090091](https://pubmed.ncbi.nlm.nih.gov/3090091/) | 1986 | Transversal | J Clin Endocrinol Metab | Análise de T4, T3, tireoglobulina e TSH em 1.218 sujeitos em área endêmica no norte da Itália (65% de prevalência de bócio); caracterização detalhada do perfil hormonal do bócio endêmico por deficiência moderada de iodo |
| [25629792](https://pubmed.ncbi.nlm.nih.gov/25629792/) | 2015 | RCT (suplementação de iodo) | Curr Med Res Opin | 460 gestantes em áreas endêmicas (grupos sem e com suplementação de iodo); suplementação melhorou parâmetros tireoidianos maternos e neonatais, reforçando a importância da correção do déficit hormonal tireoidiano nessa população |
| [263304](https://pubmed.ncbi.nlm.nih.gov/263304/) | 1978 | Observacional | J Clin Endocrinol Metab | Hipotireoidismo fetal documentado em área de bócio endêmico grave (Zaire); comparação entre grupos com e sem correção de iodo, demonstrando o impacto do déficit de T4 materno na função tireoidiana neonatal |
| [8121602](https://pubmed.ncbi.nlm.nih.gov/8121602/) | 1993 | Observacional | Minerva Ginecologica | 38 gestantes com bócio endêmico não tóxico; 10,5% (4 casos) utilizaram L-tiroxina (50–100 µg/dia) durante a gravidez; gravidez geralmente assintomática, com crescimento do bócio em 42% dos casos |
| [36839362](https://pubmed.ncbi.nlm.nih.gov/36839362/) | 2023 | Review | Nutrients | Atualização sobre deficiência de iodo e estratégias de profilaxia; abrange mecanismos de formação do bócio endêmico, requisitos de iodo por faixa etária e alternativas terapêuticas incluindo reposição hormonal |
| [6309889](https://pubmed.ncbi.nlm.nih.gov/6309889/) | 1983 | Observacional (intervenção) | J Clin Endocrinol Metab | Óleo iodado IM em 58 pacientes gregos com bócio por deficiência leve de iodo; redução do tamanho do bócio acompanhada de alterações em T4, T3 e TSH ao longo de 6 meses — descreve a dinâmica hormonal da remissão do bócio |
| [7704809](https://pubmed.ncbi.nlm.nih.gov/7704809/) | 1994 | Review | Curr Ther Endocrinol Metab | Revisão clínica sobre bócio endêmico — etiologia, diagnóstico diferencial e opções de tratamento, incluindo hormônio tireoidiano exógeno como abordagem terapêutica estabelecida |

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

> **Nota:** Os dados de advertências, contraindicações e interações medicamentosas não estavam disponíveis neste pacote de evidências. Para uso clínico ou avaliação regulatória, é imprescindível consultar a bula oficial e o perfil completo de segurança do Levothyroxine, especialmente quanto ao risco de **fibrilação atrial** e **osteoporose** associados à supressão excessiva do TSH em terapia de longo prazo.

---

## Conclusão e Próximos Passos

**Decisão: Proceed with Guardrails**

**Justificativa:**
O uso de Levothyroxine no bócio endêmico é mecanisticamente sólido (supressão de TSH → redução do estímulo proliferativo tireoidiano) e conta com suporte de estudos observacionais e ao menos um estudo multicêntrico de intervenção direta (PMID 3278876, 1988), classificando a evidência em **L3**. O principal guardrail é que a terapia supressiva com LT4 é coadjuvante — não substitui a suplementação de iodo — e exige monitoramento rigoroso de dose para evitar supressão excessiva de TSH.

**Para prosseguir, é necessário:**
- Verificar e atualizar o status de registro do Levothyroxine na ANVISA (os dados atuais indicam 0 registros, o que requer confirmação — Levothyroxine é fármaco essencial e deve ter registros vigentes)
- Obter o Mecanismo de Ação (MOA) completo via DrugBank (DB00451) para fundamentar a análise de relação mecanística
- Obter advertências e contraindicações da bula ANVISA (dados de segurança indisponíveis neste pacote)
- Definir critérios de seleção de pacientes: bócio endêmico refratário ou em contexto de inviabilidade da profilaxia com iodo
- Estabelecer metas de TSH seguras (supressão parcial: 0,1–0,5 mU/L vs. supressão total: < 0,1 mU/L) com base no risco cardiovascular e ósseo individual
- Avaliar prevalência de áreas endêmicas residuais no Brasil para dimensionar o potencial impacto desta indicação
---

