---
layout: default
title: Fosfomycin
parent: Apenas Predição do Modelo (L5)
nav_order: 328
evidence_level: L5
indication_count: 8
monitor_inn: "fosfomycin"
predicted_indications: ["uterine inflammatory disease", "xanthogranulomatous pyelonephritis", "epiglottitis", "urogenital tuberculosis", "laryngitis", "polyclonal hyperviscosity syndrome", "hyperamylasemia", "pyelitis"]
last_modified_at: 2026-10-23
description: "Fosfomycin: nova indicação prevista, Doença inflamatória uterina (uterine inflammatory disease) (nível de evidência L5). Indicação original: Antibióticos sistêmicos simples"
---

# Fosfomycin
{: .fs-9 }

Nível de evidência: **L5** | Indicações previstas: **8** 
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

## Fosfomicina: De antibiótico sistêmico à doença inflamatória uterina
{: .text-alpha }

## Resumo em Uma Frase

A fosfomicina é um antibiótico de uso sistêmico, comercializado no Brasil com registro na categoria "antibióticos sistêmicos simples".
O modelo TxGNN prevê que ela possa ser útil na **doença inflamatória uterina (uterine inflammatory disease)**.
Para essa direção, os dados compilados trazem apenas **2 estudos clínicos** (ambos pediátricos e sem relação direta com a doença) e **1 publicação** (sobre cistite, não sobre inflamação uterina). Não há estudo que investigue diretamente o uso da fosfomicina nessa doença.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Antibióticos sistêmicos simples (categoria do registro na ANVISA, sem doença específica descrita) |
| Nova Indicação Prevista | Doença inflamatória uterina (uterine inflammatory disease) |
| Pontuação de Previsão TxGNN | 0,9998 |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | Comercializado (registros ativos: 9 de 9) |
| Número de Registros | 9 (ativos: 9) |
| Decisão Recomendada | Hold |

---

## Por que Esta Previsão é Razoável?

A fosfomicina é um antibiótico bactericida de amplo espectro. Ela inibe a enzima MurA (UDP-N-acetilglucosamina enolpiruvil transferase) e bloqueia as etapas iniciais da síntese do peptidoglicano da parede bacteriana. Tem atividade contra Enterobacterales e alguns microrganismos Gram-positivos.

Doenças inflamatórias do útero e da pelve costumam envolver infecção bacteriana. Por isso, um antibiótico com esse espectro poderia, em tese, ter alguma utilidade. Trata-se de uma inferência mecanística e plausível, mas sem respaldo de dados clínicos diretos.

A única publicação associada à previsão trata de cistite (infecção urinária) em mulheres com endometriose que usaram dienogeste. É uma condição do trato urinário, não inflamação uterina, e o estudo não avalia a fosfomicina nessa doença. A pontuação alta do modelo, portanto, não é confirmada pelas evidências recuperadas.

---

## Evidências de Ensaios Clínicos

| Número do Ensaio | Fase | Status | Participantes | Principais Achados |
|---------|------|------|------|---------|
| [NCT01431326](https://clinicaltrials.gov/study/NCT01431326) | N/A | Concluído | 3.520 | Estudo farmacocinético de medicamentos pouco estudados em crianças, dados coletados durante o cuidado habitual. Não testa eficácia em doença inflamatória uterina. |
| [NCT04278404](https://clinicaltrials.gov/study/NCT04278404) | N/A | Recrutando | 5.000 | Estudo de plataforma sobre farmacocinética, farmacodinâmica e segurança de medicamentos pouco estudados em crianças e adultos jovens. Não tem desfecho de eficácia para a doença prevista. |

Os dois estudos foram avaliados como de relevância baixa (grau C) para a indicação prevista.

---

## Evidências da Literatura

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [35653789](https://pubmed.ncbi.nlm.nih.gov/35653789/) | 2022 | Coorte | J Obstet Gynaecol | Avaliou a gravidade dos sintomas de cistite aguda e a bacteriúria em mulheres com endometriose, após cirurgia laparoscópica seguida de dienogeste ou contraceptivos orais combinados. Não estuda fosfomicina nem inflamação uterina. |

---

## Informações de Comercialização no Brasil

Todos os 9 registros são de produtos com fosfomicina isolada e estão válidos. A tabela mostra os 5 primeiros.

| Número de Registro | Nome Comercial | Indicação Aprovada |
|---------|------|-----------|
| Registro nº 100840139 | Monuril | Antibióticos sistêmicos simples |
| Registro nº 101180640 | Fosfomicina trometamol | Antibióticos sistêmicos simples |
| Registro nº 117170082 | Fosfomicina trometamol | Antibióticos sistêmicos simples |
| Registro nº 117170084 | Fosfomicina trometamol | Antibióticos sistêmicos simples |
| Registro nº 114620043 | Myfos | Antibióticos sistêmicos simples |

---

## Considerações de Segurança

- **Relações de contraindicação registradas no grafo de conhecimento** (não correspondem a texto de bula): doença renal, piureter, colite por *Clostridium difficile* e enterocolite necrosante perinatal.
- **Interações medicamentosas** (3 identificadas):
  - Balsalazida: moderada.
  - Ácido picossulfúrico: moderada.
  - Metoclopramida: leve.

Consulte a bula para as advertências e contraindicações oficiais.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
- A previsão se apoia sobretudo no modelo e em um raciocínio mecanístico plausível. Os estudos recuperados não avaliam a fosfomicina na doença inflamatória uterina: são estudos farmacocinéticos pediátricos e um estudo sobre cistite.
- Sem estudo direto, o nível de evidência é L5, o que não justifica avançar.
- Entre as outras previsões do modelo para este fármaco, a pielite (infecção do trato urinário superior) tem respaldo clínico bem maior, incluindo um estudo randomizado de fase 2/3 com fosfomicina intravenosa. Essa direção merece avaliação separada.

**Para prosseguir, é necessário:**
- Estudos clínicos ou observacionais que avaliem a fosfomicina em infecções pélvicas ou uterinas, com desfechos de eficácia.
- Dados de penetração tecidual no útero e no trato genital feminino, e de atividade sobre os patógenos típicos dessas infecções.
- Revisão das advertências e contraindicações na bula aprovada pela ANVISA.
- Verificação da via de administração necessária, já que a fosfomicina oral de dose única é estabelecida apenas para infecção urinária baixa não complicada.
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

