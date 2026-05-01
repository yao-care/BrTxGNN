---
layout: default
title: Norethisterone
parent: 僅模型預測 (L5)
nav_order: 362
evidence_level: L5
indication_count: 1
---

# Norethisterone
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

Using `txgnn-pipeline` to confirm context — this is a BrTxGNN report generation task. The skill confirms the standard pipeline; the detailed report format is defined in the system prompt. Proceeding directly to the report.

---

# Norethisterone: Da contracepção hormonal à amenorreia

## Resumo em Uma Frase

Norethisterone é um progestogênio sintético classicamente utilizado na contracepção hormonal combinada e na terapia de reposição hormonal.
O modelo TxGNN prevê que pode ser eficaz para **Amenorreia (Amenorrhea)**, indicação com estreita relação mecanística ao seu modo de ação sobre o eixo hipotálamo-hipófise-ovário,
atualmente com **8 ensaios clínicos** e **20 publicações** apoiando esta direção.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Contracepção hormonal; regulação do ciclo menstrual |
| Nova Indicação Prevista | Amenorreia (Amenorrhea) |
| Pontuação de Previsão TxGNN | 99.60% |
| Nível de Evidência | L2 |
| Situação no Mercado Brasileiro | ✗ Não comercializado no Brasil |
| Número de Registros | 0 |
| Decisão Recomendada | Proceed with Guardrails |

---

## Por que Esta Previsão é Razoável?

Norethisterone é um progestogênio sintético de 19-nortestosterona que se liga seletivamente aos receptores de progesterona do endométrio, suprimindo a proliferação endometrial cíclica e inibindo os picos de LH e FSH hipofisários. Ao estabilizar o endométrio e suprimir a ovulação, o fármaco é farmacologicamente capaz tanto de cessar o sangramento menstrual (em doses contínuas) quanto de provocar sangramento de privação (quando suspenso após uso periódico). O modelo TxGNN capturou exatamente essa conexão no grafo de conhecimento: **progestogênio → regulação endometrial → amenorreia**, resultando em uma pontuação elevada de 0.996.

A relação entre a indicação original (contracepção hormonal) e a nova indicação prevista (amenorreia) é direta e clinicamente bem reconhecida. Em amenorreia secundária, o norethisterone é empregado no **teste de provocação progestagênica** (*progestogen challenge test*): a administração por 10 dias seguida de sangramento de privação confirma a presença de estrogenização endometrial adequada e exclui falha de saída uterina. Em amenorreia hipoestrôgenica, pode ainda ser prescrito em ciclos periódicos para proteção endometrial e indução de ciclicidade artificial.

Adicionalmente, norethisterone acetate (NETA) figura como componente ativo das combinações aprovadas Ryeqo/Myfembree (relugolix + estradiol + NETA), em que o controle do padrão menstrual — incluindo indução de amenorreia durante a fase de supressão de GnRH — é um dos desfechos primários dos ensaios pivotais LIBERTY 1 e LIBERTY 2. Esta participação direta em ensaios Phase 3 concluídos reforça a plausibilidade mecanística e clínica da previsão do modelo.

---

## Evidências de Ensaios Clínicos

