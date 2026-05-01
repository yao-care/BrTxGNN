---
layout: default
title: Carbamazepine
parent: 僅模型預測 (L5)
nav_order: 164
evidence_level: L5
indication_count: 10
---

# Carbamazepine
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

# Carbamazepine: Da Epilepsia à Neuralgia do Trigêmeo

## Resumo em Uma Frase

Carbamazepine (CBZ) é um anticonvulsivante e antineurálgico clássico, reconhecido mundialmente como tratamento de primeira linha para epilepsia parcial e dor neuropática, embora não figure como medicamento registrado no Brasil na base de dados consultada.
O modelo TxGNN prevê que pode ser eficaz para **Neoplasia do Nervo Trigêmeo (Trigeminal Nerve Neoplasm)** — rótulo que, na literatura clínica associada, corresponde predominantemente à **Neuralgia do Trigêmeo (TN)** —, com **1 ensaio clínico** e **20 publicações** apoiando esta direção.
Há um importante desalinhamento ontológico no dataset TxGNN: o nó "trigeminal nerve neoplasm" agrupa casos de neuralgia do trigêmeo, não de tumores, o que afeta diretamente a interpretação do nível de evidência.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Não registrado no Brasil (sem licenças na base ANVISA consultada) |
| Nova Indicação Prevista | Neoplasia do Nervo Trigêmeo / Neuralgia do Trigêmeo (Trigeminal Nerve Neoplasm) |
| Pontuação de Previsão TxGNN | 99,9976% |
| Nível de Evidência | L2 (conservador, pela ambiguidade do rótulo ontológico; potencialmente L1 se interpretado como TN) |
| Situação no Mercado Brasileiro | ✗ Não comercializado |
| Número de Registros | 0 |
| Decisão Recomendada | Proceed with Guardrails |

---

## Por que Esta Previsão é Razoável?

O CBZ é um bloqueador de canais de sódio voltagem-dependentes (Nav). Embora os dados formais de mecanismo de ação não estejam disponíveis na base consultada (DB00564), a literatura farmacológica consolidada demonstra que o fármaco inibe especificamente os canais Nav1.7 e Nav1.8 no gânglio trigêminal, reduzindo a frequência de disparos ectópicos que caracterizam a neuralgia do trigêmeo. Por esse mecanismo direto, o CBZ consta na Lista de Medicamentos Essenciais da OMS (WHO Model List) como tratamento farmacológico de primeira linha para TN.

O ponto crítico desta previsão é um problema de rótulo no banco de dados TxGNN: o nó ontológico "trigeminal nerve neoplasm" não corresponde, na prática, a neoplasias do nervo trigêmeo. Todas as publicações e o ensaio clínico associados a esse nó descrevem casos de **neuralgia do trigêmeo** — seja idiopática, por compressão vascular, ou secundária a massas que comprimem o nervo (lipomas, cistos epidermoides, meningiomas, linfomas). Tumores que invadem o nervo trigêmeo costumam causar dor facial resistente ao CBZ, o que é clinicamente distinto da neuralgia tratável com o fármaco.

Portanto, se a previsão for interpretada como TN, o nível de evidência real é L1 (suportado por múltiplos ensaios de Fase 3 concluídos globalmente). Se for interpretada como neoplasia trigêminal stricto sensu, a evidência cai para L5. O pipeline adota conservadoramente o score L2 para refletir essa ambiguidade, o que é a postura mais prudente até que o rótulo ontológico seja corrigido.

---

## Evidências de Ensaios Clínicos

