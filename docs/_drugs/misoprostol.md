---
layout: default
title: Misoprostol
parent: 僅模型預測 (L5)
nav_order: 354
evidence_level: L5
indication_count: 2
---

# Misoprostol
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

Usando o skill `txgnn-pipeline` para orientação e agora gerando o relatório com base no Evidence Pack fornecido.

---

# Misoprostol: Das Indicações Obstétricas ao Tratamento da Amenorreia

## Resumo em Uma Frase

Misoprostol é um análogo sintético da prostaglandina E1 (PGE1), amplamente utilizado em procedimentos obstétricos como interrupção medicamentosa da gravidez, tratamento de abortamento retido e indução do trabalho de parto.
O modelo TxGNN prevê que pode ser eficaz para **Amenorreia (Amenorrhea)**, atualmente com **0 ensaios clínicos** e **7 publicações** de suporte — a maioria como evidência indireta, sem estudos desenhados especificamente para o tratamento da amenorreia.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Indicações obstétricas (interrupção da gravidez, abortamento retido, indução do parto) |
| Nova Indicação Prevista | Amenorreia (Amenorrhea) |
| Pontuação de Previsão TxGNN | 99,64% |
| Nível de Evidência | L4 |
| Situação no Mercado Brasileiro | ✓ Comercializado |
| Número de Registros | 2 |
| Decisão Recomendada | Hold |

---

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação no Evidence Pack. Com base em informações conhecidas, misoprostol é um análogo sintético da prostaglandina E1 (PGE1) que atua nos receptores EP1 e EP3 do músculo liso uterino, desencadeando contrações do miométrio e descamação endometrial. É essa farmacologia que fundamenta seu uso consolidado em interrupção medicamentosa da gravidez, esvaziamento uterino em abortamento retido e preparo cervical pré-procedimento.

A conexão teórica com a amenorreia baseia-se nesse mesmo mecanismo: em subtipos de amenorreia secundária — como síndrome de Asherman (aderências intrauterinas pós-curetagem), retenção de resíduos trofoblásticos ou insuficiência lútea com endométrio atrófico —, a estimulação dos receptores EP1/EP3 poderia, em princípio, restaurar o fluxo menstrual. O caso mais direto é o abortamento retido: a amenorreia causada por tecido gestacional retido pode ser revertida pela administração de misoprostol, e há evidência clínica observacional para isso desde 1992.

Entretanto, é fundamental ressaltar que nenhum dos 7 artigos identificados foi desenhado com o **tratamento da amenorreia** como desfecho primário. A grande maioria utiliza "amenorreia ≤35 dias" como critério de inclusão para estudos de abortamento ultrarprecoce — ou seja, a amenorreia é o marcador de gravidez inicial, não a condição a ser tratada. Isso posiciona esta previsão no nível de hipótese mecanicista (L4), exigindo estudos prospectivos específicos antes de qualquer avanço clínico.

---

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados.

---

## Evidências da Literatura

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [25394644](https://pubmed.ncbi.nlm.nih.gov/25394644/) | 2015 | RCT | Reproductive Sciences | RCT com 2.500 mulheres (amenorreia ≤35 dias): doses decrescentes de mifepristona (150–50 mg) + 200 µg misoprostol para interrupção ultrarprecoce; avalia taxa de abortamento completo sem intervenção cirúrgica |
| [27678099](https://pubmed.ncbi.nlm.nih.gov/27678099/) | 2017 | RCT | Reproductive Sciences | RCT com 744 mulheres (amenorreia ≤35 dias): 75 mg mifepristona + misoprostol autoadministrado; compara administração hospitalar vs. domiciliar em termos de eficácia e aceitabilidade |
| [26001691](https://pubmed.ncbi.nlm.nih.gov/26001691/) | 2015 | Systematic Review | JOGC | Revisão sistemática sobre ablação endometrial no manejo de sangramento uterino anormal; misoprostol citado como agente de preparo cervical pré-procedimento (evidência indireta) |
| [26405260](https://pubmed.ncbi.nlm.nih.gov/26405260/) | 2015 | Cohort (Observacional) | Human Reproduction | Estudo de coorte sobre eficácia de mifepristona + misoprostol administrados antes da menstruação esperada para manutenção/restauração do estado não-gravídico |
| [29974571](https://pubmed.ncbi.nlm.nih.gov/29974571/) | 2018 | Open-label Cohort | J Obstet Gynaecol Res | Coorte aberta: baixa dose de mifepristona + misoprostol autoadministrado para interrupção precoce da gravidez; avalia segurança e eficácia em contexto de atendimento descentralizado |
| [1486304](https://pubmed.ncbi.nlm.nih.gov/1486304/) | 1992 | Prospective Observational | BMJ | Estudo pioneiro: misoprostol para manejo médico de abortamento retido e gestação anembriônica — a evidência mais direta de resolução de amenorreia causada por tecido gestacional retido |
| [37113350](https://pubmed.ncbi.nlm.nih.gov/37113350/) | 2023 | Case Report | Cureus | Relato de caso de fígado gorduroso agudo da gravidez; amenorreia figura como sintoma de apresentação, e misoprostol foi usado no manejo obstétrico (evidência indireta de contexto clínico) |

---

## Informações de Comercialização no Brasil

O Evidence Pack confirma **2 registros ativos** no Brasil com status **Comercializado**. No entanto, os dados de número de registro, nome comercial, forma farmacêutica e indicação aprovada não estão disponíveis no pacote atual. Para detalhes dos registros, consulte o [portal de consulta da ANVISA](https://consultas.anvisa.gov.br/).

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
A previsão do TxGNN (99,64%) é mecanisticamente plausível — a ação do misoprostol nos receptores EP1/EP3 com indução de descamação endometrial oferece uma base racional para subtipos de amenorreia secundária. Porém, a ausência completa de ensaios clínicos específicos e o caráter indireto de toda a literatura identificada (L4) não sustentam avanço clínico sem estudos dedicados.

**Para prosseguir, é necessário:**
- Definir o subtipo de amenorreia-alvo (ex.: amenorreia secundária por abortamento retido, síndrome de Asherman ou insuficiência lútea com endométrio atrófico)
- Obter dados completos de segurança a partir da bula registrada na ANVISA (advertências, contraindicações, perfil de eventos adversos — atualmente indisponíveis no pack)
- Projetar um estudo de viabilidade prospectivo com **restauração do ciclo menstrual** como desfecho primário, separando claramente subtipos de amenorreia
- Consultar o DrugBank (DB00929) para obter o perfil completo de MOA e interações, complementando a análise mecanicista
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

