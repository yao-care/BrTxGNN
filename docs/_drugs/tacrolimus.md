---
layout: default
title: Tacrolimus
parent: 僅模型預測 (L5)
nav_order: 452
evidence_level: L5
indication_count: 3
---

# Tacrolimus
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

O skill TxGNN Pipeline confirma o contexto do projeto. Agora vou gerar o relatório completo seguindo o formato v5 definido no prompt do sistema.

---

# Tacrolimus: Da Dermatite Atópica à Dermatite Seborreica

## Resumo em Uma Frase

Tacrolimus (Protopic®) é um inibidor tópico de calcineurina amplamente aprovado pelo FDA e EMA para o tratamento da **dermatite atópica**, condição inflamatória crônica da pele mediada por células T.
O modelo TxGNN prevê que pode ser eficaz para **Dermatite Seborreica (Seborrheic Dermatitis)**, atualmente com **2 ensaios clínicos** e **20 publicações** apoiando esta direção.
A pontuação de 99,26% e o nível de evidência L1 posicionam este reposicionamento entre os candidatos de maior maturidade clínica.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|----------|
| Indicação Original | Dermatite atópica (uso tópico, Protopic®) |
| Nova Indicação Prevista | Dermatite Seborreica (Seborrheic Dermatitis) |
| Pontuação de Previsão TxGNN | 99,26% |
| Nível de Evidência | L1 |
| Situação no Mercado Brasileiro | ✓ Comercializado |
| Número de Registros | 2 |
| Decisão Recomendada | Proceed with Guardrails |

---

## Por que Esta Previsão é Razoável?

O tacrolimus (FK506) é um macrolídeo lactônico com mecanismo de ação preciso: ele se liga à proteína FKBP12 intracelular, e o complexo resultante inibe a fosfatase calcineurina, bloqueando a translocação nuclear do NFAT (*Nuclear Factor of Activated T-cells*). Na prática, isso suprime a ativação de linfócitos T CD4+ e a liberação de citocinas pró-inflamatórias como IL-2, IL-4, IL-5, IL-13 e IFN-γ. Na forma tópica (Protopic® 0,03% e 0,1%), o tacrolimus não causa atrofia cutânea — a principal limitação do uso prolongado de corticosteroides — o que o torna especialmente adequado para regiões sensíveis como a face.

A dermatite seborreica (DS) compartilha mecanismos fisiopatológicos centrais com a dermatite atópica: ambas envolvem inflamação cutânea mediada por células T, disfunção da barreira epidérmica e desequilíbrio de citocinas Th1/Th2. Na DS, a levedura comensal *Malassezia spp.* desencadeia uma resposta imune exacerbada com recrutamento de células T CD4+, elevação de IL-17, IL-22 e ativação da via calcineurina-NFAT. O tacrolimus, ao bloquear diretamente essa via, atua no núcleo do processo inflamatório da DS com base mecanística sólida.

A aplicabilidade é reforçada pelo padrão topográfico da doença: a DS acomete preferencialmente a face (sulco nasogeniano, sobrancelhas, couro cabeludo), exatamente onde o uso de corticosteroides potentes de longo prazo é contraindicado. O tacrolimus tópico preenche essa lacuna farmacológica de forma racional — e os ensaios clínicos identificados confirmam esta hipótese em cenários de manutenção, onde a prevenção de recidivas sem efeitos adversos crônicos é o objetivo principal.

---

## Evidências de Ensaios Clínicos

