---
layout: default
title: Miglustat
parent: Apenas Predição do Modelo (L5)
nav_order: 459
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-31
monitor_inn: "miglustat"
predicted_indications: ["autosomal ichthyosis syndrome with fatal disease course", "cholesteryl ester storage disease", "Krabbe disease", "metachromatic leukodystrophy", "Wolman disease with hypolipoproteinemia and acanthocytosis", "encephalopathy due to prosaposin deficiency", "Tay-Sachs disease", "benign neoplasm of adrenal gland", "recessive X-linked ichthyosis", "fatty acid hydroxylase-associated neurodegeneration"]
description: "Miglustat: nova indicação prevista, Autosomal ichthyosis syndrome with fatal disease course (nível de evidência L5). Indicação original: OUTROS PRODS NAO ENQUADRADOS EM CLASSE TERAPEUTICA ESPECIF"
---

# Miglustat
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

## Miglustat: Autosomal ichthyosis syndrome with fatal disease course
{: .text-alpha }

## Resumo em Uma Frase

Miglustate (nome comercial ZAVESCA) é um inibidor da glicosilceramida sintase, registrado na ANVISA em uma categoria terapêutica genérica ("outros produtos não enquadrados em classe terapêutica específica"); na literatura, é usado no tratamento da doença de Gaucher.
O modelo TxGNN prevê que pode ser eficaz para a **doença de Tay-Sachs (Tay-Sachs disease)**, a previsão de maior sustentação entre as 10 avaliadas, atualmente com **4 ensaios clínicos** e **11 publicações** apoiando esta direção.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | OUTROS PRODS NAO ENQUADRADOS EM CLASSE TERAPEUTICA ESPECIF |
| Nova Indicação Prevista | Autosomal ichthyosis syndrome with fatal disease course |
| Pontuação de Previsão TxGNN | 0.9983 |
| Nível de Evidência | L5 (conforme classificação dos dados compilados; ver ressalva abaixo) |
| Situação no Mercado Brasileiro | Comercializado (registros ativos: 1 de 2) |
| Número de Registros | 2 (ativos: 1) |
| Decisão Recomendada | Proceed with Guardrails |

**Ressalva sobre a escolha da indicação:** a primeira indicação da lista de previsões (ictiose autossômica com curso fatal, pontuação 0,9983) não tem nenhum ensaio ou publicação. Neste relatório, foi destacada a doença de Tay-Sachs (7ª colocada, 0,9975), pois é a única previsão com evidências reais. As demais previsões estão resumidas ao final.

**Ressalva sobre o nível de evidência:** o nível L1 foi atribuído nos dados compilados, mas os ensaios de Fase 3 listados são pequenos (n=10 e n=30), um deles foi encerrado precocemente e nenhum demonstrou eficácia clara. O nível deve ser interpretado com cautela.

---

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação na base compilada. Segundo a literatura, o miglustate é um inibidor oral de pequena massa molecular da glicosilceramida sintase (gene UGCG), que reduz a síntese de glicoesfingolipídios derivados da glicosilceramida. Está aprovado em outros países para a doença de Gaucher tipo 1.

Na doença de Tay-Sachs, a deficiência da enzima β-hexosaminidase A causa acúmulo do gangliosídeo GM2, principalmente nos neurônios. A lógica da terapia de redução de substrato é diminuir a síntese desse gangliosídeo, de modo que a atividade enzimática residual consiga dar conta do que é produzido. O miglustate atravessa a barreira hematoencefálica, o que é relevante para uma doença neuronopática.

A coerência mecanística é boa, mas os resultados clínicos são mistos. Um relato de dois pacientes com a forma infantil mostrou concentração significativa do fármaco no líquor e prevenção de macrocefalia, porém sem deter a deterioração neurológica. A revisão sistemática de 2023 aponta que os resultados anteriores sobre eficácia e segurança foram inconsistentes.

---

## Evidências de Ensaios Clínicos

