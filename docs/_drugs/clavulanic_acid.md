---
layout: default
title: Clavulanic Acid
parent: 僅模型預測 (L5)
nav_order: 190
evidence_level: L5
indication_count: 10
---

# Clavulanic Acid
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

---

# Ácido Clavulânico: De inibidor de beta-lactamase para uretrite gonocócica

## Resumo em Uma Frase

Ácido clavulânico é um inibidor irreversível de beta-lactamase, utilizado em combinação com amoxicilina (Augmentin) para tratar infecções bacterianas causadas por microrganismos produtores de penicilinase.
O modelo TxGNN prevê que pode ser eficaz para **Uretrite Gonocócica (Gonococcal Urethritis)**, com **0 ensaios clínicos registrados** e **14 publicações** apoiando esta direção.
A previsão é biologicamente fundamentada: *Neisseria gonorrhoeae* produtora de penicilinase (PPNG) é diretamente sensível à inibição de beta-lactamase pelo ácido clavulânico, restaurando a eficácia da amoxicilina.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Inibidor de beta-lactamase; uso combinado com amoxicilina para infecções por microrganismos produtores de penicilinase |
| Nova Indicação Prevista | Uretrite Gonocócica (Gonococcal Urethritis) |
| Pontuação de Previsão TxGNN | 99.93% |
| Nível de Evidência | L2 |
| Situação no Mercado Brasileiro | ✗ Não comercializado |
| Número de Registros ANVISA | 0 |
| Decisão Recomendada | Proceed with Guardrails |

---

## Por que Esta Previsão é Razoável?

Ácido clavulânico é um produto natural derivado de *Streptomyces clavuligerus* que age como inibidor suicida de beta-lactamases bacterianas. Ao se ligar irreversivelmente ao sítio ativo dessas enzimas, ele impede a hidrólise dos antibióticos beta-lactâmicos parceiros, como a amoxicilina. Isolado, não possui atividade antibacteriana clinicamente relevante; seu papel é exclusivamente o de "escudo protetor" que garante a eficácia do agente beta-lactâmico associado.

*Neisseria gonorrhoeae* produtora de penicilinase (PPNG) expressa uma beta-lactamase do tipo TEM que inativa a amoxicilina antes que esta possa exercer sua ação bactericida. Ao inibir irreversivelmente essa enzima, o ácido clavulânico restaura a atividade da amoxicilina contra cepas de PPNG — mecanismo diretamente pertinente ao tratamento da uretrite gonocócica resistente. Este foi o fundamento central do uso clínico de Augmentin (amoxicilina-clavulanato) no tratamento da gonorreia nas décadas de 1980 e 1990.

A relação entre a indicação funcional original (infecções por bactérias produtoras de beta-lactamase) e a nova indicação prevista (uretrite gonocócica por PPNG) é mecanisticamente direta e não especulativa. Os estudos clínicos históricos documentam taxas de cura de **85 a 97%** com doses únicas orais de amoxicilina-clavulanato em gonorreia urogenital não complicada, incluindo regiões com alta prevalência de PPNG (como Nigéria e Singapura nos anos 1980). O maior obstáculo atual não é a plausibilidade biológica, mas sim o perfil contemporâneo de resistência de *N. gonorrhoeae*, que evoluiu consideravelmente desde esses estudos seminais.

---

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados.

---

