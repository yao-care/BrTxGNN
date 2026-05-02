---
layout: default
title: Tenecteplase
parent: 僅模型預測 (L5)
nav_order: 459
evidence_level: L5
indication_count: 10
---

# Tenecteplase
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

Using `txgnn-pipeline` skill para orientar a geração do relatório de reposicionamento de fármacos TxGNN. Procedendo à análise do Evidence Pack e à geração do relatório.

---

# Tenecteplase: Do Infarto Agudo do Miocárdio ao Infarto Posteroinferior

## Resumo em Uma Frase

Tenecteplase é um agente trombolítico fibrina-específico de terceira geração (tPA recombinante modificado), aprovado para o tratamento do infarto agudo do miocárdio com supradesnivelamento do segmento ST (STEMI).
O modelo TxGNN prevê que pode ser eficaz para **Infarto Posteroinferior (Posteroinferior Myocardial Infarction)** com pontuação de **99,87%** — esta indicação corresponde a uma subclassificação anatômica do STEMI, mecanisticamente coberta pela aprovação regulatória já existente.
No pacote de evidências atual, não há ensaios clínicos ou publicações específicas indexadas para esta subclassificação.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Infarto Agudo do Miocárdio com Supradesnivelamento do ST (STEMI) |
| Nova Indicação Prevista | Infarto Posteroinferior (Posteroinferior Myocardial Infarction) |
| Pontuação de Previsão TxGNN | 99,87% |
| Nível de Evidência | L1 (subclassificação anatômica de indicação já aprovada via ASSENT-2 Phase 3) |
| Situação no Mercado Brasileiro | ✓ Comercializado |
| Número de Registros | 1 |
| Decisão Recomendada | Proceed with Guardrails |

---

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação (MOA) disponíveis neste pacote de evidências. Com base em informações estabelecidas, Tenecteplase é um ativador do plasminogênio tecidual (tPA) recombinante com três modificações moleculares em relação ao alteplase: substituição de aminoácidos que aumentam a especificidade pela fibrina (~14×), reduzem a inibição pelo PAI-1 e prolongam a meia-vida plasmática, permitindo administração como bolus intravenoso único. Seu mecanismo central consiste em ativar plasminogênio → plasmina, que cliva as ligações cruzadas da fibrina no trombo coronariano, restaurando a perfusão miocárdica.

O infarto posteroinferior é uma subclassificação anatômica do STEMI — corresponde à oclusão da artéria coronária direita (ACD) ou da artéria circunflexa esquerda (ACX) com isquemia atingindo a parede posterior e inferior do ventrículo esquerdo. Eletrocardiograficamente, manifesta-se com supradesnivelamento em derivações inferiores (DII, DIII, aVF) e, nas derivações posteriores (V7–V9), o que é o critério diagnóstico para o subtipo posteroinferior. Clinicamente, segue os mesmos protocolos de reperfusão do STEMI em geral, inclusive trombólise farmacológica quando a ICP-P não está disponível em tempo hábil.

Portanto, a previsão do TxGNN não representa reposicionamento no sentido estrito: o mecanismo trombolítico de Tenecteplase aplica-se diretamente ao infarto posteroinferior como subclassificação anatômica do STEMI. O ensaio ASSENT-2 (Phase 3, n > 16.000), pivô da aprovação de Tenecteplase para STEMI, não excluiu pacientes com base na localização anatômica do infarto — incluindo, portanto, o subtipo posteroinferior. Isso confere base de evidências de nível L1 por cobertura direta da indicação aprovada.

---

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados especificamente para infarto posteroinferior e Tenecteplase.

---

## Evidências da Literatura

Atualmente não há literatura relacionada especificamente para infarto posteroinferior e Tenecteplase.

---

## Informações de Comercialização no Brasil

Tenecteplase possui **1 registro ativo no Brasil** com status de produto comercializado. Os detalhes do registro — número de registro, nome comercial, forma farmacêutica e texto integral da indicação aprovada — não foram recuperados no presente pacote de evidências. Para consulta completa, acesse diretamente a base de dados de medicamentos da ANVISA (Bulário Eletrônico / Consulta de Produtos Registrados).

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Proceed with Guardrails**

**Justificativa:**
O infarto posteroinferior é uma subclassificação anatômica do STEMI — indicação para a qual Tenecteplase já possui aprovação regulatória sustentada por ensaio de Phase 3 (ASSENT-2, n > 16.000) — tornando o mecanismo trombolítico diretamente aplicável sem necessidade de novos ensaios de Phase 3 específicos. A recomendação de avançar com cautela reflete as lacunas de dados ainda pendentes no registro brasileiro e nas informações de segurança.

**Para prosseguir, é necessário:**
- Confirmar os detalhes do registro junto à ANVISA: número de registro, nome comercial, forma farmacêutica e indicação aprovada em bula (remediation DG001)
- Obter dados formais do mecanismo de ação via DrugBank API (DrugBank ID: DB00031 — remediation DG002)
- Recuperar advertências e contraindicações da bula ANVISA/TFDA, especialmente contraindicações à trombólise (cirurgia recente, sangramento ativo, AVC hemorrágico, HAS grave não controlada)
- Verificar protocolos clínicos específicos para infarto posteroinferior, incluindo critérios diagnósticos por derivações posteriores (V7–V9) e manejo de complicações associadas (bloqueio AV, disfunção do VD em infarto de parede inferior)
- Avaliar disponibilidade de ICP-P no contexto brasileiro e janela temporal para trombólise, considerando a infraestrutura hospitalar local
---

