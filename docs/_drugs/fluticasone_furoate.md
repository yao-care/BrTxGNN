---
layout: default
title: Fluticasone Furoate
parent: Apenas Predição do Modelo (L5)
nav_order: 325
evidence_level: L5
indication_count: 7
last_modified_at: 2026-10-31
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

Atualmente, não há dados detalhados sobre o mecanismo de ação nos dados compilados para este relatório. Segundo informações conhecidas, a fluticasona furoato é um agonista potente do receptor de glicocorticoide, com ação anti-inflamatória. Sua eficácia em doenças inflamatórias alérgicas das vias aéreas (asma, rinite) é estabelecida.

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

| Número de Registro | Nome Comercial | Forma Farmacêutica | Indicação Aprovada |
|---------|------|------|-----------|
| Registro 101070271 | AVAMYS | — | Glicocorticoides tópicos simples, exceto uso oftálmico |
| Registro 101070299 | RELVAR ELLIPTA | — | Antiasmáticos |
| Registro 101070344 | TRELEGY | — | Broncodilatadores |

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
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

