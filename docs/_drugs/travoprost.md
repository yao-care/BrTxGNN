---
layout: default
title: Travoprost
parent: 僅模型預測 (L5)
nav_order: 493
evidence_level: L5
indication_count: 10
---

# Travoprost
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

Usando o skill `txgnn-pipeline` para orientar a geração do relatório de reposicionamento, e analisando o Evidence Pack JSON fornecido — Travoprost (DB00287), indicação prevista rank 1: visceral calciphylaxis — segue o relatório:

---

# Travoprost: Do Glaucoma à Calcifiláxia Visceral

## Resumo em Uma Frase

Travoprost é um análogo sintético da prostaglandina F2α (PGF2α), originalmente indicado para o tratamento do **glaucoma de ângulo aberto e hipertensão ocular**, reduzindo a pressão intraocular pelo aumento do escoamento uveoescleral.
O modelo TxGNN prevê que pode ser eficaz para **Calcifiláxia Visceral (Visceral Calciphylaxis)**, porém sem nenhum ensaio clínico e sem nenhuma publicação apoiando diretamente esta direção — trata-se de uma previsão computacional sem suporte empírico disponível.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Glaucoma de ângulo aberto / Hipertensão ocular |
| Nova Indicação Prevista | Calcifiláxia Visceral (Visceral Calciphylaxis) |
| Pontuação de Previsão TxGNN | 99.99% |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | ✓ Comercializado |
| Número de Registros | 20 |
| Decisão Recomendada | Hold |

---

## Por que Esta Previsão é Razoável?

Travoprost é um análogo sintético da prostaglandina F2α que atua como **agonista seletivo do receptor FP**. No contexto oftalmológico, seu mecanismo principal é a redução da pressão intraocular via aumento do fluxo uveoescleral, com eficácia clínica bem estabelecida para glaucoma de ângulo aberto e hipertensão ocular. Os dados detalhados de mecanismo de ação sistêmico não estão disponíveis neste Evidence Pack; as informações abaixo baseiam-se no conhecimento farmacológico consolidado da classe.

A calcifiláxia visceral é uma condição rara e grave, caracterizada por **calcificação vascular progressiva, trombose microangiopática e necrose isquêmica tecidual** — predominantemente em pacientes com doença renal crônica avançada. A lógica teórica de reposicionamento parte do fato de que algumas prostaglandinas (PGE1/alprostadil e PGI2/prostaciclina) possuem propriedades vasodilatadoras e antiagregantes com potencial protetor vascular, o que pode ter gerado esta associação no grafo do conhecimento do TxGNN.

No entanto, **esta previsão apresenta limitações mecanísticas importantes**. O receptor FP — alvo de Travoprost — exerce efeito predominantemente **vasoconstritivo** nos vasos sistêmicos, o oposto do que seria necessário para reverter a isquemia tecidual da calcifiláxia. As prostaglandinas com propriedade terapêutica em vasculopatias (PGE1, PGI2) atuam por receptores EP e IP, farmacologicamente distintos do FP. A previsão do TxGNN provavelmente reflete ruído de conectividade no agrupamento vascular do grafo, sem base biológica direta para este reposicionamento.

---

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados.

---

## Evidências da Literatura

Atualmente não há literatura relacionada.

---

## Informações de Comercialização no Brasil

Travoprost possui **20 registros ativos** no Brasil. Os detalhes individuais (número de registro, nome comercial, forma farmacêutica e indicação aprovada) não constam nos dados deste Evidence Pack. Para informações completas, consulte o portal de consultas de medicamentos da ANVISA.

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
A previsão TxGNN para calcifiláxia visceral é nível L5 (apenas previsão de modelo, sem estudos reais), e o mecanismo de ação do Travoprost como agonista FP **contradiz** o perfil farmacológico necessário para abordar a fisiopatologia da condição — vasoconstrição sistêmica é o oposto do efeito desejado. Não há qualquer evidência clínica ou pré-clínica que suporte este reposicionamento.

**Para prosseguir, seria necessário:**
- Evidências pré-clínicas demonstrando que o agonismo do receptor FP tem efeito protetor em modelos de calcificação vascular
- Elucidação formal do mecanismo de ação sistêmico do Travoprost (atualmente lacuna de dados crítica)
- Dados completos da bula registrada na ANVISA para avaliação de advertências e contraindicações
- Reavaliação da relevância biológica com base em dados de expressão do receptor FP em tecidos vasculares sistêmicos afetados pela calcifiláxia
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

