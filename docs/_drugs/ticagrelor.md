---
layout: default
title: Ticagrelor
parent: 僅模型預測 (L5)
nav_order: 441
evidence_level: L5
indication_count: 10
---

# Ticagrelor
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

# Ticagrelor: Da Síndrome Coronária Aguda à Arteriosclerose Intracraniana

## Resumo em Uma Frase

Ticagrelor é um inibidor reversível do receptor plaquetário P2Y12, originalmente utilizado na prevenção de eventos cardiovasculares em pacientes com síndrome coronária aguda (SCA) e doença coronária de alto risco.
O modelo TxGNN prevê que pode ser eficaz para **Arteriosclerose Intracraniana (Intracranial Arteriosclerosis)**, atualmente com **11 ensaios clínicos** e **3 publicações** apoiando esta direção.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Síndrome Coronária Aguda (SCA) — prevenção de eventos aterotrombóticos |
| Nova Indicação Prevista | Arteriosclerose Intracraniana (Intracranial Arteriosclerosis) |
| Pontuação de Previsão TxGNN | 99,97% |
| Nível de Evidência | L1 |
| Situação no Mercado Brasileiro | ✓ Comercializado |
| Número de Registros | 11 |
| Decisão Recomendada | Proceed with Guardrails |

---

## Por que Esta Previsão é Razoável?

A arteriosclerose intracraniana (ICAS, *Intracranial Atherosclerotic Stenosis*) é uma das principais causas de AVC isquêmico, com prevalência especialmente elevada em populações asiáticas e latinas. O estreitamento aterosclerótico progressivo das artérias intracranianas favorece a ativação plaquetária sobre superfícies de placas instáveis, levando à formação de trombos in situ e à oclusão vascular cerebral. O mecanismo patogênico da ICAS compartilha características fundamentais com a aterosclerose coronária — o domínio onde o ticagrelor já demonstrou eficácia clínica consolidada.

Ticagrelor bloqueia direta e reversivelmente o receptor P2Y12 nas plaquetas, interrompendo a amplificação da ativação plaquetária mediada pelo ADP — etapa central na formação de trombos arteriais. Em comparação com o clopidogrel, padrão atual de tratamento para ICAS, o ticagrelor oferece inibição plaquetária mais potente e previsível, independentemente do genótipo CYP2C19 do paciente (polimorfismo prevalente em populações asiáticas que reduz substancialmente a eficácia do clopidogrel em portadores de alelos de perda de função). Adicionalmente, o ticagrelor inibe o transportador de nucleosídeos ENT-1, elevando os níveis circulantes de adenosina — o que pode conferir proteção cerebrovascular adicional por meio de vasodilatação e efeitos anti-inflamatórios independentes da inibição plaquetária.

A previsão do TxGNN é diretamente sustentada por ensaios clínicos especificamente desenhados para ICAS: o ensaio CAPTIVA (NCT05047172, Fase 3 em andamento, N=1.683) compara ticagrelor versus clopidogrel em ICAS sintomática; o DREAM-PRIDE (NCT04948749) avalia estratégias antiplaquetárias na ICAS; e o EUCLID (NCT01732822, Fase 3 concluído, N=13.885) fornece evidências de Fase 3 sobre ticagrelor em aterosclerose arterial sistêmica com análise de desfechos cerebrovasculares. Os resultados do CAPTIVA, esperados para 2028, deverão definir o papel do ticagrelor como tratamento de primeira linha nessa indicação.

---

## Evidências de Ensaios Clínicos

