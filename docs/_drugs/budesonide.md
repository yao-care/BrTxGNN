---
layout: default
title: Budesonide
parent: 僅模型預測 (L5)
nav_order: 139
evidence_level: L5
indication_count: 10
---

# Budesonide
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

O skill `txgnn-pipeline` cobre gestão de modelos e pipelines — não se aplica diretamente à geração de relatórios de avaliação. Prossigo com o relatório seguindo o Prompt v5 especificado no sistema.

---

# Budesonide: Das Doenças Inflamatórias das Vias Aéreas ao Eczema Atópico

## Resumo em Uma Frase

Budesonide é um corticosteroide glicocorticoide sintético amplamente utilizado no tratamento de asma, DPOC e doenças inflamatórias intestinais (doença de Crohn, colite microscópica). O modelo TxGNN prevê que pode ser eficaz para **Eczema Atópico (Atopic Eczema)**, atualmente com **2 ensaios clínicos** e **20 publicações** apoiando esta direção. A maior parte das evidências aborda o budesonide em condições atópicas relacionadas e o risco de sensibilização de contato, com um estudo translacional de 2024 oferecendo base direta para formulações tópicas dérmicas inovadoras.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Dados de registro no Brasil não disponíveis (corticosteroide para asma/DPOC e doenças inflamatórias intestinais) |
| Nova Indicação Prevista | Eczema Atópico (Atopic Eczema) |
| Pontuação de Previsão TxGNN | 99.96% |
| Nível de Evidência | L3 |
| Situação no Mercado Brasileiro | ✓ Comercializado |
| Número de Registros | 1 |
| Decisão Recomendada | Hold |

---

## Por que Esta Previsão é Razoável?

Budesonide é um corticosteroide glicocorticoide de segunda geração com alta afinidade pelos receptores de glicocorticoides e mínima biodisponibilidade sistêmica. Embora os dados de MOA detalhados não estejam disponíveis no Evidence Pack atual, o budesonide atua suprimindo a expressão de citocinas pró-inflamatórias — especialmente IL-4 e IL-13 da via Th2 —, estabilizando mastócitos e reduzindo a infiltração de eosinófilos nos tecidos-alvo. Como inibidor da fosfolipase A2 e bloqueador da transcrição de NF-κB, o fármaco exerce efeito anti-inflamatório local potente com mínimos efeitos sistêmicos.

O eczema atópico (dermatite atópica) é uma doença inflamatória crônica mediada centralmente pela via Th2, com IL-4 e IL-13 como mediadores-chave da inflamação e da disfunção de barreira cutânea — os mesmos alvos moleculares do budesonide. Os corticosteroides tópicos constituem o pilar do tratamento de primeira linha para dermatite atópica em todas as diretrizes internacionais (EADV, AAD, JDA). A questão de reposicionamento aqui não é a indicação em si, mas o desenvolvimento de formulações tópicas cutâneas específicas de budesonide, dado que o fármaco não possui formulação dérmica amplamente aprovada para essa indicação.

Um estudo de 2024 (PMID 38275852) demonstrou que nanopartículas de budesonide encapsuladas em polímero Eudragit L100 e incorporadas em hidrogéis pH-sensíveis superam as barreiras de penetração cutânea convencional, oferecendo liberação controlada e direcionada às lesões atópicas — onde o pH está tipicamente alterado. Isso confirma que a principal barreira para o uso de budesonide na dermatite atópica é tecnológica (formulação), e não mecanística.

---

## Evidências de Ensaios Clínicos

