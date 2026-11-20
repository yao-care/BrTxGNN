---
layout: default
title: Ciprofloxacin
parent: Apenas Predição do Modelo (L5)
nav_order: 223
evidence_level: L5
indication_count: 9
monitor_inn: "Ciprofloxacin"
predicted_indications: ["diffuse scleroderma", "hyperamylasemia", "polyclonal hyperviscosity syndrome", "congenital analbuminemia", "blood group incompatibility", "premalignant hematological system disease", "punctate epithelial keratoconjunctivitis", "monoclonal gammopathy", "hematological disease associated with an acquired peripheral neuropathy"]
last_modified_at: 2026-11-20
description: "Ciprofloxacin: nova indicação prevista, esclerodermia difusa (diffuse scleroderma) (nível de evidência L5). No Brasil, registros na ANVISA: 188 (ativos: 61)"
---

# Ciprofloxacin
{: .fs-9 }

Nível de evidência: **L5** | Indicações previstas: **9** 
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

## Ciprofloxacino: antibacteriano da classe das fluoroquinolonas → esclerodermia difusa (diffuse scleroderma)
{: .text-alpha }

## Resumo em Uma Frase

O ciprofloxacino é um antibacteriano da classe das fluoroquinolonas, usado em infecções bacterianas. O modelo TxGNN prevê que ele pode ser eficaz para **esclerodermia difusa (diffuse scleroderma)**. Atualmente, há **0 ensaios clínicos registrados** e **2 publicações** relacionadas a esta direção, ambas de apoio limitado.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Não consta nos dados locais |
| Nova Indicação Prevista | esclerodermia difusa (diffuse scleroderma) |
| Pontuação de Previsão TxGNN | 0,9987 |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | Comercializado (registros ativos: 61 de 188) |
| Número de Registros | 188 (ativos: 61) |
| Decisão Recomendada | Hold |

## Por que Esta Previsão é Razoável?

Segundo as seções “Mechanism of Action” e “Microbiology” da bula aprovada pela FDA dos EUA (Prescribing Information) para Ciprofloxacin (tradução não oficial): “A ciprofloxacina é um membro da classe de agentes antibacterianos das fluoroquinolonas. […] A ação bactericida da ciprofloxacina resulta da inibição das enzimas topoisomerase II (DNA girase) e topoisomerase IV (ambas topoisomerases do Tipo II), que são necessárias para a replicação, transcrição, reparo e recombinação do DNA bacteriano.” Texto original em inglês: "Ciprofloxacin is a member of the fluoroquinolone class of antibacterial agents. […] The bactericidal action of ciprofloxacin results from inhibition of the enzymes topoisomerase II (DNA gyrase) and topoisomerase IV (both Type II topoisomerases), which are required for bacterial DNA replication, transcription, repair, and recombination." ([DailyMed: Ciprofloxacin In Dextrose (ciprofloxacin) prescribing information, Hospira, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=cbbbf939-3219-4515-a48e-ca264daa4d07), versão de 2025-11-04; acessado em 2026-11-19). Sabe-se, de forma geral, que o ciprofloxacino é uma fluoroquinolona que inibe a DNA girase e a topoisomerase IV bacterianas, o que explica sua ação antibacteriana.

Para a esclerodermia, a hipótese presente na literatura é dupla. A primeira é um possível efeito antifibrótico na pele, talvez por modulação da síntese de colágeno ou da atividade dos fibroblastos (PMID 20507401). A segunda é indireta: tratar o supercrescimento bacteriano no intestino delgado, comum na esclerose sistêmica e causa de diarreia crônica e perda de peso (PMID 7728404).

Nenhuma dessas linhas fornece evidência controlada de modificação da doença. A pontuação muito alta do TxGNN é uma previsão computacional e não substitui dados clínicos.

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados.

## Evidências da Literatura

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [20507401](https://pubmed.ncbi.nlm.nih.gov/20507401/) | 2010 | Estudo exploratório (ensaio randomizado duplo-cego descrito no resumo) | The Journal of Dermatology | Avalia se o ciprofloxacino oral reduz a gravidade da esclerodermia, com foco em efeito antifibrótico na pele. O resumo disponível está truncado e não traz os resultados. |
| [7728404](https://pubmed.ncbi.nlm.nih.gov/7728404/) | 1995 | Estudo de coorte/diagnóstico | British Journal of Rheumatology | 24 pacientes com esclerose sistêmica e sintomas de má absorção investigados para supercrescimento bacteriano no intestino delgado, com avaliação do desfecho do tratamento; apenas 6 tinham a forma difusa. |

## Considerações de Segurança

- **Interações Medicamentosas**: o levantamento identificou 100 interações. Entre as de nível maior estão hidrocortisona, triamcinolona, dexametasona, betametasona e bupropiona. Há também interações de nível moderado, por exemplo com acarbose, famotidina, metformina, pioglitazona, loperamida, ácido acetilsalicílico e budesonida.

Para advertências e contraindicações, consulte a bula.

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
- A previsão se apoia em apenas duas publicações, sem ensaios clínicos registrados e sem resultados controlados que comprovem benefício na esclerodermia difusa. O nível de evidência é L4 e a pontuação do modelo, isoladamente, não sustenta uma decisão de avanço.

**Para prosseguir, é necessário:**
- Obter o texto completo e os resultados do ensaio randomizado (PMID 20507401) e avaliar sua qualidade metodológica.
- Obter dados detalhados do mecanismo de ação e investigar o possível efeito antifibrótico em modelos pré-clínicos.
- Obter e analisar a bula da ANVISA (advertências e contraindicações), etapa necessária para a triagem de segurança.
- Avaliar o perfil de risco-benefício em uma doença crônica, considerando os riscos conhecidos das fluoroquinolonas (por exemplo, tendinopatia e neuropatia periférica) e o uso prolongado.
- Se houver sinal de benefício, planejar um ensaio controlado específico em esclerodermia difusa.

<!-- review:begin log -->

## Registro de verificação

Abaixo, o registro de verificação desta página. A frase que dizia não haver dados sobre o mecanismo de ação foi substituída por um trecho da bula oficial citada (com tradução não oficial); as previsões do modelo, os níveis de evidência e as conclusões não foram reescritos.

| Data da verificação | Item | Ação | Fonte |
|------|------|------|------|
| 2026-11-19 | Frase “não há dados sobre o mecanismo de ação” substituída por trecho da bula dos EUA | Frase sobre a falta de dados do mecanismo de ação substituída por um trecho com fonte | [DailyMed: Ciprofloxacin In Dextrose (ciprofloxacin) prescribing information, Hospira, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=cbbbf939-3219-4515-a48e-ca264daa4d07) |

<!-- review:end log -->

## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

