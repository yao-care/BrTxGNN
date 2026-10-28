---
layout: default
title: Cefalotin
parent: Apenas Predição do Modelo (L5)
nav_order: 203
evidence_level: L5
indication_count: 8
last_modified_at: 2026-10-13
description: "Cefalotin: nova indicação prevista, Uretrite gonocócica (Gonococcal urethritis) (nível de evidência L4). Indicação original: Cefalosporinas / antibióticos sistêmicos simples"
monitor_inn: "cefalotin"
predicted_indications: ["gonococcal urethritis", "Ureaplasma urethritis", "bronchitis", "polyclonal hyperviscosity syndrome", "hyperamylasemia", "uterine inflammatory disease", "xanthogranulomatous pyelonephritis", "congenital analbuminemia"]
---

# Cefalotin
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

## Cefalotina: Da antibioticoterapia sistêmica à uretrite gonocócica
{: .text-alpha }

## Resumo em Uma Frase

Cefalotina (cefalotina sódica) é uma cefalosporina de primeira geração, registrada na ANVISA como antibiótico sistêmico, usada originalmente no tratamento de infecções bacterianas.
O modelo TxGNN prevê que pode ser eficaz para **uretrite gonocócica (gonococcal urethritis)**, mas atualmente há **0 ensaios clínicos** e **0 publicações** apoiando esta direção; a previsão se baseia apenas no modelo e em raciocínio indireto.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Cefalosporinas / antibióticos sistêmicos simples |
| Nova Indicação Prevista | Uretrite gonocócica (Gonococcal urethritis) |
| Pontuação de Previsão TxGNN | 0,9925 |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | Comercializado (registros ativos: 9 de 9) |
| Número de Registros | 9 (ativos: 9) |
| Decisão Recomendada | Hold |

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação nos dados compilados. Segundo informações conhecidas, a cefalotina é uma cefalosporina de primeira geração que inibe a síntese da parede celular bacteriana ao se ligar às proteínas ligadoras de penicilina (PBP). Sua eficácia em infecções bacterianas, sobretudo por Gram-positivos, é reconhecida, e mecanisticamente poderia ser aplicável a outras infecções bacterianas.

A uretrite gonocócica é uma infecção bacteriana, o que explica a pontuação alta do TxGNN como associação de classe antibacteriana. Contudo, as cefalosporinas de primeira geração têm atividade limitada contra *Neisseria gonorrhoeae*, e as diretrizes atuais se baseiam em cefalosporinas de terceira geração, como a ceftriaxona.

Além disso, o produto está cancelado no mercado brasileiro e é de uso exclusivamente parenteral. A previsão deve ser tratada como hipótese, sem suporte clínico direto.

**Outras indicações previstas (todas sem ensaios clínicos ou literatura):**

| Posição | Indicação | Pontuação | Nível | Comentário |
|---|---|---|---|---|
| 2 | Uretrite por *Ureaplasma* | 0,9925 | L5 | *Ureaplasma* não possui parede celular; beta-lactâmicos são mecanisticamente ineficazes |
| 3 | Bronquite | 0,9925 | L4 | Maioria é viral; antibiótico só seria plausível em casos bacterianos |
| 4 | Síndrome de hiperviscosidade policlonal | 0,9916 | L5 | Sem vínculo mecanístico plausível; a pontuação vem do modelo TxGNN (deep learning) e pode refletir semelhanças aprendidas pelo modelo entre doenças relacionadas, não evidência biológica |
| 5 | Hiperamilasemia | 0,9916 | L5 | Achado laboratorial sem relação com a ação antibacteriana |
| 6 | Doença inflamatória uterina | 0,9911 | L4 | Racional indireto (profilaxia cirúrgica); cobertura anaeróbica limitada |
| 7 | Pielonefrite xantogranulomatosa | 0,9909 | L4 | Tratamento é tipicamente cirúrgico; atividade limitada contra Gram-negativos |
| 8 | Analbuminemia congênita | 0,9901 | L5 | Doença genética; sem mecanismo plausível |

## Informações de Comercialização no Brasil

Todos os 9 registros encontrados estão válidos; o medicamento é comercializado.

| Número de Registro | Nome Comercial | Forma Farmacêutica | Indicação Aprovada |
|---------|------|------|-----------|
| Registro 116370100 | Cefalotina Sódica | Não informada | Cefalosporinas |
| Registro 100410215 | Cefalotina Sódica | Não informada | Cefalosporinas |
| Registro 104970176 | Cefalotil | Não informada | Antibióticos sistêmicos simples |
| Registro 174200013 | Cefalotina Sódica | Não informada | Cefalosporinas |
| Registro 100630084 | Kefalomax | Não informada | Cefalosporinas |

Há ainda outros 4 registros cancelados (Cefariston, Cefalotina Sódica ×2 e Keflin Neutro).

## Considerações de Segurança

- **Interações Medicamentosas:** foram identificadas 12 interações de gravidade moderada (base DDInter):
  - **Aminoglicosídeos:** canamicina, neomicina, estreptomicina, amicacina (incluindo a forma lipossomal) e gentamicina.
  - **Outros:** ácido picossulfúrico, varfarina, cloranfenicol, etinilestradiol, ácido micofenólico e pemetrexede.
- **Transportadores:** a cefalotina inibe o transportador de ânions orgânicos OAT3 (SLC22A8) e interage com o OAT4 (SLC22A11), o que pode alterar a eliminação renal de outros fármacos.

Para advertências e contraindicações, consulte a bula.

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
- Não há ensaios clínicos nem literatura apoiando a previsão; a evidência é apenas indireta (L4).
- O fármaco tem atividade limitada contra *N. gonorrhoeae*, existem alternativas padrão (ceftriaxona) e o medicamento é comercializado no Brasil (9 de 9 registros válidos).

**Para prosseguir, é necessário:**
- Dados de mecanismo de ação (MOA) e do perfil de sensibilidade de *N. gonorrhoeae* à cefalotina.
- Bula da ANVISA com advertências e contraindicações, para triagem de segurança.
- Estudos in vitro ou clínicos que mostrem vantagem sobre os tratamentos atuais.
- Avaliação da viabilidade regulatória, dado que não há registro válido no Brasil.
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

