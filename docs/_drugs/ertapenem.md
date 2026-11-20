---
layout: default
title: Ertapenem
parent: Apenas Predição do Modelo (L5)
nav_order: 296
evidence_level: L5
indication_count: 1
monitor_inn: "ertapenem"
predicted_indications: ["bacterial arthritis"]
last_modified_at: 2026-11-03
description: "Ertapenem: nova indicação prevista, artrite bacteriana (bacterial arthritis) (nível de evidência L5). Indicação original: ANTIBIOTICOS SISTEMICOS SIMPLES"
---

# Ertapenem
{: .fs-9 }

Nível de evidência: **L5** | Indicações previstas: **1** 
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

## Ertapenem: antibacteriano carbapenêmico → artrite bacteriana (bacterial arthritis)
{: .text-alpha }

## Resumo em Uma Frase

Ertapenem é um antibiótico carbapenêmico de uso sistêmico, com registros na ANVISA.
O modelo TxGNN prevê que pode ser eficaz para **artrite bacteriana (bacterial arthritis)**, mas não há ensaios clínicos registrados para esta doença; as evidências disponíveis são **10 publicações** (principalmente relatos de caso e coortes).

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | ANTIBIOTICOS SISTEMICOS SIMPLES; ANTIBACTERIANOS PARA USO SISTÊMICO |
| Nova Indicação Prevista | artrite bacteriana (bacterial arthritis) |
| Pontuação de Previsão TxGNN | 0,9972 |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | Comercializado (registros ativos: 4 de 4) |
| Número de Registros | 4 (ativos: 4) |
| Decisão Recomendada | Hold |

## Por que Esta Previsão é Razoável?

Segundo as seções “Mechanism of Action” e “Microbiology” da bula aprovada pela FDA dos EUA (Prescribing Information) para Ertapenem (tradução não oficial): “O ertapeném sódico é um antibiótico carbapenêmico. […] O ertapeném tem atividade in vitro contra bactérias aeróbias e anaeróbias Gram-positivas e Gram-negativas. A atividade bactericida do ertapeném resulta da inibição da síntese da parede celular e é mediada pela ligação do ertapeném às proteínas de ligação à penicilina (PBPs).” Texto original em inglês: "Ertapenem sodium is a carbapenem antibiotic. […] Ertapenem has in vitro activity against Gram-positive and Gram-negative aerobic and anaerobic bacteria. The bactericidal activity of ertapenem results from the inhibition of cell wall synthesis and is mediated through ertapenem binding to penicillin binding proteins (PBPs)." ([DailyMed: Invanz (ertapenem sodium) prescribing information, Merck Sharp & Dohme LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=33f3b99b-fa82-42e0-26bf-f49891ae3d22), versão de 2026-02-04; acessado em 2026-11-19). Pelo conhecimento geral da farmacologia dos carbapenêmicos, o ertapenem inibe a síntese da parede celular bacteriana ao se ligar às proteínas ligadoras de penicilina (PBPs). Isso é biologicamente plausível para infecções osteoarticulares causadas por enterobactérias sensíveis, anaeróbios e estreptococos.

Por ser um antibacteriano de amplo espectro, a artrite bacteriana está dentro do espectro de ação esperado da classe. Trata-se, portanto, mais de uma extensão de espectro do que de um reposicionamento no sentido estrito. A pontuação do modelo é apenas uma previsão e não substitui evidência clínica.

Ressalva sobre o nível de evidência: os estudos recuperados tratam de artrite séptica ou infecções osteoarticulares tratadas com ertapenem apenas em relatos de caso e coortes, o que sustenta o nível L4 de forma limitada. Vários trabalhos recuperados não são pertinentes (revisão sobre hidradenite supurativa, estudo in vitro com auranofina, estudo sobre temocilina como agente alternativo).

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados.

