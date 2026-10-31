---
layout: default
title: Mecobalamin
parent: Apenas Predição do Modelo (L5)
nav_order: 436
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-31
description: "Mecobalamin: nova indicação prevista, Colangite Esclerosante (Sclerosing Cholangitis) (nível de evidência L5). Indicação original: Monovitaminas, exceto vitamina K"
monitor_inn: "mecobalamin"
predicted_indications: ["sclerosing cholangitis", "multiple endocrine neoplasia", "bone Paget disease"]
---

# Mecobalamin
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

## Mecobalamina: De monovitamina (vitamina B12) para colangite esclerosante
{: .text-alpha }

## Resumo em Uma Frase

Mecobalamina (metilcobalamina, forma ativa da vitamina B12) foi originalmente registrada no Brasil como monovitamina.
O modelo TxGNN prevê que pode ser eficaz para **Colangite Esclerosante (Sclerosing Cholangitis)**,
mas atualmente há **0 ensaios clínicos** e **0 publicações** apoiando esta direção; trata-se apenas de uma previsão computacional.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Monovitaminas, exceto vitamina K |
| Nova Indicação Prevista | Colangite Esclerosante (Sclerosing Cholangitis) |
| Pontuação de Previsão TxGNN | 0,9950 |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | Comercializado (registros ativos: 16 de 17) |
| Número de Registros | 17 (ativos: 16) |
| Decisão Recomendada | Hold |

---

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação. Segundo informações conhecidas, a mecobalamina é uma forma ativa da vitamina B12, que atua na metilação e no metabolismo de um carbono, apoiando a função metabólica neuronal e hepática. Sua utilização estabelecida é como suplemento vitamínico.

Não há, nos dados compilados para este relatório, uma ligação direta entre esse papel metabólico e a colangite esclerosante, doença caracterizada por colestase e fibrose biliar de base imunomediada. A pontuação elevada do TxGNN (0,9950) vem do modelo TxGNN (deep learning) e pode refletir similaridades que o modelo aprendeu entre doenças relacionadas, não evidência biológica. Sem dados de mecanismo de ação original, a plausibilidade mecanística não pode ser avaliada com mais profundidade.

Outras previsões do modelo, também sem evidências, foram: neoplasia endócrina múltipla (0,9934) e doença óssea de Paget (0,9931). No primeiro caso, trata-se de uma síndrome tumoral hereditária de origem genética (por exemplo, *MEN1*, *RET*), sem mecanismo plausível para um análogo da vitamina B12; a pontuação provavelmente reflete similaridades que o modelo aprendeu entre doenças relacionadas, não evidência biológica. No segundo, há apenas discussões indiretas na literatura sobre vitamina B12/homocisteína e metabolismo ósseo, não sustentadas pelos dados aqui compilados.

---

## Informações de Comercialização no Brasil

Todos os 12 registros encontrados estão **válidos**. Principais registros:

| Registro | Produto | Empresa detentora | Situação |
|------|------|------|------|
| 100431532 | DOZI | EUROFARMA LABORATORIOS S.A. | Ativo |
| 100431535 | MEC 12 | EUROFARMA LABORATORIOS S.A. | Ativo |
| 100431605 | DOZI | EUROFARMA LABORATORIOS S.A. | Ativo |
| 101180664 | COBI-12 | APSEN FARMACEUTICA S/A | Ativo |
| 101550248 | DOZEMAST | MARJAN INDÚSTRIA E COMÉRCIO LTDA | Ativo |
| 101550253 | DOZEMAST TRIO | MARJAN INDÚSTRIA E COMÉRCIO LTDA | Ativo |
| 102351475 | MECODOZZE | EMS S/A | Ativo |
| 105730116 | DODIBE | ACHÉ LABORATÓRIOS FARMACÊUTICOS S.A | Ativo |
| 109740360 | ATIVB | BIOLAB SANUS FARMACÊUTICA LTDA | Ativo |
| 109740365 | DEFB | BIOLAB SANUS FARMACÊUTICA LTDA | Ativo |
| 109740371 | MECOBALAMINA | BIOLAB SANUS FARMACÊUTICA LTDA | Ativo |
| 114620042 | MECOBE | MYRALIS INDÚSTRIA FARMACÊUTICA LTDA | Ativo |
| 114620052 | MECOBALAMINA | MYRALIS INDÚSTRIA FARMACÊUTICA LTDA | Ativo |
| 114620054 | PERI B12 | MYRALIS INDÚSTRIA FARMACÊUTICA LTDA | Ativo |
| 135170093 | MECOBALAMINA | ALTHAIA S.A. INDUSTRIA FARMACEUTICA | Ativo |
| 156650006 | BMAST | DROXTER INDUSTRIA, COMÉRCIO E PARTICIPAÇÕES LTDA | Ativo |
| 103410056 | METHYCOBAL | TRB PHARMA INDÚSTRIA QUÍMICA E FARMACÊUTICA LTDA | Cancelado |

---

## Considerações de Segurança

- **Contraindicações (associações do grafo de conhecimento, não texto de bula)**: deficiência de potássio, gastrite atrófica crônica e neuropatia óptica hereditária de Leber.
- **Interações Medicamentosas** (13 identificadas):
  - **Moderadas**: trióxido de arsênio e cloranfenicol.
  - **Leves**: antagonistas H2 (famotidina, ranitidina, cimetidina, nizatidina, ranitidina com citrato de bismuto) e inibidores da bomba de prótons (rabeprazol, dexlansoprazol, omeprazol, lansoprazol, pantoprazol, esomeprazol).

Consulte a bula para advertências e contraindicações formais.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
- Não há ensaios clínicos nem literatura que sustentem a indicação prevista (nível L5), e a pontuação alta do TxGNN, isoladamente, não estabelece vínculo terapêutico. Além disso, o medicamento é comercializado no Brasil, com 12 registros válidos de 12.

**Para prosseguir, é necessário:**
- Obter e analisar a bula na ANVISA para advertências e contraindicações (lacuna de dados bloqueante para a triagem de segurança).
- Complementar os dados de mecanismo de ação (por exemplo, via consulta à API do DrugBank).
- Realizar busca sistemática de literatura e de ensaios clínicos sobre vitamina B12/mecobalamina em colangite esclerosante.
- Investigar estudos pré-clínicos que sustentem um vínculo biológico plausível.
- Avaliar a compatibilidade de vias de administração e a viabilidade regulatória, dado que não há registro válido no Brasil.
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

