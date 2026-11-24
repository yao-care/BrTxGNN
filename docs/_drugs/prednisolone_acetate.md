---
layout: default
title: Prednisolone Acetate
parent: Apenas Predição do Modelo (L5)
nav_order: 546
evidence_level: L5
indication_count: 10
monitor_inn: "PREDNISOLONE ACETATE"
predicted_indications: ["conjunctival folliculosis", "serous conjunctivitis except viral", "chronic follicular conjunctivitis", "parasitic conjunctivitis", "papillary conjunctivitis", "Angelucci syndrome", "pseudomembranous conjunctivitis", "acute hemorrhagic conjunctivitis", "vernal conjunctivitis", "postinfectious vasculitis"]
last_modified_at: 2026-11-24
description: "Prednisolone Acetate: nova indicação prevista, Foliculose conjuntival (nível de evidência L5). Indicação original: Glicocorticoides tópicos oftalmológicos simples"
---

# Prednisolone Acetate
{: .fs-9 }

Nível de evidência: **L5** | Indicações previstas: **10** 
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

## Acetato de Prednisolona: Da corticoterapia oftálmica tópica à foliculose conjuntival
{: .text-alpha }

## Resumo em Uma Frase

O acetato de prednisolona é um glicocorticoide de uso tópico oftálmico, registrado no Brasil para essa finalidade.
O modelo TxGNN prevê que pode ser eficaz para **foliculose conjuntival (conjunctival folliculosis)**, mas essa previsão se baseia apenas no modelo: **não há ensaios clínicos nem publicações** sobre essa doença nos dados compilados para este relatório.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Glicocorticoides tópicos oftalmológicos simples |
| Nova Indicação Prevista | Foliculose conjuntival |
| Pontuação de Previsão TxGNN | 0,9974 |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | Comercializado (registros ativos: 7 de 7) |
| Número de Registros | 7 (ativos: 7) |
| Decisão Recomendada | Hold |

---

## Por que Esta Previsão é Razoável?

Segundo a seção “Mechanism of Action” da bula aprovada pela FDA dos EUA (Prescribing Information) para Prednisolone Acetate (tradução não oficial): “A prednisolona é um fármaco esteroide adrenocortical sintético com propriedades predominantemente glicocorticoides. Algumas dessas propriedades reproduzem as ações fisiológicas dos glicocorticosteroides endógenos, mas outras não refletem necessariamente nenhuma das funções normais dos hormônios adrenais; elas são observadas somente após a administração de grandes doses terapêuticas do fármaco.” Texto original em inglês: "Prednisolone is a synthetic adrenocortical steroid drug with predominantly glucocorticoid properties. Some of these properties reproduce the physiological actions of endogenous glucocorticosteroids, but others do not necessarily reflect any of the adrenal hormones' normal functions; they are seen only after administration of large therapeutic doses of the drug." ([DailyMed: Orapred Odt (prednisolone sodium phosphate) prescribing information, Advanz Pharma (US) Corp.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=1e379543-c4cf-4e72-953b-db15b7f0c2a1), versão de 2025-06-03; acessado em 2026-11-19). Segundo informações conhecidas, o acetato de prednisolona é um corticosteroide tópico oftálmico, e sua ação anti-inflamatória na superfície ocular é bem estabelecida. Mecanisticamente, isso pode ser aplicável a quadros inflamatórios da conjuntiva.

A indicação original (corticoterapia tópica oftálmica) e a nova indicação (foliculose conjuntival) envolvem o mesmo tecido-alvo, a conjuntiva. Por isso, a lógica de ação anti-inflamatória é plausível. Ainda assim, nenhum estudo foi recuperado para essa entidade específica, e a similaridade formal com a indicação original ainda não foi avaliada.

Outras condições conjuntivais previstas com pontuação semelhante (conjuntivite serosa não viral, conjuntivite folicular crônica, conjuntivite papilar, conjuntivite primaveril) seguem a mesma lógica. A evidência para elas também é indireta, como detalhado abaixo.

---

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados para foliculose conjuntival.

Para fins de contexto, entre as demais previsões do modelo, há dois estudos em condições conjuntivais vizinhas. Nenhum testa diretamente o acetato de prednisolona:

