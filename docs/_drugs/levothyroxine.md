---
layout: default
title: Levothyroxine
parent: Apenas Predição do Modelo (L5)
nav_order: 416
evidence_level: L5
indication_count: 4
monitor_inn: "Levothyroxine"
predicted_indications: ["renal hypodysplasia/aplasia", "bilateral renal agenesis", "Potter sequence", "Carney complex"]
last_modified_at: 2026-10-28
description: "Levothyroxine: nova indicação prevista, Hipodisplasia/aplasia renal (renal hypodysplasia/aplasia) (nível de evidência L5). Indicação original: HORMONIOS TIREOIDEANOS SIMPLES OU ASSOCIADOS ENTRE SI"
---

# Levothyroxine
{: .fs-9 }

Nível de evidência: **L5** | Indicações previstas: **4** 
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

## Levothyroxine: Hipodisplasia/aplasia renal (renal hypodysplasia/aplasia)
{: .text-alpha }

## Resumo em Uma Frase

Levotiroxina é um hormônio tireoidiano sintético (T4), registrado no Brasil para "hormônios tireoidianos simples ou associados entre si".
O modelo TxGNN prevê que ela poderia ser útil para **hipodisplasia/aplasia renal (renal hypodysplasia/aplasia)**,
mas **não há ensaios clínicos nem publicações** nos dados compilados para este relatório que apoiem essa direção; trata-se apenas de uma previsão do modelo.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | HORMONIOS TIREOIDEANOS SIMPLES OU ASSOCIADOS ENTRE SI |
| Nova Indicação Prevista | Hipodisplasia/aplasia renal (renal hypodysplasia/aplasia) |
| Pontuação de Previsão TxGNN | 0.9967 |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | Comercializado (registros ativos: 6 de 6) |
| Número de Registros | 6 (ativos: 6) |
| Decisão Recomendada | Hold |

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação nos dados compilados. Segundo informações conhecidas, a levotiroxina é a forma sintética do hormônio tireoidiano T4, e a sinalização tireoidiana tem papel geral no crescimento fetal e na maturação de órgãos, incluindo o rim em desenvolvimento.

A razoabilidade, porém, é fraca. A hipodisplasia/aplasia renal é uma malformação congênita estrutural, geralmente associada a defeitos genéticos (como PAX2, HNF1B e RET). Não há mecanismo estabelecido pelo qual a levotiroxina exógena reverta ou trate essa condição. A pontuação alta (0,9967) é apenas uma previsão computacional, provavelmente refletindo proximidade na rede de conhecimento.

Outras previsões do modelo seguem a mesma lógica e também carecem de evidências: agenesia renal bilateral (0.9960), sequência de Potter (0.9933) e complexo de Carney (0.9918). Neste último há uma conexão endócrina frouxa (envolvimento da tireoide), e a levotiroxina poderia servir como terapia de suporte, por exemplo no hipotireoidismo pós-cirúrgico ou na supressão de TSH, e não como tratamento modificador da doença.

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados.

## Evidências da Literatura

Atualmente não há literatura relacionada.

## Informações de Comercialização no Brasil

| Número de Registro | Nome Comercial | Forma Farmacêutica | Indicação Aprovada |
|---------|------|------|-----------|
| Registro nº 100890359 | EUTHYROX | Não informada | Hormônios tireoidianos simples ou associados entre si |
| Registro nº 105530329 | SYNTHROID | Não informada | Hormônios tireoidianos simples ou associados entre si |
| Registro nº 100890416 | LEVOTIROXINA SÓDICA | Não informada | Hormônios tireoidianos simples ou associados entre si |
| Registro nº 183260353 | PURAN T4 | Não informada | Hormônios tireoidianos simples ou associados entre si |
| Registro nº 105730366 | LEVOID | Não informada | Hormônios tireoidianos simples ou associados entre si |

Há ainda um sexto registro válido (nº 100890202, EUTHYROX), com a mesma indicação.

## Considerações de Segurança

As advertências e contraindicações da bula não estavam disponíveis nos dados compilados; consulte a bula para essas informações.

- **Relações de contraindicação registradas no grafo de conhecimento** (não são texto de bula): hipertensão, hipopituitarismo e deficiências hormonais hipofisárias (incluindo deficiência de hormônio do crescimento, síndrome de Kallmann e síndrome de Sheehan), hipogonadismo hipogonadotrófico, osteoporose (incluindo pós-menopausa), diabetes mellitus, cetoacidose diabética, doença arterial coronariana, infarto do miocárdio e doenças do timo.
- **Interações medicamentosas**: foram identificadas 100 interações. As listadas são majoritariamente de gravidade moderada, incluindo:
  - antidiabéticos (acarbose, metformina, pioglitazona, alogliptina, canagliflozina, dapagliflozina, empagliflozina, clorpropamida, albiglutida, dulaglutida);
  - inibidores da bomba de prótons (omeprazol, rabeprazol, dexlansoprazol);
  - sais de cálcio e magnésio (fosfato e acetato de cálcio, óxido de magnésio);
  - simpatomiméticos (epinefrina, isometepteno, dietilpropiona).
  - A cimetidina tem interação de gravidade leve.

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
- Não existe nenhum ensaio clínico ou publicação sobre levotiroxina nas indicações previstas (nível L5), e não há mecanismo plausível para tratar malformações renais estruturais congênitas. A pontuação alta do modelo não substitui evidência real.

**Para prosseguir, é necessário:**
- Dados do mecanismo de ação da levotiroxina.
- Advertências e contraindicações da bula da ANVISA, para triagem de segurança.
- Revisão sistemática da literatura e de registros de ensaios para qualquer das doenças previstas (por exemplo, estudos pré-clínicos sobre hormônio tireoidiano e desenvolvimento renal).
- Avaliação de se a previsão do complexo de Carney (apenas como terapia de suporte) merece análise separada.
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