## Evidências da Literatura

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|-----------|-------------------|
| [3533755](https://pubmed.ncbi.nlm.nih.gov/3533755/) | 1986 | Comparative Trial | Genitourinary Medicine | Estudo randomizado com 500 pacientes: cefuroxima axetil vs amoxicilina 3g + clavulanato 0,25g (dose única) para gonorreia urogenital e retal não complicada; ambos combinados com probenecida |
| [3721514](https://pubmed.ncbi.nlm.nih.gov/3721514/) | 1986 | 3-arm Comparative Trial | Genitourinary Medicine | Três regimes de penicilina comparados; Augmentin 3,25g + probenecida oral avaliado em gonorreia masculina; taxas de cura diferenciadas em cepas PPNG e não-PPNG |
| [4007860](https://pubmed.ncbi.nlm.nih.gov/4007860/) | 1985 | Dose Comparison Trial | Genitourinary Medicine | Dose única amox 3g + clavulanato 125mg: 97% de cura em 100 pacientes; 85% de cura mesmo em 13 pacientes com cepas PPNG, incluindo uma cepa PPNG resistente à espectinomicina |
| [6428699](https://pubmed.ncbi.nlm.nih.gov/6428699/) | 1984 | Clinical Trial | Br J Venereal Diseases | 192 homens com uretrite gonocócica aguda: Augmentin em duas doses (95,9% curados) vs kanamicina IM (87,4%); eficácia equivalente em cepas PPNG e não-PPNG |
| [6365235](https://pubmed.ncbi.nlm.nih.gov/6365235/) | 1984 | Comparative Clinical Trial | Br J Venereal Diseases | 121 homens com uretrite gonocócica não complicada: amox + clavulanato oral vs penicilina procaína IM; falha de tratamento 9,4% vs 26,3%, respectivamente |
| [3004176](https://pubmed.ncbi.nlm.nih.gov/3004176/) | 1985 | Clinical Trial | African J Medicine | Augmentin (amox 3,0g + clavulanato 125mg) em Ibadan, Nigéria, onde ~80% das cepas circulantes são PPNG; comparação de duas formulações; alta taxa de cura documentada |
| [6757686](https://pubmed.ncbi.nlm.nih.gov/6757686/) | 1982 | Clinical Trial | Medical J Malaysia | Estudo pioneiro de dose única oral de amoxicilina + clavulanato para uretrite gonocócica masculina; um dos primeiros relatos clínicos publicados |
| [3147528](https://pubmed.ncbi.nlm.nih.gov/3147528/) | 1988 | Clinical Study | Sexually Transmitted Diseases | Análise comparativa de regimes para gonorreia resistente a antibióticos (PPNG); clavulanato + amoxicilina avaliado para infecções uretrais, cervicais, faríngeas e retais |
| [7958383](https://pubmed.ncbi.nlm.nih.gov/7958383/) | 1994 | Open Study | J International Medical Research | 55 pacientes com gonorreia aguda; 92,5% das cepas resistentes à penicilina; penicilina procaína IM + Augmentin oral; 96,4% com descarga purulenta e 85,5% com disúria no início |
| [19544099](https://pubmed.ncbi.nlm.nih.gov/19544099/) | 2009 | Retrospective Review | Rev Esp Quimioterapia | Revisão de 3 anos (Madri) sobre prevalência e tendências dos microrganismos causadores de uretrite em homens; contexto epidemiológico contemporâneo |

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Proceed with Guardrails**

**Justificativa:**
Existe fundamento mecanístico direto e múltiplos estudos clínicos da era 1982–1994 documentando eficácia da associação amoxicilina-clavulanato no tratamento da uretrite gonocócica, com taxas de cura de 85–97% inclusive em populações com alta prevalência de cepas PPNG. A previsão TxGNN é biologicamente coerente, mas a evidência provém inteiramente de estudos históricos — o perfil atual de resistência de *N. gonorrhoeae* exige validação contemporânea antes de qualquer aplicação clínica.

**Para prosseguir, é necessário:**
- **Atualização do perfil de resistência**: *N. gonorrhoeae* desenvolveu resistência crescente a múltiplas classes desde os anos 1980; confirmar sensibilidade atual ao regime amoxicilina-clavulanato no Brasil
- **Dados de segurança completos**: Obter bula, advertências e contraindicações junto à ANVISA ou à fonte do fabricante (atualmente indisponíveis)
- **Registro da combinação no Brasil**: Verificar se Augmentin (amoxicilina-clavulanato) possui registro ANVISA vigente — sem ele, a aplicação clínica fica inviabilizada independentemente da evidência
- **Ensaios clínicos modernos**: Os estudos disponíveis têm entre 30 e 44 anos; novos estudos prospectivos com cepas contemporâneas são necessários para suportar uso clínico atual
- **Dados completos de MOA via DrugBank**: Complementar o gap de mecanismo de ação para análise farmacológica formal
---

