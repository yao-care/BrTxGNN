---
layout: default
title: Cyanocobalamin
parent: 僅模型預測 (L5)
nav_order: 202
evidence_level: L5
indication_count: 1
---

# Cyanocobalamin
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

A skill foi carregada. O contexto TxGNN não sobrepõe as instruções do prompt de relatório. Gerando o relatório agora com base no Evidence Pack fornecido.

---

# Cianocobalamina: Da deficiência de vitamina B12 à doença metabólica da biotina

## Resumo em Uma Frase

Cianocobalamina é a forma farmacêutica sintética da vitamina B12, classicamente utilizada no tratamento e prevenção da deficiência de cobalamina, incluindo anemia perniciosa e neuropatia associada.
O modelo TxGNN prevê que pode ser eficaz para **Doença Metabólica da Biotina (Biotin Metabolic Disease)**,
com **15 ensaios clínicos identificados** e **20 publicações** como suporte contextual — a maioria com relevância indireta, baseada na adjacência metabólica entre cobalamina e biotina na via do propionato.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Deficiência de vitamina B12 / Anemia perniciosa (indicação clínica clássica; sem registro ANVISA identificado) |
| Nova Indicação Prevista | Doença Metabólica da Biotina (Biotin Metabolic Disease) |
| Pontuação de Previsão TxGNN | 99.60% |
| Nível de Evidência | L4 |
| Situação no Mercado Brasileiro | ✗ Não comercializado (0 registros identificados) |
| Número de Registros | 0 |
| Decisão Recomendada | Hold |

---

## Por que Esta Previsão é Razoável?

Atualmente, este Evidence Pack não contém dados detalhados sobre o mecanismo de ação (MOA) da cianocobalamina (Data Gap DG002). Com base no conhecimento publicado, a cianocobalamina — forma farmacêutica da vitamina B12 — atua como cofator para duas reações enzimáticas fundamentais: a conversão de methylmalonyl-CoA em succinyl-CoA (pela methylmalonyl-CoA mutase, cobalamina-dependente) e a remeti­lação da homocisteína em metionina (pela metionina sintase). Ambas as reações integram o metabolismo de carbono de um carbono e a síntese de ácidos nucleicos.

A relação com a doença metabólica da biotina emerge da adjacência metabólica direta: a biotina é cofator indispensável da propionyl-CoA carboxylase, que converte propionato em methylmalonyl-CoA — o substrato exato que a cobalamina processa na etapa seguinte. Nas formas clínicas mais comuns (deficiência de biotinidase ou de holocarboxylase sintase), o acúmulo de propionato e ácido metilmalônico cria uma pressão metabólica secundária que a suplementação de cobalamina pode parcialmente aliviar. A revisão de referência PMID 23622402 agrupa explicitamente cobalamina e biotina como ferramentas terapêuticas para "vitamin-responsive metabolic disorders", e o estudo clínico PMID 1909779 documentou 4 de 8 pacientes com acidemia metilmalônica (MMA) responsivos à vitamina B12 — uma condição metabólica diretamente adjacente.

Entretanto, é fundamental ressaltar que a cianocobalamina **não substitui** a biotina como tratamento etiológico da doença metabólica da biotina. O papel da cobalamina seria exclusivamente adjuvante — atuando sobre o metabolismo downstream da via afetada. O alto score TxGNN (99.60%) reflete, sobretudo, a proximidade dos dois cofatores no grafo de conhecimento metabólico, e não uma relação de tratamento primário. A decisão de "Hold" é, portanto, tecnicamente justificada até que estudos específicos sejam conduzidos.

---

## Evidências de Ensaios Clínicos

