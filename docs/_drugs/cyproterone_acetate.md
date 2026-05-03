---
layout: default
title: Cyproterone Acetate
parent: 僅模型預測 (L5)
nav_order: 206
evidence_level: L5
indication_count: 10
---

# Cyproterone Acetate
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

A skill `txgnn-pipeline` foi carregada. Agora vou gerar o relatório de avaliação completo com base no Evidence Pack fornecido.

---

# Acetato de Ciproterona: Do Hiperandrogenismo à Enxaqueca

## Resumo em Uma Frase

O acetato de ciproterona (CPA) é um antiandrogênio esteroidal e progestagênio, estabelecido internacionalmente para o tratamento do hiperandrogenismo feminino (PCOS, hirsutismo) e do câncer de próstata avançado, porém **sem nenhum registro vigente no Brasil (ANVISA)**.
O modelo TxGNN prevê que pode ser eficaz para **Enxaqueca (Migraine Disorder)**, com base em sua atividade neuroendócrina sobre o eixo hormonal-trigeminovascular,
atualmente com **0 ensaios clínicos** e **3 publicações** apoiando esta direção.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|----------|
| Indicação Original | Não registrado no Brasil — uso internacional estabelecido: hiperandrogenismo, PCOS, câncer de próstata |
| Nova Indicação Prevista | Enxaqueca (Migraine Disorder) |
| Pontuação de Previsão TxGNN | 99,66% |
| Nível de Evidência | L4 |
| Situação no Mercado Brasileiro | Não comercializado |
| Número de Registros ANVISA | 0 |
| Decisão Recomendada | Hold |

---

## Por que Esta Previsão é Razoável?

Não há dados de mecanismo de ação (MOA) disponíveis na base de dados atual para o CPA. Com base em informações conhecidas, o acetato de ciproterona é um antiandrogênio esteroidal de ação dual: bloqueia receptores androgênicos nos tecidos-alvo e suprime a secreção de LH/FSH pelo eixo hipotálamo-hipófise-gonadal. Adicionalmente, o CPA exerce efeitos neuroativos por meio de metabólitos que interagem com receptores GABA-A (mecanismo análogo ao da alopregnanolona), aumenta respostas dopaminérgicas no estriado e se liga a receptores opioides de forma independente de sua atividade antiandrogênica clássica.

A ligação teórica com enxaqueca parte do papel central das flutuações hormonais na fisiopatologia migranosa feminina: a enxaqueca menstrual e as variações cíclicas de progesterona/estrogênio são fenômenos bem documentados. Como análogo progestagênico potente, o CPA poderia estabilizar essas flutuações ao longo do ciclo e, via modulação GABAérgica, influenciar o limiar de excitabilidade do sistema trigeminovascular responsável pelas crises. Este raciocínio é consistente com o nó de conhecimento que conecta hormônios esteroidais ao grafo de suscetibilidade migranosa no modelo TxGNN.

Contudo, a evidência disponível não sustenta o CPA como agente terapêutico direto para enxaqueca. As três publicações identificadas tratam de efeitos gerais de progestagênios no SNC ou reportam que terapias hormonais combinadas têm impacto **bifásico** na enxaqueca — podendo tanto melhorar quanto agravar a condição — sem estudos de intervenção desenhados para avaliar CPA como tratamento migranoso. A previsão TxGNN expressa uma associação estrutural no grafo de conhecimento, não uma eficácia clínica verificada.

> ⚠️ **Alerta Crítico de Segurança:** A 2ª indicação prevista pelo TxGNN (enxaqueca com aura do tronco encefálico, rank 2) é uma **contraindicação documentada** para o uso de CPA combinado com etinilestradiol (Diane-35), conforme diretrizes internacionais (CNGOF, OMS) — pelo risco aumentado de AVC isquêmico. Este achado reforça a necessidade de cautela antes de qualquer exploração de CPA em cenários migranosos.

---

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados para CPA na indicação de enxaqueca.

---

