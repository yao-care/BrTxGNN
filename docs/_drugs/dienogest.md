---
layout: default
title: Dienogest
parent: Evidência Moderada (L3-L4)
nav_order: 267
evidence_level: L4
indication_count: 10
last_modified_at: 2026-10-13
description: "Dienogest: nova indicação prevista, Amenorreia (amenorrhea) (nível de evidência L4). Indicação original: Não disponível"
---

# Dienogest
{: .fs-9 }

Nível de evidência: **L4** | Indicações previstas: **10** 
{: .fs-6 .fw-300 }

---

## Índice
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Relatório de avaliação farmacêutica

</div>

# Dienogeste: Da indicação original não registrada à amenorreia (previsão do modelo)

## Resumo em Uma Frase

Dienogeste é um progestágeno de quarta geração, conhecido principalmente pelo uso no tratamento da endometriose. Não há indicação original registrada no Brasil nos dados compilados para este relatório.
O modelo TxGNN prevê que pode ser eficaz para **Amenorreia (amenorrhea)**, atualmente com **0 ensaios clínicos** e **7 publicações** associadas a esta direção. Nenhuma delas demonstra benefício terapêutico na amenorreia, que é um efeito esperado do fármaco.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Não disponível (nenhuma licença registrada no Brasil) |
| Nova Indicação Prevista | Amenorreia (amenorrhea) |
| Pontuação de Previsão TxGNN | 99,71% |
| Nível de Evidência | L4 |
| Situação no Mercado Brasileiro | Não comercializado |
| Número de Registros | 0 |
| Decisão Recomendada | Hold |

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação nos dados compilados. Segundo informações conhecidas, o dienogeste é um progestágeno com forte atividade antiproliferativa sobre o endométrio, além de supressão parcial da ovulação e do estradiol. É usado na endometriose, e a amenorreia é um efeito bem conhecido desse tratamento.

A relação com a nova indicação é, portanto, biologicamente plausível, mas com ressalva importante: a amenorreia aqui é um **efeito farmacodinâmico ou adverso esperado** (supressão do sangramento), não um alvo terapêutico. A amenorreia, como doença (ausência de menstruação), não é um objetivo de tratamento adequado para um fármaco que a provoca. A supressão do eixo hipotálamo-hipófise-ovário poderia, em teoria, ajudar em sangramento uterino anormal, mas isso é outra indicação.

A pontuação alta do TxGNN provavelmente reflete a associação fármaco-doença no grafo de conhecimento, e não benefício terapêutico real. Outras previsões do modelo, como falência ovariana primária, hipogonadismo hipogonadotrófico e deficiência isolada de hormônio do crescimento, também carecem de plausibilidade mecanística e de evidências.

## Evidências da Literatura

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [39090694](https://pubmed.ncbi.nlm.nih.gov/39090694/) | 2024 | Revisão sistemática/meta-análise | BMC Pharmacol Toxicol | Resume os eventos adversos associados ao dienogeste e sua prevalência em endometriose e adenomiose |
| [29161960](https://pubmed.ncbi.nlm.nih.gov/29161960/) | 2018 | Coorte retrospectiva | Reprod Sci | 514 mulheres com endometrioma ovariano; avaliou eficácia, segurança e recorrência com uso prolongado (>12 meses) de 2 mg/dia |
| [34405378](https://pubmed.ncbi.nlm.nih.gov/34405378/) | 2022 | Revisão | Rev Endocr Metab Disord | Base endócrina dos tratamentos hormonais da endometriose (dependência de estrogênio e resistência à progesterona) |
| [41329046](https://pubmed.ncbi.nlm.nih.gov/41329046/) | 2026 | Estudo farmacodinâmico/clínico | Eur J Contracept Reprod Health Care | Dienogeste 2 mg com alta taxa de inibição e índice de transformação na endometriose; um dos objetivos dos tratamentos hormonais é induzir amenorreia |
| [40543564](https://pubmed.ncbi.nlm.nih.gov/40543564/) | 2025 | Revisão | J Pediatr Adolesc Gynecol | Visualização avançada (3D/RV) de anomalias müllerianas para diagnóstico e planejamento cirúrgico; relação indireta |
| [34918698](https://pubmed.ncbi.nlm.nih.gov/34918698/) | 2021 | Relato de caso | Medicine | Tumor de células da granulosa ovariano em paciente com síndrome dos ovários policísticos; relação indireta |
| [42438810](https://pubmed.ncbi.nlm.nih.gov/42438810/) | 2026 | Relato de caso | JCEM Case Rep | Hiperparatireoidismo primário evidenciado cerca de 6 meses após início de dienogeste 0,5 mg 2x/dia por menorragia |

Nenhum estudo avalia o dienogeste como tratamento da amenorreia.

## Considerações de Segurança

- **Contraindicações descritas na base de conhecimento do modelo (não é texto de bula)**: hipertensão, epilepsia, transtornos de ansiedade e neuróticos, distimia, porfirias, doença renal, doença hepática, doença da vesícula biliar, hipotireoidismo, lúpus eritematoso sistêmico, asma, diabetes mellitus e cetoacidose diabética, hipertrigliceridemia, hipercalcemia e nefrocalcinose, carcinoma de mama feminino e tromboflebite.
- **Interações medicamentosas**: 37 interações identificadas. Entre as de nível **grave**: sugamadex, griseofulvina, bexaroteno, brigatinibe, dabrafenibe e encorafenibe. Entre as de nível **moderado**: linaclotida, metreleptina, prucaloprida, miltefosina, adalimumabe, alefacepte, anakinra, asparaginase, canaquinumabe, certolizumabe pegol, cladribina, emapalumabe e enasidenibe. Etanol tem nível leve.
- **Sinal de segurança na literatura**: relato de caso de hiperparatireoidismo primário evidenciado após o início do dienogeste (PMID 42438810), com alteração da homeostase do cálcio.

Consulte a bula para as advertências e contraindicações oficiais.

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
- A previsão tem pontuação alta no modelo, mas a amenorreia é um efeito esperado do dienogeste, não um objetivo terapêutico. Não há ensaios clínicos, e a literatura não apoia eficácia. O fármaco não está comercializado no Brasil.

**Para prosseguir, é necessário:**
- Definir se há uma indicação clínica real por trás do sinal, por exemplo sangramento uterino anormal ou endometriose, em vez de amenorreia como doença.
- Obter dados de mecanismo de ação do DrugBank.
- Obter as advertências e contraindicações da bula na ANVISA, hoje uma lacuna que bloqueia a triagem de segurança.
- Verificar a situação regulatória do dienogeste no Brasil (nenhum registro nos dados compilados).
- Analisar o risco-benefício, dadas as contraindicações e as interações graves identificadas.
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

