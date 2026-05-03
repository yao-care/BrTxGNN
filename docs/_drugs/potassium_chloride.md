---
layout: default
title: Potassium Chloride
parent: 僅模型預測 (L5)
nav_order: 406
evidence_level: L5
indication_count: 1
---

# Potassium Chloride
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

Using `txgnn-pipeline` para gerar o relatório de reposicionamento. Analisando o Evidence Pack para POTASSIUM CHLORIDE → Renal Tubular Acidosis.

---

# Cloreto de Potássio: Do Suplemento Eletrolítico à Acidose Tubular Renal

## Resumo em Uma Frase

Cloreto de Potássio (KCl) é amplamente utilizado na prática clínica como suplemento eletrolítico para correção e prevenção da hipocalemia. O modelo TxGNN prevê que pode ser eficaz no manejo da **Acidose Tubular Renal (Renal Tubular Acidosis)**, atualmente com **9 ensaios clínicos** e **19 publicações** apoiando esta direção.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Suplementação de potássio / correção de hipocalemia |
| Nova Indicação Prevista | Acidose Tubular Renal (Renal Tubular Acidosis) |
| Pontuação de Previsão TxGNN | 99.87% |
| Nível de Evidência | L3 |
| Situação no Mercado Brasileiro | ✗ Não comercializado |
| Número de Registros | 0 |
| Decisão Recomendada | Proceed with Guardrails |

---

## Por que Esta Previsão é Razoável?

Na acidose tubular renal (RTA), especialmente nos tipos 1 (distal) e 2 (proximal), há um defeito na secreção de H⁺ ou na reabsorção de HCO₃⁻ pelo túbulo renal. Como mecanismo compensatório, ocorre aumento da excreção urinária de K⁺, levando frequentemente à **hipocalemia** — uma das manifestações mais características da RTA distal. O Cloreto de Potássio atua diretamente nesse desequilíbrio, suprindo o K⁺ perdido e auxiliando nos mecanismos de troca iônica intracelular/extracelular.

A relação entre KCl e RTA é, portanto, mecanisticamente direta: a hipocalemia causada pela perda tubular de potássio representa uma indicação clínica clássica para reposição de potássio. Na prática, o KCl frequentemente compõe os esquemas de tratamento da RTA em associação com agentes alcalinizantes (Citrato de Potássio ou NaHCO₃), para correção simultânea da acidose e da depleção de K⁺.

Um ponto crítico de segurança: o **Tipo 4 de RTA** (hipercalêmica, associada a resistência à aldosterona) representa uma **contraindicação absoluta** ao uso de KCl, pois nesses pacientes já existe retenção de potássio. O uso clínico com KCl é restrito e fundamentado para os Tipos 1 e 2, em que a hipocalemia está documentada.

---

## Evidências de Ensaios Clínicos

