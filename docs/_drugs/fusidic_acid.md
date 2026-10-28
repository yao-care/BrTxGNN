---
layout: default
title: Fusidic Acid
parent: Apenas Predição do Modelo (L5)
nav_order: 330
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-28
description: "Fusidic Acid: nova indicação prevista, Ceratite de exposição (exposure keratitis) (nível de evidência L4). Indicação original: Antiinfecciosos tópicos"
monitor_inn: "fusidic acid"
predicted_indications: ["exposure keratitis", "non-human animal disease", "otitis externa", "postinfectious vasculitis", "post-bacterial disorder", "post-infectious syndrome", "infective urethral stricture", "Chagas cardiomyopathy", "infection-related hemolytic uremic syndrome", "parasitic eyelid infestation"]
---

# Fusidic Acid
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

## Ácido fusídico: De antiinfeccioso tópico à ceratite de exposição
{: .text-alpha }

## Resumo em Uma Frase

O ácido fusídico é um antibiótico de uso tópico, originalmente registrado no Brasil como antiinfeccioso tópico (isolado ou associado a outros medicamentos).
O modelo TxGNN prevê que pode ser eficaz para **ceratite de exposição (exposure keratitis)**, mas atualmente há **0 ensaios clínicos** e apenas **1 publicação** (uma série de casos sobre infecções oculares por *Tsukamurella*, que não demonstra eficácia do ácido fusídico) relacionada a esta direção.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Antiinfecciosos tópicos |
| Nova Indicação Prevista | Ceratite de exposição (exposure keratitis) |
| Pontuação de Previsão TxGNN | 0,9995 |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | Comercializado (registros ativos: 5 de 5) |
| Número de Registros | 5 (ativos: 5) |
| Decisão Recomendada | Hold |

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação na base compilada para este relatório. Segundo informações conhecidas, o ácido fusídico inibe a síntese proteica bacteriana ao bloquear o fator de elongação G (EF-G), com atividade principalmente contra bactérias Gram-positivas, como *Staphylococcus*.

A ceratite de exposição é uma lesão da superfície da córnea causada pelo fechamento incompleto das pálpebras. Uma infecção bacteriana secundária poderia, em tese, ser tratada por um antibacteriano tópico, o que dá alguma plausibilidade biológica à previsão.

Porém, o vínculo é indireto. A única publicação disponível é uma série de casos sobre infecções oculares por *Tsukamurella*, sem demonstração de que o ácido fusídico seja o agente eficaz. A pontuação elevada do TxGNN provavelmente reflete a classe geral dos antibacterianos, e não uma evidência específica.

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados.

## Evidências da Literatura

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [31246677](https://pubmed.ncbi.nlm.nih.gov/31246677/) | 2019 | Série de casos | Cornea | Maior série de casos de infecções oftálmicas associadas a *Tsukamurella*, com ênfase em espectro clínico, fatores de risco, tratamento e desfecho; inclui o primeiro relato de infecção de implante ocular após enucleação. Não avalia o ácido fusídico. |

## Informações de Comercialização no Brasil

| Número de Registro | Nome Comercial | Forma Farmacêutica | Indicação Aprovada |
|---------|------|------|-----------|
| Registro nº 185690002 | VERUTEX | Não informada | Antiinfecciosos tópicos |
| Registro nº 155840106 | ÁCIDO FUSÍDICO | Não informada | Antiinfecciosos tópicos |
| Registro nº 185690001 | VERUTEX B | Não informada | Antiinfecciosos tópicos – associações medicamentosas |
| Registro nº 110130273 | DERMOTIL FUSID | Não informada | Antiinfecciosos tópicos – associações medicamentosas |
| Registro nº 118190298 | ÁCIDO FUSÍDICO + VALERATO DE BETAMETASONA | Não informada | Antimicóticos para uso tópico |

Os cinco registros constam como válidos.

## Considerações de Segurança

- **Contraindicações segundo o grafo de conhecimento (PrimeKG, não texto de bula)**: o grafo associa o fármaco a diversas condições, entre elas insuficiência hepática, doença renal, diabetes mellitus, cetoacidose diabética, fibrilação atrial, glaucoma, hipertensão ocular, ceratite por herpes simples, conjuntivite, infecções oculares, colite por *Clostridium difficile*, miastenia gravis e bloqueio atrioventricular. Essa lista deve ser interpretada com cautela, pois não provém de bula e pode refletir informações de outros medicamentos da mesma classe ou de associações. Chama atenção a presença de condições oculares (glaucoma, conjuntivite, infecção ocular), relevantes para a indicação prevista.
- **Interações medicamentosas**: não foram encontradas interações na consulta realizada.

Para advertências e contraindicações oficiais, consulte a bula.

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
- A previsão tem pontuação alta no modelo, mas sem ensaios clínicos e com uma única série de casos que não envolve o ácido fusídico (nível L4). Além disso, o medicamento é comercializado no Brasil, com 5 registros válidos de 5, e não há dados de segurança de bula.

**Para prosseguir, é necessário:**
- Obter e analisar a bula na ANVISA (advertências e contraindicações), pois a ausência desses dados impede a triagem de segurança.
- Obter dados do mecanismo de ação (por exemplo, via DrugBank).
- Buscar evidências específicas do uso de ácido fusídico oftálmico em ceratite de exposição ou em suas infecções secundárias.
- Avaliar a compatibilidade de via de administração e formulação oftálmica, além da situação regulatória, já que não há registro vigente.
- Considerar a análise de outras indicações previstas, como a otite externa (rank 3), cuja plausibilidade biológica é maior (infecção por *S. aureus*), embora a literatura disponível seja indireta (bacteriologia e vigilância de resistência, em grande parte veterinária) e exija revisão dos dados de resistência.
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

