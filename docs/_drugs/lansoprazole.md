---
layout: default
title: Lansoprazole
parent: 僅模型預測 (L5)
nav_order: 299
evidence_level: L5
indication_count: 10
---

# Lansoprazole
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

Usando o skill **txgnn-pipeline** para enquadrar o contexto do relatório TxGNN. Vou agora gerar o relatório completo com base no Evidence Pack fornecido.

---

# Lansoprazole: De úlcera péptica ao refluxo duodenogástrico

## Resumo em Uma Frase

Lansoprazole é um inibidor da bomba de prótons (PPI) da classe das benzimidazolinas, amplamente utilizado no tratamento de doenças ácido-relacionadas — incluindo úlcera péptica, doença do refluxo gastroesofágico (DRGE) e erradicação de *Helicobacter pylori* — com uso clínico consolidado há mais de três décadas.
O modelo TxGNN prevê que pode ser eficaz para **Refluxo Duodenogástrico (Duodenogastric Reflux)**, atualmente com **0 ensaios clínicos** e **2 publicações** apoiando esta direção — sendo uma delas um sinal de segurança negativo em modelo animal.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Úlcera péptica, DRGE e erradicação de *H. pylori* (uso internacionalmente consolidado; sem registros ANVISA localizados) |
| Nova Indicação Prevista | Refluxo Duodenogástrico (Duodenogastric Reflux) |
| Pontuação de Previsão TxGNN | 99.69% |
| Nível de Evidência | L4 |
| Situação no Mercado Brasileiro | ✗ Não comercializado |
| Número de Registros | 0 |
| Decisão Recomendada | Hold |

---

## Por que Esta Previsão é Razoável?

Lansoprazole suprime a secreção ácida gástrica de forma dose-dependente e prolongada por meio da inibição irreversível da H⁺/K⁺-ATPase (bomba de prótons) nas células parietais — independentemente do estímulo primário de secreção. É o mecanismo de ação compartilhado por todos os PPIs e responsável pelos seus efeitos clínicos nas doenças ácido-pépticas.

A lógica da previsão TxGNN para o refluxo duodenogástrico (DGR) apoia-se na ideia de que a acidez gástrica potencializa o dano mucoso causado pelo conteúdo biliar refluxado. Ao reduzir o ácido, o lansoprazole poderia, em tese, atenuar a injúria combinada ácido-bílis sobre a mucosa gástrica. Há também sobreposição fisiopatológica com a DRGE, uma indicação já estabelecida.

Contudo, a previsão enfrenta duas limitações críticas. Primeiro, o componente principal do DGR é a bile — não o ácido gástrico — de modo que o mecanismo de ação do lansoprazole é apenas indiretamente relevante. Segundo, e mais importante, o único estudo pré-clínico disponível com lansoprazole em modelo animal de DGR (PMID 15052437) demonstrou que o fármaco **promoveu** carcinogênese gástrica nessa condição, ao invés de proteger — configurando um sinal de segurança negativo que contraindica o avanço clínico nesta direção sem investigação adicional.

---

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados.

---

## Evidências da Literatura

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [18679668](https://pubmed.ncbi.nlm.nih.gov/18679668/) | 2008 | Review | Eur J Clin Pharmacol | PPIs (incluindo lansoprazole) são fármacos de primeira escolha para úlcera péptica, infecção por *H. pylori*, DRGE, lesões por AINEs e síndrome de Zollinger-Ellison; revisão abrangente de farmacocinética e uso clínico |
| [15052437](https://pubmed.ncbi.nlm.nih.gov/15052437/) | 2004 | Animal Study (in vivo) | Gastric Cancer | **⚠ Sinal de segurança negativo**: em ratos com DGR experimental, lansoprazole promoveu — e não inibiu — o desenvolvimento de carcinoma gástrico, sugerindo que a inibição ácida pode ser deletéria nessa condição específica |

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
A evidência disponível para lansoprazole em refluxo duodenogástrico restringe-se a estudos pré-clínicos (L4), e o único dado experimental publicado constitui um sinal de segurança negativo — o fármaco exacerbou a carcinogênese gástrica em modelo animal de DGR. Somado ao fato de que o mecanismo de ação da supressão ácida é apenas indireto nessa patologia, não há base suficiente para avançar com esta indicação.

**Para prosseguir, seria necessário:**
- Obter dados detalhados de MOA e perfil de segurança via DrugBank e bula ANVISA/FDA
- Conduzir revisão sistemática específica sobre PPI em DGR humano (há sinal de risco oncológico a ser caracterizado)
- Avaliar a relação risco-benefício frente a alternativas como agentes pró-cinéticos e quelantes de bile, que agem diretamente no mecanismo do DGR
- Considerar a priorização de indicações com suporte mais robusto neste mesmo Evidence Pack: **Gastrojejunal Ulcer** (L1 — *Proceed with Guardrails*), **Peptic Ulcer Perforation** (L2) e **Duodenitis** (L2), todas com mecanismo de ação diretamente aplicável e ensaios clínicos disponíveis
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

