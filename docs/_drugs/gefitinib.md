---
layout: default
title: Gefitinib
parent: 僅模型預測 (L5)
nav_order: 263
evidence_level: L5
indication_count: 10
---

# Gefitinib
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

# Gefitinib: Do câncer de pulmão à fibromatose gengival

## Resumo em Uma Frase

Gefitinib (Iressa®) é um inibidor seletivo da tirosina quinase do EGFR (receptor do fator de crescimento epidérmico), amplamente utilizado no tratamento de câncer de pulmão de não pequenas células (CPNPC) com mutações ativadoras do EGFR. O modelo TxGNN prevê que pode ser eficaz para **Fibromatose Gengival (Fibromatosis, Gingival)**, porém atualmente **sem ensaios clínicos** e **sem publicações** apoiando diretamente esta direção. A pontuação de previsão é elevada (99,89%), mas baseia-se exclusivamente em inferência topológica do grafo de conhecimento, sem suporte de evidências clínicas ou pré-clínicas diretas.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Câncer de pulmão de não pequenas células (CPNPC) com mutações ativadoras do EGFR |
| Nova Indicação Prevista | Fibromatose Gengival (Fibromatosis, Gingival) |
| Pontuação de Previsão TxGNN | 99,89% |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | ✓ Comercializado |
| Número de Registros | 10 |
| Decisão Recomendada | Hold |

---

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação disponíveis no Evidence Pack. Com base no conhecimento consolidado da literatura, Gefitinib atua como inibidor seletivo da tirosina quinase do domínio intracelular do EGFR, bloqueando a fosforilação do receptor e interrompendo as cascatas de sinalização downstream — especialmente RAS/MAPK e PI3K/AKT — que são responsáveis por promover proliferação celular, angiogênese e resistência à apoptose. O fármaco demonstrou eficácia superior à quimioterapia convencional em pacientes com CPNPC portadores de mutações ativadoras nos exons 19 e 21 do EGFR, estabelecendo-se como um dos marcos da era das terapias-alvo em oncologia torácica.

A fibromatose gengival é uma condição caracterizada por proliferação excessiva e descontrolada de fibroblastos gengivais, resultando em espessamento progressivo do tecido gengival. O EGFR tem papel indireto na ativação e migração de fibroblastos, e sob esta perspectiva teórica, a inibição do EGFR poderia, em princípio, suprimir a proliferação fibrótica do tecido gengival. No entanto, a expressão e a função do EGFR em fibroblastos gengivais não estão estabelecidas por estudos específicos nesta condição.

A pontuação elevada do TxGNN (0,9989) provavelmente decorre da proximidade topológica no grafo de conhecimento entre os nós "EGFR", "proliferação de fibroblastos" e "fibromatose", configurando uma inferência de vizinhança e não um sinal de indicação direta. A ausência completa de evidências clínicas ou pré-clínicas torna esta previsão especulativa e insuficiente para justificar avanço clínico sem etapas robustas de validação experimental prévia.

---

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados.

---

## Evidências da Literatura

Atualmente não há literatura relacionada.

---

## Informações de Comercialização no Brasil

Gefitinib possui **10 registros ativos** no Brasil. No entanto, os dados individuais de cada produto (número de registro, nome comercial, forma farmacêutica e indicação aprovada) não estão disponíveis nesta versão do Evidence Pack — todos os campos correspondentes encontram-se sem preenchimento. Recomenda-se consulta direta ao portal de consulta de medicamentos da ANVISA para obter as informações completas de cada registro.

---

## Citotoxicidade

| Item | Conteúdo |
|------|------|
| Classificação de Citotoxicidade | Terapia-alvo (Inibidor de tirosina quinase do EGFR — EGFR-TKI de 1ª geração; não citotóxico convencional) |
| Risco de Mielossupressão | Baixo (mielossupressão não é toxicidade característica de EGFR-TKIs; diferente de quimioterapia citotóxica) |
| Classificação de Emetogenicidade | Baixa (agente oral com baixo potencial emetogênico) |
| Itens de Monitoramento | Função hepática (ALT/AST/bilirrubina — hepatotoxicidade frequente), função pulmonar (pneumonite intersticial — evento adverso grave), avaliação cutânea (erupção acneiforme — toxicidade mais comum), função renal |
| Proteção no Manuseio | Recomendado seguir regulamentos institucionais de manuseio de agentes antineoplásicos, conforme orientação da ANVISA e protocolos farmacêuticos locais |

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
A previsão do TxGNN para fibromatose gengival é classificada como nível de evidência L5 — exclusivamente inferência do modelo, sem qualquer estudo clínico ou pré-clínico de suporte. A conexão mecanística entre inibição do EGFR e fibromatose gengival é especulativa e sem sustentação experimental, e o uso de um inibidor sistêmico de tirosina quinase para uma condição benigna proliferativa — onde o risco de toxicidade (pneumonite intersticial, hepatotoxicidade, toxicidade cutânea) supera amplamente qualquer benefício teórico — não encontra embasamento clínico.

**Para prosseguir, é necessário:**
- Estudos pré-clínicos in vitro com fibroblastos gengivais humanos para validar a hipótese mecanística (requisito mínimo antes de qualquer avanço)
- Dados completos de MOA via DrugBank API (lacuna DG002 — severidade Alta)
- Advertências, contraindicações e precauções da bula ANVISA (lacuna DG001 — severidade Bloqueante)
- Dados individuais dos 10 registros ANVISA (números, formas farmacêuticas, indicações aprovadas)
- Avaliação do perfil de segurança em população com condição benigna, onde a relação risco-benefício é particularmente desfavorável para agentes antineoplásicos sistêmicos
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

