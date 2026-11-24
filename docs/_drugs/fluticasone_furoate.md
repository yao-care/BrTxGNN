---
layout: default
title: Fluticasone Furoate
parent: Apenas Predição do Modelo (L5)
nav_order: 325
evidence_level: L5
indication_count: 7
last_modified_at: 2026-11-24
description: "Fluticasone Furoate: nova indicação prevista, Eczema atópico (atopic eczema) (nível de evidência L5). Indicação original: Glicocorticoides tópicos simples, exceto uso oftálmico"
monitor_inn: "FLUTICASONE FUROATE"
predicted_indications: ["atopic eczema", "bronchitis", "2-hydroxyethyl methacrylate sensitization", "dermatitis, atopic", "contact dermatitis", "occupational dermatitis", "phototoxic dermatitis"]
---

# Fluticasone Furoate
{: .fs-9 }

Nível de evidência: **L5** | Indicações previstas: **7** 
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

## Fluticasona Furoato: De glicocorticoide tópico/antiasmático para eczema atópico
{: .text-alpha }

## Resumo em Uma Frase

Fluticasona furoato é um corticosteroide inalatório e nasal, originalmente registrado no Brasil como glicocorticoide tópico (exceto uso oftálmico), antiasmático e broncodilatador (em associações).
O modelo TxGNN prevê que pode ser eficaz para **eczema atópico (atopic eczema)**, mas atualmente há **0 ensaios clínicos** e apenas **2 publicações indiretas** apoiando esta direção. Trata-se, portanto, de uma previsão computacional sem confirmação experimental.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Glicocorticoides tópicos simples, exceto uso oftálmico |
| Nova Indicação Prevista | Eczema atópico (atopic eczema) |
| Pontuação de Previsão TxGNN | 0,9998 |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | Comercializado (registros ativos: 3 de 3) |
| Número de Registros | 3 (ativos: 3) |
| Decisão Recomendada | Hold |

## Por que Esta Previsão é Razoável?

Segundo a seção “Mechanism of Action” da bula aprovada pela FDA dos EUA (Prescribing Information) para Fluticasone Furoate (tradução não oficial): “O furoato de fluticasona é um corticosteroide trifluorado sintético com atividade anti-inflamatória. Foi demonstrado in vitro que o furoato de fluticasona apresenta uma afinidade de ligação ao receptor de glicocorticoide humano aproximadamente 29,9 vezes maior que a da dexametasona e 1,7 vez maior que a do propionato de fluticasona.” Texto original em inglês: "Fluticasone furoate is a synthetic trifluorinated corticosteroid with anti-inflammatory activity. Fluticasone furoate has been shown in vitro to exhibit a binding affinity for the human glucocorticoid receptor that is approximately 29.9 times that of dexamethasone and 1.7 times that of fluticasone propionate." ([DailyMed: Fluticasone Furoate Ellipta (fluticasone furoate) prescribing information, Prasco Laboratories](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=d3e797fc-2636-49a0-b89e-5246b18ee440), versão de 2025-03-06; acessado em 2026-11-19). Segundo informações conhecidas, a fluticasona furoato é um agonista potente do receptor de glicocorticoide, com ação anti-inflamatória. Sua eficácia em doenças inflamatórias alérgicas das vias aéreas (asma, rinite) é estabelecida.

O eczema atópico é uma doença inflamatória da pele, e os corticosteroides tópicos são uma classe padrão de tratamento. Por isso, mecanisticamente a previsão é plausível, e há proximidade com a indicação original (glicocorticoide tópico).

Contudo, as duas publicações associadas (uma revisão sobre supressão adrenal por corticosteroides intranasais e um relato de caso sobre imunoterapia alérgica) não testam a fluticasona furoato no eczema. A pontuação alta do TxGNN é apenas uma previsão computacional. Outras indicações previstas (bronquite, dermatite de contato, dermatite ocupacional, dermatite fototóxica) seguem lógica semelhante, e algumas, como a bronquite, se sobrepõem ao uso respiratório já existente, não representando um sinal real de reposicionamento.

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados.

