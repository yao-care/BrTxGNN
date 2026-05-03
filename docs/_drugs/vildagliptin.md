---
layout: default
title: Vildagliptin
parent: 僅模型預測 (L5)
nav_order: 504
evidence_level: L5
indication_count: 10
---

# Vildagliptin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

A skill foi verificada — não contém instruções específicas para geração de relatórios individuais. Prossigo diretamente com o relatório conforme o formato v5 definido no system prompt.

---

# Vildagliptin: Do diabetes mellitus tipo 2 à síndrome de rigidez muscular clássica

## Resumo em Uma Frase

Vildagliptin é um inibidor seletivo da DPP-4 (dipeptidil peptidase-4), utilizado no tratamento do diabetes mellitus tipo 2, onde melhora o controle glicêmico ao potencializar os efeitos dos hormônios incretínicos GLP-1 e GIP.
O modelo TxGNN prevê que pode ser eficaz para a **Síndrome de Rigidez Muscular Clássica (Classic Stiff Person Syndrome)**, porém atualmente **não há ensaios clínicos nem publicações** apoiando diretamente esta direção.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Diabetes mellitus tipo 2 |
| Nova Indicação Prevista | Síndrome de Rigidez Muscular Clássica (Classic Stiff Person Syndrome) |
| Pontuação de Previsão TxGNN | 99.88% |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | ✓ Comercializado |
| Número de Registros | 20 |
| Decisão Recomendada | Hold |

---

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação disponíveis neste pacote de evidências. Segundo informações conhecidas, vildagliptin é um inibidor seletivo e potente da DPP-4, aprovado para o tratamento do diabetes mellitus tipo 2. Seu mecanismo central consiste em bloquear a degradação das incretinas GLP-1 e GIP, potencializando a secreção de insulina dependente de glicose e suprimindo a secreção inapropriada de glucagon — resultado é melhora sustentada do controle glicêmico com baixo risco de hipoglicemia.

A síndrome de rigidez muscular clássica é uma doença autoimune rara do sistema GABAérgico, mediada por anticorpos anti-GAD65 (descarboxilase do ácido glutâmico). A destruição autoimune das vias GABAérgicas provoca rigidez muscular progressiva e espasmos dolorosos. Embora os inibidores de DPP-4 possuam efeitos imunomoduladores secundários documentados, não existe nenhuma ligação mecanística direta conhecida entre a inibição da DPP-4 e a síntese ou sinalização do GABA, nem com a resposta imune anti-GAD65 que caracteriza esta doença.

A alta pontuação do TxGNN (99.88%) é muito provavelmente decorrente de um efeito de vizinhança em nós neuro-imunes dentro da ontologia de doenças do modelo — e não de um sinal terapêutico biologicamente plausível e independente. A ausência total de evidências clínicas ou pré-clínicos direcionadas a esta indicação reforça esta interpretação. A previsão deve ser tratada com cautela significativa.

---

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados.

---

## Evidências da Literatura

Atualmente não há literatura relacionada.

---

## Informações de Comercialização no Brasil

Vildagliptin está registrado no mercado brasileiro com **20 licenças ativas** (situação: ✓ Comercializado). Os dados individuais de cada registro (número, nome comercial, forma farmacêutica, indicação aprovada) não estão disponíveis neste pacote de evidências e devem ser consultados diretamente no sistema de consulta da ANVISA.

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
Não existe nenhuma evidência clínica, pré-clínica ou mecanística que apoie o uso de vildagliptin para a síndrome de rigidez muscular clássica. A alta pontuação TxGNN (99.88%) é atribuída a artefatos de vizinhança na ontologia de doenças, e não a sinal terapêutico genuíno — classificando esta previsão como nível L5, a categoria de menor suporte evidente.

**Para prosseguir, seria necessário:**
- Identificar qualquer mecanismo biológico plausível entre a inibição de DPP-4 e a patologia GABAérgica autoimune (anti-GAD65)
- Conduzir estudos pré-clínicos em modelos animais de síndrome de rigidez muscular antes de qualquer ensaio humano
- Obter os dados detalhados dos 20 registros ANVISA para rastreabilidade regulatória completa
- Coletar informações de segurança completas (advertências, contraindicações) via bula oficial ANVISA antes de qualquer avaliação clínica
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