## Evidências da Literatura

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|-----------|-------------------|
| [12390622](https://pubmed.ncbi.nlm.nih.gov/12390622/) | 2002 | Clinical Study | *Headache* | Avalia 3 esquemas de TRH oral (incluindo combinação progestagênica) na enxaqueca pós-menopausa; demonstra que o tipo e regime progestagênico influenciam diferentemente o curso das crises migranosas |
| [14670648](https://pubmed.ncbi.nlm.nih.gov/14670648/) | 2003 | Review | *Maturitas* | Descreve interações de progestagênios (incluindo CPA) com receptores GABA-A, dopamina e opioides, fornecendo a principal base mecanística para efeitos neuroativos do CPA relevantes à fisiopatologia da enxaqueca |
| [10857213](https://pubmed.ncbi.nlm.nih.gov/10857213/) | 2000 | Retrospective Study | *Zentralbl. Gynakol.* | Estudo multicêntrico com 2.506 pacientes (7.971 pacientes-ano) em uso de CPA; avalia efeitos adversos de longo prazo e potencial mutagênico; não foca em enxaqueca, mas documenta o perfil de segurança geral do CPA em doses contínuas baixas |

---

## Informações de Comercialização no Brasil

O acetato de ciproterona não possui nenhum registro ativo na ANVISA e não é comercializado no Brasil. Nenhum produto com este fármaco como componente ativo foi localizado na base de dados regulatória brasileira.

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

> **Nota baseada nas evidências coletadas neste Evidence Pack:** A literatura identificada para as demais indicações previstas pelo TxGNN aponta os seguintes sinais de segurança com relevância clínica para o CPA:
>
> - **Risco tromboembólico:** CPA — especialmente em combinação com etinilestradiol — aumenta significativamente o risco de TVP, TEP e eventos arteriais (AVC, IAM). Dados de farmacovigilância francesa ([PMID 24634164](https://pubmed.ncbi.nlm.nih.gov/24634164/)) e diretrizes CNGOF ([PMID 30389542](https://pubmed.ncbi.nlm.nih.gov/30389542/)) confirmam este risco.
> - **Interação com trombofilias hereditárias:** A combinação CPA+EE com mutação de Fator V de Leiden ou deficiência de proteína S amplifica consideravelmente o risco de TVP ([PMID 29614525](https://pubmed.ncbi.nlm.nih.gov/29614525/)).
> - **Contraindicação em enxaqueca com aura:** O uso de CPA+EE é contraindicado em mulheres com enxaqueca com aura (inclusive com aura do tronco encefálico) pelo risco de AVC isquêmico, conforme diretrizes CNGOF e OMS ([PMID 30389542](https://pubmed.ncbi.nlm.nih.gov/30389542/)).

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
Apesar da alta pontuação TxGNN (99,66%), a evidência disponível para enxaqueca é insuficiente e o perfil de segurança do CPA é problemático neste contexto: nenhum ensaio clínico registrado, publicações sem estudos de intervenção direta com CPA para enxaqueca, e o fato de que a enxaqueca com aura — subgrupo muito prevalente — constitui contraindicação documentada para formulações contendo CPA. Adicionalmente, o CPA não possui registro na ANVISA, criando uma barreira regulatória primária para qualquer uso no Brasil.

> **Nota sobre indicação alternativa com evidência mais robusta:** No presente Evidence Pack, a indicação **amenorreia/PCOS (rank 8)** apresenta nível de evidência **L2** (4 ensaios clínicos, incluindo Phase 4 direto com CPA+EE) e recomendação *Research Question* — sendo esta a direção com maior potencial de exploração na perspectiva de reposicionamento ou regularização no Brasil.

**Para prosseguir (enxaqueca), é necessário:**
- Obtenção de dados completos de MOA, advertências, contraindicações e DDI (bula internacional ou DrugBank API — DG001 e DG002 identificados como lacunas bloqueantes)
- Processo de registro ou importação excepcional junto à ANVISA
- Estudos de mecanismo específicos sobre CPA monodrogas (sem EE) e modulação trigeminal
- Estratificação obrigatória por subtipo de enxaqueca (com ou sem aura) antes de qualquer protocolo, dado o risco de AVC em portadoras de enxaqueca com aura
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