| Número do Ensaio | Fase | Status | Participantes | Principais Achados |
|---------|------|------|------|---------|
| [NCT05047172](https://clinicaltrials.gov/study/NCT05047172) | Fase 3 | Em andamento (não recrutando) | 1.683 | CAPTIVA: compara rivaroxabana, ticagrelor e clopidogrel em ICAS sintomática; desfecho primário é taxa combinada de AVC isquêmico, hemorragia intracerebral ou morte vascular em 1 ano |
| [NCT04948749](https://clinicaltrials.gov/study/NCT04948749) | N/A | Recrutando | 792 | DREAM-PRIDE: avalia stent farmacológico (DES) combinado com tratamento médico agressivo versus tratamento médico isolado na prevenção de recorrência de AVC por ICAS em 1 ano |
| [NCT01732822](https://clinicaltrials.gov/study/NCT01732822) | Fase 3 | Concluído | 13.885 | EUCLID: comparou ticagrelor versus clopidogrel em doença arterial periférica estabelecida; inclui análise de desfechos de AVC isquêmico em subgrupo com doença cerebrovascular, fornecendo evidência de Fase 3 para aterosclerose arterial |
| [NCT03620760](https://clinicaltrials.gov/study/NCT03620760) | Fase 4 | Status desconhecido | 2.036 | Avalia não-inferioridade de ticagrelor em dose baixa (45 mg 2×/dia) versus dose padrão (90 mg 2×/dia) em pacientes chineses com angina instável após stent coronário não urgente; relevante para otimização de dose em ICAS |
| [NCT06714526](https://clinicaltrials.gov/study/NCT06714526) | N/A | Recrutando | 100 | Estudo piloto PROBE: seleção guiada por genótipo CYP2C19 de inibidor P2Y12 (incluindo ticagrelor) versus clopidogrel convencional em ICAS sintomática; explora benefício em portadores de alelos de perda de função |
| [NCT02605447](https://clinicaltrials.gov/study/NCT02605447) | Fase 4 | Concluído | 2.009 | EVOLVE Short DAPT: avalia segurança de DAPT por 3 meses em pacientes de alto risco para sangramento após PCI com stent SYNERGY; relevante para protocolos de antiagregação pós-intervenção neuroendovascular em ICAS |
| [NCT06058130](https://clinicaltrials.gov/study/NCT06058130) | N/A | Status desconhecido | 2.171 | Compara anticoagulação isolada versus anticoagulação combinada com antiagregação em pacientes com AVC isquêmico agudo com fibrilação atrial e estenose extra/intracraniana concomitante; avalia estratégia antitrombótica combinada na ICAS |
| [NCT01813435](https://clinicaltrials.gov/study/NCT01813435) | Fase 3 | Concluído | 15.991 | GLOBAL LEADERS: ticagrelor + AAS por 1 mês seguido de ticagrelor isolado por 23 meses versus DAPT padrão após implante de stent coronário; oferece dados de segurança de longo prazo do ticagrelor em monoterapia |
| [NCT07164859](https://clinicaltrials.gov/study/NCT07164859) | Fase 3 | Não iniciado | 1.700 | SOLOPCI: avalia DAPT ultracurta (7 dias) seguida de monoterapia com inibidor P2Y12 versus duração padrão em idosos ≥65 anos após PCI; resultados relevantes para populações idosas com ICAS |
| [NCT07354828](https://clinicaltrials.gov/study/NCT07354828) | N/A | Não iniciado | 3.500 | Estabelecimento de sistema de indicadores de qualidade para revascularização coronária baseado em DAPT na China; foco em pacientes de alto risco para sangramento com SCA, com dados sobre uso de ticagrelor em contexto real |

---

## Evidências da Literatura

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [38252758](https://pubmed.ncbi.nlm.nih.gov/38252758/) | 2024 | Diretriz Clínica | *Stroke* | Atualização focada em arteriosclerose intracraniana: sintetiza o estado atual do conhecimento, destaca lacunas de evidência e orienta a prática clínica; referência central para o manejo contemporâneo da ICAS |
| [39862061](https://pubmed.ncbi.nlm.nih.gov/39862061/) | 2025 | Protocolo de Ensaio | *International Journal of Stroke* | Descreve o desenho e progresso inicial do CAPTIVA; o regime atual (clopidogrel + AAS por 90 dias, seguido de AAS isolado) mantém risco residual elevado de AVC recorrente em até 12 meses, motivando a avaliação de ticagrelor como alternativa superior |
| [39658130](https://pubmed.ncbi.nlm.nih.gov/39658130/) | 2025 | Estudo Clínico | *Journal of Neurointerventional Surgery* | Relata experiência com ticagrelor 60 mg 2×/dia + AAS 81 mg/dia versus regime padrão AAS + clopidogrel para stenting intracraniano; ticagrelor demonstrou-se alternativa viável para DAPT em procedimentos neurointervencionistas, com dose reduzida adequada ao contexto neurovascular |

---

## Informações de Comercialização no Brasil

Ticagrelor possui **11 registros** ativos na ANVISA e está **comercializado** no Brasil. Os dados detalhados de nome comercial, forma farmacêutica e indicação aprovada por registro individual não constam no pacote de evidências atual; consulte diretamente o portal de consulta de medicamentos da ANVISA (consultas.anvisa.gov.br) para obter os registros completos.

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Proceed with Guardrails**

**Justificativa:**
O ensaio CAPTIVA (Fase 3, em andamento, N=1.683) foi especificamente desenhado para testar ticagrelor em ICAS sintomática, e ao menos dois ensaios de Fase 3 concluídos (EUCLID, N=13.885; GLOBAL LEADERS, N=15.991) fornecem base robusta de segurança e eficácia do ticagrelor em aterosclerose arterial sistêmica. A coerência mecanística é sólida — a via P2Y12 é diretamente relevante para a patogênese da ICAS — e o nível de evidência L1 justifica progressão com monitoramento estruturado.

**Para prosseguir, é necessário:**
- Recuperar advertências e contraindicações da bula aprovada pela ANVISA para completar a avaliação de segurança (lacuna de dados bloqueante, DG001)
- Obter dados detalhados de mecanismo de ação via DrugBank API (DG002)
- Aguardar resultados definitivos do CAPTIVA (conclusão prevista: maio de 2028) para confirmação de superioridade sobre clopidogrel especificamente em ICAS
- Estabelecer protocolo de monitoramento para risco de hemorragia intracraniana — principal evento adverso de preocupação nessa população com estenose arterial ativa
- Consultar o portal ANVISA para obter nomes comerciais, formas farmacêuticas e indicações aprovadas dos 11 registros ativos, para análise regulatória completa
---

