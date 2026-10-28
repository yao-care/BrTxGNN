---
layout: default
title: Clavulanic Acid
parent: Apenas Predição do Modelo (L5)
nav_order: 227
evidence_level: L5
indication_count: 10
monitor_inn: "Clavulanic acid"
predicted_indications: ["Ureaplasma urethritis", "gonococcal urethritis", "uterine inflammatory disease", "xanthogranulomatous pyelonephritis", "urogenital tuberculosis", "celiac trunk compression syndrome", "abdominal ectopic pregnancy", "abdominal cystic lymphangioma", "lymph node palisaded myofibroblastoma", "disease of uterine broad ligament"]
last_modified_at: 2026-10-28
description: "Clavulanic Acid: nova indicação prevista, Uretrite por Ureaplasma (Ureaplasma urethritis) (nível de evidência L5). Indicação original: Antibióticos sistêmicos – associações medicamentosas"
---

# Clavulanic Acid
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

## Ácido clavulânico: De associação antibiótica sistêmica para uretrite por Ureaplasma
{: .text-alpha }

## Resumo em Uma Frase

O ácido clavulânico é um inibidor de beta-lactamase, comercializado no Brasil em associação com antibióticos sistêmicos (como a amoxicilina).
O modelo TxGNN prevê que pode ser eficaz para **uretrite por Ureaplasma (Ureaplasma urethritis)**, a previsão de maior pontuação, mas sem nenhum ensaio clínico e sem estudo que avalie diretamente essa doença. A indicação com mais respaldo na literatura é a **uretrite gonocócica**, com **9 publicações**, a maioria estudos clínicos da década de 1980.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Antibióticos sistêmicos – associações medicamentosas |
| Nova Indicação Prevista | Uretrite por Ureaplasma (Ureaplasma urethritis) |
| Pontuação de Previsão TxGNN | 0,9993 |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | Comercializado (registros ativos: 2 de 2) |
| Número de Registros | 2 (ativos: 2) |
| Decisão Recomendada | Hold |

Observações sobre a classificação:
- Nenhuma das 4 publicações recuperadas para uretrite por Ureaplasma estuda essa doença com o ácido clavulânico (tratam de *Pasteurella bettyae*, tratamento empírico de uretrite em geral, diagnóstico microbiológico e prostatite crônica). Pela regra do teto de evidência, o nível é L5, e não o L4 atribuído na compilação de dados.
- Entre as previsões de maior pontuação, a **uretrite gonocócica** (pontuação 0,9993) é a única com estudos que a investigam diretamente. Ela é detalhada abaixo como alternativa mais relevante, com nível L3.

---

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação nos dados compilados. Segundo informações conhecidas, o ácido clavulânico é um inibidor de beta-lactamase que, usado em associação com amoxicilina, protege o antibiótico da degradação enzimática e amplia seu espectro de ação.

Para **Ureaplasma**, o mecanismo **não sustenta** a previsão: esse microrganismo não tem parede celular, portanto antibióticos beta-lactâmicos (incluindo amoxicilina/clavulanato) não são esperados como ativos. O tratamento padrão é doxiciclina ou um macrolídeo. A pontuação alta vem do modelo TxGNN (deep learning) e pode refletir semelhanças que o modelo aprendeu entre doenças relacionadas, e não evidência biológica nem atividade específica contra o organismo.

Já para a **uretrite gonocócica**, o mecanismo é coerente: o ácido clavulânico inibe a penicilinase produzida por *Neisseria gonorrhoeae*, restaurando a atividade da amoxicilina contra cepas produtoras de penicilinase. Porém, as diretrizes atuais não recomendam mais amoxicilina/clavulanato, devido à ampla resistência cromossômica e mediada por plasmídeos. A evidência é, portanto, histórica e de relevância clínica atual limitada.

---

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados.

---

## Evidências da Literatura