| Número do Ensaio | Fase | Status | Participantes | Principais Achados |
|---------|------|------|------|---------|
| [NCT03354507](https://clinicaltrials.gov/study/NCT03354507) | N/A | Desconhecido | 40 | Estudo piloto em pacientes pediátricos com epilepsia usando Topiramato (indutor clássico de RTA Tipo 2); avalia efeito do NaHCO₃ oral na acidose metabólica tubular — KCl como suporte eletrolítico padrão nesse contexto |
| [NCT01894594](https://clinicaltrials.gov/study/NCT01894594) | Phase 1 | Encerrado | 7 | Terapia alcalinizante (Alkali Therapy) em doença falciforme com bicarbonato deprimido; RTA é complicação renal frequente nessa doença, e reposição de K⁺ é componente essencial da alcalinização |
| [NCT01843309](https://clinicaltrials.gov/study/NCT01843309) | Phase 4 | Encerrado | 36 | Espironolactona para prevenção de anomalias eletrolíticas em pacientes tratados com Anfotericina B — fármaco classicamente indutor de RTA Tipo 1 distal; KCl como suporte obrigatório na correção de hipocalemia induzida |
| [NCT03644706](https://clinicaltrials.gov/study/NCT03644706) | Phase 3 | Encerrado | 3 | Estudo de retirada controlado por placebo avaliando ADV7103 (formulação combinada de sais de potássio) em RTA distal primária pediátrica e adulta; encerrado precocemente por baixo recrutamento |
| [NCT01834768](https://clinicaltrials.gov/study/NCT01834768) | Phase 2 | Desconhecido | 31 | Segurança da Eplerenona em receptores de transplante renal tratados com Ciclosporina A; monitoramento de K⁺ sérico como desfecho secundário em contexto de RTA pós-transplante |
| [NCT07273838](https://clinicaltrials.gov/study/NCT07273838) | Phase 2 | Em andamento | 130 | Inibidor de SGLT2 para síndrome cardiorrenal aguda; disfunção tubular e hipocalemia são complicações frequentes, com KCl como terapia de suporte eletrolítico |
| [NCT06750172](https://clinicaltrials.gov/study/NCT06750172) | N/A | Em andamento | 33 | Consistência da aldosterona urinária de 24h no diagnóstico de hiperaldosteronismo primário; distúrbio associado a acidose hipocalêmica com perfil fisiopatológico similar à RTA Tipo 4 |
| [NCT06867471](https://clinicaltrials.gov/study/NCT06867471) | N/A | Em andamento | 43 | Efeito da cetose exógena na proteinúria e função renal em DRC e doença renal policística; monitoramento eletrolítico inclui K⁺ sérico, relevante em pacientes com acidose tubular subjacente |
| [NCT00120731](https://clinicaltrials.gov/study/NCT00120731) | N/A | Cancelado | 0 | Citrato de Potássio em crianças com hipercalciúria idiopática e urolitíase — complicações típicas da RTA distal; estudo cancelado antes de iniciar, sem dados disponíveis |

---

## Evidências da Literatura

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [33459628](https://pubmed.ncbi.nlm.nih.gov/33459628/) | 2021 | Clinical Management Review | Arch Esp Urol | RTA é grupo de distúrbios raros de acidificação tubular; reposição de K⁺ e alcalinização são os pilares do tratamento da RTA distal e proximal, especialmente quando associada a cálculos renais |
| [8694660](https://pubmed.ncbi.nlm.nih.gov/8694660/) | 1996 | Pathophysiology Review | Arch Intern Med | Fisiopatologia e diagnóstico da RTA: K⁺ urinário e sérico são parâmetros centrais no diagnóstico diferencial dos subtipos; hipocalemia é achado cardinal da RTA distal |
| [21314872](https://pubmed.ncbi.nlm.nih.gov/21314872/) | 2011 | Clinical Review | Int J Clin Pract | Abordagem clínica da RTA em adultos: Tipo 1 associado a hipocalemia, manejo requer alcalinização e suplementação de potássio com KCl ou citrato de potássio |
| [3518609](https://pubmed.ncbi.nlm.nih.gov/3518609/) | 1986 | Clinical Review | Annu Rev Med | Espectro clínico da RTA: subtipos hipocalêmico e hipercalêmico com implicações terapêuticas distintas; reposição de K⁺ indicada nos Tipos 1 e 2 |
| [17297212](https://pubmed.ncbi.nlm.nih.gov/17297212/) | 2007 | Clinical Review | Acta Med Indones | Hipocalemia frequente na prática clínica; RTA como causa renal importante de perda de potássio; suplementação com KCl descrita como abordagem de primeira linha |
| [783200](https://pubmed.ncbi.nlm.nih.gov/783200/) | 1976 | Clinical Study | J Clin Invest | Em 10 pacientes com RTA Tipo 1 clássica, correção da acidose com bicarbonato de potássio oral demonstrou comprometimento da conservação renal de sódio; reforça necessidade de monitoramento eletrolítico abrangente |
| [37081692](https://pubmed.ncbi.nlm.nih.gov/37081692/) | 2023 | Literature Review | Endocrine J | Reclassificação do pseudo-hipoaldosteronismo Tipo II como RTA Tipo 4; distinções entre subtipos são críticas para evitar uso inadequado de KCl em formas hipercalêmicas |
| [38445406](https://pubmed.ncbi.nlm.nih.gov/38445406/) | 2023 | Cohort/Genetic Study | Tunis Med | Correlação genótipo-fenótipo na RTA distal: hipocalemia e hipercalciúria como manifestações fenotípicas centrais que requerem suplementação de K⁺ como parte do manejo |
| [20228475](https://pubmed.ncbi.nlm.nih.gov/20228475/) | 2010 | Case Report | Neurology India | Paralisia respiratória por RTA distal com hipocalemia grave (K⁺ = 1,6 mEq/L); recuperação completa após NaHCO₃ e suplementação de potássio — caso ilustrativo da urgência clínica |
| [34748193](https://pubmed.ncbi.nlm.nih.gov/34748193/) | 2022 | Case Report | J Nephrol | RTA distal com paralisia periódica hipocalêmica durante a gestação; manejo com suplementação de potássio e bicarbonato como intervenção essencial |

---

## Informações de Comercialização no Brasil

Cloreto de Potássio **não possui registros ativos** na base regulatória consultada. O fármaco não consta com registro vigente no mercado brasileiro neste levantamento (data de corte: 2026-05-01).

> **Nota:** Na prática hospitalar brasileira, soluções injetáveis e orais de KCl são amplamente utilizadas como insumos farmacêuticos hospitalares e suplementos eletrolíticos. Recomenda-se verificação direta junto à ANVISA para confirmação atualizada do status regulatório das diferentes formulações disponíveis.

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

> **Alerta clínico baseado no mecanismo (derivado do rationale de reposicionamento):** O uso de KCl é **contraindicado na RTA Tipo 4** (hipercalêmica/hiperaldosteronismo), onde já existe retenção de potássio. O uso é clinicamente suportado apenas para RTA Tipos 1 e 2, com hipocalemia documentada. Monitoramento de K⁺ sérico é obrigatório durante o tratamento.

---

## Conclusão e Próximos Passos

**Decisão: Proceed with Guardrails**

**Justificativa:**
O KCl possui papel mecanisticamente consolidado na correção da hipocalemia associada à RTA Tipos 1 e 2, suportado por extensa literatura clínica (19 publicações incluindo revisões de manejo clínico e estudos fisiológicos). Contudo, as evidências são predominantemente observacionais e revisões narrativas (L3), sem ensaios clínicos randomizados específicos avaliando KCl isolado como intervenção para RTA.

**Para prosseguir, é necessário:**
- Confirmar o status regulatório atualizado das formulações de KCl junto à ANVISA
- Obter dados completos de segurança (bula ou RCM) para advertências e contraindicações formais
- Estratificar o subtipo de RTA **antes** do uso: excluir RTA Tipo 4 (hipercalêmica) para evitar hipercalemia grave
- Avaliar necessidade de combinação com agente alcalinizante (Citrato de Potássio ou NaHCO₃) para manejo completo da acidose metabólica
- Definir protocolo de monitoramento: K⁺ sérico, pH arterial/venoso, bicarbonato, função renal (creatinina, TFG) em acompanhamento seriado
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

