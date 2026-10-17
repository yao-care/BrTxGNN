---
layout: default
title: Diazoxide
parent: Apenas Predição do Modelo (L5)
nav_order: 265
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Diazoxide: nova indicação prevista, Hipotricose simples do couro cabeludo (hypotrichosis simplex of the s… (nível de evidência L5). Indicação original: Vasodilatadores"
monitor_inn: "diazoxide"
predicted_indications: ["hypotrichosis simplex of the scalp", "congenital hypotrichosis milia", "diffuse alopecia areata", "alopecia", "Ambras type hypertrichosis universalis congenita", "malformation syndrome with odontal and/or periodontal component", "hypertrichosis (disease)", "syndrome with a Dandy-Walker malformation as major feature", "isolated genetic hair shaft abnormality"]
---

# Diazoxide
{: .fs-9 }

Nível de evidência: **L5** | Indicações previstas: **10** 
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

# Diazóxido: De vasodilatador à alopecia (previsão do TxGNN)

## Resumo em Uma Frase

Diazóxido foi originalmente registrado no Brasil como vasodilatador (produto TENSURIL, atualmente com registro cancelado).
O modelo TxGNN prevê que pode ser eficaz para **Hipotricose simples do couro cabeludo (hypotrichosis simplex of the scalp)**, a previsão de maior pontuação, mas sem nenhum ensaio clínico ou publicação direta que a sustente. A indicação com algum respaldo indireto é a **Alopecia (alopecia)**, com **6 publicações** (sobretudo revisões, relatos de caso e um estudo em primatas) e **nenhum ensaio clínico**.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Vasodilatadores |
| Nova Indicação Prevista | Hipotricose simples do couro cabeludo (hypotrichosis simplex of the scalp) |
| Pontuação de Previsão TxGNN | 99,96% |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | ✗ Apenas registro cancelado |
| Número de Registros | 1 |
| Decisão Recomendada | Hold |

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação nos registros compilados. Segundo informações conhecidas, o diazóxido é um abridor de canais de potássio sensíveis ao ATP (KATP), atuando como vasodilatador e também na redução da secreção de insulina. Sua ação vasodilatadora foi a base do registro original no Brasil.

A relação com a nova indicação vem de um efeito adverso bem documentado: a hipertricose (crescimento excessivo de pelos). O minoxidil, outro abridor de canais KATP e vasodilatador, é um estimulante conhecido do crescimento capilar. Por analogia, o diazóxido poderia estimular o folículo piloso. Um estudo antigo em macacos de cauda curta (PMID 2085505) mostrou que o diazóxido tópico estimulou o crescimento folicular no couro cabeludo calvo.

Essa lógica, porém, tem limites. Para a hipotricose hereditária e a hipotricose congênita com milia, a ligação é apenas extrapolada do efeito adverso. Na alopecia areata, que é autoimune, não há ação imunomoduladora conhecida do diazóxido. Em outras previsões do modelo (hipertricose, hipertricose de Ambras), o fármaco causaria ou agravaria o quadro, o que sugere falso positivo por associação de fenótipo, e não benefício terapêutico.

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados.

## Evidências da Literatura

As publicações abaixo referem-se à indicação **Alopecia** (rank 4), a única entre as previsões de cabelo com literatura recuperada.

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [2085505](https://pubmed.ncbi.nlm.nih.gov/2085505/) | 1990 | Estudo animal (primata) | J Dermatol Sci | Diazóxido tópico em macacos de cauda curta com calvície frontal, avaliando rebrota capilar e efeitos sistêmicos |
| [8326148](https://pubmed.ncbi.nlm.nih.gov/8326148/) | 1993 | Revisão | J Invest Dermatol | Minoxidil e diazóxido tópicos induziram rebrota significativa no couro cabeludo calvo de macacos |
| [8018303](https://pubmed.ncbi.nlm.nih.gov/8018303/) | 1994 | Revisão | Drug Safety | Medicamentos que causam queda ou crescimento de cabelo; incidência, manejo e prevenção |
| [37042338](https://pubmed.ncbi.nlm.nih.gov/37042338/) | 2023 | Relato de caso | Pediatr Dermatol | Hipertricose generalizada em criança por exposição secundária a minoxidil tópico; cita o diazóxido como causa de hipertricose |
| [4340017](https://pubmed.ncbi.nlm.nih.gov/4340017/) | 1972 | Série de casos | Arch Dis Child | Exposição fetal ao diazóxido em quatro lactentes (tema de segurança, não de alopecia) |
| [20682429](https://pubmed.ncbi.nlm.nih.gov/20682429/) | 2010 | Revisão | Vet Clin North Am Exot Anim Pract | Manejo de insulinoma em furões, incluindo o uso de diazóxido (sem relação direta com alopecia) |

## Informações de Comercialização no Brasil

| Número de Registro | Nome Comercial | Forma Farmacêutica | Indicação Aprovada |
|---------|------|------|-----------|
| Registro 102980041 (cancelado) | TENSURIL | Não informada | Vasodilatadores |

## Considerações de Segurança

- **Contraindicações (com base no grafo de conhecimento do TxGNN, não em texto de bula)**: doença renal, insuficiência renal, uremia, doença hepática, doença da vesícula biliar, hiperglicemia, diabetes mellitus, cetoacidose diabética, insuficiência cardíaca congestiva, doença arterial coronariana, doença cerebrovascular, deficiência de potássio, gota, hiperuricemia, hipotensão ortostatica, síndrome da taquicardia postural ortostática, atrofia de múltiplos sistemas e piureter.
- **Interações Medicamentosas**: foram identificadas 209 interações; as 20 exibidas são todas de gravidade moderada, incluindo antidiabéticos (acarbose, metformina, pioglitazona, alogliptina, clorpropamida, acetoexamida, dulaglutida, albiglutida e inibidores de SGLT2 como canagliflozina, dapagliflozina, empagliflozina e ertugliflozina), corticosteroides (hidrocortisona, triancinolona, dexametasona, betametasona e budesonida), além de bupropiona, morfina e dronabinol.
- **Efeitos adversos descritos na literatura**: hipertricose, retenção de líquidos e insuficiência cardíaca, hiperglicemia, insuficiência renal aguda e enterocolite necrosante em neonatos. O uso sistêmico traz riscos cardiovasculares e metabólicos, de modo que somente a via tópica seria razoável de explorar.

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
- Todas as previsões estão em nível L5, exceto alopecia (L4, apenas com dados pré-clínicos em primatas e relatos indiretos). Não há ensaios clínicos em humanos, o produto não está mais comercializado no Brasil e a segurança sistêmica é desfavorável. Alopecia é, no máximo, uma questão de pesquisa a investigar por via tópica.

**Para prosseguir, é necessário:**
- Obter e analisar a bula na ANVISA (advertências e contraindicações), lacuna que impede a triagem de segurança.
- Confirmar o mecanismo de ação em fonte dedicada (por exemplo, DrugBank).
- Avaliar a viabilidade de formulação tópica e estudos de absorção sistêmica, já que não há rota compatível definida.
- Realizar estudos pré-clínicos e ensaios de fase inicial em alopecia androgenética, comparando com o minoxidil.
- Descartar previsões com direção provavelmente invertida (hipertricose, hipertricose de Ambras) e verificar em fontes especializadas a previsão de hiperinsulinismo por deficiência de Kir6.2, já que a resposta ao diazóxido depende de canais funcionais.
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