| Número do Ensaio | Fase | Status | Participantes | Principais Achados |
|---------|------|------|------|---------|
| [NCT01437982](https://clinicaltrials.gov/study/NCT01437982) | Phase 4 | Concluído | 140 | Vigilância pós-comercialização de etabonato de loteprednol 0,5% (outro corticosteroide), relacionada à conjuntivite papilar |
| [NCT04705584](https://clinicaltrials.gov/study/NCT04705584) | Não aplicável | Desconhecido | 180 | Ciclosporina A 2% vs. tacrolimo 0,3% na conjuntivite primaveril resistente, como alternativa aos esteroides |

---

## Evidências da Literatura

Atualmente não há literatura relacionada à foliculose conjuntival.

Como contexto, a única publicação identificada que avalia o acetato de prednisolona em modelo de conjuntivite alérgica é pré-clínica, e não se refere à doença prevista:

<!-- review:begin br-lic-20261106-prednisolone_acetate-1 -->

> **Correção de verificação (2026-11-06)**: Texto original: “Há ainda mais dois registros válidos (PREDOPTIC e ZYPRED, este classificado como anti-infeccioso tópico em associações medicamentosas), totalizando 7.” Removido: a indicação de produtos de princípio ativo único ou em associação não correspondia aos dados de registro (dados abertos de medicamentos da ANVISA, em 2026-11-06). Fonte: [ANVISA – Dados abertos de medicamentos](https://dados.anvisa.gov.br/dados/DADOS_ABERTOS_MEDICAMENTOS.csv).

<!-- review:end br-lic-20261106-prednisolone_acetate-1 -->

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [24055903](https://pubmed.ncbi.nlm.nih.gov/24055903/) | 2013 | RCT (modelo experimental) | Cornea | Compara ciclosporina A 0,05% e 2%, epinastina 0,05% e acetato de prednisolona 1% na inflamação alérgica em modelo experimental de conjuntivite alérgica |

---

## Informações de Comercialização no Brasil

<!-- licenses:begin -->

| Registro | Produto | Situação |
|------|------|------|
| 101470006 | PRED | Ativo |
| 101470175 | ZYPRED | Ativo |
| 102980481 | OFTPRED | Ativo |
| 104971287 | STER | Ativo |
| 154230189 | PREDOPTIC | Ativo |
| 154230190 | ACETATO DE PREDNISOLONA | Ativo |
| 154230331 | VISIOPRED | Ativo |

<!-- licenses:end -->

---

## Considerações de Segurança

- **Relações registradas no grafo de conhecimento (não são texto de bula):** doenças associadas a contraindicação ao fármaco incluem ceratite por herpes simples, glaucoma de ângulo aberto, hipertensão ocular, infecções oculares (virais, fúngicas, tuberculose ocular, conjuntivite infecciosa), diabetes mellitus, cetoacidose diabética, porfirias, deficiência de G6PD, doença de depósito de glicogênio, cistinúria, galactosemia e pigmentação da córnea.
- **Riscos relevantes ao uso crônico:** a literatura recuperada destaca o aumento da pressão intraocular e o risco de catarata com esteroides tópicos prolongados, preocupação especial em doenças crônicas ou pediátricas.
- **Interações medicamentosas:** nenhuma interação foi encontrada na consulta realizada.

Para advertências e contraindicações oficiais, consulte a bula.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
- A previsão para foliculose conjuntival se apoia somente na pontuação do modelo (nível L5), sem ensaios clínicos nem publicações sobre a doença. O uso de corticosteroide em doença crônica traz riscos conhecidos (pressão intraocular, catarata).

**Para prosseguir, é necessário:**
- Revisão da literatura e de diretrizes clínicas específicas para foliculose conjuntival.
- Dados de mecanismo de ação do fármaco e avaliação formal de similaridade com a indicação original.
- Bula oficial da ANVISA, com advertências e contraindicações, e dados de forma farmacêutica e via de administração.
- Estudos clínicos que avaliem diretamente o acetato de prednisolona na doença-alvo, com monitoramento de pressão intraocular.
- Antes de qualquer uso, descartar etiologia infecciosa, dada a contraindicação em infecções oculares.

<!-- review:begin log -->

## Registro de verificação

Abaixo está o registro de verificação desta página: afirmações conferidas com os dados oficiais de registro (dados abertos de medicamentos da ANVISA). As correções se limitam a fatos básicos; as previsões do modelo, os níveis de evidência e as conclusões não foram reescritos. A frase que dizia não haver dados sobre o mecanismo de ação foi substituída por um trecho da bula oficial citada (com tradução não oficial).

| Data da verificação | Item | Ação | Fonte |
|------|------|------|------|
| 2026-11-06 | Removido: “Há ainda mais dois registros válidos (PREDOPTIC e ZYPRED, este classificado como anti-infeccioso tópico em associações medicamentosas), tota” | Corrigido | [ANVISA – Dados abertos de medicamentos](https://dados.anvisa.gov.br/dados/DADOS_ABERTOS_MEDICAMENTOS.csv) |
| 2026-11-19 | Frase “não há dados sobre o mecanismo de ação” substituída por trecho da bula dos EUA | Frase sobre a falta de dados do mecanismo de ação substituída por um trecho com fonte | [DailyMed: Orapred Odt (prednisolone sodium phosphate) prescribing information, Advanz Pharma (US) Corp.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=1e379543-c4cf-4e72-953b-db15b7f0c2a1) |

<!-- review:end log -->

## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