## Evidências da Literatura

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [24709258](https://pubmed.ncbi.nlm.nih.gov/24709258/) | 2014 | Coorte | Antimicrob Agents Chemother | Estudo retrospectivo de 306 pacientes em terapia ambulatorial com ertapenem; indicações incluíam infecções ósseas e articulares |
| [31220276](https://pubmed.ncbi.nlm.nih.gov/31220276/) | 2019 | Coorte | J Antimicrob Chemother | Terapia supressiva subcutânea com β-lactâmico em 10 pacientes com infecções osteoarticulares |
| [22233826](https://pubmed.ncbi.nlm.nih.gov/22233826/) | 2011 | Relato de caso | J Chemother | Artrite séptica de punho por Klebsiella pneumoniae tratada com sucesso com ertapenem e levofloxacino |
| [31352398](https://pubmed.ncbi.nlm.nih.gov/31352398/) | 2019 | Relato de caso | BMJ Case Rep | Citrobacter koseri em osteomielite de pé diabético com artrite séptica, tratado com ertapenem |
| [31585203](https://pubmed.ncbi.nlm.nih.gov/31585203/) | 2020 | Relato de caso | Anaerobe | Artrite séptica e osteomielite de ombro por Clostridium paraputrificum |
| [37578166](https://pubmed.ncbi.nlm.nih.gov/37578166/) | 2023 | Relato de caso | J Investig Med High Impact Case Rep | Artrite séptica por Prevotella bivia em adulto imunocompetente |
| [39193962](https://pubmed.ncbi.nlm.nih.gov/39193962/) | 2024 | Coorte | Clin Lab | Distribuição de patógenos e resistência em infecções osteoarticulares em crianças pequenas |
| [41878879](https://pubmed.ncbi.nlm.nih.gov/41878879/) | 2026 | Coorte | J Antimicrob Chemother | Temocilina como alternativa aos carbapenêmicos em infecções osteoarticulares por enterobactérias resistentes a cefalosporinas de 3ª geração |
| [38924836](https://pubmed.ncbi.nlm.nih.gov/38924836/) | 2024 | In vitro | Diagn Microbiol Infect Dis | Auranofina restaurou a sensibilidade de E. coli resistente a carbapenêmicos ao ertapenem |
| [29183082](https://pubmed.ncbi.nlm.nih.gov/29183082/) | 2017 | Revisão | JAMA | Revisão sobre hidradenite supurativa (pouco pertinente) |

## Informações de Comercialização no Brasil

| Número de Registro | Nome Comercial | Forma Farmacêutica | Indicação Aprovada |
|---------|------|------|-----------|
| Registro 174200004 | Ertapeném sódico | Não informada | Antibióticos sistêmicos simples |
| Registro 155620061 | Ertapeném sódico | Não informada | Antibacterianos para uso sistêmico |
| Registro 102010064 | Ertapeném sódico | Não informada | Antibióticos sistêmicos simples |
| Registro 101710224 | Invanz | Não informada | Antibióticos sistêmicos simples |

## Considerações de Segurança

- **Contraindicações**: não há texto de bula disponível nos dados compilados para este relatório; é necessário consultar a bula para advertências e contraindicações.
- **Interações Medicamentosas**: foram identificadas 38 interações. A de maior gravidade é com **bupropiona (Major)**. Interações de gravidade moderada: ácido picossulfúrico, polietilenoglicol (3350 com eletrólitos) e sulfato de sódio. As demais têm gravidade não classificada (por exemplo, ácido acetilsalicílico, metronidazol, vancomicina, morfina, metformina).

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
- Não há ensaios clínicos para artrite bacteriana; o suporte vem de relatos de caso e coortes, com vários estudos pouco pertinentes. A pontuação elevada do modelo é apenas uma previsão.

**Para prosseguir, é necessário:**
- Estudos clínicos comparativos (idealmente randomizados) de ertapenem em artrite séptica/infecções osteoarticulares
- Dados de mecanismo de ação e análise de sensibilidade dos patógenos mais comuns
- Advertências e contraindicações da bula da ANVISA para a triagem de segurança
- Avaliação das interações medicamentosas relevantes, em especial com bupropiona

<!-- review:begin log -->

## Registro de verificação

Abaixo, o registro de verificação desta página. A frase que dizia não haver dados sobre o mecanismo de ação foi substituída por um trecho da bula oficial citada (com tradução não oficial); as previsões do modelo, os níveis de evidência e as conclusões não foram reescritos.

| Data da verificação | Item | Ação | Fonte |
|------|------|------|------|
| 2026-11-19 | Frase “não há dados sobre o mecanismo de ação” substituída por trecho da bula dos EUA | Frase sobre a falta de dados do mecanismo de ação substituída por um trecho com fonte | [DailyMed: Invanz (ertapenem sodium) prescribing information, Merck Sharp & Dohme LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=33f3b99b-fa82-42e0-26bf-f49891ae3d22) |

<!-- review:end log -->

## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