| Número do Ensaio | Fase | Status | Participantes | Principais Achados |
|---------|------|------|------|---------|
| [NCT01028560](https://clinicaltrials.gov/study/NCT01028560) | Phase 1/2 | Concluído | 58 | Imunoterapia para alergia em crianças atópicas com sibilância recorrente e alto risco de asma; recruta crianças com eczema/atopia mas não avalia budesonide diretamente para eczema |
| [NCT04680117](https://clinicaltrials.gov/study/NCT04680117) | NA | Desconhecido | 150 | Caracterização de endótipos de asma grave pediátrica combinando fenótipo, imunologia, metabolômica e microbiota; recruta crianças atópicas mas com foco em desfechos de asma, não eczema |

> **Nota:** Ambos os ensaios têm relevância indireta (Grau C) para budesonide no eczema atópico. Não foram identificados ensaios clínicos registrados avaliando diretamente budesonide tópico dérmico para dermatite atópica em humanos.

---

## Evidências da Literatura

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [38275852](https://pubmed.ncbi.nlm.nih.gov/38275852/) | 2024 | Pré-clínico/Formulação | Gels (Basel) | Nanopartículas poliméricas de budesonide em hidrogéis pH-sensíveis para terapia local de dermatite atópica pediátrica; supera limitações de penetração cutânea do budesonide convencional |
| [19875223](https://pubmed.ncbi.nlm.nih.gov/19875223/) | 2010 | Subgrupo RCT | Allergologia et Immunopathologia | Resposta ao budesonide inalatório em crianças atópicas vs. não-atópicas com sibilância recorrente; atopia associada a maior resposta ao fármaco |
| [8864369](https://pubmed.ncbi.nlm.nih.gov/8864369/) | 1996 | Coorte | Dermatology | Budesonide tópico em crianças com DA: avaliação do eixo IGF e turnover ósseo/colágeno, confirmando absorção percutânea e atividade sistêmica |
| [9496795](https://pubmed.ncbi.nlm.nih.gov/9496795/) | 1998 | Coorte | Pediatric Dermatology | Knemometria em crianças com DA tratadas com budesonide tópico; monitora supressão de crescimento como marcador de atividade sistêmica |
| [21062310](https://pubmed.ncbi.nlm.nih.gov/21062310/) | 2010 | RCT (Veterinário) | J Vet Pharmacol Ther | Budesonide 0,025% (Barazone) vs. placebo em dermatite atópica canina: redução significativa de lesões cutâneas e prurido em estudo cruzado randomizado de 3 semanas |
| [35133669](https://pubmed.ncbi.nlm.nih.gov/35133669/) | 2022 | Transversal | Contact Dermatitis | Padrão de sensibilização de contato em pacientes com e sem DA em centro asiático; budesonide identificado como marcador de hipersensibilidade a corticosteroides |
| [24603519](https://pubmed.ncbi.nlm.nih.gov/24603519/) | 2014 | Transversal | Dermatitis | Hipersensibilidade de contato à série europeia padrão e à série de corticosteroides em adolescentes/adultos com DA |
| [30053491](https://pubmed.ncbi.nlm.nih.gov/30053491/) | 2018 | Transversal | J Am Acad Dermatol | DA associada a maior risco de dermatite de contato alérgica a medicamentos tópicos em adultos, incluindo budesonide como alérgeno relevante |
| [33931866](https://pubmed.ncbi.nlm.nih.gov/33931866/) | 2021 | Observacional | Contact Dermatitis | Patch testing de budesonide na Itália (2018–2019): tendência de diminuição das taxas de alergia ao budesonide na última década |
| [40020933](https://pubmed.ncbi.nlm.nih.gov/40020933/) | 2025 | Translacional | J Allergy Clin Immunol | Síntese de ceramidas cutâneas alterada em esofagite eosinofílica pediátrica; reforça conexão mecanística entre disfunção de barreira epitelial e DA como contexto comum de atuação do budesonide |

---

## Informações de Comercialização no Brasil

| Número de Registro | Nome Comercial | Forma Farmacêutica | Indicação Aprovada |
|---------|------|------|-----------|
| (não informado) | (não informado) | (não informado) | (não informado) |

> **Nota:** O Evidence Pack registra 1 licença ativa no Brasil para budesonide, porém os campos de detalhe (número de registro, nome comercial, forma farmacêutica e indicação aprovada) não estão preenchidos nesta versão dos dados. Budesonide é comercialmente disponível no Brasil em formulações inalatórias (ex.: Pulmicort®) e orais/entéricas (ex.: Entocort®), sem formulação tópica cutânea aprovada pela ANVISA especificamente para dermatite atópica.

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

> **Alerta específico para esta indicação:** A literatura científica identifica budesonide como um dos marcadores padrão de hipersensibilidade a corticosteroides na Série Europeia de Patch Test. Em pacientes com dermatite atópica — exatamente a população-alvo desta indicação —, taxas de sensibilização de contato ao budesonide de 5–10% foram documentadas em múltiplos estudos. Esse risco de sensibilização cruzada representa uma consideração de segurança crítica para o desenvolvimento de qualquer formulação tópica dermatológica de budesonide nessa população.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
O mecanismo de ação de budesonide é farmacologicamente compatível com o eczema atópico (inibição da via Th2), e os corticosteroides tópicos já constituem padrão de tratamento para essa doença; contudo, os dois ensaios clínicos identificados têm relevância apenas indireta (ambos Grau C), a literatura humana disponível trata predominantemente do risco de alergia de contato ao budesonide em pacientes com DA, e o único dado diretamente relevante para reposicionamento é um estudo pré-clínico de formulação (2024) — sem qualquer ensaio clínico em humanos avaliando budesonide tópico dérmico para eczema atópico.

**Para prosseguir, é necessário:**
- Validação clínica (Fase 1/2) da formulação em nanopartículas/hidrogéis de budesonide para DA em humanos
- Avaliação sistemática do risco de sensibilização de contato a budesonide na população com DA (triagem com patch test)
- Obtenção dos dados completos de MOA via DrugBank API (remediação de DG002)
- Complementação das advertências e contraindicações da ANVISA (remediação de DG001 — Bloqueante)
- Preenchimento dos detalhes dos registros brasileiros de budesonide (número de registro, formas farmacêuticas e indicações aprovadas)
---

