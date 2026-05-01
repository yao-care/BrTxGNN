---
layout: default
title: Colchicine
parent: 僅模型預測 (L5)
nav_order: 200
evidence_level: L5
indication_count: 3
---

# Colchicine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

O skill TxGNN Pipeline não fornece instruções específicas para geração de relatórios — o sistema prompt já contém o formato completo. Vou gerar o relatório diretamente com base no Evidence Pack.

---

# Colchicine: Da Gota à Malária por Plasmodium falciparum

## Resumo em Uma Frase

Colchicine é um alcaloide natural derivado do açafrão-dos-prados (*Colchicum autumnale*), classicamente utilizado no tratamento agudo da gota e como profilaxia da Febre Mediterrânea Familiar (FMF). O modelo TxGNN prevê que pode ser eficaz contra a **Malária por Plasmodium falciparum**, atualmente apoiada por **6 publicações científicas** — todas restritas a estudos *in vitro* ou básicos, sem nenhum ensaio clínico registrado nessa indicação.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Gota aguda / Febre Mediterrânea Familiar (FMF) |
| Nova Indicação Prevista | Malária por Plasmodium falciparum |
| Pontuação de Previsão TxGNN | 99,60% |
| Nível de Evidência | L4 (apenas estudos pré-clínicos) |
| Situação no Mercado Brasileiro | Não comercializado (sem registros ANVISA) |
| Número de Registros | 0 |
| Decisão Recomendada | Hold |

---

## Por que Esta Previsão é Razoável?

Colchicine liga-se com alta afinidade à subunidade β da tubulina no chamado **sítio de ligação da colchicine**, impedindo a polimerização dos microtúbulos e bloqueando a divisão celular na fase G2/M do ciclo mitótico. É esse mesmo mecanismo que explica sua ação anti-inflamatória: ao desestabilizar os microtúbulos de neutrófilos, inibe a migração, desgranulação e ativação do inflamassoma de pirina. Trata-se, portanto, de um fármaco cujo alvo molecular é a dinâmica dos microtúbulos em células eucarióticas.

O *Plasmodium falciparum* depende criticamente de um sistema de microtúbulos funcional em múltiplas etapas do seu ciclo de vida intraeritrocítico — incluindo a montagem do fuso mitótico durante a esquizogonia, a formação dos merozoítos e o desenvolvimento dos gametócitos. Compostos que interferem na dinâmica do citoesqueleto parasitário demonstraram atividade inibitória *in vitro*: o colcemid (análogo estrutural da colchicine) inibiu a síntese proteica em *P. falciparum* (PMID 2221861), e substâncias ligantes de tubulina mostraram atividade antimalárica experimental (PMIDs 2670249/2655935). Existe, portanto, uma base mecanística plausível para a previsão do modelo.

Contudo, há ressalvas importantes que justificam cautela: (1) as tubulinas do *P. falciparum* apresentam diferenças moleculares significativas em relação às de mamíferos, o que pode limitar a seletividade; (2) toda a evidência disponível data de estudos *in vitro* publicados entre 1984 e 2013, sem nenhum dado *in vivo* ou clínico; (3) a colchicine possui janela terapêutica estreita, o que impõe limitações sérias ao uso em doses antiparasitárias. O salto translacional da bancada para a clínica permanece completamente inexplorado.

---

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados para Colchicine em Malária por *Plasmodium falciparum*.

---

## Evidências da Literatura

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [2221861](https://pubmed.ncbi.nlm.nih.gov/2221861/) | 1990 | In vitro | Antimicrob Agents Chemother | Colcemid (análogo da colchicine) inibiu síntese proteica em *P. falciparum*, semelhante às tubulozolas; aponta o citoesqueleto parasitário como alvo relevante |
| [2670249](https://pubmed.ncbi.nlm.nih.gov/2670249/) | 1989 | In vitro | Cell Biol Int Rep | Nove compostos ligantes de tubulina testados contra desenvolvimento intraeritrocítico de *P. falciparum*; tubulinas do parasita diferem molecularmente das de mamíferos |
| [2655935](https://pubmed.ncbi.nlm.nih.gov/2655935/) | 1989 | In vitro | Cell Biol Int Rep | Mesmo experimento (possível publicação duplicada): compostos ligantes do citoesqueleto com atividade antimalárica *in vitro*; tubulozola-T destaque como candidato antimalarial |
| [23505424](https://pubmed.ncbi.nlm.nih.gov/23505424/) | 2013 | In vitro | PLoS ONE | Curcumina (outro ligante de tubulina) disrupta microtúbulos de *P. falciparum*; suporte indireto ao conceito de alvo tubulínico no parasita |
| [6362934](https://pubmed.ncbi.nlm.nih.gov/6362934/) | 1984 | Observacional | Clin Exp Immunol | 82% dos pacientes com malária aguda apresentavam anticorpos anti-filamentos intermediários do citoesqueleto; evidência de envolvimento imunológico do citoesqueleto na patogênese |
| [7511206](https://pubmed.ncbi.nlm.nih.gov/7511206/) | 1994 | Básico/Molecular | Mol Cell Biol | Estudo sobre pfmdr1 e resistência à cloroquina em *P. falciparum*; relevância periférica ao contexto de alvos moleculares no parasita |

---

## Informações de Comercialização no Brasil

Colchicine **não possui registros ativos na ANVISA** conforme dados disponíveis neste Evidence Pack. Não há licenças, formas farmacêuticas registradas ou indicações aprovadas no Brasil.

---

## Considerações de Segurança

Colchicine possui **estreita janela terapêutica**, sem distinção clara entre doses não tóxicas, tóxicas e letais. Consulte a bula oficial e as diretrizes clínicas vigentes para informações completas sobre advertências, contraindicações e interações medicamentosas antes de qualquer uso clínico.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
Toda a evidência disponível para colchicine em malária por *P. falciparum* se restringe a estudos *in vitro* publicados entre 1984 e 2013, sem nenhum ensaio clínico registrado e sem modelos *in vivo* publicados. O nível L4 de evidência, combinado com a janela terapêutica estreita do fármaco, é insuficiente para avançar sem dados experimentais adicionais. Ademais, a ausência de registro na ANVISA impõe barreira regulatória adicional para qualquer desenvolvimento clínico no Brasil.

> **⚠️ Achado paralelo de alta relevância:** A segunda indicação prevista pelo TxGNN — **Febre Mediterrânea Familiar (FMF)** — possui evidência de nível **L1**, com colchicine reconhecida globalmente como tratamento de primeira linha (grau A pelas diretrizes EULAR/ACR). Este achado deve ser priorizado em análises subsequentes.

**Para prosseguir com a indicação de malária, é necessário:**
- Estudos *in vivo* em modelos animais de *P. falciparum* para determinar eficácia e janela terapêutica segura
- Determinação da IC₅₀ da colchicine diretamente contra *P. falciparum* (separado dos dados de análogos estruturais como colcemid)
- Avaliação do risco de toxicidade sistêmica em doses antiparasitárias
- Obtenção do MOA completo via DrugBank API (gap DG002) e triagem de interações medicamentosas relevantes ao contexto de malária
- Regularização do registro na ANVISA caso se avance para estudos clínicos no Brasil
---

