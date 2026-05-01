---
layout: default
title: Fexofenadine
parent: 僅模型預測 (L5)
nav_order: 251
evidence_level: L5
indication_count: 10
---

# Fexofenadine
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

# Fexofenadine: Da Alergia Sazonal à Conjuntivite da Rosácea

## Resumo em Uma Frase

Fexofenadine é um anti-histamínico de segunda geração (antagonista H1), amplamente utilizado no tratamento de rinite alérgica sazonal e urticária crônica idiopática.
O modelo TxGNN prevê que pode ser eficaz para **Conjuntivite da Rosácea (Rosacea Conjunctivitis)**,
porém atualmente **não há ensaios clínicos nem publicações** registrados apoiando diretamente esta indicação — toda a evidência provém da previsão computacional.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Rinite alérgica sazonal / Urticária crônica idiopática |
| Nova Indicação Prevista | Conjuntivite da Rosácea (Rosacea Conjunctivitis) |
| Pontuação de Previsão TxGNN | 99.85% |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | ✗ Não comercializado |
| Número de Registros | 0 |
| Decisão Recomendada | Hold |

---

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação a partir da fonte oficial. Segundo informações disponíveis no Evidence Pack, fexofenadine atua como **antagonista seletivo do receptor H1 da histamina**, bloqueando a cascata de sinalização mediada por histamina responsável por vasodilatação, prurido e aumento da permeabilidade vascular — mecanismo central no tratamento das alergias sistêmicas.

A rosácea é uma doença inflamatória crônica com componente imune Th1/Th17. Quando acomete os olhos (rosácea ocular), provoca conjuntivite acompanhada de ativação de mastócitos e liberação local de histamina. Nesse contexto, o bloqueio H1 de fexofenadine poderia, teoricamente, aliviar vasodilatação e prurido ocular mediados por histamina.

No entanto, a rosácea conjunctivitis é uma condição multifatorial: a inflamação vai além do eixo histamínico e envolve disfunção das glândulas de Meibômio, disbiose do microbioma ocular e desregulação imune adaptativa. Fexofenadine não possui formulação oftalmológica aprovada, e não há estudos específicos para rosácea ocular publicados. A previsão é mecanisticamente plausível no componente histamínico, mas insuficientemente suportada por evidências clínicas diretas.

---

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados.

---

## Evidências da Literatura

Atualmente não há literatura relacionada.

---

## Informações de Comercialização no Brasil

Fexofenadine não possui registro ativo no Brasil conforme os dados disponíveis. Nenhum registro foi identificado no sistema regulatório consultado (0 licenças ativas).

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
A previsão do TxGNN baseia-se exclusivamente no modelo computacional (nível L5), sem nenhum ensaio clínico ou publicação indexada de suporte. Embora a conexão mecanística via bloqueio H1 seja plausível para o componente alérgico da conjuntivite da rosácea, a ausência de dados clínicos e de formulação oftalmológica adequada impedem qualquer avanço imediato.

**Para prosseguir, é necessário:**
- Realizar busca ampliada de literatura sobre anti-histamínicos sistêmicos em rosácea ocular (incluindo olopatadine, cetirizina e loratadina como referência de classe)
- Avaliar se dados existentes de fexofenadine para sintomas oculares alérgicos em geral (conjuntivite alérgica sazonal) podem ser extrapolados
- Identificar formulação farmacêutica adequada para a indicação ocular (solução oftalmológica ou colírio)
- Confirmar mecanismo de ação (MOA) completo via consulta à API do DrugBank (DG002)
- Verificar registro e situação regulatória no Brasil via ANVISA, incluindo download e análise de bula para advertências e contraindicações (DG001)
- Mapear a rosácea ocular como subconjunto dentro de estudos clínicos existentes de anti-histamínicos H1 de segunda geração
---

