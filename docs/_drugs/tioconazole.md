---
layout: default
title: Tioconazole
parent: Apenas Predição do Modelo (L5)
nav_order: 640
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-31
description: "Tioconazole: nova indicação prevista, Vulvovaginite (Vulvovaginitis) (nível de evidência L1). Indicação original: Antimicóticos para uso tópico"
monitor_inn: "tioconazole"
predicted_indications: ["vulvovaginitis", "vulvitis", "postmenopausal atrophic vaginitis"]
---

# Tioconazole
{: .fs-9 }

Nível de evidência: **L5** | Indicações previstas: **3** 
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

## Tioconazol: Do uso antifúngico tópico à vulvovaginite
{: .text-alpha }

## Resumo em Uma Frase

Tioconazol é um antifúngico imidazólico de uso tópico, originalmente registrado no Brasil como antimicótico para uso tópico (isolado ou associado ao tinidazol em produtos ginecológicos).
O modelo TxGNN prevê que pode ser eficaz para **Vulvovaginite (Vulvovaginitis)**, atualmente com **0 ensaios clínicos registrados** e **20 publicações** apoiando esta direção.
Trata-se, na prática, de um uso já estabelecido (candidíase vaginal), e não de um reposicionamento propriamente dito.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Antimicóticos para uso tópico |
| Nova Indicação Prevista | Vulvovaginite (Vulvovaginitis) |
| Pontuação de Previsão TxGNN | 0,9923 |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | Comercializado (registros ativos: 18 de 62) |
| Número de Registros | 62 (ativos: 18) |
| Decisão Recomendada | Proceed with Guardrails |

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação no campo original de MOA. Segundo informações conhecidas, o tioconazol é um antifúngico imidazólico que inibe a lanosterol 14-α-desmetilase (CYP51/ERG11) em fungos e leveduras. Sem esta enzima, o fungo não produz ergosterol, componente essencial da membrana celular, e perde a integridade da membrana. Dados farmacológicos também indicam que o tioconazol inibe a enzima humana CYP8B1, envolvida na síntese de ácidos biliares.

A vulvovaginite é causada com frequência por espécies de *Candida*, o principal alvo do mecanismo azólico. Por isso, a previsão do modelo coincide com um uso já conhecido: a candidíase vulvovaginal. A pontuação muito alta (0,992) é coerente com isso. Os registros brasileiros do medicamento, em grande parte associações com tinidazol em produtos ginecológicos, reforçam a relação com a nova indicação.

Há também previsões de menor suporte para o mesmo fármaco. A **vulvite** (pontuação 0,9920, nível L2) é plausível apenas quando de origem infecciosa por *Candida*; não se aplica a vulvites irritativas, alérgicas ou dermatológicas. A **vaginite atrófica pós-menopausa** (0,9919, nível L5, decisão Hold) não tem ligação mecanística clara, pois decorre de deficiência estrogênica e não de infecção. A pontuação alta provavelmente reflete proximidade na rede com outras vaginites.

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados.