| Número do Ensaio | Fase | Status | Participantes | Principais Achados |
|---------|------|------|------|---------|
| [NCT02426775](https://clinicaltrials.gov/study/NCT02426775) | Phase 3 | Concluído | 33 | RCT multicêntrico do ácido cargluímico em acidemia propiônica (PA) e acidemia metilmalônica (MMA) — ambas com sobreposição metabólica direta com a doença metabólica da biotina; relevante como modelo de intervenção em doenças de ácidos orgânicos adjacentes |
| [NCT01173315](https://clinicaltrials.gov/study/NCT01173315) | Phase 2 | Concluído | 75 | RCT de suplementação de vitaminas e minerais (incluindo B12) para neuropatia e nefropatia em diabetes tipo 2; fornece suporte mecanístico indireto ao papel do grupo B em doenças metabólicas com componente neurológico |
| [NCT04312152](https://clinicaltrials.gov/study/NCT04312152) | N/A | Desconhecido | 200 | RCT crossover duplo-cego de suporte metabólico com Q10 ubiquinol + complexo vitamínico B e E em autismo idiopático e síndrome de Phelan-McDermid; avalia vitaminas B em distúrbios do metabolismo energético |
| [NCT05832190](https://clinicaltrials.gov/study/NCT05832190) | N/A | Encerrado | 5 | Intervenção combinada de fibras + **biotina** no período pré-cirurgia bariátrica para melhora do microbioma; único ensaio do conjunto que manipula diretamente biotina; encerrado precocemente (n=5) |
| [NCT05687474](https://clinicaltrials.gov/study/NCT05687474) | N/A | Concluído | 6.824 | Triagem genômica universal em recém-nascidos (Baby Detect), cobrindo 126 doenças genéticas tratáveis incluindo deficiência de biotinidase; não avalia tratamento com B12, mas mapeia a população-alvo da indicação prevista |
| [NCT03655223](https://clinicaltrials.gov/study/NCT03655223) | N/A | Recrutamento por convite | 30.000 | Plataforma Early Check de triagem neonatal expandida para condições raras; potencial fonte de coorte para doenças metabólicas da biotina em fase pré-sintomática |

---

## Evidências da Literatura

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [23622402](https://pubmed.ncbi.nlm.nih.gov/23622402/) | 2013 | Review | Handbook of Clinical Neurology | **Referência central:** agrupa cobalamina, folato e biotina como "vitamin-responsive disorders"; descreve erros inatos do metabolismo de cobalamina e biotina com apresentação neurológica e opções de tratamento vitamínico |
| [38203763](https://pubmed.ncbi.nlm.nih.gov/38203763/) | 2024 | Review | Int J Mol Sciences | Mecanismos moleculares da deficiência de B12 no sistema nervoso; cita explicitamente que B12 é cofator na via succinyl-CoA/biotina, caracterizando a adjacência metabólica que fundamenta a previsão TxGNN |
| [1909779](https://pubmed.ncbi.nlm.nih.gov/1909779/) | 1991 | Estudo clínico | Pediatric Research | Metabolismo de ¹³C-propionato em pacientes com PA e MMA: **4 de 8 pacientes com MMA foram responsivos à vitamina B12** — evidência clínica direta de cobalamina em doença do metabolismo de ácidos orgânicos adjacente à biotina |
| [958746](https://pubmed.ncbi.nlm.nih.gov/958746/) | 1976 | Review/Série de casos | Pediatric Clinics of North America | Aminoacidopatias responsivas a megavitaminas do grupo B, incluindo B12; descreve a racionalidade de ensaios terapêuticos com cofatores vitamínicos em erros inatos do metabolismo |
| [6152513](https://pubmed.ncbi.nlm.nih.gov/6152513/) | 1983 | Review | Advances in Clinical Chemistry | Erros inatos do metabolismo responsivos a vitaminas; revisão abrangente de cofatores vitamínicos em doenças metabólicas congênitas, incluindo cobalamina e biotina |
| [7027768](https://pubmed.ncbi.nlm.nih.gov/7027768/) | 1981 | Review | Acta Vitaminologica et Enzymologica | Vitaminas em doenças metabólicas; discute síndromes vitamina-dependentes por deficiência de apoenzima, onde doses farmacológicas (não nutricionais) de vitamina são necessárias |
| [36476407](https://pubmed.ncbi.nlm.nih.gov/36476407/) | 2023 | Experimental | J Endocrinology | Deficiência de B12 em ratas produz fenótipo pré-diabético com intolerância à glicose e cetogênese; conecta mecanisticamente B12 ao metabolismo intermediário |
| [11031989](https://pubmed.ncbi.nlm.nih.gov/11031989/) | 2000 | Review | Ryoikibetsu Shokogun Shirizu | Síndrome de dependência vitamínica; revisão clínica japonesa de distúrbios vitamina-dependentes incluindo cobalamina |
| [25388747](https://pubmed.ncbi.nlm.nih.gov/25388747/) | 2015 | Review | Endocr Metab Immune Disord Drug Targets | Vitaminas e diabetes tipo 2; menciona biotina, tiamina e piridoxina no contexto de doenças metabólicas com déficit de cofatores enzimáticos |
| [7015958](https://pubmed.ncbi.nlm.nih.gov/7015958/) | 1980 | Review | Ann NY Academy of Sciences | Interações entre vitaminas do complexo B essenciais para reações metabólicas e catabólicas; contextualiza a interdependência funcional entre B12 e biotina |

---

## Informações de Comercialização no Brasil

Cianocobalamina **não possui registros identificados na base ANVISA** consultada neste levantamento (0 registros encontrados, status: não comercializado).

> ⚠️ A ausência de registros nesta consulta não implica necessariamente que produtos à base de cianocobalamina sejam inexistentes no mercado brasileiro. Recomenda-se verificação direta no portal da ANVISA ([consulta.anvisa.gov.br](https://consulta.anvisa.gov.br)) para produtos farmacêuticos e suplementos contendo cianocobalamina.

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
A previsão TxGNN está mecanisticamente fundamentada na adjacência metabólica entre cobalamina e biotina na via do propionato (evidência L4), mas não há ensaios clínicos testando diretamente cianocobalamina no tratamento da doença metabólica da biotina. O tratamento etiológico desta condição já é bem estabelecido (reposição de biotina), o que posiciona a cianocobalamina apenas como potencial terapia adjuvante — papel que ainda carece de validação clínica.

**Para prosseguir, é necessário:**
- Obter informações de segurança e contraindicações da bula (remediar DG001 via ANVISA)
- Confirmar o mecanismo de ação completo via DrugBank API (remediar DG002)
- Conduzir revisão sistemática focada especificamente em cobalamina como adjuvante em doenças de deficiência de biotinidase ou holocarboxylase sintase
- Verificar registros ANVISA de cianocobalamina diretamente no portal da Agência
- Avaliar se existe justificativa clínica suficiente para um ensaio piloto de fase 1/2 testando cianocobalamina adjuvante em pacientes pediátricos com doença metabólica da biotina confirmada por diagnóstico genético
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

