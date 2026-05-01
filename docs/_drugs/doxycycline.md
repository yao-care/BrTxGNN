---
layout: default
title: Doxycycline
parent: 僅模型預測 (L5)
nav_order: 230
evidence_level: L5
indication_count: 10
---

# Doxycycline
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

Usando o skill `txgnn-pipeline` para contexto do pipeline TxGNN. Agora vou gerar o relatório com base no Evidence Pack fornecido.

---

# Doxycycline: De infecções bacterianas para ceratoconjuntivite epitelial punctata

## Resumo em Uma Frase

Doxycycline é um antibiótico de amplo espectro da classe das tetraciclinas, amplamente utilizado no tratamento de infecções por patógenos intracelulares como *Chlamydia trachomatis*, *Rickettsia* spp. e *Borrelia burgdorferi*.
O modelo TxGNN prevê que pode ser eficaz para **Ceratoconjuntivite Epitelial Punctata (Punctate Epithelial Keratoconjunctivitis)**, atualmente com **0 ensaios clínicos** e **1 publicação** apoiando esta direção.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|----------|
| Indicação Original | Infecções bacterianas por patógenos intracelulares (Chlamydia, Rickettsia, Borrelia, entre outros) |
| Nova Indicação Prevista | Ceratoconjuntivite Epitelial Punctata (Punctate Epithelial Keratoconjunctivitis) |
| Pontuação de Previsão TxGNN | 99.94% |
| Nível de Evidência | L4 |
| Situação no Mercado Brasileiro | Não comercializado |
| Número de Registros | 0 |
| Decisão Recomendada | Hold |

---

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação disponíveis neste Evidence Pack. Com base no conhecimento estabelecido, doxycycline é um antibiótico tetracíclico que atua inibindo a síntese proteica bacteriana ao bloquear a subunidade ribossomal 30S, sendo eficaz contra uma ampla gama de bactérias gram-positivas, gram-negativas e organismos intracelulares obrigatórios.

A relação entre a indicação original e a ceratoconjuntivite epitelial punctata é de natureza **indireta e mecanisticamente plausível**: *Chlamydia trachomatis* é o principal agente etiológico da conjuntivite folicular infecciosa, e doxycycline é o tratamento de primeira linha recomendado pela OMS para esta infecção. A ceratoconjuntivite epitelial punctata pode emergir como sequela corneal pós-infecciosa, decorrente de inflamação residual ou resposta imune persistente após o episódio de conjuntivite clamidiana.

O mecanismo proposto é, portanto, **de causa raiz**: a eliminação do patógeno primário (*C. trachomatis*) previne ou interrompe o processo inflamatório que leva ao comprometimento epitelial corneal. Não há evidências diretas de ação anti-inflamatória de doxycycline sobre o epitélio corneal neste contexto específico, e a previsão do TxGNN reflete essencialmente a associação patogênica entre as duas condições.

---

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados.

---

## Evidências da Literatura

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|-----------|-------------------|
| [1424659](https://pubmed.ncbi.nlm.nih.gov/1424659/) | 1992 | Case Series | Cornea | Dois casos de conjuntivite folicular por *C. trachomatis* tratados com tetraciclina oral ou doxycycline evoluíram para ceratoconjuntivite epitelial punctata persistente bilateral; lesões recorrentes em epitélio corneal com edema estromal anterior em um dos casos |

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
A previsão TxGNN tem base mecanística indireta (doxycycline como agente etiológico no tratamento de *C. trachomatis*, cuja infecção pode causar ceratoconjuntivite punctata), porém a evidência clínica se resume a uma única série de casos de 1992, sem ensaios clínicos registrados e sem dados regulatórios no Brasil. O nível de evidência L4 e a ausência de comercialização local inviabilizam progressão imediata.

**Para prosseguir, é necessário:**
- Conduzir estudos clínicos prospectivos avaliando doxycycline sistêmico ou tópico na prevenção e tratamento de ceratoconjuntivite epitelial punctata pós-clamidiana
- Confirmar o mecanismo de ação (MOA) detalhado, especialmente quanto a eventual efeito anti-inflamatório direto sobre o epitélio corneal
- Regularizar o status junto à ANVISA — o registro de doxycycline no Brasil é esperado dado seu uso clínico difundido; recomenda-se auditoria da base de dados consultada
- Avaliar a viabilidade de formulação tópica ocular como via de administração alternativa
- Obter dados de segurança locais (contraindicações, interações medicamentosas e advertências da bula brasileira) antes de qualquer avanço no pipeline
---

