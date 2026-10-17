---
layout: default
title: Degarelix
parent: Apenas Predição do Modelo (L5)
nav_order: 254
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Degarelix: nova indicação prevista, Hipertricose (hypertrichosis) (nível de evidência L5). Indicação original: Não disponível nos dados compilados"
monitor_inn: "DEGARELIX"
predicted_indications: ["hypertrichosis (disease)", "Ambras type hypertrichosis universalis congenita", "syndrome with a Dandy-Walker malformation as major feature", "malformation syndrome with odontal and/or periodontal component", "isolated genetic hair shaft abnormality", "allergic urticaria", "cold urticaria", "familial male-limited precocious puberty", "centra precocious puberty 1", "familial isolated trichomegaly"]
---

# Degarelix
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

# Degarelix: Do uso original à hipertricose (previsão do modelo)

## Resumo em Uma Frase

Degarelix é um antagonista do receptor de GnRH. Não há indicação original registrada no Brasil nos dados compilados para este relatório.
O modelo TxGNN prevê que pode ser eficaz para **Hipertricose (hypertrichosis)**, mas **não há ensaios clínicos nem publicações** apoiando esta direção; a previsão é puramente computacional.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Não disponível nos dados compilados (nenhum registro na ANVISA) |
| Nova Indicação Prevista | Hipertricose (hypertrichosis) |
| Pontuação de Previsão TxGNN | 99,99% |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | ✗ Não comercializado |
| Número de Registros | 0 |
| Decisão Recomendada | Hold |

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação registrados nos dados compilados. Segundo informações conhecidas, o degarelix é um antagonista do receptor de GnRH: suprime LH e FSH e, com isso, reduz a testosterona e os androgênios derivados.

A relação com a nova indicação é fraca. A hipertricose, em geral, não depende de androgênios (diferente do hirsutismo), de modo que a supressão androgênica não tem justificativa mecanística clara. A pontuação muito alta do TxGNN (0,9999) reflete apenas uma associação baseada em grafo, sem estudos que a sustentem.

Outras previsões do modelo seguem o mesmo padrão: hipertricose congênita de Ambras (ligada a rearranjos que afetam o TRPS1, fora do eixo androgênico), síndromes malformativas, anomalias genéticas da haste capilar e tricomegalia familiar. Em todas, a previsão não tem respaldo clínico. As urticárias (alérgica e ao frio) merecem cautela: antagonistas de GnRH podem ativar mastócitos (via MRGPRX2), de modo que o fármaco poderia causar, e não tratar, esses quadros.

A previsão biologicamente mais coerente do conjunto é a **puberdade precoce central** (pontuação de 99,67%), por envolver diretamente o eixo hipotálamo-hipófise-gonadal. Ainda assim, não há estudos pediátricos nos dados e os agonistas de depósito são o padrão estabelecido. A puberdade precoce familiar limitada ao sexo masculino, por sua vez, é causada por mutações ativadoras do LHCGR, a jusante do eixo GnRH-LH, e o degarelix provavelmente seria ineficaz.

## Informações de Comercialização no Brasil

O degarelix não possui registro ativo nos dados da ANVISA compilados para este relatório (situação: não comercializado; 0 registros).

## Considerações de Segurança

- **Contraindicações segundo o grafo de conhecimento (não é texto de bula)**: síndrome do QT longo, síndrome do QT longo familiar, torsades de pointes, doença hepática, doença da vesícula biliar e deficiência de potássio.
- **Interações medicamentosas**: foram identificadas 100 interações; as principais entre as listadas:
  - **Graves (Major)**: cisaprida, dolasetrona (risco ligado ao prolongamento do intervalo QT).
  - **Moderadas**: claritromicina, levofloxacino, ondansetrona, granisetrona, palonosetrona, famotidina, loperamida e diversos laxantes (bisacodil, ácido picossulfúrico, polietilenoglicol com eletrólitos, óleo de rícino, glicerina, lactitol, lactulose, citrato e hidróxido de magnésio, óleo mineral).
  - **Leve (Minor)**: metronidazol.
- Os dados de advertências e contraindicações da bula não estavam disponíveis; consulte a bula para informações de segurança completas.

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
- A previsão para hipertricose tem apenas suporte computacional (L5), sem ensaios clínicos ou literatura, e o mecanismo proposto é fraco. Além disso, o fármaco não está registrado no Brasil.

**Para prosseguir, é necessário:**
- Obter e analisar a bula da ANVISA (advertências e contraindicações), pois a ausência desses dados bloqueia a triagem de segurança.
- Complementar os dados de mecanismo de ação (por exemplo, via DrugBank).
- Realizar revisão sistemática da literatura sobre hipertricose e antagonistas de GnRH.
- Se houver interesse em uma direção mais plausível, priorizar a puberdade precoce central, com revisão da literatura e avaliação de segurança pediátrica.
- Avaliar o risco de prolongamento do QT, dadas as contraindicações do grafo e as interações graves identificadas.
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

