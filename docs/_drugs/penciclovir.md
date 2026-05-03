---
layout: default
title: Penciclovir
parent: 僅模型預測 (L5)
nav_order: 391
evidence_level: L5
indication_count: 10
---

# Penciclovir
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

Usando o skill `txgnn-pipeline` para orientar a geração deste relatório de reposicionamento. A seguir, o relatório completo baseado no Evidence Pack fornecido:

---

# Penciclovir: Do herpes labial à fasciolíase

## Resumo em Uma Frase

Penciclovir é um antiviral nucleosídeo análogo aprovado para uso tópico no tratamento do herpes labial (herpes simples tipo 1).
O modelo TxGNN prevê potencial para **Fasciolíase (Fascioliasis)**, contudo esta direção possui **0 ensaios clínicos** e **0 publicações** de suporte — a plausibilidade biológica desta previsão é considerada muito baixa, com elevada probabilidade de falso positivo estrutural do modelo.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Herpes labial (herpes simples tipo 1) |
| Nova Indicação Prevista | Fasciolíase (Fascioliasis) |
| Pontuação de Previsão TxGNN | 99.06% |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | ✓ Comercializado |
| Número de Registros | 8 |
| Decisão Recomendada | Hold |

---

## Por que Esta Previsão é Razoável?

Atualmente não há dados detalhados de mecanismo de ação (MOA) disponíveis neste pacote. Com base no conhecimento farmacológico estabelecido, o Penciclovir é um análogo da guanosina que, após ativação pela **timidina quinase (TK) viral** presente exclusivamente em células infectadas por herpesvírus (HSV-1, HSV-2, VZV), tem sua forma trifosforilada ativar a inibição seletiva da **DNA polimerase viral**, interrompendo a replicação do vírus. A formulação disponível é exclusivamente tópica (creme).

A fasciolíase é uma parasitose hepática causada por trematódeos (*Fasciola hepatica* e *F. gigantica*), com biologia fundamentalmente distinta dos vírus DNA. Helmintos **não possuem enzimas homólogas à TK viral** responsável pela ativação do Penciclovir — portanto, o fármaco não pode ser convertido à sua forma ativa no ambiente parasitário, e a inibição de DNA polimerase viral não tem paralelo funcional na biologia de worms.

A pontuação elevada do TxGNN (99.06%) provavelmente reflete um **viés estrutural no grafo de conhecimento**: o nó "nucleosídeo análogo" apresenta alta conectividade com o nó genérico "doenças infecciosas", gerando associações artificiais com doenças parasitárias. Este padrão se repete nas posições 2 a 4 do ranking (cysticercosis, coenurosis, intestinal helminthiasis), reforçando o diagnóstico de **agrupamento de falso positivo** (*parasitic cluster bias*).

---

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados.

---

## Evidências da Literatura

Atualmente não há literatura relacionada.

---

## Informações de Comercialização no Brasil

O Penciclovir possui **8 registros ativos** no mercado brasileiro com status de comercialização confirmado. Os dados individuais de cada registro (número ANVISA, nome comercial, forma farmacêutica e indicação aprovada) não estão disponíveis neste pacote de evidências.

Para consulta completa dos registros, acesse: [Consulta de Medicamentos ANVISA](https://consultas.anvisa.gov.br/#/medicamentos/)

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
O mecanismo de ação do Penciclovir — inibição da DNA polimerase viral dependente de ativação por TK viral exclusiva de herpesvírus — é biologicamente incompatível com a fasciolíase (infecção por helminto). Somada à ausência total de evidências clínicas ou pré-clínicas e à limitação crítica da via de administração exclusivamente tópica, esta candidatura é classificada como **falso positivo de alta probabilidade** e não deve avançar para nenhum estágio de investigação translacional.

**Para prosseguir, seria necessário:**
- Dados completos de MOA (via DrugBank API ou ANVISA/bula)
- Detalhes dos 8 registros ANVISA (nomes comerciais, formas farmacêuticas, indicações aprovadas)
- Revisão crítica do grafo de conhecimento TxGNN para mitigar o viés de agrupamento entre nós de "nucleosídeos análogos" e "doenças infecciosas parasitárias"
- Reavaliação das posições 2–10 do ranking (todas pertencentes a dois clusters de falso positivo: parasitárias e mesotelioma) para priorizar candidaturas com maior plausibilidade biológica para Penciclovir — como infecções virais sistêmicas por HSV em locais além da pele
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

