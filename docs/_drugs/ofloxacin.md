---
layout: default
title: Ofloxacin
parent: Apenas Predição do Modelo (L5)
nav_order: 483
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-31
description: "Ofloxacin: nova indicação prevista, Polyclonal hyperviscosity syndrome (síndrome de hiperviscosidade poli… (nível de evidência L5). Indicação original: Antiinfecciosos"
monitor_inn: "ofloxacin"
predicted_indications: ["polyclonal hyperviscosity syndrome", "hyperamylasemia", "congenital analbuminemia", "blood group incompatibility", "premalignant hematological system disease", "monoclonal gammopathy", "hematological disease associated with an acquired peripheral neuropathy", "septicemic plague", "congenital hematological disorder", "punctate epithelial keratoconjunctivitis"]
---

# Ofloxacin
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

## Ofloxacino: De antiinfeccioso a polyclonal hyperviscosity syndrome (previsão do modelo, sem evidências)
{: .text-alpha }

## Resumo em Uma Frase

Ofloxacino é um antibiótico fluoroquinolona, registrado no Brasil como antiinfeccioso (inclusive de uso oftálmico tópico) e antibiótico sistêmico simples.
O modelo TxGNN prevê que pode ser eficaz para a **síndrome de hiperviscosidade policlonal (polyclonal hyperviscosity syndrome)**, mas a previsão não tem **nenhum ensaio clínico** nem **nenhuma publicação** que a sustente.
Entre as 10 previsões analisadas, a mais bem sustentada por dados é a **peste septicêmica (septicemic plague)**, com 11 publicações pré-clínicas (estudos in vitro e em animais).

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Antiinfecciosos |
| Nova Indicação Prevista | Polyclonal hyperviscosity syndrome (síndrome de hiperviscosidade policlonal) |
| Pontuação de Previsão TxGNN | 0,9991 |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | Comercializado (registros ativos: 6 de 30) |
| Número de Registros | 30 (ativos: 6) |
| Decisão Recomendada | Hold |

> Observação: as 10 previsões têm pontuações muito próximas (0,9957 a 0,9991), então a posição no ranking do modelo não distingue bem a plausibilidade biológica. A pontuação da previsão de maior valor vem do modelo TxGNN (aprendizado profundo) e pode refletir semelhanças que o modelo aprendeu entre doenças relacionadas, não evidência biológica. A tabela abaixo resume as demais previsões.

| Posição | Indicação prevista | Pontuação TxGNN | Nível | Recomendação |
|------|------|------|------|------|
| 1 | Polyclonal hyperviscosity syndrome | 0,9991 | L5 | Hold |
| 2 | Hiperamilasemia (hyperamylasemia) | 0,9991 | L5 | Hold |
| 3 | Analbuminemia congênita | 0,9990 | L5 | Hold |
| 4 | Incompatibilidade de grupo sanguíneo | 0,9986 | L5 | Hold |
| 5 | Doença hematológica pré-maligna | 0,9984 | L5 | Hold |
| 6 | Gamopatia monoclonal | 0,9982 | L5 | Hold |
| 7 | Doença hematológica associada a neuropatia periférica adquirida | 0,9980 | L5 | Hold |
| 8 | Peste septicêmica | 0,9979 | L4 | Questão de pesquisa |
| 9 | Distúrbio hematológico congênito | 0,9972 | L5 | Hold |
| 10 | Ceratoconjuntivite epitelial punctata | 0,9957 | L4 | Hold |

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação no material compilado. Segundo informações conhecidas, o ofloxacino é uma fluoroquinolona que inibe a DNA girase e a topoisomerase IV bacterianas, e sua eficácia antibacteriana está estabelecida.

Para a previsão principal (síndrome de hiperviscosidade policlonal), **não há vínculo mecanístico plausível**: o ofloxacino não tem efeito conhecido sobre a viscosidade sérica nem sobre a elevação policlonal de imunoglobulinas. A pontuação alta vem do modelo TxGNN (aprendizado profundo) e pode refletir semelhanças que o modelo aprendeu entre doenças relacionadas, não evidência biológica. O mesmo vale para hiperamilasemia, analbuminemia congênita, doenças hematológicas e gamopatia monoclonal. Para a doença hematológica associada a neuropatia periférica, as fluoroquinolonas podem causar neuropatia periférica como efeito adverso, o que contraria a hipótese de benefício e levanta preocupação de segurança.

Duas previsões têm algum respaldo biológico, ambas como extensão do uso antibacteriano já conhecido, e não como um novo mecanismo:
- **Peste septicêmica:** *Yersinia pestis* é sensível às fluoroquinolonas in vitro, e há estudos em camundongos e em outros animais com ofloxacino em peste pneumônica e bubônica experimental.
- **Ceratoconjuntivite epitelial punctata:** o ofloxacino já é usado como antibacteriano oftálmico, então o uso na superfície ocular é plausível para tratar ou prevenir infecção bacteriana secundária. Muitos casos, porém, são virais ou alérgicos, nos quais antibacterianos não oferecem benefício primário.

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados para a previsão principal nem para as demais previsões analisadas.

