---
layout: default
title: Gefitinib
parent: Apenas Predição do Modelo (L5)
nav_order: 337
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Gefitinib: nova indicação prevista, Fibromatose Gengival (Fibromatosis, gingival) (nível de evidência L5). Indicação original: Carcinoma pulmonar de células não pequenas / câncer de pulmão"
monitor_inn: "Gefitinib"
predicted_indications: ["fibromatosis, gingival", "fibroma of lung", "inclusion body myopathy with early-onset Paget disease with or without frontotemporal dementia", "hamartoma of lung", "lung hilum carcinoma", "lung benign neoplasm", "Leukomelanoderma-infantilism-intellectual disability-hypodontia-hypotrichosis syndrome", "pulmonary sulcus neoplasm", "lung germ cell tumor", "junctional epidermolysis bullosa"]
---

# Gefitinib
{: .fs-9 }

Nível de evidência: **L5** | Indicações previstas: **10** 
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

# Gefitinibe: Do câncer de pulmão de células não pequenas à fibromatose gengival

## Resumo em Uma Frase

Gefitinibe é um inibidor da tirosina quinase do receptor do fator de crescimento epidérmico (EGFR), originalmente usado no tratamento do câncer de pulmão de células não pequenas.
O modelo TxGNN prevê que pode ser eficaz para **Fibromatose Gengival (Fibromatosis, gingival)**, mas essa previsão é **apenas do modelo**: não há **nenhum ensaio clínico** nem **nenhuma publicação** que a apoie.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Carcinoma pulmonar de células não pequenas / câncer de pulmão |
| Nova Indicação Prevista | Fibromatose Gengival (Fibromatosis, gingival) |
| Pontuação de Previsão TxGNN | 99,89% |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | Não comercializado |
| Número de Registros | 0 |
| Decisão Recomendada | Hold |

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação nos dados compilados para este relatório. Segundo informações conhecidas, o gefitinibe é um inibidor seletivo da tirosina quinase do EGFR. Sua eficácia no câncer de pulmão de células não pequenas com mutações de EGFR está bem estabelecida, e a bloqueio dessa via reduz a proliferação e a sobrevivência celular.

A relação com a fibromatose gengival é, por ora, especulativa. Uma hipótese plausível, porém não verificada, é o envolvimento da sinalização EGFR/ERK na proliferação de fibroblastos. A similaridade com a indicação original não foi avaliada, e a compatibilidade de via de administração também está pendente.

A pontuação alta (99,89%) reflete a posição do candidato no modelo de grafo de conhecimento e não equivale a evidência de eficácia. Para esta doença, não foi reunido nenhum ensaio clínico nem artigo.

## Outras Indicações Previstas (Contexto)

O modelo gerou outras previsões com pontuações semelhantes. Todas permanecem em **Hold**, com evidência apenas indireta:

| Posição | Doença prevista | Pontuação | Nível | Observação |
|------|------|------|------|------|
| 2 | Fibroma de pulmão | 99,86% | L5 | Sem estudos; ligação mecanística especulativa |
| 3 | Miopatia por corpúsculos de inclusão com doença de Paget precoce ± demência frontotemporal | 99,86% | L5 | Doença causada por mutações em VCP; sem conexão evidente com EGFR |
| 4 | Hamartoma de pulmão | 99,86% | L5 | Sem estudos |
| 5 | Carcinoma do hilo pulmonar | 99,86% | L4 | Um relato de caso de cirurgia de resgate após resposta ao gefitinibe em câncer de pulmão avançado |
| 6 | Neoplasia benigna de pulmão | 99,85% | L4 | Literatura sobre câncer de pulmão maligno, não benigno; perfil risco-benefício desfavorável |
| 7 | Síndrome leucomelanodermia-infantilismo-deficiência intelectual-hipodontia-hipotricose | 99,84% | L5 | Literatura trata de eventos adversos, não de eficácia |
| 8 | Neoplasia do sulco pulmonar (tumor de Pancoast) | 99,84% | L4 | Subtipo anatômico de câncer de pulmão; evidência indireta |
| 9 | Tumor de células germinativas do pulmão | 99,84% | L4 | Um ensaio fase I em câncer de cabeça e pescoço/pulmão, sem relação direta |
| 10 | Epidermólise bolhosa juncional | 99,84% | L5 | Toxicidade cutânea do gefitinibe é preocupação em pele frágil |

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados para fibromatose gengival.

## Evidências da Literatura

Atualmente não há literatura relacionada para fibromatose gengival.

## Considerações de Segurança

- **Contraindicações no grafo de conhecimento** (relações do grafo, não texto de bula): doença hepática, doença da vesícula biliar, doença pulmonar intersticial, fibrose pulmonar e fibrose pulmonar pós-inflamatória.
- **Alerta da literatura:** relatos de pneumonite aguda e doença pulmonar intersticial associadas ao gefitinibe (incluindo caso fatal), além de toxicidade cutânea, prolongamento do intervalo QT e eventos cardiovasculares.
- **Interações medicamentosas:** foram identificadas 100 interações no total; as principais, de gravidade moderada, incluem:
  - Antiácidos e redutores de acidez gástrica: famotidina, ranitidina, cimetidina, nizatidina e inibidores da bomba de prótons (omeprazol, esomeprazol, pantoprazol, lansoprazol, dexlansoprazol, rabeprazol)
  - Claritromicina, miconazol, clotrimazol
  - Aprepitanto, dexametasona, naltrexona, troglitazona
  - Calcitriol e glimepirida (gravidade não classificada)

Para advertências e contraindicações de bula, consulte a bula do produto.

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
A previsão para fibromatose gengival baseia-se exclusivamente na pontuação do modelo (nível L5), sem ensaios clínicos nem literatura de suporte. Além disso, o fármaco não está registrado no Brasil e traz riscos relevantes (pneumonite, toxicidade cutânea e hepática) que exigiriam justificativa sólida para uso em uma condição não maligna.

**Para prosseguir, é necessário:**
- Dados detalhados do mecanismo de ação (MOA) do gefitinibe
- Estudos pré-clínicos que testem a via EGFR/ERK em fibroblastos gengivais
- Revisão sistemática da literatura específica sobre fibromatose gengival e inibidores de EGFR
- Obtenção e análise da bula (advertências e contraindicações) para triagem de segurança
- Avaliação da situação regulatória no Brasil (o fármaco consta como não comercializado) e da compatibilidade de via de administração
- Avaliação comparativa de risco-benefício frente às alternativas terapêuticas existentes
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