| Número do Ensaio | Fase | Status | Participantes | Principais Achados |
|------------------|------|--------|---------------|--------------------|
| [NCT02004860](https://clinicaltrials.gov/study/NCT02004860) | Phase 3 | Concluído | 120 | Avalia tacrolimus (Protopic®) como tratamento de **manutenção da DS grave facial** em adultos; desenhado para reduzir frequência de recidivas, prolongar remissões pós-tratamento de ataque e diminuir uso de corticosteroides tópicos |
| [NCT01591070](https://clinicaltrials.gov/study/NCT01591070) | Phase 4 | Concluído | 104 | Estudo de tratamento **proativo** com tacrolimus 0,1% uma ou duas vezes por semana; avalia se a aplicação intermitente mantém a DS facial adulta em remissão e reduz a incidência de exacerbações |

---

## Evidências da Literatura

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|-----------|-------------------|
| [33010323](https://pubmed.ncbi.nlm.nih.gov/33010323/) | 2021 | RCT Multicêntrico Duplo-Cego | J Am Acad Dermatol | Tacrolimus 0,1% vs ciclopiroxolamina 1% para manutenção de DS grave facial; primeiro RCT de longa duração desenhado especificamente para terapia de manutenção em DS |
| [26512166](https://pubmed.ncbi.nlm.nih.gov/26512166/) | 2015 | Ensaio Clínico | Ann Dermatol | Tratamento de manutenção de DS facial com tacrolimus 0,1%; demonstra que inibidores de calcineurina tópicos reduzem recidivas em DS de forma análoga ao seu efeito na DA |
| [24171300](https://pubmed.ncbi.nlm.nih.gov/24171300/) | 2013 | RCT Comparativo | Ann Parasitol | 60 pacientes com DS; compara sertaconazol 2% vs tacrolimus 0,03%; avalia a contribuição do componente anti-inflamatório (tacrolimus) versus antifúngico no controle da doença |
| [39219446](https://pubmed.ncbi.nlm.nih.gov/39219446/) | 2024 | Revisão Sistemática Cochrane / NMA | Clin Exp Allergy | Meta-análise em rede de tratamentos anti-inflamatórios tópicos para eczema; posiciona tacrolimus na hierarquia de eficácia e segurança dos agentes disponíveis |
| [27804089](https://pubmed.ncbi.nlm.nih.gov/27804089/) | 2017 | Revisão Sistemática | Am J Clin Dermatol | Revisão sistemática de tratamentos tópicos para DS facial; abrange antifúngicos, corticosteroides e inibidores de calcineurina, consolidando o papel do tacrolimus |
| [19222250](https://pubmed.ncbi.nlm.nih.gov/19222250/) | 2009 | Revisão | Am J Clin Dermatol | Papel dos inibidores de calcineurina tópicos no tratamento da DS: fisiopatologia, segurança e eficácia; fundamenta o tacrolimus como alternativa segura aos esteroides |
| [15461548](https://pubmed.ncbi.nlm.nih.gov/15461548/) | 2004 | Revisão | Expert Opin Pharmacother | Tacrolimus tópico para DA e outras doenças inflamatórias cutâneas; mecanismo de inibição de calcineurina como base para uso em múltiplas dermatoses inflamatórias |
| [12833030](https://pubmed.ncbi.nlm.nih.gov/12833030/) | 2003 | Estudo Piloto (Open-label) | J Am Acad Dermatol | Primeiro estudo piloto de tacrolimus 0,1% para DS; 18 pacientes, 61% obtiveram remissão completa em 28 dias; estabeleceu a prova de conceito inicial para esta indicação |
| [37067129](https://pubmed.ncbi.nlm.nih.gov/37067129/) | 2023 | Ensaio Clínico Comparativo | Indian J Dermatol Venereol Leprol | Comparação de itraconazol oral 2 dias + tacrolimus tópico vs tacrolimus tópico isolado para manutenção de DS; contexto asiático (Vietnã), relevante para populações de pele mista |
| [19213227](https://pubmed.ncbi.nlm.nih.gov/19213227/) | 2009 | Revisão | J Drugs Dermatol | DS facial: estado atual e horizontes terapêuticos; descreve papel dos imunomoduladores tópicos frente à etiologia multifatorial envolvendo *Malassezia*, sebo e resposta imune |

---

## Informações de Comercialização no Brasil

Constam **2 registros ativos** de tacrolimus no Brasil (situação: comercializado). Os dados detalhados de nome comercial, forma farmacêutica e texto de indicação aprovada não estão disponíveis nesta versão do Evidence Pack — os campos correspondentes nos registros retornados estão sem preenchimento. Recomenda-se consultar diretamente a base de dados da **ANVISA (Consulta a Produtos Registrados)** para verificar os registros vigentes, as formas farmacêuticas disponíveis e as indicações aprovadas.

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Proceed with Guardrails**

**Justificativa:**
O tacrolimus tópico possui 1 Phase 3 RCT e 1 Phase 4 RCT concluídos diretamente em dermatite seborreica, apoiados por múltiplos RCTs comparativos, revisões sistemáticas e meta-análises em rede — atingindo nível de evidência L1. O mecanismo de inibição de calcineurina é biologicamente coerente com a fisiopatologia da DS, e a ausência de atrofia cutânea representa vantagem clínica concreta para uso facial de longo prazo.

**Para prosseguir, é necessário:**
- Obter e analisar a **bula oficial do tacrolimus tópico registrado no Brasil (ANVISA)** para mapeamento completo de advertências, contraindicações, populações especiais e interações
- Confirmar os textos de indicação aprovada dos 2 registros ANVISA vigentes e verificar se DS já consta como indicação oficial no Brasil
- Definir **protocolo de monitoramento para uso de manutenção**: frequência de reavaliações dermatológicas, vigilância de infecções oportunistas (ex.: *tinea incognito* por uso de imunomodulador tópico) e critérios de descontinuação
- Avaliar estratégia regulatória para extensão de indicação junto à ANVISA, caso a DS não esteja formalmente incluída na bula atual
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