## Evidências da Literatura

Para a previsão principal (síndrome de hiperviscosidade policlonal), atualmente não há literatura relacionada. Para as demais previsões, a literatura recuperada é a seguinte (até 10 publicações mais relevantes, priorizando a previsão mais bem sustentada, a peste septicêmica):

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [9517950](https://pubmed.ncbi.nlm.nih.gov/9517950/) | 1998 | Estudo animal | Antimicrob Agents Chemother | Modelo murino de peste pneumônica para comparar o tratamento antibiótico com estreptomicina e outros antibióticos |
| [16127904](https://pubmed.ncbi.nlm.nih.gov/16127904/) | 2002 | Estudo animal | Antibiot Khimioter | Eficácia do ofloxacino na profilaxia e no tratamento de peste experimental em camundongos; menor eficácia com cepas sem fração I e toxina murina |
| [8203841](https://pubmed.ncbi.nlm.nih.gov/8203841/) | 1994 | Estudo animal | Antimicrob Agents Chemother | Ofloxacino, entre outros antibióticos, foi ativo in vitro e avaliado em infecção murina sistêmica por *Y. pestis* |
| [8540736](https://pubmed.ncbi.nlm.nih.gov/8540736/) | 1995 | In vitro | Antimicrob Agents Chemother | Em 78 cepas de *Y. pestis*, ceftriaxona e ciprofloxacino foram os mais ativos, seguidos de ofloxacino e ampicilina |
| [8913481](https://pubmed.ncbi.nlm.nih.gov/8913481/) | 1996 | In vitro | Antimicrob Agents Chemother | Em 100 isolados humanos, ofloxacino e levofloxacino tiveram alta atividade (CIM90 < 0,03 µg/mL) |
| [10987101](https://pubmed.ncbi.nlm.nih.gov/10987101/) | 2000 | Estudo animal | Antibiot Khimioter | Fluoroquinolonas, incluindo ofloxacino, impediram a formação de imunidade pós-vacinal em camundongos; uma cepa vacinal resistente permitiu a imunidade |
| [11871319](https://pubmed.ncbi.nlm.nih.gov/11871319/) | 2001 | Estudo animal | Antibiot Khimioter | Modelo de peste bubônica em babuínos para avaliar a eficácia de novos antibacterianos |
| [11858365](https://pubmed.ncbi.nlm.nih.gov/11858365/) | 2002 | Relato de caso | Joint Bone Spine | Discite por *S. lugdunensis* em paciente com mieloma múltiplo tratado com ofloxacino e pristinamicina; o artigo não trata de gamopatia monoclonal como alvo terapêutico |
| [16670489](https://pubmed.ncbi.nlm.nih.gov/16670489/) | 2006 | Relato de caso | Cornea | Cicatrização de úlcera em escudo vernal após desbridamento cirúrgico; evidência indireta |
| [18644132](https://pubmed.ncbi.nlm.nih.gov/18644132/) | 2008 | In vitro | BMC Microbiol | Triagem de determinantes de resistência a antibióticos em *Y. pestis*; apenas indiretamente relevante |

Outros trabalhos recuperados tratam de resistência em outros organismos (por exemplo, *Burkholderia pseudomallei* e *Vibrio cholerae*) ou de mutantes resistentes de *Y. pestis*, e têm relevância apenas indireta. Um artigo sobre estreptococo beta-hemolítico (PMID 22808724) foi associado à incompatibilidade de grupo sanguíneo, mas parece ser um artefato de palavras-chave.

## Informações de Comercialização no Brasil

Todos os 8 registros estão vigentes (8 licenças válidas de 8); o medicamento é comercializado no Brasil.

| Registro | Produto | Empresa detentora | Situação |
|------|------|------|------|
| 101470027 | OFLOX | ALLERGAN PRODUTOS FARMACÊUTICOS LTDA | Ativo |
| 102350779 | OFLOXACINO | EMS S/A | Ativo |
| 102980492 | NOSTIL | CRISTÁLIA PRODUTOS QUÍMICOS FARMACÊUTICOS LTDA. | Ativo |
| 107150097 | FLOXINA | CAZI QUIMICA FARMACEUTICA INDUSTRIA E COMERCIO LTD | Ativo |
| 126250061 | LFM - OFLOXACINO | LABORATÓRIO FARMACÊUTICO DA MARINHA | Ativo |
| 167730555 | OFLOXALIS | LEGRAND PHARMA INDÚSTRIA FARMACÊUTICA LTDA | Ativo |
| 100230246 | OFLOXACINO | ALCON LABORATÓRIOS DO BRASIL LTDA. | Cancelado |
| 102700116 | OXITOPENA | ARISTON INDS QUIMS FTCAS LTDA | Cancelado |
| 103700384 | OFLOXACINO | LABORATÓRIO TEUTO BRASILEIRO S/A | Cancelado |
| 104650507 | OFLOXACINO | LABORATÓRIO NEO QUÍMICA COMÉRCIO E INDÚSTRIA LTDA | Cancelado |
| 104970260 | OFLOXITRAT | UNIÃO QUÍMICA FARMACÊUTICA NACIONAL S/A | Cancelado |
| 104971284 | GENOXACIN | UNIÃO QUÍMICA FARMACÊUTICA NACIONAL S/A | Cancelado |
| 105730423 | OFLOXACINO | ACHÉ LABORATÓRIOS FARMACÊUTICOS S.A | Cancelado |
| 105830453 | OFLOXACINO | GERMED FARMACEUTICA LTDA | Cancelado |
| 105830871 | OFLOXACINO | GERMED FARMACEUTICA LTDA | Cancelado |
| 108840356 | IQUEGO-OFLOXACINO | INDÚSTRIA QUÍMICA DO ESTADO DE GOIÁS S/A - IQUEGO | Cancelado |
| 112080033 | LQFEX - OFLOXACINO | LABORATÓRIO QUÍMICO FARMACÊUTICO DO EXÉRCITO | Cancelado |
| 112130437 | OFLOXACINO | BIOSINTÉTICA FARMACÊUTICA LTDA | Cancelado |
| 112363340 | FLOXSTAT | JANSSEN-CILAG FARMACÊUTICA LTDA | Cancelado |
| 117250016 | NOSTIL | LATINOFARMA INDUSTRIAS FARMACEUTICAS LTDA | Cancelado |
| 123520082 | OFLOXACINO | RANBAXY FARMACÊUTICA LTDA | Cancelado |
| 123610008 | OFLOCIN | UCB BIOPHARMA LTDA. | Cancelado |
| 135690324 | OFLOXACINO | EMS SIGMA PHARMA LTDA | Cancelado |
| 137640056 | FLOGIRAX | ASPEN PHARMA INDÚSTRIA FARMACÊUTICA LTDA | Cancelado |
| 148690018 | GENOXACIN | FORMIL FARMACÊUTICA LTDA | Cancelado |
| 155840312 | OFLOXACINO | BRAINFARMA INDÚSTRIA QUÍMICA E FARMACÊUTICA S.A | Cancelado |
| 167730240 | OFLOXACINO | LEGRAND PHARMA INDÚSTRIA FARMACÊUTICA LTDA | Cancelado |
| 167730512 | OFLOXACINO | LEGRAND PHARMA INDÚSTRIA FARMACÊUTICA LTDA | Cancelado |
| 172870405 | OFLOXACINO | HYPERA S.A. | Cancelado |
| 178170124 | OFLOXINO | COSMED INDUSTRIA DE COSMETICOS E MEDICAMENTOS S.A. | Cancelado |

## Considerações de Segurança

- **Contraindicações (associações do grafo de conhecimento, não texto de bula):** síndrome do QT longo (inclusive familiar) e torsades de pointes; insuficiência e doença hepáticas, lesão hepática induzida por fármacos; doença renal e função renal comprometida; epilepsia; miastenia gravis e doenças da junção neuromuscular; tendinite e outras doenças de tendão e periarticulares; neuropatia periférica; diabetes mellitus e cetoacidose diabética; rabdomiólise; trombocitopenia, leucopenia e anemias; deficiência de potássio; colite por *Clostridium difficile*; doenças da vesícula biliar.
- **Interações medicamentosas:** foram identificadas 383 interações. Entre as listadas, as de gravidade **maior** incluem corticosteroides (hidrocortisona, triamcinolona, dexametasona, betametasona), bupropiona e clorpropamida. As de gravidade **moderada** incluem antidiabéticos (acarbose, metformina, pioglitazona, canagliflozina, alogliptina, albiglutida), famotidina, loperamida, ácido acetilsalicílico, balsalazida, bisacodil e sais de cálcio e potássio.

Consulte a bula para advertências principais e contraindicações oficiais; os dados da bula da ANVISA não estavam disponíveis.

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
- A previsão principal (síndrome de hiperviscosidade policlonal) é apenas uma previsão do modelo (L5), sem ensaios, sem literatura e sem mecanismo plausível. Além disso, o medicamento é comercializado no Brasil (8 registros válidos de 8), e o perfil de segurança exige cautela em várias condições.
- A peste septicêmica (L4) é a hipótese mais defensável, mas é uma extensão do uso antibacteriano existente e se apoia apenas em dados in vitro e em animais. Pode ser tratada como questão de pesquisa, não como candidata a reposicionamento imediato.

**Para prosseguir, é necessário:**
- Obter e analisar a bula da ANVISA (advertências e contraindicações), hoje um bloqueio para a triagem de segurança.
- Obter dados detalhados do mecanismo de ação (por exemplo, via DrugBank).
- Para peste septicêmica: revisar diretrizes e dados clínicos de fluoroquinolonas e avaliar a viabilidade de estudos em humanos.
- Para qualquer nova indicação: confirmar a compatibilidade de via de administração e a situação regulatória, já que não há registro vigente no Brasil.
- Descartar ou despriorizar as previsões hematológicas sem respaldo mecanístico.
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

