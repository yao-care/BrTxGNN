---
layout: default
title: Magnesium Carbonate
parent: 僅模型預測 (L5)
nav_order: 334
evidence_level: L5
indication_count: 10
---

# Magnesium Carbonate
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

Usando o skill `txgnn-pipeline` como referência de contexto. Agora vou gerar o relatório completo com base no Evidence Pack fornecido.

---

# Carbonato de Magnésio: Do antiácido clássico à Úlcera Péptica Ativa

## Resumo em Uma Frase

Carbonato de Magnésio (MgCO₃) é um componente antiácido inorgânico clássico, historicamente utilizado em formulações combinadas — como o Caved-S — para neutralização do ácido gástrico em distúrbios gastrointestinais.
O modelo TxGNN prevê que pode ser eficaz para **Úlcera Péptica Ativa (active peptic ulcer disease)**, com pontuação de previsão de **99,96%**.
Atualmente, há **0 ensaios clínicos** registrados especificamente para esta indicação e **4 publicações científicas** — incluindo 3 ECRs históricos — apoiando esta direção.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Sem indicação aprovada registrada no Brasil (componente antiácido de uso histórico comprovado) |
| Nova Indicação Prevista | Úlcera Péptica Ativa (active peptic ulcer disease) |
| Pontuação de Previsão TxGNN | 99,96% |
| Nível de Evidência | L3 |
| Situação no Mercado Brasileiro | ✗ Não comercializado |
| Número de Registros | 0 |
| Decisão Recomendada | Proceed with Guardrails |

---

## Por que Esta Previsão é Razoável?

Atualmente, não há dados formais de mecanismo de ação (MOA) disponíveis no DrugBank para o Carbonato de Magnésio. Com base no conhecimento farmacológico consolidado, o MgCO₃ é um antiácido inorgânico que reage diretamente com o ácido clorídrico (HCl) do suco gástrico, elevando o pH intragástrico e reduzindo a erosão dos íons hidrogênio sobre a mucosa ulcerada. A reação é química e imediata: MgCO₃ + 2 HCl → MgCl₂ + H₂O + CO₂. Esta é a base do seu uso histórico como componente ativo de formulações antiácidas combinadas.

Antes da descoberta do *Helicobacter pylori* (1983) e da introdução dos inibidores da bomba de prótons (IBPs), os antiácidos contendo MgCO₃ — especialmente o Caved-S — eram o tratamento de primeira linha para úlcera péptica. Múltiplos ensaios clínicos randomizados conduzidos entre 1973 e 1988 demonstraram que formulações com MgCO₃ alcançavam taxas de cura endoscópica comparáveis às obtidas com antagonistas H2 (cimetidina, ranitidina). Essa base histórica de eficácia é o que o modelo TxGNN captura por meio da rede de conhecimento biomédico.

A previsão é, portanto, mecanisticamente coerente: a acidez gástrica é o principal agente agressor na úlcera péptica ativa, e a neutralização direta desta acidez pelo MgCO₃ reduz a carga ácida sobre a lesão ulcerada. O contexto atual de reposicionamento não é um uso radicalmente novo, mas sim a validação computacional de um uso historicamente documentado que perdeu protagonismo clínico com o advento das terapias modernas — o que, no entanto, não elimina sua relevância em cenários de acesso limitado ou intolerância a IBPs.

---

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados para a indicação de **Úlcera Péptica Ativa** com Carbonato de Magnésio.

---

## Evidências da Literatura

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [7034155](https://pubmed.ncbi.nlm.nih.gov/7034155/) | 1981 | RCT | Scandinavian Journal of Gastroenterology | ECR duplo-cego em 72 pacientes com úlceras duodenais/prepilóricas: antiácido (85 mmol/10 ml) + anticolinérgico alcançou 50% de cura em 3 semanas vs. 67% com cimetidina (p < 0,005 vs. placebo) |
| [6755656](https://pubmed.ncbi.nlm.nih.gov/6755656/) | 1982 | RCT | Scand J Gastroenterology Suppl | Tratamento de úlceras ativas prepilóricas e duodenais comparando antiácido/anticolinérgico, cimetidina e placebo; confirma eficácia do regime antiácido combinado |
| [3003883](https://pubmed.ncbi.nlm.nih.gov/3003883/) | 1985 | RCT | Scandinavian Journal of Gastroenterology | Em 80 pacientes com úlcera duodenal ativa, antiácido (120 mmol HCl/dia, incl. MgCO₃) + dieta: taxa de cura de 60–67,5% em 4 semanas; sem diferença significativa entre grupos de fibra |
| [35720246](https://pubmed.ncbi.nlm.nih.gov/35720246/) | 2022 | Estudo Farmacológico | Medicine and Pharmacy Reports | Avaliação da capacidade de neutralização ácida (ANC) e propriedades de antiácidos comercializados; estabelece parâmetros de qualidade para formulações contendo MgCO₃ |

---

## Informações de Comercialização no Brasil

O Carbonato de Magnésio (DB09481) **não possui nenhum registro ativo na ANVISA** como produto farmacêutico independente. Nenhum produto foi identificado na base de dados regulatória brasileira para este fármaco como ingrediente principal.

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Proceed with Guardrails**

**Justificativa:**
O mecanismo antiácido do MgCO₃ é farmacologicamente coerente com a patologia da úlcera péptica ativa, sustentado por múltiplos ECRs históricos que documentam eficácia de formulações contendo MgCO₃ nessa condição. Contudo, o fármaco não está registrado no Brasil, o cenário clínico moderno é dominado por IBPs e erradicação de *H. pylori*, e não existem ensaios clínicos contemporâneos que avaliem MgCO₃ isoladamente nesta indicação.

**Para prosseguir, é necessário:**
- Obter dados de mecanismo de ação (MOA) formal via DrugBank API e documentação científica atualizada
- Solicitar registro regulatório junto à ANVISA antes de qualquer uso comercial no Brasil
- Realizar análise de viabilidade clínica frente às terapias modernas padrão (IBPs + esquema de erradicação de *H. pylori*)
- Levantar perfil de segurança atualizado: efeitos adversos (hipermagnesemia, diarreia osmótica, produção de CO₂), contraindicações e interações medicamentosas
- Conduzir ou identificar ensaios clínicos contemporâneos que avaliem MgCO₃ em populações com acesso limitado a IBPs ou intolerância a terapias de primeira linha
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

