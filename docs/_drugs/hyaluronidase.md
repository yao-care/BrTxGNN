---
layout: default
title: Hyaluronidase
parent: Apenas Predição do Modelo (L5)
nav_order: 354
evidence_level: L5
indication_count: 10
monitor_inn: "hyaluronidase"
predicted_indications: ["esotropia", "amenorrhea (disease)", "severe nonproliferative diabetic retinopathy", "renal tubular acidosis", "dermatitis", "diabetic retinopathy", "acrodermatitis chronica atrophicans", "diabetic cataract", "neonatal dermatomyositis", "non-syndromic esophageal malformation"]
last_modified_at: 2026-11-20
description: "Hyaluronidase: nova indicação prevista, Esotropia (nível de evidência L5). Indicação original: GLICOCORTICOIDES TOPICOS - ASSOCIACAO MEDICAMENTOSA"
---

# Hyaluronidase
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

## Hialuronidase: enzima hidrolítica de ácido hialurônico → Esotropia (esotropia)
{: .text-alpha }

## Resumo em Uma Frase

Hialuronidase é uma enzima que degrada o ácido hialurônico, registrada no Brasil em produtos de uso tópico em associação medicamentosa.
O modelo TxGNN prevê que pode ser eficaz para **Esotropia (esotropia)**, mas não há ensaios clínicos e apenas **1 publicação** relacionada, que descreve estrabismo como complicação após anestesia local, e não como alvo de tratamento.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | GLICOCORTICOIDES TOPICOS - ASSOCIACAO MEDICAMENTOSA; ANTINFECCIOSOS TOPICOS-ASSOCIACOES MEDICAMENTOSAS |
| Nova Indicação Prevista | Esotropia (esotropia) |
| Pontuação de Previsão TxGNN | 0,9989 |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | Comercializado (registros ativos: 3 de 7) |
| Número de Registros | 7 (ativos: 3) |
| Decisão Recomendada | Hold |

## Por que Esta Previsão é Razoável?

Segundo a seção “Mechanism of Action” da bula aprovada pela FDA dos EUA (Prescribing Information) para Hyaluronidase (tradução não oficial): “A hialuronidase é um agente de dispersão que modifica a permeabilidade do tecido conjuntivo por meio da hidrólise do ácido hialurônico, um polissacarídeo encontrado na substância fundamental intercelular do tecido conjuntivo e de certos tecidos especializados, como o cordão umbilical e o humor vítreo. O ácido hialurônico também está presente nas cápsulas dos estreptococos hemolíticos dos tipos A e C.” Texto original em inglês: "Hyaluronidase is a dispersion agent, which modifies the permeability of connective tissue through the hydrolysis of hyaluronic acid, a polysaccharide found in the intercellular ground substance of connective tissue, and of certain specialized tissues, such as the umbilical cord and vitreous humor. Hyaluronic acid is also present in the capsules of type A and C hemolytic streptococci." ([DailyMed: Hylenex Recombinant (hyaluronidase) prescribing information, Antares Pharma, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=3023cc56-ed4b-4e87-b3a1-81b20943f658), versão de 2024-11-11; acessado em 2026-11-19). Sabe-se de forma geral que a enzima degrada o ácido hialurônico da matriz extracelular e é usada para aumentar a difusão de outros medicamentos nos tecidos, inclusive como adjuvante em anestesia ocular.

Não há mecanismo terapêutico estabelecido para a esotropia. A única publicação encontrada (PMID 16934027) relata diplopia e estrabismo persistentes após cirurgia de catarata sob anestesia local, na qual a hialuronidase foi usada como adjuvante anestésico. Nesse contexto, o estrabismo é um evento adverso ou complicação, não um alvo terapêutico. A pontuação alta do modelo, portanto, não encontra respaldo em evidência clínica.

Como a publicação citada não estuda a esotropia como doença tratável com o fármaco, o nível de evidência é L5, apesar de a base de dados a classificar como L4.

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados.

## Evidências da Literatura

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [16934027](https://pubmed.ncbi.nlm.nih.gov/16934027/) | 2006 | Relato de caso/Revisão | Binocular Vision & Strabismus Quarterly | Descreve as características clínicas e os tratamentos de diplopia e estrabismo persistentes após cirurgia de catarata com anestesia local; o estrabismo aparece como complicação, não como indicação de tratamento. |

## Informações de Comercialização no Brasil

| Registro | Produto | Empresa detentora | Situação |
|------|------|------|------|
| 101180021 | OTO - XILODASE | APSEN FARMACEUTICA S/A | Ativo |
| 101180164 | POSTEC | APSEN FARMACEUTICA S/A | Ativo |
| 101180625 | HYAX | APSEN FARMACEUTICA S/A | Ativo |
| 101180012 | HYALOZIMA | APSEN FARMACEUTICA S/A | Cancelado |
| 101180037 | XILODASE | APSEN FARMACEUTICA S/A | Cancelado |
| 102350306 | VASOLIS | EMS S/A | Cancelado |
| 103720020 | LANABIOTIC | SUPERA FARMA LABORATÓRIOS S.A | Cancelado |

## Considerações de Segurança

- **Interações Medicamentosas**: foram identificadas 63 interações no total; as principais listadas, todas de gravidade menor, incluem hidrocortisona, triancinolona, ácido acetilsalicílico, dexametasona, betametasona, budesonida, prednisolona, prednisona, prometazina, lidocaína, clorfeniramina, loratadina, cetirizina, estradiol e etinilestradiol.

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
- Não há ensaios clínicos nem estudos que avaliem a hialuronidase como tratamento da esotropia; a única publicação trata o estrabismo como complicação associada ao uso do fármaco como adjuvante anestésico. A pontuação alta do modelo é uma previsão computacional sem sustentação clínica.

**Para prosseguir, é necessário:**
- Dados de mecanismo de ação que justifiquem uma ligação plausível com a esotropia
- Estudos pré-clínicos ou clínicos que avaliem diretamente a hialuronidase na esotropia
- Informações de segurança da bula (advertências e contraindicações), ainda não disponíveis nos dados compilados
- Esclarecimento da situação de comercialização dos registros atuais

<!-- review:begin log -->

## Registro de verificação

Abaixo, o registro de verificação desta página. A frase que dizia não haver dados sobre o mecanismo de ação foi substituída por um trecho da bula oficial citada (com tradução não oficial); as previsões do modelo, os níveis de evidência e as conclusões não foram reescritos.

| Data da verificação | Item | Ação | Fonte |
|------|------|------|------|
| 2026-11-19 | Frase “não há dados sobre o mecanismo de ação” substituída por trecho da bula dos EUA | Frase sobre a falta de dados do mecanismo de ação substituída por um trecho com fonte | [DailyMed: Hylenex Recombinant (hyaluronidase) prescribing information, Antares Pharma, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=3023cc56-ed4b-4e87-b3a1-81b20943f658) |

<!-- review:end log -->

## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