## Evidências da Literatura

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [19571596](https://pubmed.ncbi.nlm.nih.gov/19571596/) | 2009 | Revisão | Neuroimmunomodulation | Revisa a supressão do eixo hipotálamo-hipófise-adrenal por corticosteroides intranasais usados na rinite alérgica, frequentemente associada a asma e dermatite atópica. Aborda segurança, não eficácia no eczema. |
| [40066386](https://pubmed.ncbi.nlm.nih.gov/40066386/) | 2025 | Relato de caso | Indian J Otolaryngol Head Neck Surg | Discute imunoterapia alérgica em pacientes com autoimunidade, mencionando a dermatite atópica como aplicação recente. Não avalia a fluticasona furoato. |

## Informações de Comercialização no Brasil

Todos os 3 registros abaixo estão válidos; o medicamento está comercializado.

<!-- licenses:begin -->

| Registro | Produto | Situação |
|------|------|------|
| 101070271 | AVAMYS | Ativo |
| 101070299 | RELVAR ELLIPTA | Ativo |
| 101070344 | TRELEGY | Ativo |

<!-- licenses:end -->

## Considerações de Segurança

- **Contraindicações (com base no grafo de conhecimento do TxGNN, não em texto de bula)**: o grafo associa o fármaco a condições em que corticosteroides exigem cautela ou são contraindicados, incluindo:
  - Infecções: sarampo, ceratite por herpes simples, varicela-zóster, infecções fúngicas, dermatofitose, tuberculose pulmonar, infecções parasitárias e doenças infecciosas em geral.
  - Oculares: hipertensão ocular e glaucoma.
  - Endócrinas: insuficiência adrenocortical, doença de Addison, hiperfunção adrenal e síndrome de Cushing.
  - Vias aéreas: doenças do trato respiratório inferior e superior, dos seios paranasais e da cavidade nasal.
- **Preocupação sistêmica**: a literatura associada destaca a possível supressão do eixo hipotálamo-hipófise-adrenal por corticosteroides intranasais, relevante em uso prolongado ou em crianças.
- **Interações medicamentosas**: não foram encontradas interações nos dados compilados.

Consulte a bula para advertências e contraindicações oficiais, que não estavam disponíveis.

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
A previsão é mecanisticamente plausível, mas não há ensaios clínicos nem literatura direta sobre a fluticasona furoato no eczema atópico (nível L5). Além disso, os 3 registros brasileiros estão válidos e o medicamento está comercializado, mas faltam dados de bula.

**Para prosseguir, é necessário:**
- Obter e analisar as bulas na ANVISA (advertências e contraindicações), o que bloqueia a triagem de segurança.
- Obter dados do mecanismo de ação (por exemplo, via DrugBank).
- Buscar estudos clínicos ou pré-clínicos diretos da fluticasona furoato em dermatite atópica.
- Avaliar a viabilidade de forma farmacêutica e via de administração cutânea, já que os produtos conhecidos são inalatórios e nasais.
- Esclarecer a situação regulatória atual e comparar com corticosteroides tópicos já estabelecidos para eczema.

<!-- review:begin br-lic-20261031-fluticasone_furoate-1 -->

> **Correção de verificação (2026-10-31)**: Texto original: “Esclarecer a situação regulatória atual (registros cancelados) e comparar com corticosteroides tópicos já estabelecidos para eczema.” Removido: a afirmação de que os registros estariam cancelados, vencidos ou inválidos não correspondia aos dados de registro (dados abertos de medicamentos da ANVISA, em 2026-10-31). Os números atualizados de registros estão no resumo rápido e nas informações de comercialização. Fonte: [ANVISA – Dados abertos de medicamentos](https://dados.anvisa.gov.br/dados/DADOS_ABERTOS_MEDICAMENTOS.csv).

<!-- review:end br-lic-20261031-fluticasone_furoate-1 -->

<!-- review:begin log -->

## Registro de verificação

Abaixo está o registro de verificação desta página: afirmações conferidas com os dados oficiais de registro (dados abertos de medicamentos da ANVISA). As correções se limitam a fatos básicos; as previsões do modelo, os níveis de evidência e as conclusões não foram reescritos. A frase que dizia não haver dados sobre o mecanismo de ação foi substituída por um trecho da bula oficial citada (com tradução não oficial).

| Data da verificação | Item | Ação | Fonte |
|------|------|------|------|
| 2026-10-31 | Removido: “(registros cancelados)” | Corrigido (revisado em 2026-11-24; versão anterior guardada no registro) | [ANVISA – Dados abertos de medicamentos](https://dados.anvisa.gov.br/dados/DADOS_ABERTOS_MEDICAMENTOS.csv) |
| 2026-11-19 | Frase “não há dados sobre o mecanismo de ação” substituída por trecho da bula dos EUA | Frase sobre a falta de dados do mecanismo de ação substituída por um trecho com fonte | [DailyMed: Fluticasone Furoate Ellipta (fluticasone furoate) prescribing information, Prasco Laboratories](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=d3e797fc-2636-49a0-b89e-5246b18ee440) |

<!-- review:end log -->

## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

