---
layout: default
title: Procaine
parent: 僅模型預測 (L5)
nav_order: 417
evidence_level: L5
indication_count: 10
---

# Procaine
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

Usando `txgnn-pipeline` para verificar contexto do projeto. Agora vou gerar o relatório completo com base no Evidence Pack fornecido.

---

# Procaína: De Anestesia Local a Metemoglobinemia

## Resumo em Uma Frase

Procaína é um anestésico local do tipo éster, originalmente utilizado para bloqueios nervosos periféricos, infiltrações e anestesia regional em procedimentos médicos e odontológicos.
O modelo TxGNN prevê uma associação com **Metemoglobinemia (Methemoglobinemia)** como indicação de maior pontuação, com **0 ensaios clínicos** e **8 publicações** relacionados a essa direção.
⚠️ A análise de evidências indica que essa associação reflete uma **relação de efeito adverso documentado**, não uma indicação terapêutica emergente.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Anestesia local (anestésico do tipo éster) |
| Nova Indicação Prevista | Metemoglobinemia (Methemoglobinemia) |
| Pontuação de Previsão TxGNN | 99,50% |
| Nível de Evidência | L4 |
| Situação no Mercado Brasileiro | ✗ Não comercializado |
| Número de Registros | 0 |
| Decisão Recomendada | Hold |

---

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação no Evidence Pack. Com base no conhecimento farmacológico consolidado, a procaína é um anestésico local do tipo éster que bloqueia reversivamente os canais de sódio dependentes de voltagem (Nav1.x), impedindo a geração e propagação de potenciais de ação em fibras nervosas sensitivas. É rapidamente hidrolisada por colinesterases plasmáticas, gerando como metabólito principal o ácido para-aminobenzóico (PABA).

A relação entre procaína e metemoglobinemia é de natureza **adversa, não terapêutica**: os metabólitos oxidativos da procaína (intermediários semelhantes a nitritos) podem oxidar o ferro heme da hemoglobina de Fe²⁺ para Fe³⁺, formando metemoglobina incapaz de transportar oxigênio. Esse mecanismo de toxicidade é documentado especialmente em situações de doses elevadas, administração intravenosa ou em neonatos — que possuem capacidade reduzida de redução da metemoglobina pela NADH metemoglobina redutase.

O modelo TxGNN provavelmente interpretou a elevada co-ocorrência de "procaína" e "metemoglobinemia" na literatura científica como uma relação farmacológica positiva (drug–disease), quando na realidade trata-se de uma **causalidade de dano documentado**. Não existe hipótese mecanística plausível que suporte o uso terapêutico da procaína para tratar metemoglobinemia — de fato, essa classe de pacientes deve evitar o fármaco.

---

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados.

---

## Evidências da Literatura

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [6705717](https://pubmed.ncbi.nlm.nih.gov/6705717/) | 1984 | Revisão | *Drugs* | Uso racional de anestésicos locais — propriedades farmacológicas, classificação de bloqueios regionais e perfil de segurança clínica |
| [5118947](https://pubmed.ncbi.nlm.nih.gov/5118947/) | 1971 | Revisão | *Laval Medical* | Revisão geral sobre anestésicos locais, incluindo mecanismo e perfil de toxicidade da procaína |
| [6745527](https://pubmed.ncbi.nlm.nih.gov/6745527/) | 1984 | Revisão | *Fundam Appl Toxicol* | Mecanismos de interações toxicológicas com organofosforados — inibição de esterases e alteração no metabolismo de ésteres como a procaína |
| [3691245](https://pubmed.ncbi.nlm.nih.gov/3691245/) | 1987 | Observacional | *Zhonghua Wai Ke Za Zhi* | Avaliação dos níveis de metemoglobina durante anestesia intravenosa com procaína em pacientes cirúrgicos |
| [5644303](https://pubmed.ncbi.nlm.nih.gov/5644303/) | 1968 | Farmacocinética | *Am J Obstet Gynecol* | Passagem transplacentária de procaína e PABA — relevância para risco de toxicidade oxidativa em neonatos |
| [5529388](https://pubmed.ncbi.nlm.nih.gov/5529388/) | 1970 | Relato de Caso | *Acta Physiol Lat Am* | Metemoglobinemia documentada após administração intravenosa de procaína — confirmação de causalidade adversa |
| [705003](https://pubmed.ncbi.nlm.nih.gov/705003/) | 1978 | Relato de Caso | *Rev Esp Anestesiol Reanim* | Metemoglobinemia em recém-nascido após infiltração subcutânea de novocaína durante anestesia geral |
| [14246695](https://pubmed.ncbi.nlm.nih.gov/14246695/) | 1965 | Relato de Caso | *Lancet* | Metemoglobinemia seguindo anestésico local tipo amida — contextualiza toxicidade oxidativa como risco de classe dos anestésicos locais |

---

## Informações de Comercialização no Brasil

A procaína não possui registros ativos na ANVISA e não está comercializada no Brasil. Nenhuma licença foi localizada na base regulatória consultada.

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
A previsão TxGNN de rank 1 (metemoglobinemia) reflete uma **relação de efeito adverso estabelecido**, não uma nova indicação terapêutica. A procaína induz metemoglobinemia como toxicidade — o oposto de um tratamento. Prosseguir nessa direção não tem base científica e representaria risco clínico real.

**Para prosseguir, é necessário:**
- Redirecionar a análise para as indicações com potencial terapêutico real identificadas no mesmo Evidence Pack:
  - **Fibromialgia (rank 7, L3, "Research Question")** — mecanismo plausível via bloqueio de sensibilização central por neural therapy; há série de casos e literatura de suporte
  - **Tendinite (rank 8, L3, "Research Question")** — existe um ensaio clínico publicado (PMID [35480510](https://pubmed.ncbi.nlm.nih.gov/35480510/), 2022) sobre injeção de procaína 1% em tendinopatia do supraespinhoso
- Obter dados completos de mecanismo de ação via DrugBank API (gap DG002)
- Consultar advertências e contraindicações na bula ANVISA/TFDA (gap DG001 — bloqueante)
- Verificar viabilidade regulatória: a ausência de registro no Brasil exigiria processo de registro na ANVISA antes de qualquer desenvolvimento clínico local
- Avaliar a viabilidade de uma revisão sistemática sobre *neural therapy* com procaína como ponto de entrada para um possível futuro estudo prospectivo em dor musculoesquelética
---

