---
layout: default
title: Vancomycin
parent: Apenas Predição do Modelo (L5)
nav_order: 665
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-31
description: "Vancomycin: nova indicação prevista, Esclerodermia difusa (diffuse scleroderma) (nível de evidência L5). Indicação original: Antibióticos sistêmicos simples"
monitor_inn: "Vancomycin"
predicted_indications: ["diffuse scleroderma", "paratyphoid fever", "salmonellosis", "congenital analbuminemia", "polyclonal hyperviscosity syndrome", "hyperamylasemia", "typhoid fever", "blood group incompatibility", "streptococcal pneumonia", "premalignant hematological system disease"]
---

# Vancomycin
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

## Vancomicina: De antibiótico sistêmico para esclerodermia difusa
{: .text-alpha }

## Resumo em Uma Frase

A vancomicina é um antibiótico glicopeptídico, registrado no Brasil como "antibiótico sistêmico simples".
O modelo TxGNN prevê que ela pode ser eficaz para **esclerodermia difusa (diffuse scleroderma)**, mas **não há ensaios clínicos** e a única publicação encontrada é um relato de caso sobre erupção esfoliativa com sepse, sem relação com o tratamento da esclerodermia. A previsão parece ser um artefato do modelo.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Antibióticos sistêmicos simples |
| Nova Indicação Prevista | Esclerodermia difusa (diffuse scleroderma) |
| Pontuação de Previsão TxGNN | 0,9992 |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | Comercializado (registros ativos: 10 de 41) |
| Número de Registros | 41 (ativos: 10) |
| Decisão Recomendada | Hold |

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação nos dados compilados para este relatório. Segundo informações conhecidas, a vancomicina é um antibiótico glicopeptídico que inibe a síntese da parede celular bacteriana, ligando-se às extremidades D-Ala-D-Ala dos precursores do peptideoglicano. Sua eficácia está estabelecida em infecções por bactérias Gram-positivas.

**Na prática, a previsão não se sustenta.** A esclerodermia difusa é uma doença autoimune e fibrótica, sem causa bacteriana, e não existe vínculo mecanístico plausível com um inibidor da síntese da parede celular bacteriana. A pontuação alta do TxGNN (0.9992) vem do modelo TxGNN (deep learning) e pode refletir semelhanças que o modelo aprendeu entre doenças relacionadas, não evidência biológica. O único artigo recuperado (relato de caso de erupção esfoliativa com sepse e eosinofilia, 2019) não trata de esclerodermia.

### Outras previsões avaliadas

Outras indicações previstas também foram analisadas e, em geral, carecem de fundamento:

- **Febre paratifoide, salmonelose e febre tifoide:** os agentes são bactérias Gram-negativas (Salmonella), intrinsecamente resistentes à vancomicina, que não atravessa a membrana externa. A literatura recuperada trata de vigilância de resistência e relatos de caso, sem evidência de eficácia.
- **Analbuminemia congênita, hiperamilasemia, síndrome de hiperviscosidade policlonal, incompatibilidade de grupo sanguíneo e doença hematológica pré-maligna:** não há vínculo mecanístico nem estudos.
- **Pneumonia estreptocócica:** é a única com mecanismo plausível (a vancomicina atua contra *Streptococcus pneumoniae*, incluindo cepas resistentes à penicilina), mas trata-se de uso antibacteriano já estabelecido, não de reposicionamento real. A literatura é composta por revisões e vigilância de resistência, sem ensaios registrados. Nível de evidência L4, classificada como "questão de pesquisa".

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados.