**Uretrite por Ureaplasma (indicação de maior pontuação):** nenhuma das publicações estuda diretamente a doença com ácido clavulânico.

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [21947096](https://pubmed.ncbi.nlm.nih.gov/21947096/) | 2011 | Revisão | Rev Esp Quimioter | Melhor tratamento empírico de uretrite em pacientes no centro de Madri |
| [19544099](https://pubmed.ncbi.nlm.nih.gov/19544099/) | 2009 | Coorte | Rev Esp Quimioter | Prevalência e tendência dos microrganismos causadores de uretrite em homens |
| [34366085](https://pubmed.ncbi.nlm.nih.gov/34366085/) | 2021 | Relato de caso | Infect Dis Now | Uretrite e balanite por *Pasteurella bettyae* em homens que fazem sexo com homens |
| [9669200](https://pubmed.ncbi.nlm.nih.gov/9669200/) | 1998 | Revisão | Int J Androl | Possível papel de bactérias anaeróbias na prostatite crônica |

**Uretrite gonocócica (alternativa com estudos diretos):**

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [3533755](https://pubmed.ncbi.nlm.nih.gov/3533755/) | 1986 | Ensaio clínico comparativo randomizado | Genitourin Med | Cefuroxima axetil vs. amoxicilina 3 g + ácido clavulânico 0,25 g em dose única, em 500 pacientes com gonorreia não complicada |
| [6365235](https://pubmed.ncbi.nlm.nih.gov/6365235/) | 1984 | Ensaio clínico comparativo | Br J Vener Dis | Em 121 homens, 9,4% com cultura ainda positiva após amoxicilina/clavulanato vs. 26,3% com penicilina procaína IM |
| [6428699](https://pubmed.ncbi.nlm.nih.gov/6428699/) | 1984 | Estudo clínico | Br J Vener Dis | Duas doses de Augmentin curaram 95,9% vs. 87,4% com canamicina, em 192 homens |
| [4007860](https://pubmed.ncbi.nlm.nih.gov/4007860/) | 1985 | Ensaio de comparação de doses | Genitourin Med | Amoxicilina 3 g + clavulanato 125 mg e probenecida curou 97 de 100 pacientes avaliáveis; 85% de cura nas cepas produtoras de penicilinase |
| [3004176](https://pubmed.ncbi.nlm.nih.gov/3004176/) | 1985 | Estudo clínico de dose única | Afr J Med Med Sci | Augmentin em dose única em Ibadan, onde cerca de 80% das cepas produzem penicilinase |
| [6757686](https://pubmed.ncbi.nlm.nih.gov/6757686/) | 1982 | Estudo clínico de dose única | Med J Malaysia | Amoxicilina oral + ácido clavulânico em dose única em homens com uretrite gonocócica |
| [3147528](https://pubmed.ncbi.nlm.nih.gov/3147528/) | 1988 | Estudo clínico | Sex Transm Dis | Opções de tratamento para gonorreia por cepas resistentes, incluindo clavulanato associado |
| [3132029](https://pubmed.ncbi.nlm.nih.gov/3132029/) | 1988 | Laboratorial | Hinyokika Kiyo | Detecção de *N. gonorrhoeae* produtora de penicilinase e sensibilidade a amoxicilina/clavulanato |
| [21947096](https://pubmed.ncbi.nlm.nih.gov/21947096/) | 2011 | Revisão | Rev Esp Quimioter | Tratamento empírico de uretrite |

---

## Informações de Comercialização no Brasil

| Número de Registro | Nome Comercial | Forma Farmacêutica | Indicação Aprovada |
|---------|------|------|-----------|
| Registro 105730210 | NOVAMOX | Não informada | Antibióticos sistêmicos – associações medicamentosas |
| Registro 101070076 | CLAVULIN | Não informada | Antibióticos sistêmicos – associações medicamentosas entre antiinfecciosos |

Os textos de indicação correspondem a classificações de categoria terapêutica, não a indicações clínicas detalhadas.

---

## Considerações de Segurança

- **Relações de contraindicação registradas no grafo de conhecimento** (não são texto de bula): doença renal, piureter, doença hepática, doença da vesícula biliar, colite por *Clostridium difficile*, enterocolite necrosante perinatal, colestase, colestase intra-hepática recorrente benigna, colestase intra-hepática familiar, mononucleose infecciosa e síndrome de infecção crônica pelo vírus Epstein-Barr.
- **Interações medicamentosas** (16 registradas): as de gravidade **maior** são com **leflunomida** e **teriflunomida**. As demais são de gravidade moderada, incluindo naltrexona, balsalazida, asparaginase, pegaspargase, brentuximabe vedotina, clofarabina, epirrubicina, idelalisibe, interferon beta-1a e beta-1b, peginterferon beta-1a, tioguanina, trabectedina e metotrexato.

Consulte a bula para advertências e contraindicações formais.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
- Para uretrite por Ureaplasma, não há estudo direto, e o mecanismo (ausência de parede celular) contradiz a previsão; o nível é L5.
- A uretrite gonocócica tem respaldo histórico (L3), mas as diretrizes atuais não recomendam mais amoxicilina/clavulanato por resistência, o que limita o interesse clínico. As demais previsões (endometrite, pielonefrite xantogranulomatosa, tuberculose urogenital e condições não infecciosas) têm evidência indireta ou inexistente.

**Para prosseguir, é necessário:**
- Obter e analisar a bula da ANVISA (advertências e contraindicações), lacuna de dados bloqueante para a triagem de segurança.
- Obter os dados de mecanismo de ação no DrugBank.
- Se houver interesse em uretrite gonocócica, comparar os dados históricos de eficácia com os perfis atuais de resistência de *N. gonorrhoeae* e com as diretrizes vigentes.
- Para Ureaplasma, não há justificativa para avançar sem nova evidência microbiológica ou clínica direta.
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