| Número do Ensaio | Fase | Status | Participantes | Principais Achados |
|---------|------|------|------|---------|
| [NCT00672022](https://clinicaltrials.gov/study/NCT00672022) | Phase 3 | Concluído | 10 | Farmacocinética, segurança e tolerabilidade do miglustate em gangliosidose GM2 de início infantil (2004–2007); amostra pequena, desenho voltado a segurança e PK |
| [NCT02030015](https://clinicaltrials.gov/study/NCT02030015) | Phase 4 | Terminado | 16 | Estudo Syner-G: miglustate associado a dieta cetogênica em gangliosidoses; o regime combinado dificulta atribuir efeitos ao miglustate, e o término precoce limita conclusões |
| [NCT00418847](https://clinicaltrials.gov/study/NCT00418847) | Phase 2 | Concluído | 5 | Farmacocinética e tolerabilidade em gangliosidose GM2 juvenil; amostra muito pequena |
| [NCT03822013](https://clinicaltrials.gov/study/NCT03822013) | Phase 3 | Terminado | 30 | Efeitos do miglustate em sintomas neurológicos e sistêmicos das formas infantis de Sandhoff e Tay-Sachs (2019–2025); encerrado precocemente |

---

## Evidências da Literatura

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [19346952](https://pubmed.ncbi.nlm.nih.gov/19346952/) | 2009 | RCT | Genetics in Medicine | Estudo randomizado e controlado de 12 meses, com 24 meses de extensão, sobre segurança e eficácia do miglustate na gangliosidose GM2 (Tay-Sachs de início tardio) |
| [37209042](https://pubmed.ncbi.nlm.nih.gov/37209042/) | 2023 | Revisão sistemática | European Journal of Neurology | Avalia eficácia e segurança do miglustate na gangliosidose GM2, diante de resultados prévios inconsistentes |
| [42794762](https://pubmed.ncbi.nlm.nih.gov/42794762/) | 2026 | Revisão | Int J Mol Sci | Racional biológico, evidência clínica e limites do reposicionamento do miglustate em doenças lisossômicas neuronopáticas; o fármaco cruza a barreira hematoencefálica |
| [16434676](https://pubmed.ncbi.nlm.nih.gov/16434676/) | 2006 | Série de casos | Neurology | Dois pacientes com Tay-Sachs infantil: o fármaco chegou ao líquor e evitou macrocefalia, mas não interrompeu a deterioração neurológica |
| [30743792](https://pubmed.ncbi.nlm.nih.gov/30743792/) | 2009 | Revisão | Expert Rev Endocrinol Metab | Terapia de redução de substrato com miglustate em doenças de armazenamento de glicoesfingolipídios com acometimento cerebral |
| [16763917](https://pubmed.ncbi.nlm.nih.gov/16763917/) | 2006 | Revisão | J Inherit Metab Dis | Terapia de redução de substrato em doenças de armazenamento de glicoesfingolipídios |
| [30524313](https://pubmed.ncbi.nlm.nih.gov/30524313/) | 2018 | Revisão | Frontiers in Physiology | Novas abordagens terapêuticas para a doença de Tay-Sachs |
| [28476546](https://pubmed.ncbi.nlm.nih.gov/28476546/) | 2017 | História natural/Revisão | Mol Genet Metab | Cronologia clínica das gangliosidoses infantis; o miglustate foi tentado, mas limitado por efeitos adversos gastrointestinais |
| [12808890](https://pubmed.ncbi.nlm.nih.gov/12808890/) | 2003 | Perfil do fármaco | Curr Opin Investig Drugs | Miglustate desenvolvido para Gaucher tipo 1 e em estudo para Tay-Sachs, Fabry e Niemann-Pick tipo C |
| [18618288](https://pubmed.ncbi.nlm.nih.gov/18618288/) | 2008 | Estudo piloto | J Inherit Metab Dis | Testes neurocognitivos na doença de Tay-Sachs de início tardio como possível desfecho clínico |

---

## Informações de Comercialização no Brasil

| Registro | Produto | Empresa detentora | Situação |
|------|------|------|------|
| 112363431 | ZAVESCA | JANSSEN-CILAG FARMACÊUTICA LTDA | Ativo |
| 155380002 | ZAVESCA | ACTELION PHARMACEUTICALS DO BRASIL LTDA | Cancelado |

---

## Considerações de Segurança

- **Contraindicações segundo o grafo de conhecimento (não é texto de bula):** doença do sistema nervoso periférico, neuropatia periférica e doença com comprometimento da função renal.
- **Interações Medicamentosas:**
  - **Imiglucerase** (gravidade moderada, fonte DDInter).
  - O alvo farmacológico do miglustate é a UDP-glicose ceramida glicosiltransferase (UGCG), o que corresponde ao mecanismo de ação, não a uma interação adversa.
- Na literatura, foram descritos efeitos adversos gastrointestinais que limitam o uso em gangliosidoses infantis.

Para advertências e contraindicações formais, consulte a bula.

---

## Conclusão e Próximos Passos

**Decisão: Proceed with Guardrails**

**Justificativa:**
Há racional mecanístico coerente e ensaios clínicos reais em gangliosidose GM2, mas os estudos são pequenos, vários foram encerrados precocemente e os resultados de eficácia são inconsistentes. Os dados de segurança da bula brasileira estão ausentes e o único registro no Brasil está cancelado, de modo que só se justifica avançar como questão de pesquisa, com salvaguardas.

**Para prosseguir, é necessário:**
- Obter a bula da ANVISA (advertências e contraindicações), lacuna que bloqueia a triagem de segurança.
- Complementar os dados oficiais de mecanismo de ação (DrugBank).
- Analisar em detalhe os resultados do RCT de 2009 (PMID 19346952) e da revisão sistemática de 2023 (PMID 37209042).
- Definir plano de monitoramento de segurança, em especial para neuropatia periférica, função renal e efeitos gastrointestinais.
- Avaliar a situação regulatória: o registro cancelado implica que um novo registro ou uso excepcional seria necessário no Brasil.

---

## Outras Previsões do Modelo (Apenas Previsão, Sem Evidências)

Todas com nível L5 e recomendação **Hold**, sem ensaios clínicos ou literatura nos dados compilados:

| Posição | Doença | Pontuação TxGNN | Observação |
|------|------|------|------|
| 1 | Síndrome de ictiose autossômica com curso fatal | 0,9983 | Vínculo apenas teórico com o metabolismo de glicoesfingolipídios e ceramidas da epiderme |
| 2 | Doença de armazenamento de ésteres de colesterol | 0,9982 | Deficiência de lipase ácida lisossômica; sem relevância mecanística clara |
| 3 | Doença de Krabbe | 0,9978 | Conceito de redução de substrato plausível, mas não validado; o substrato difere do alvo principal |
| 4 | Leucodistrofia metacromática | 0,9977 | Vínculo indireto (via do sulfatídeo distinta da glicosilceramida) |
| 5 | Doença de Wolman com hipolipoproteinemia e acantocitose | 0,9976 | Deficiência de lipase ácida; sem vínculo claro |
| 6 | Encefalopatia por deficiência de prosaposina | 0,9975 | Redução de substrato conceitualmente plausível, sem evidência clínica |
| 8 | Neoplasia benigna da glândula adrenal | 0,9974 | Nenhum mecanismo plausível identificado |
| 9 | Ictiose recessiva ligada ao X | 0,9973 | Vínculo especulativo |
| 10 | Neurodegeneração associada à hidroxilase de ácidos graxos | 0,9972 | Direção do efeito incerta |
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

