---
layout: default
title: Ibuprofen
parent: Apenas Predição do Modelo (L5)
nav_order: 358
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Ibuprofen: nova indicação prevista, Displasia acromesomélica tipo Hunter-Thompson (Acromesomelic dysplasi… (nível de evidência L5). Indicação original: Artrite reumatoide (entre outras: cefaleia, ost…"
---

# Ibuprofen
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

# Ibuprofeno: Da artrite reumatoide à displasia acromesomélica tipo Hunter-Thompson

## Resumo em Uma Frase

Ibuprofeno é um anti-inflamatório não esteroidal (AINE), originalmente usado no tratamento de artrite reumatoide, osteoartrite, cefaleia e artropatias, entre outras condições.
O modelo TxGNN prevê que pode ser eficaz para **displasia acromesomélica tipo Hunter-Thompson (Acromesomelic dysplasia, Hunter-Thompson type)**,
mas atualmente há **0 ensaios clínicos** e **0 publicações** apoiando esta direção. A previsão baseia-se apenas no modelo computacional.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Artrite reumatoide (entre outras: cefaleia, osteoartrite, artropatia, artrite idiopática juvenil, espondiloartropatia, persistência do canal arterial) |
| Nova Indicação Prevista | Displasia acromesomélica tipo Hunter-Thompson (Acromesomelic dysplasia, Hunter-Thompson type) |
| Pontuação de Previsão TxGNN | 99,74% |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | ✗ Não comercializado (nos dados compilados) |
| Número de Registros | 0 |
| Decisão Recomendada | Hold |

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação nos dados compilados. Segundo o conhecimento geral, o ibuprofeno inibe as enzimas ciclo-oxigenase 1 e 2 (COX-1 e COX-2), reduzindo a produção de prostaglandinas e, com isso, a inflamação, a dor e a febre. Sua eficácia em doenças articulares e musculoesqueléticas inflamatórias é bem estabelecida.

Não há relação mecanística plausível com a nova indicação. A displasia acromesomélica tipo Hunter-Thompson é uma doença esquelética rara, causada por variantes de perda de função no gene *CDMP1/GDF5* (via de sinalização BMP), sem relação com a inibição de COX. Uma ação anti-inflamatória não corrigiria um defeito genético do desenvolvimento.

A pontuação elevada (0,997) provavelmente reflete a proximidade, no grafo de conhecimento, com termos musculoesqueléticos e de artropatia, e não uma justificativa biológica. Deve ser interpretada com cautela.

## Informações de Comercialização no Brasil

Nos dados compilados, não há registros de ibuprofeno na ANVISA (situação: não comercializado; 0 registros). Recomenda-se confirmar diretamente no portal da ANVISA, pois o ibuprofeno costuma ter ampla presença comercial em muitos países.

## Considerações de Segurança

Não há dados de advertências e contraindicações de bula nos dados compilados. Consulte a bula para esses itens.

- **Contraindicações/precauções derivadas do grafo de conhecimento** (não correspondem ao texto de bula): hipertensão, insuficiência hepática, doença renal, úlcera péptica, doença inflamatória intestinal, trombocitopenia, distúrbios da coagulação sanguínea, acidente vascular cerebral, infarto do miocárdio, lúpus eritematoso sistêmico, diabetes mellitus, epilepsia, DPOC, hipotireoidismo, deficiência de potássio, hiperplasia prostática benigna, hipotensão, abuso/dependência de substâncias, entre outras.
- **Interações medicamentosas** (100 interações registradas; exibidas as principais):
  - **Maior:** ácido acetilsalicílico.
  - **Moderadas:** corticosteroides (betametasona, budesonida, dexametasona, hidrocortisona), sulfonilureias (acetoexamida, clorpropamida, glimepirida, glipizida, glibenclamida), aprepitanto, balsalazida, dexfenfluramina, fenfluramina, exenatida, canamicina, levofloxacino.
  - **Menores:** famotidina, ranitidina, cimetidina.
- **Observação sobre a indicação prevista:** no caso de condições com neutropenia ou citopenia (como a síndrome WHIM, outra previsão do modelo), o uso de AINEs exigiria cautela.

## Outras Previsões do Modelo

Além da primeira, o modelo previu as indicações abaixo. Todas têm nível L5, sem ensaios clínicos nem literatura nos dados compilados, e decisão **Hold**.

| Posição | Doença prevista | Pontuação TxGNN | Avaliação do vínculo mecanístico |
|------|------|------|------|
| 2 | Síndrome braquiolmia-amelogênese imperfeita | 99,71% | Sem vínculo estabelecido |
| 3 | Miosclerose | 99,68% | Fraco e especulativo; no máximo alívio sintomático |
| 4 | Braquiolmia | 99,67% | Sem vínculo; no máximo analgesia genérica |
| 5 | Síndrome braquidactilia-sindactilia | 99,66% | Sem vínculo estabelecido |
| 6 | Pseudoacondroplasia | 99,66% | Indireto e fraco; uso apenas sintomático para dor articular |
| 7 | Síndrome de microftalmia colobomatosa-displasia rizomélica | 99,60% | Sem vínculo estabelecido |
| 8 | Hipotricose simples do couro cabeludo | 98,59% | Sem vínculo; hipótese especulativa via prostaglandinas |
| 9 | Síndrome WHIM | 98,43% | Sem vínculo (via CXCR4); cautela com AINEs |
| 10 | Hipotricose congênita com milia | 98,31% | Sem vínculo estabelecido |

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
A previsão tem apenas suporte computacional (L5), sem ensaios clínicos nem literatura, e carece de mecanismo plausível: o ibuprofeno não atua na via BMP/GDF5 envolvida na doença. A pontuação alta do modelo provavelmente reflete proximidade no grafo de conhecimento, e não biologia relevante.

**Para prosseguir, é necessário:**
- Dados de mecanismo de ação (MOA) consultados na DrugBank.
- Bula da ANVISA (advertências e contraindicações) e confirmação da situação de registro no Brasil.
- Evidências pré-clínicas que mostrem efeito do ibuprofeno sobre a via de sinalização GDF5/BMP, ou outra justificativa biológica.
- Revisão sistemática da literatura sobre AINEs em displasias esqueléticas, para avaliar apenas o benefício sintomático (dor).
- Avaliação de viabilidade da via de administração e análise de similaridade com as indicações originais (ambas ainda pendentes).
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