## Evidências da Literatura

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [3524439](https://pubmed.ncbi.nlm.nih.gov/3524439/) | 1986 | RCT | Antimicrob Agents Chemother | Dose única de tioconazol a 6,5% vs clotrimazol por 3 dias em 80 pacientes com candidíase vulvovaginal: 84% vs 85% assintomáticas após 4 semanas |
| [6347833](https://pubmed.ncbi.nlm.nih.gov/6347833/) | 1983 | RCT | Gynakol Rundsch | Comparação duplo-cega de tioconazol vs placebo em candidíase vaginal, com avaliação de absorção sistêmica |
| [3510114](https://pubmed.ncbi.nlm.nih.gov/3510114/) | 1986 | Revisão | Drugs | Amplo espectro in vitro; ensaios abertos e controlados demonstraram eficácia e segurança de preparações tópicas em micoses superficiais e candidíase vaginal |
| [40464716](https://pubmed.ncbi.nlm.nih.gov/40464716/) | 2025 | Revisão | Expert Rev Anti Infect Ther | Opções não invasivas de azólicos para candidíase vulvovaginal, incluindo casos complicados e recorrentes |
| [6094282](https://pubmed.ncbi.nlm.nih.gov/6094282/) | 1984 | Ensaio randomizado aberto | J Int Med Res | Tioconazol tópico 6% em dose única vs cetoconazol oral por 5 dias (40 pacientes): ambos erradicaram a infecção; sintomas melhoraram mais rápido com o tópico |
| [3984688](https://pubmed.ncbi.nlm.nih.gov/3984688/) | 1985 | Estudo clínico | Acta Obstet Gynecol Scand | Creme vaginal a 2% por 3 dias em 29 mulheres sintomáticas: cura micológica de 88,5% |
| [3485546](https://pubmed.ncbi.nlm.nih.gov/3485546/) | 1986 | Estudo aberto não comparativo | J Int Med Res | Creme a 2% em 20 pacientes com *T. vaginalis* ou infecções mistas: 95% de cura na primeira avaliação |
| [6347834](https://pubmed.ncbi.nlm.nih.gov/6347834/) | 1983 | Ensaio comparativo aberto | Gynakol Rundsch | Tioconazol vs econazol em tratamento de 3 dias da candidíase vaginal |
| [6873744](https://pubmed.ncbi.nlm.nih.gov/6873744/) | 1983 | Ensaio comparativo aberto | Gynakol Rundsch | Creme de tioconazol vs óvulos de econazol em tratamento de 3 dias |
| [10990271](https://pubmed.ncbi.nlm.nih.gov/10990271/) | 2000 | Estudo laboratorial | Microb Drug Resist | Resistência cruzada de isolados de *C. albicans* e *C. glabrata* a azólicos de venda livre usados em vaginites |

## Informações de Comercialização no Brasil

Todos os 18 registros estão válidos. Principais registros:

| Registro | Produto | Empresa detentora | Situação |
|------|------|------|------|
| 101550194 | TAKIL | MARJAN INDÚSTRIA E COMÉRCIO LTDA | Ativo |
| 101550251 | TRIVIFEME | MARJAN INDÚSTRIA E COMÉRCIO LTDA | Ativo |
| 102350580 | TIOCONAZOL + TINIDAZOL | EMS S/A | Ativo |
| 102350801 | TIOTRAX | EMS S/A | Ativo |
| 103900115 | GYNOMAX | FARMOQUÍMICA S/A | Ativo |
| 103900165 | GYNOPAC | FARMOQUÍMICA S/A | Ativo |
| 105350154 | TIOCONAZOL + TINIDAZOL | LABORATÓRIO GLOBO SA | Ativo |
| 105710175 | GYNBEN | BELFAR LTDA | Ativo |
| 105830290 | TIOCONAZOL + TINIDAZOL | GERMED FARMACEUTICA LTDA | Ativo |
| 107150136 | TIONAZEN | CAZI QUIMICA FARMACEUTICA INDUSTRIA E COMERCIO LTD | Ativo |
| 118190129 | TIOCONAZOL | MULTILAB INDUSTRIA E COMERCIO DE PRODUTOS FARMACEU | Ativo |
| 125680086 | TIOCONAZOL + TINIDAZOL | PRATI DONADUZZI & CIA LTDA | Ativo |
| 154230084 | TIOCONAZOL + TINIDAZOL | GEOLAB INDÚSTRIA FARMACÊUTICA S/A | Ativo |
| 154230087 | TININ | GEOLAB INDÚSTRIA FARMACÊUTICA S/A | Ativo |
| 155840160 | TIOCONAZOL + TINIDAZOL | BRAINFARMA INDÚSTRIA QUÍMICA E FARMACÊUTICA S.A | Ativo |
| 155840204 | VULNAGEN | BRAINFARMA INDÚSTRIA QUÍMICA E FARMACÊUTICA S.A | Ativo |
| 167730166 | TIOCONAZOL + TINIDAZOL | LEGRAND PHARMA INDÚSTRIA FARMACÊUTICA LTDA | Ativo |
| 188710005 | AMPLOGIN | GALLIA INDUSTRIA FARMACEUTICA LTDA | Ativo |
| 100430894 | TIOCONAZOL | EUROFARMA LABORATORIOS S.A. | Cancelado |
| 100930252 | GINOTINIX | MANTECORP INDÚSTRIA QUÍMICA E FARMACÊUTICA S.A. | Cancelado |
| 101810301 | SECZOL | MEDLEY INDÚSTRIA FARMACÊUTICA LTDA | Cancelado |
| 101810317 | MONIZOL | MEDLEY INDÚSTRIA FARMACÊUTICA LTDA | Cancelado |
| 101810345 | TIOCONAZOL | MEDLEY INDÚSTRIA FARMACÊUTICA LTDA | Cancelado |
| 101810348 | TIOCONAZOL | MEDLEY INDÚSTRIA FARMACÊUTICA LTDA | Cancelado |
| 101810367 | TIOCONAZOL + TINIDAZOL | MEDLEY INDÚSTRIA FARMACÊUTICA LTDA | Cancelado |
| 102160040 | TRALEN | LABORATÓRIOS PFIZER LTDA | Cancelado |
| 102160047 | CARTRAX | LABORATÓRIOS PFIZER LTDA | Cancelado |
| 102350621 | TIOCONAZOL | EMS S/A | Cancelado |
| 102350623 | TIOCONAZOL | EMS S/A | Cancelado |
| 102350627 | TIOCONAZOL | EMS S/A | Cancelado |

A tabela mostra até 30 registros (os ativos primeiro). A lista completa está na consulta de medicamentos da ANVISA (https://consultas.anvisa.gov.br/#/medicamentos/).

## Considerações de Segurança

- **Interações Medicamentosas**: foram identificadas 2 entradas. Com **omeprazol** (nível de gravidade não classificado). Com a enzima humana **CYP8B1**, que o tioconazol inibe (envolvida na biossíntese de ácidos biliares); não há nível de gravidade definido.

Consulte a bula para advertências e contraindicações, pois não há dados disponíveis neste relatório.

## Conclusão e Próximos Passos

**Decisão: Proceed with Guardrails**

**Justificativa:**
- Há dois RCTs e vários estudos clínicos que apoiam o uso do tioconazol na candidíase vulvovaginal, e o mecanismo azólico corresponde ao principal patógeno. Porém, os estudos são antigos (1983–1988), não há ensaios registrados, e os 18 registros no Brasil estão cancelados.

**Para prosseguir, é necessário:**
- Obter e analisar as bulas na ANVISA para advertências e contraindicações (lacuna de segurança bloqueante).
- Confirmar o mecanismo de ação no DrugBank.
- Esclarecer a situação regulatória: motivo dos cancelamentos e viabilidade de novo registro.
- Verificar a resistência atual de espécies de *Candida* a azólicos tópicos.
- Restringir o escopo à vulvite e vulvovaginite infecciosas por *Candida*; a vaginite atrófica (Hold) não deve avançar sem evidências próprias.
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