## Evidências da Literatura

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [31541072](https://pubmed.ncbi.nlm.nih.gov/31541072/) | 2019 | Relato de caso | The American Journal of Case Reports | Homem de 56 anos com erupção esfoliativa difusa, sepse e eosinofilia (investigação de eritrodermia). Não aborda tratamento de esclerodermia com vancomicina. |

## Informações de Comercialização no Brasil

O medicamento é comercializado no Brasil: os 10 registros estão válidos (10 de 10).

| Registro | Produto | Empresa detentora | Situação |
|------|------|------|------|
| 102980511 | VANK | CRISTÁLIA PRODUTOS QUÍMICOS FARMACÊUTICOS LTDA. | Ativo |
| 103700461 | CLORIDRATO DE VANCOMICINA | LABORATÓRIO TEUTO BRASILEIRO S/A | Ativo |
| 104970242 | VANCOTRAT | UNIÃO QUÍMICA FARMACÊUTICA NACIONAL S/A | Ativo |
| 110110010 | NOVAMICIN | NEWCOM FARMACEUTICA LTDA. | Ativo |
| 110110023 | CLORIDRATO DE VANCOMICINA | NEWCOM FARMACEUTICA LTDA. | Ativo |
| 116370092 | CLORIDRATO DE VANCOMICINA | BLAU FARMACÊUTICA S.A. | Ativo |
| 116370114 | VANCOSON | BLAU FARMACÊUTICA S.A. | Ativo |
| 116370183 | HICOVAN | BLAU FARMACÊUTICA S.A. | Ativo |
| 155620005 | VANCOCINA CP | ANTIBIÓTICOS DO BRASIL LTDA | Ativo |
| 155620041 | CLORIDRATO DE VANCOMICINA | ANTIBIÓTICOS DO BRASIL LTDA | Ativo |
| 100410188 | NOVAMICIN | FRESENIUS KABI BRASIL LTDA | Cancelado |
| 100410202 | CLORIDRATO DE VANCOMICINA | FRESENIUS KABI BRASIL LTDA | Cancelado |
| 100430579 | VANCOMICINA | EUROFARMA LABORATORIOS S.A. | Cancelado |
| 100430709 | CLORIDRATO DE VANCOMICINA | EUROFARMA LABORATORIOS S.A. | Cancelado |
| 100630157 | VANCOCID | INSTITUTO BIOCHIMICO INDÚSTRIA FARMACÊUTICA LTDA | Cancelado |
| 102700083 | VANCOSON | ARISTON INDS QUIMS FTCAS LTDA | Cancelado |
| 102700129 | CLORIDRATO DE VANCOMICINA | ARISTON INDS QUIMS FTCAS LTDA | Cancelado |
| 103110123 | HICOVAN | HALEX ISTAR INDÚSTRIA FARMACÊUTICA SA | Cancelado |
| 103110137 | HICOVAN | HALEX ISTAR INDÚSTRIA FARMACÊUTICA SA | Cancelado |
| 103460017 | CLORIDRATO DE VANCOMICINA | BEKER PRODUTOS FÁRMACO HOSPITALARES LTDA | Cancelado |
| 103700230 | VANCLOMIN | LABORATÓRIO TEUTO BRASILEIRO S/A | Cancelado |
| 104080039 | VANCOPLUS | ROYTON QUÍMICA FARMACÊUTICA LTDA | Cancelado |
| 105530211 | VANCOABBOTT | ABBOTT LABORATÓRIOS DO BRASIL LTDA | Cancelado |
| 106460132 | AMPLOBAC | LABORATORIO QUIMICO FARMACEUTICO BERGAMO LTDA | Cancelado |
| 108580168 | CLORIDRATO DE VANCOMICINA | PRODOTTI LABORATÓRIO FARMACÊUTICO LTDA. | Cancelado |
| 111020002 | EDICIN | INTERLAB FARMACÊUTICA LTDA | Cancelado |
| 112600013 | VANCOCINA CP | ELI LILLY DO BRASIL LTDA | Cancelado |
| 112830046 | VANCO - MAX | LABORATORIO ITAFARMA LTDA | Cancelado |
| 114020029 | NOVAMICIN | NOVAFARMA INDÚSTRIA FARMACÊUTICA LTDA | Cancelado |
| 114020090 | CLORIDRATO DE VANCOMICINA | NOVAFARMA INDÚSTRIA FARMACÊUTICA LTDA | Cancelado |

A tabela mostra até 30 registros (os ativos primeiro). A lista completa está na consulta de medicamentos da ANVISA (https://consultas.anvisa.gov.br/#/medicamentos/).

## Considerações de Segurança

- **Contraindicações segundo o grafo de conhecimento (não é texto de bula):** doença renal, piureter, neutropenia, agranulocitose, distúrbio auditivo e doenças do sistema auditivo.
- **Interações medicamentosas:** foram identificadas 100 interações; entre as principais:
  - **Graves (Major):** imunoglobulina G humana intravenosa, imunoglobulina humana antitoxina botulínica A/B e vacina viva contra cólera (*Vibrio cholerae* CVD 103-HgR).
  - **Moderadas:** anti-inflamatórios não esteroidais (cetorolaco, ibuprofeno, diclofenaco, celecoxibe), anfotericina B (incluindo complexo lipídico), amicacina, capreomicina, carboplatina, bacitracina, mesalazina, balsalazida, ibandronato, metformina, estradiol, etinilestradiol e colestiramina. Vários deles têm potencial nefrotóxico ou ototóxico aditivo.

Para advertências e contraindicações baseadas em bula, consulte a bula; esses dados ainda não foram obtidos.

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
- Para esclerodermia difusa, não há ensaios clínicos, a literatura recuperada é irrelevante e não existe vínculo mecanístico plausível. A pontuação alta do TxGNN (0.9992) vem do modelo TxGNN (deep learning) e pode refletir semelhanças aprendidas entre doenças relacionadas, não evidência biológica; o nível de evidência é L5. O medicamento é comercializado no Brasil, com 10 registros válidos de 10.

**Para prosseguir, é necessário:**
- Não há justificativa para investir em esclerodermia; recomenda-se não avançar nessa direção, salvo surgimento de evidência biológica nova.
- Obter e analisar a bula da ANVISA (advertências e contraindicações), lacuna que impede a triagem de segurança.
- Complementar os dados de mecanismo de ação (por exemplo, via DrugBank).
- Se houver interesse em uma direção plausível, tratar a pneumonia estreptocócica como questão de pesquisa, reconhecendo que é uso antibacteriano já existente e não reposicionamento, e confirmar a situação regulatória atual da vancomicina no Brasil.
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