| Número do Ensaio | Fase | Status | Participantes | Principais Achados |
|---------|------|------|------|---------|
| [NCT06853119](https://clinicaltrials.gov/study/NCT06853119) | N/A | Ainda não recrutando | 120 | Estudo observacional por MRI analisando mudanças de rede cerebral, microestrutura e barreira hematoencefálica em pacientes com neuralgia do trigêmeo; não avalia diretamente a eficácia do CBZ, fornecendo apenas contexto sobre mecanismos neurais da doença |

---

## Evidências da Literatura

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [36824641](https://pubmed.ncbi.nlm.nih.gov/36824641/) | 2022 | Review | Acta Clinica Croatica | Revisão abrangente das opções terapêuticas para TN; posiciona CBZ como padrão farmacológico de primeira linha, com discussão de etiologia por compressão vascular e processos tumorais |
| [17997704](https://pubmed.ncbi.nlm.nih.gov/17997704/) | 2007 | Review | Expert Review of Neurotherapeutics | Análise dos múltiplos tratamentos para TN; destaca desmielinização focal por compressão vascular como etiologia predominante e CBZ como principal referência farmacológica |
| [11286444](https://pubmed.ncbi.nlm.nih.gov/11286444/) | 2001 | Survey / Clinical Practice Review | British Journal of Oral & Maxillofacial Surgery | Levantamento entre 254 cirurgiões bucomaxilofaciais britânicos sobre investigação e manejo de TN; discute rastreamento de causas secundárias e monitoramento do tratamento com CBZ |
| [22647513](https://pubmed.ncbi.nlm.nih.gov/22647513/) | 2012 | Case Report | No Shinkei Geka | Neuralgia trigeminoglossof​aríngea combinada por compressão vascular tratada inicialmente com CBZ; descompressão microvascular realizada após falha da terapia farmacológica |
| [9109911](https://pubmed.ncbi.nlm.nih.gov/9109911/) | 1997 | Case Report | Neurology | Neuromiotonia pós-irradiação em distribuição bilateral facial e trigêminal com resposta favorável ao tratamento com CBZ, demonstrando eficácia em hiperexcitabilidade neuronal induzida por dano |
| [30741017](https://pubmed.ncbi.nlm.nih.gov/30741017/) | 2023 | Case Report | British Journal of Neurosurgery | Neurolinfomatose primária do nervo trigêmeo apresentando dor facial; CBZ prescrito inicialmente sem melhora, levando à investigação por MRI — ilustra diagnóstico diferencial crucial entre TN e neoplasia |
| [3181365](https://pubmed.ncbi.nlm.nih.gov/3181365/) | 1988 | Pre-clinical | Experimental Neurology | CBZ intravenoso inibiu atividade espontânea em neuromas experimentais em ratos, demonstrando supressão de disparos ectópicos em fibras A-alfa/beta e A-delta como mecanismo direto de ação |
| [25433061](https://pubmed.ncbi.nlm.nih.gov/25433061/) | 2014 | Case Report + Literature Review | No Shinkei Geka | TN por lipoma no ângulo cerebelopontino; CBZ usado inicialmente com controle parcial limitado por efeitos colaterais, levando à ressecção cirúrgica |
| [19184299](https://pubmed.ncbi.nlm.nih.gov/19184299/) | 2009 | Case Report | Odontology | TN secundária a cisto epidermoide no ângulo cerebelopontino; revisão da patogênese e dos critérios para tratamento farmacológico com CBZ versus intervenção cirúrgica |
| [25968963](https://pubmed.ncbi.nlm.nih.gov/25968963/) | 2015 | Case Report + Literature Review | World Neurosurgery | TN causada por angioma venoso; revisão da fisiopatologia da desmielinização por trauma mecânico pulsátil e do papel do CBZ como tratamento médico antes de considerar cirurgia |

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Proceed with Guardrails**

**Justificativa:**
O CBZ possui evidência de eficácia de nível mundial (L1) para neuralgia do trigêmeo — a indicação que o nó ontológico "trigeminal nerve neoplasm" representa na prática clínica —, mas a ausência de registro no Brasil e o desalinhamento do rótulo TxGNN exigem verificação e correção antes de qualquer avanço regulatório ou clínico.

**Para prosseguir, é necessário:**
- Verificar o status regulatório atual do CBZ no Brasil via portal ANVISA (é possível que existam registros não contemplados na base consultada, dado que CBZ é um medicamento essencial da OMS)
- Obter a bula oficial (SMPC/RDC) para levantamento completo de advertências, contraindicações e interações medicamentosas relevantes para o mercado brasileiro
- Confirmar dados formais de mecanismo de ação via DrugBank API (DB00564) para completar a análise de MOA
- Sinalizar para a equipe TxGNN o desalinhamento do rótulo ontológico "trigeminal nerve neoplasm": se a intenção for cobrir neuralgia do trigêmeo, o label deve ser corrigido para evitar interpretações incorretas em outros relatórios
- Caso o objetivo seja avaliar CBZ para neoplasias trigêminais stricto sensu (tumores do nervo), redesenhar busca de evidências com foco nessa indicação específica — nesse cenário, a recomendação seria **Hold**
---

