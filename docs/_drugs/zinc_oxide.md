---
layout: default
title: Zinc Oxide
parent: 僅模型預測 (L5)
nav_order: 513
evidence_level: L5
indication_count: 10
---

# Zinc Oxide
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

Using `txgnn-pipeline` skill loaded. Generating the Brazilian drug repurposing evaluation report now.

---

# Zinc Oxide: Da proteção cutânea ao tratamento da Acne Vulgaris

## Resumo em Uma Frase

Zinc oxide (óxido de zinco) é um composto inorgânico amplamente utilizado como protetor cutâneo, excipiente dermatológico e filtro solar em formulações tópicas.
O modelo TxGNN prevê que pode ser eficaz para **Acne Vulgaris (acne disease)**,
atualmente com **0 ensaios clínicos** e **7 publicações** apoiando esta direção.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Protetor cutâneo / excipiente dermatológico (uso tópico) |
| Nova Indicação Prevista | Acne Vulgaris (acne disease) |
| Pontuação de Previsão TxGNN | 99.86% |
| Nível de Evidência | L3 |
| Situação no Mercado Brasileiro | ✗ Não comercializado |
| Número de Registros | 0 |
| Decisão Recomendada | Proceed with Guardrails |

---

## Por que Esta Previsão é Razoável?

Atualmente não há dados detalhados sobre o mecanismo de ação disponíveis no sistema. Com base na literatura científica disponível, zinc oxide é um composto inorgânico com propriedades antimicrobianas e anti-inflamatórias amplamente documentadas na dermatologia.

O óxido de zinco libera íons Zn²⁺ que exercem efeito bactericida direto contra *Cutibacterium acnes* (anteriormente denominado *Propionibacterium acnes*) — o principal patógeno bacteriano responsável pelo desenvolvimento da acne. Paralelamente, o zinco inibe a sinalização inflamatória mediada por TLR2, suprimindo a produção de citocinas pró-inflamatórias (IL-1β, TNF-α) e reduzindo a inflamação perifolicular característica das lesões acneicas.

Formulações tópicas baseadas em nanopartículas de ZnO demonstram capacidade de penetração cutânea com modulação local do estresse oxidativo associado à hipersecreção sebácea. Considerando que o zinc oxide já é amplamente empregado em formulações dermatológicas tópicas, a aplicação no tratamento da acne representa uma extensão natural e mecanisticamente coerente de seu uso estabelecido.

---

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados para Zinc Oxide em acne vulgaris.

---

## Evidências da Literatura

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|-----------|-------------------|
| [29193602](https://pubmed.ncbi.nlm.nih.gov/29193602/) | 2018 | Revisão da Literatura | Dermatologic Therapy | Revisão abrangente do papel do zinco no tratamento da acne; documenta propriedades antibacterianas e anti-inflamatórias de formulações tópicas e sistêmicas de zinco |
| [15536660](https://pubmed.ncbi.nlm.nih.gov/15536660/) | 2004 | Estudo Clínico Controlado (Split-face) | Skin Research and Technology | Avaliação clínica e bioinstrumental de formulação para acne inflamatória catamenial; fornece evidência controlada direta de eficácia em condição acneica |
| [21342155](https://pubmed.ncbi.nlm.nih.gov/21342155/) | 2011 | Revisão | Int Journal of Dermatology | Propriedades únicas de nanopartículas de ZnO para uso em cuidados da pele; investigação de nano-preparações como tratamento inovador para acne vulgaris |
| [36888703](https://pubmed.ncbi.nlm.nih.gov/36888703/) | 2023 | Experimental (In vitro/In vivo) | Science Advances | Microagulha de hialuronato de sódio com nanopartículas de ZnO ativadas por ultrassom; demonstra eficácia antibacteriana contra *P. acnes* e redução de inflamação sem uso de antibióticos |
| [31322532](https://pubmed.ncbi.nlm.nih.gov/31322532/) | 2019 | Desenvolvimento de Formulação | Georgian Medical News | Desenvolvimento de fórmulas em pó com ZnO como cosmecêutico de uso diário para tratamento preventivo e terapêutico de acne leve |
| [29284390](https://pubmed.ncbi.nlm.nih.gov/29284390/) | 2018 | Ciência de Materiais / Formulação | Current Medicinal Chemistry | Funcionalização de têxteis com nanopartículas de ZnO para tratamento de doenças de pele, incluindo acne; evidência de capacidade antimicrobiana sustentada |
| [41033952](https://pubmed.ncbi.nlm.nih.gov/41033952/) | 2025 | Ciência Básica (Mecanismo) | Science Bulletin | Heterojunção piezoelétrica ZnO@Viologen-COF ativada pelo metabolismo respiratório de *C. acnes*; modulação seletiva da microbiota cutânea por características redox bacterianas |

---

## Informações de Comercialização no Brasil

Zinc oxide (DB09321) **não possui registro ativo na ANVISA**. Não foram localizadas licenças de comercialização no banco de dados consultado (consulta realizada em 2026-03-24).

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Proceed with Guardrails**

**Justificativa:**
A literatura dermatológica apoia de forma consistente o papel do zinco no tratamento da acne, com mecanismo de ação biologicamente plausível (atividade antibacteriana contra *C. acnes* e modulação da resposta inflamatória mediada por TLR2). Contudo, a ausência de ensaios clínicos registrados especificamente para zinc oxide em acne e a inexistência de registro na ANVISA impedem aplicação clínica imediata sem etapas adicionais de validação.

**Para prosseguir, é necessário:**
- Realizar levantamento complementar de ensaios clínicos para formulações tópicas de zinc oxide em acne (distinguindo zinc oxide de sais de zinco oral, que possuem maior corpo de evidências)
- Obter dados de segurança e mecanismo de ação (MOA) via DrugBank API (DG002)
- Obter e analisar a bula/monografia do produto para extração de advertências e contraindicações (DG001)
- Providenciar registro ou notificação na ANVISA para viabilizar comercialização no Brasil
- Avaliar conformidade regulatória para formulações contendo nanopartículas de ZnO, conforme exigências da ANVISA para nanomateriais dermatológicos
- Conduzir estudo clínico controlado comparando zinc oxide tópico com tratamentos padrão para acne (peróxido de benzoíla, antibióticos tópicos) para estabelecimento de evidência L2/L1
---