| Número do Ensaio | Fase | Status | Participantes | Principais Achados |
|---------|------|------|------|---------|
| [NCT06953076](https://clinicaltrials.gov/study/NCT06953076) | N/A | Recrutando | 111 | MySaturn Study: avaliação de transformações morfológicas de fibromas uterinos por ultrassom durante tratamento com relugolix + estradiol + norethisterone; norethisterone incluído como componente direto |
| [NCT01441635](https://clinicaltrials.gov/study/NCT01441635) | Phase 2 | Concluído | 271 | Elagolix versus placebo para redução de sangramento uterino e volume de fibromas em mulheres pré-menopáusicas; norethisterone envolvido como possível add-back |
| [NCT05620355](https://clinicaltrials.gov/study/NCT05620355) | Phase 3 | Desconhecido | 312 | BG2109 isolado ou combinado com add-back (incluindo norethisterone) para sangramento menstrual intenso associado a fibromas; status de conclusão incerto |
| [NCT01817530](https://clinicaltrials.gov/study/NCT01817530) | Phase 2b | Concluído | 571 | Elagolix ± add-back versus placebo em mulheres com fibromas e sangramento intenso; amenorreia avaliada como desfecho secundário de eficácia |
| [NCT03751124](https://clinicaltrials.gov/study/NCT03751124) | Phase 3 | Concluído | 229 | Estudo de retirada aleatória de relugolix + estradiol + norethisterone acetate por até 104 semanas; amenorreia como desfecho de eficácia direto da combinação |
| [NCT03049735](https://clinicaltrials.gov/study/NCT03049735) | Phase 3 | Concluído | 388 | LIBERTY 1: relugolix ± estradiol + norethisterone acetate versus placebo por 24 semanas; norethisterone como componente direto da terapia combinada aprovada |
| [NCT03103087](https://clinicaltrials.gov/study/NCT03103087) | Phase 3 | Concluído | 382 | LIBERTY 2: confirmação independente de LIBERTY 1, mesmo desenho; norethisterone no controle de amenorreia induzida por supressão de GnRH |
| [NCT03412890](https://clinicaltrials.gov/study/NCT03412890) | Phase 3 | Concluído | 477 | LIBERTY EXTENSION: extensão aberta de 28 semanas avaliando eficácia e segurança sustentadas de relugolix + estradiol + norethisterone em participantes das fases pivotais |

---

## Evidências da Literatura

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [37863160](https://pubmed.ncbi.nlm.nih.gov/37863160/) | 2024 | RCT Subgrupo | Am J Obstet Gynecol | LIBERTY Long-Term Extension: relugolix + estradiol + norethisterone acetate (40/1/0,5 mg/dia) reduziu substancialmente sangramento intenso em mulheres negras/afro-americanas ao longo de 52 semanas; norethisterone como componente ativo |
| [41489365](https://pubmed.ncbi.nlm.nih.gov/41489365/) | 2026 | Análise Secundária RCT | Biol Reprod | Estudo secundário do WHICH Trial (521 mulheres): NET-EN e DMPA-IM suprimem igualmente o estradiol, mas DMPA-IM induz mais amenorreia; norethisterone enantato associado a menor taxa de amenorreia, confirmando ação diferencial no eixo HPO |
| [38530848](https://pubmed.ncbi.nlm.nih.gov/38530848/) | 2024 | RCT (WHICH) | PLoS One | WHICH Trial randomizado: NET-EN versus DMPA-IM — efeitos sobre estradiol, depressão, atividade sexual e padrão menstrual; dados diretos sobre amenorreia induzida por norethisterone enantato |
| [6786825](https://pubmed.ncbi.nlm.nih.gov/6786825/) | 1981 | Ensaio Fase I | Contraception | Ensaio Fase I (20 mulheres): norethisterone enantato injetável e norethisterone acetate minipílula aboliram completamente os picos de LH/FSH; amenorreia, spotting e irregularidades menstruais documentadas como efeitos do tratamento |
| [23641480](https://pubmed.ncbi.nlm.nih.gov/23641480/) | 2013 | Revisão Cochrane | Cochrane Database Syst Rev | Contracepção injetável combinada (incluindo preparações com norethisterone): método altamente eficaz e reversível, com aceitabilidade limitada por alterações no padrão de sangramento, incluindo amenorreia |
| [18843662](https://pubmed.ncbi.nlm.nih.gov/18843662/) | 2008 | Revisão Cochrane | Cochrane Database Syst Rev | Revisão Cochrane anterior sobre contracepção injetável combinada; descreve impacto no ciclo menstrual e incidência de amenorreia como efeito de classe dos progestogênios injetáveis |
| [37103532](https://pubmed.ncbi.nlm.nih.gov/37103532/) | 2023 | Revisão | Obstet Gynecol | Antagonistas orais de GnRH co-administrados com hormônios em dose de reposição (incluindo norethisterone): revisão de eficácia e segurança em leiomiomas uterinos; supressão menstrual como desfecho chave |
| [2660092](https://pubmed.ncbi.nlm.nih.gov/2660092/) | 1989 | Revisão | Pediatr Clin North Am | Princípios da contracepção hormonal em adolescentes; mecanismo de ação dos progestogênios (incluindo norethisterone) sobre o eixo HPO e ciclo menstrual |
| [12335903](https://pubmed.ncbi.nlm.nih.gov/12335903/) | 1979 | Revisão | Contracept Fertil Sex | Endometriose e infertilidade: papel dos progestogênios na supressão hormonal e amenorreia terapêutica |
| [4596680](https://pubmed.ncbi.nlm.nih.gov/4596680/) | 1974 | Revisão | Clin Obstet Gynecol | Esteroides contraceptivos e DIU: papel dos progestogênios sintéticos no controle do ciclo menstrual e amenorreia induzida |

---

## Informações de Comercialização no Brasil

Norethisterone **não possui registros ativos na ANVISA** e não está comercializado no Brasil de forma independente (market status: não comercializado; total de registros: 0).

> **Nota regulatória:** Formulações combinadas contendo norethisterone acetate aprovadas internacionalmente (ex.: Ryeqo/Myfembree) ainda não possuem registro no Brasil. Qualquer uso clínico requereria processo regulatório específico junto à ANVISA.

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Proceed with Guardrails**

**Justificativa:**
Norethisterone possui mecanismo de ação diretamente vinculado à regulação do ciclo menstrual e à amenorreia — esta previsão do TxGNN não representa um reposicionamento disruptivo, mas a formalização clínica de um uso farmacologicamente fundamentado e parcialmente documentado em ensaios Phase 3 concluídos (LIBERTY 1, LIBERTY 2, extensões). O principal obstáculo não é a plausibilidade científica, mas a ausência de registro no Brasil e a lacuna de dados de segurança formais na base consultada.

**Para prosseguir, é necessário:**
- Iniciar processo de registro na ANVISA (o fármaco não possui qualquer registro vigente no Brasil)
- Obter e analisar a bula oficial (advertências, contraindicações, interações medicamentosas)
- Definir a subcategoria de amenorreia a ser investigada: primária, secundária funcional ou induzida por supressão de GnRH
- Avaliar as vias de administração disponíveis internacionalmente (oral, injetável de longa duração — NET-EN) e sua adequação ao contexto clínico brasileiro
- Consultar especialistas em ginecologia endocrinológica para validação de protocolo e definição de critérios de inclusão/exclusão
---

