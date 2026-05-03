---
layout: default
title: Valine
parent: 僅模型預測 (L5)
nav_order: 499
evidence_level: L5
indication_count: 10
---

# Valine
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

# Valina: De Suplemento de Aminoácido Essencial à Colangite Esclerosante

## Resumo em Uma Frase

Valina (Valine) é um aminoácido essencial de cadeia ramificada (BCAA), utilizado clinicamente como suporte nutricional em condições de hepatopatia crônica e depleção proteica.
O modelo TxGNN prevê que pode ser eficaz para **Colangite Esclerosante (Sclerosing Cholangitis)**,
atualmente com **0 ensaios clínicos** e **2 publicações** apoiando esta direção.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|----------|
| Indicação Original | Suplementação de aminoácido essencial (sem indicação aprovada registrada) |
| Nova Indicação Prevista | Colangite Esclerosante (Sclerosing Cholangitis) |
| Pontuação de Previsão TxGNN | 99.42% |
| Nível de Evidência | L4 |
| Situação no Mercado Brasileiro | ✗ Não comercializado |
| Número de Registros | 0 |
| Decisão Recomendada | Hold |

---

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação no Evidence Pack. Valina é um dos três aminoácidos de cadeia ramificada (BCAAs — junto com leucina e isoleucina), essencial porque o organismo humano não consegue sintetizá-lo, sendo obtido exclusivamente pela dieta ou suplementação. Em contexto clínico, BCAAs são utilizados no manejo de hepatopatias avançadas, especialmente na prevenção e tratamento da encefalopatia hepática.

Na colangite esclerosante primária (PSC) e na cirrose biliar primária (PBC), a fadiga é um problema clínico prevalente associado a desequilíbrios nos padrões de aminoácidos plasmáticos. Em particular, a razão BCAA/aminoácidos aromáticos (razão de Fischer) costuma estar reduzida nessas condições colestáticas crônicas, o que confere uma plausibilidade metabólica à suplementação de Valina como BCAA.

Um estudo de Randomização Mendeliana publicado em 2024 (PMID 39015781) investigou a relação causal entre metabólitos sanguíneos e as duas principais colangiopatias colestáticas (PBC e PSC), sugerindo que perturbações metabólicas — potencialmente incluindo vias de aminoácidos — podem ter relevância causal na patogênese da PSC. Contudo, nenhum estudo investigou diretamente Valina como agente terapêutico para colangite esclerosante. A previsão do TxGNN permanece no estágio de hipótese mecanística, necessitando validação experimental.

---

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados.

---

## Evidências da Literatura

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|-----------|-------------------|
| [39015781](https://pubmed.ncbi.nlm.nih.gov/39015781/) | 2024 | Mendelian Randomization | Frontiers in Medicine | Investigou relação causal entre metabólitos sanguíneos e doenças colestáticas (PBC e PSC); vias metabólicas de aminoácidos podem ter relevância causal no risco de PSC |
| [15790420](https://pubmed.ncbi.nlm.nih.gov/15790420/) | 2005 | Cross-sectional / Observational | BMC Gastroenterology | Pacientes com PBC e PSC apresentam padrões anormais de aminoácidos plasmáticos; alterações em tirosina e na razão BCAA/AAA estão associadas à fadiga nessas condições |

---

## Informações de Comercialização no Brasil

Valina (DB00161) não possui nenhum registro ativo na ANVISA. O produto não está comercializado no Brasil.

---

## ⚠️ Alerta de Qualidade das Previsões

**A maioria das 10 indicações previstas neste pacote apresenta fortes sinais de falso positivo**, provavelmente decorrentes de confusão no grafo de conhecimento entre o nó "Valine" (fármaco/suplemento) e referências a "resíduos de valina" em proteínas descritas na literatura genética.

| Rank | Indicação | Sinal de Alerta |
|------|-----------|----------------|
| 2 | Glaucoma de ângulo fechado | Publicações descrevem mutações nas proteínas PRPH2 e TIGR/MYOC envolvendo resíduos de valina — sem relação com Valina como fármaco |
| 4–7 | Outros tipos de glaucoma | Nenhuma evidência clínica ou mecanística; possível propagação do sinal espúrio no grafo |
| 8 | Resistência ao hormônio tireoidiano (RTH-β) | 7 publicações descrevem substituições Leu→Val no receptor THR-β (V336M, V349M, L346V etc.) — genética molecular, não farmacologia de Valina |
| 10 | Hipertiroxinemia | Publicações descrevem mutação Val109 na Transtirretina (TTR) e mutações THR-β — mesma confusão de falso positivo |
| 9 | Bundle branch block (obsolete) | Diagnóstico marcado como obsoleto na ontologia; zero evidências |

**Apenas o Rank 1 (Colangite Esclerosante)** possui justificativa mecanística minimamente plausível via metabolismo de BCAAs em hepatopatias colestáticas. Recomenda-se revisão do pipeline de recuperação de evidências para distinguir "Valine como fármaco" de "valine residue" em estudos de genética molecular.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
As evidências disponíveis para a única indicação mecanisticamente plausível (colangite esclerosante) são exclusivamente observacionais e de randomização mendeliana (L4), sem nenhum ensaio clínico registrado que avalie Valina como intervenção terapêutica direta. A inexistência de registros na ANVISA e a ausência de dados de segurança formais impedem qualquer progressão imediata.

**Para prosseguir, é necessário:**
- Conduzir revisão sistemática focada em suplementação de BCAAs (especialmente Valina) em doenças colestáticas crónicas (PSC/PBC)
- Investigar estudos sobre razão de Fischer e suplementação de BCAA em pacientes com PSC
- Suprir DG001: obter advertências e contraindicações completas da bula (necessário para avaliação de segurança S1)
- Suprir DG002: confirmar mecanismo de ação formal via consulta à API do DrugBank
- Revisar o pipeline de _evidence retrieval_ para filtrar falsos positivos oriundos de confusão "fármaco Valina" vs. "resíduo de valina" em estudos de genética molecular

---

> ⚕️ **Aviso:** Este relatório é gerado automaticamente pelo pipeline TxGNN para fins de pesquisa. Os resultados não constituem aconselhamento médico. Candidatos a reposicionamento requerem validação clínica antes de qualquer aplicação terapêutica.
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

