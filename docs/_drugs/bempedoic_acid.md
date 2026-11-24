---
layout: default
title: Bempedoic Acid
parent: Apenas Predição do Modelo (L5)
nav_order: 114
evidence_level: L5
indication_count: 9
last_modified_at: 2026-11-24
description: "Bempedoic Acid: nova indicação prevista, Hipertireoidismo (Hyperthyroidism) (nível de evidência L5). Indicação original: Antilipêmicos"
monitor_inn: "bempedoic acid"
predicted_indications: ["hyperthyroidism", "resistance to thyroid hormone due to a mutation in thyroid hormone receptor beta", "malignant catarrh", "infectious bovine rhinotracheitis", "cytomegalovirus infection", "hyperthyroxinemia", "drug-induced osteoporosis", "multiple endocrine neoplasia", "pregnancy associated osteoporosis"]
---

# Bempedoic Acid
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

## Ácido bempedoico: De antilipêmico para hipertireoidismo (previsão do modelo)
{: .text-alpha }

## Resumo em Uma Frase

O ácido bempedoico (NUSTENDI) foi originalmente registrado na ANVISA como antilipêmico, ou seja, para redução de lipídios no sangue.
O modelo TxGNN (deep learning) prevê que pode ser eficaz para **Hipertireoidismo (Hyperthyroidism)**, mas esta previsão vem apenas do modelo e pode refletir similaridades aprendidas entre doenças relacionadas, não evidência biológica, com **0 ensaios clínicos** e **0 publicações** apoiando esta direção.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Antilipêmicos |
| Nova Indicação Prevista | Hipertireoidismo (Hyperthyroidism) |
| Pontuação de Previsão TxGNN | 0,9961 |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | Comercializado (registros ativos: 1 de 1) |
| Número de Registros | 1 (ativos: 1) |
| Decisão Recomendada | Hold |

## Por que Esta Previsão é Razoável?

Segundo a seção “Mechanism of Action” da bula aprovada pela FDA dos EUA (Prescribing Information) para Bempedoic Acid (tradução não oficial): “O ácido bempedoico é um inibidor da adenosina trifosfato-citrato liase (ACL) que reduz o LDL-C por meio da inibição da síntese de colesterol no fígado. A ACL é uma enzima situada a montante da 3-hidroxi-3-metil-glutaril-coenzima A (HMG-CoA) redutase na via de biossíntese do colesterol.” Texto original em inglês: "Bempedoic acid is an adenosine triphosphate-citrate lyase (ACL) inhibitor that lowers LDL-C by inhibition of cholesterol synthesis in the liver. ACL is an enzyme upstream of 3-hydroxy-3-methyl-glutaryl-coenzyme A (HMG-CoA) reductase in the cholesterol biosynthesis pathway." ([DailyMed: Nexletol (bempedoic acid) prescribing information, Esperion Therapeutics, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=88d06d89-a3da-40b4-b273-8f4f7d56c4c9), versão de 2026-06-25; acessado em 2026-11-19). Segundo conhecimento farmacológico geral, o ácido bempedoico inibe a enzima ATP-citrato liase (ACLY) no fígado, etapa anterior à HMG-CoA redutase, o que aumenta a expressão de receptores de LDL e reduz o LDL-colesterol.

Não há vínculo mecanístico claro entre essa via e a síntese ou secreção de hormônios tireoidianos. A pontuação alta (0,9961) vem do modelo TxGNN (deep learning) e pode refletir similaridades aprendidas entre doenças relacionadas, não evidência biológica, sem ensaios ou literatura que a sustentem. Portanto, a previsão deve ser tratada com cautela e, por ora, como hipótese sem respaldo.

**Outras previsões do modelo (todas com nível L5, salvo indicação):**

| Posição | Doença prevista | Pontuação | Comentário |
|------|------|------|------|
| 2 | Resistência ao hormônio tireoidiano (mutação no receptor beta) | 0,9958 | Sobreposição conceitual frouxa com metabolismo lipídico hepático; especulativo |
| 3 | Febre catarral maligna | 0,9958 | Doença veterinária de ruminantes; pontuação do modelo TxGNN (deep learning), que pode refletir similaridades aprendidas entre doenças relacionadas, não evidência biológica |
| 4 | Rinotraqueíte infecciosa bovina | 0,9958 | Doença veterinária; pontuação do modelo TxGNN (deep learning), que pode refletir similaridades aprendidas entre doenças relacionadas, não evidência biológica |
| 5 | Infecção por citomegalovírus | 0,9953 | Conceitualmente concebível via metabolismo lipídico do hospedeiro, sem dados |
| 7 | Hipertiroxinemia | 0,9934 | Sem vínculo conhecido |
| 8 | Osteoporose induzida por fármacos | 0,9921 | Sem mecanismo conhecido |
| 9 | Neoplasia endócrina múltipla | 0,9918 | Sem racional mecanístico |
| 10 | Osteoporose associada à gestação | 0,9917 | Sem vínculo; preocupações de segurança na gravidez |

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados para hipertireoidismo.

## Evidências da Literatura

Atualmente não há literatura relacionada ao hipertireoidismo.

*Nota: a literatura disponível refere-se à HoFH (previsão de posição 6), não ao hipertireoidismo. Para referência, os estudos mais relevantes foram:*

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [41274797](https://pubmed.ncbi.nlm.nih.gov/41274797/) | 2026 | Coorte (mundo real) | Journal of Clinical Lipidology | Avaliação da eficácia e tolerabilidade do ácido bempedoico em pacientes com HoFH |
| [33766264](https://pubmed.ncbi.nlm.nih.gov/33766264/) | 2021 | Revisão | J Am Coll Cardiol | Terapias novas e emergentes para redução de LDL-C, incluindo o ácido bempedoico |
| [41741298](https://pubmed.ncbi.nlm.nih.gov/41741298/) | 2026 | Consenso de especialistas | Journal of Clinical Lipidology | Atualização da National Lipid Association sobre hipercolesterolemia familiar |
| [35466160](https://pubmed.ncbi.nlm.nih.gov/35466160/) | 2022 | Revisão | J Atheroscler Thromb | Avanços no tratamento da HoFH |
| [41106315](https://pubmed.ncbi.nlm.nih.gov/41106315/) | 2025 | Revisão | Experimental and Molecular Pathology | Terapias inovadoras para o manejo da HoFH |

## Informações de Comercialização no Brasil

<!-- licenses:begin -->

| Registro | Produto | Situação |
|------|------|------|
| 104540195 | NUSTENDI | Ativo |

<!-- licenses:end -->

## Considerações de Segurança

**Interações Medicamentosas** (23 interações identificadas; as principais estão listadas abaixo):

- **Gravidade maior**: corticosteroides (hidrocortisona, triancinolona, dexametasona, betametasona, budesonida, prednisolona, prednisona, metilprednisolona, deflazacort, fludrocortisona), levofloxacino e sinvastatina.
- **Gravidade moderada**: empagliflozina, glibenclamida, repaglinida, rifaximina, rosuvastatina, selexipague, fexofenadina e revefenacina.

Para advertências e contraindicações, consulte a bula.

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
A previsão para hipertireoidismo baseia-se apenas na pontuação do modelo (nível L5), sem ensaios, literatura ou vínculo mecanístico plausível.

<!-- review:begin br-lic-20261106-bempedoic_acid-2 -->

> **Correção de verificação (2026-11-06)**: Texto original: “A previsão para hipertireoidismo baseia-se apenas na pontuação do modelo (nível L5), sem ensaios, literatura ou vínculo mecanístico plausível. Além disso, o único registro no Brasil está cancelado.” Removido: a afirmação de que os registros estariam cancelados, vencidos ou inválidos não correspondia aos dados de registro (dados abertos de medicamentos da ANVISA, em 2026-11-06). Os números atualizados de registros estão no resumo rápido e nas informações de comercialização. Fonte: [ANVISA – Dados abertos de medicamentos](https://dados.anvisa.gov.br/dados/DADOS_ABERTOS_MEDICAMENTOS.csv).

<!-- review:end br-lic-20261106-bempedoic_acid-2 -->

**Para prosseguir, é necessário:**
- Dados do mecanismo de ação documentados e uma análise que relacione ACLY à fisiologia tireoidiana
- Obtenção e análise da bula na ANVISA (advertências e contraindicações), pendência bloqueante para a triagem de segurança
- Estudos pré-clínicos que sustentem qualquer efeito sobre a função tireoidiana
- Esclarecimento da situação regulatória no Brasil
- Considerar priorizar a avaliação da HoFH (posição 6), com evidências observacionais, mas atentando à limitação mecanística em pacientes com receptor de LDL ausente

<!-- review:begin br-lic-20261031-bempedoic_acid-1 -->

> **Correção de verificação (2026-10-31)**: Texto original: “Esclarecimento da situação regulatória no Brasil (registro cancelado)” Removido: a afirmação de que os registros estariam cancelados, vencidos ou inválidos não correspondia aos dados de registro (dados abertos de medicamentos da ANVISA, em 2026-10-31). Os números atualizados de registros estão no resumo rápido e nas informações de comercialização. Fonte: [ANVISA – Dados abertos de medicamentos](https://dados.anvisa.gov.br/dados/DADOS_ABERTOS_MEDICAMENTOS.csv).

<!-- review:end br-lic-20261031-bempedoic_acid-1 -->

<!-- review:begin log -->

## Registro de verificação

Abaixo está o registro de verificação desta página: afirmações conferidas com os dados oficiais de registro (dados abertos de medicamentos da ANVISA). As correções se limitam a fatos básicos; as previsões do modelo, os níveis de evidência e as conclusões não foram reescritos. A frase que dizia não haver dados sobre o mecanismo de ação foi substituída por um trecho da bula oficial citada (com tradução não oficial).

| Data da verificação | Item | Ação | Fonte |
|------|------|------|------|
| 2026-10-31 | Removido: “(registro cancelado)” | Corrigido (revisado em 2026-11-24; versão anterior guardada no registro) | [ANVISA – Dados abertos de medicamentos](https://dados.anvisa.gov.br/dados/DADOS_ABERTOS_MEDICAMENTOS.csv) |
| 2026-11-06 | Removido: “Além disso, o único registro no Brasil está cancelado” | Corrigido (revisado em 2026-11-24; versão anterior guardada no registro) | [ANVISA – Dados abertos de medicamentos](https://dados.anvisa.gov.br/dados/DADOS_ABERTOS_MEDICAMENTOS.csv) |
| 2026-11-12 | Tabela: registro 104540195 (NUSTENDI) está ativo, não cancelado | Substituído pela tabela de registros gerada por programa (antes: Corrigido) | [ANVISA – Dados abertos de medicamentos](https://dados.anvisa.gov.br/dados/DADOS_ABERTOS_MEDICAMENTOS.csv) |
| 2026-11-19 | Frase “não há dados sobre o mecanismo de ação” substituída por trecho da bula dos EUA | Frase sobre a falta de dados do mecanismo de ação substituída por um trecho com fonte | [DailyMed: Nexletol (bempedoic acid) prescribing information, Esperion Therapeutics, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=88d06d89-a3da-40b4-b273-8f4f7d56c4c9) |

<!-- review:end log -->

## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

