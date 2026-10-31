---
layout: default
title: Methotrexate
parent: Apenas Predição do Modelo (L5)
nav_order: 451
evidence_level: L5
indication_count: 7
last_modified_at: 2026-10-31
description: "Methotrexate: nova indicação prevista, Blastoma Pulmonar (Pulmonary Blastoma) (nível de evidência L5). Indicação original: Antineoplásico"
monitor_inn: "Methotrexate"
predicted_indications: ["pulmonary blastoma", "primary pulmonary lymphoma", "well-differentiated fetal adenocarcinoma of the lung", "Hodgkins lymphoma", "rhabdomyosarcoma (disease)", "parameningeal embryonal rhabdomyosarcoma", "botryoid-type embryonal rhabdomyosarcoma of the vagina"]
---

# Methotrexate
{: .fs-9 }

Nível de evidência: **L5** | Indicações previstas: **7** 
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

## Metotrexato: De antineoplásico citotóxico a Blastoma Pulmonar
{: .text-alpha }

## Resumo em Uma Frase

Metotrexato é um antimetabólito antagonista do ácido fólico, registrado na ANVISA como antineoplásico citotóxico.
O modelo TxGNN prevê que pode ser eficaz para **Blastoma Pulmonar (Pulmonary Blastoma)**, porém atualmente **não há ensaios clínicos nem publicações** que apoiem diretamente esta previsão específica; a sustentação é apenas a pontuação do modelo.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Antineoplásico |
| Nova Indicação Prevista | Blastoma Pulmonar (Pulmonary Blastoma) |
| Pontuação de Previsão TxGNN | 0,9945 |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | Comercializado (registros ativos: 9 de 10) |
| Número de Registros | 10 (ativos: 9) |
| Decisão Recomendada | Hold |

---

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação nos dados compilados para este relatório. Segundo informações conhecidas, o metotrexato é um antagonista do folato (inibidor da di-hidrofolato redutase, DHFR) que prejudica a síntese de nucleotídeos em células de divisão rápida. Sua eficácia como antineoplásico citotóxico é estabelecida em diversos tumores.

O blastoma pulmonar é uma neoplasia pulmonar rara e agressiva. A lógica é que um antimetabólito que atua sobre células de proliferação rápida poderia, em princípio, ser aplicável a esse tipo de tumor. Contudo, esse vínculo baseia-se unicamente na pontuação do TxGNN; não foram fornecidos ensaios ou literatura que o sustentem.

### Outras indicações previstas (contexto)

O modelo também previu outras indicações com pontuações semelhantes (0,9921 a 0,9945). Em ordem de força de evidência:

| Indicação prevista | Nível | Observação |
|------|------|------|
| Linfoma de Hodgkin | L3 | Regime VBM (vimblastina, bleomicina, metotrexato) em doença precoce, com literatura antiga; ensaios de Fase 3 são indiretos (linfoma B não Hodgkin e profilaxia de GVHD) |
| Rabdomiossarcoma | L3 | Ensaio de Fase II de metotrexato em altas doses em crianças (PMID 9329466); estudos antigos ou pequenos, não randomizados |
| Linfoma pulmonar primário | L4 | Evidência indireta; sobretudo relatos de caso e estudos em linfoma do SNC |
| Carcinoma pulmonar de pequenas células | L4 | Literatura antiga (1981–1992); ensaios recuperados são em CPNPC ou prevenção de reação à infusão |
| Demais subtipos (adenocarcinoma fetal, LLC/LLP, rabdomiossarcomas raros) | L5 | Somente previsão do modelo |

---

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados para Blastoma Pulmonar.

---

## Evidências da Literatura

Atualmente não há literatura relacionada para Blastoma Pulmonar.

---

## Informações de Comercialização no Brasil

Todos os 10 registros encontrados estão **válidos**; o metotrexato está atualmente comercializado (10 registros válidos de 10).

| Número de Registro | Nome Comercial | Forma Farmacêutica | Indicação Aprovada |
|---------|------|------|-----------|
| Registro nº 116370033 | METREXATO | Não informada | Antineoplásico |
| Registro nº 122140018 | TECNOMET | Não informada | Antimetabólicos antagonistas do ácido fólico |
| Registro nº 100431549 | METOTREXATO | Não informada | Antimetabólicos antagonistas do ácido fólico |
| Registro nº 116370137 | MTX | Não informada | Antineoplásicos citotóxicos |
| Registro nº 155370010 | HYTAS | Não informada | Antineoplásico |

*(Exibidos os 5 primeiros de 10 registros, todos cancelados.)*

---

## Citotoxicidade

| Item | Conteúdo |
|------|------|
| Classificação de Citotoxicidade | Citotóxico convencional (antimetabólito, antagonista do ácido fólico) |
| Risco de Mielossupressão | Alto, conforme o perfil de segurança (leucopenia, trombocitopenia e anemia constam entre as condições de contraindicação do grafo de conhecimento) |
| Classificação de Emetogenicidade | Consulte as advertências e precauções na bula |
| Itens de Monitoramento | Hemograma completo com diferencial, função hepática e renal; atenção a sintomas pulmonares |
| Proteção no Manuseio | Necessário seguir os regulamentos de manuseio de citotóxicos |

---

## Considerações de Segurança

- **Condições de risco/contraindicação (grafo de conhecimento TxGNN, não texto de bula)**: insuficiência e doença hepática, doença renal, doença da vesícula biliar, trombocitopenia, leucopenia, anemias (incluindo macrocítica), doença pulmonar intersticial e fibrose pulmonar, úlcera gástrica e péptica, colite ulcerativa e doença inflamatória intestinal, estomatite, doenças do sistema imune, uso/dependência de substâncias e piureter.
- **Interações medicamentosas** (100 interações registradas; principais de gravidade **Maior**):
  - Rabeprazol
  - Amoxicilina
  - Ácido acetilsalicílico
  - Há ainda interações de gravidade moderada, por exemplo com corticosteroides (hidrocortisona, dexametasona, betametasona, triancinolona, budesonida), tetraciclinas, doxiciclina, anfotericina B, claritromicina, bupropiona, mesalazina e balsalazida.
- **Sinal de segurança na literatura**: foram descritos distúrbios linfoproliferativos associados ao metotrexato em pacientes com artrite reumatoide, e toxicidade pulmonar induzida pelo fármaco, aspecto relevante para indicações pulmonares.

Consulte a bula para advertências e contraindicações oficiais.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
- A previsão para Blastoma Pulmonar tem apenas a pontuação do modelo (nível L5), sem ensaios clínicos nem literatura. Por outro lado, o medicamento está comercializado no Brasil, com 10 registros válidos de 10.
- Entre as indicações previstas, Linfoma de Hodgkin e Rabdomiossarcoma têm evidência um pouco mais robusta (L3), mas ainda indireta ou antiga, por isso são classificadas como questões de pesquisa.

**Para prosseguir, é necessário:**
- Obter e analisar a bula da ANVISA (advertências e contraindicações), lacuna que impede a triagem de segurança.
- Complementar os dados de mecanismo de ação (DrugBank).
- Realizar revisão de literatura e de relatos de caso específicos de blastoma pulmonar.
- Esclarecer a situação regulatória e a disponibilidade de formulações.
- Avaliar o risco de toxicidade pulmonar do metotrexato em contexto de tumor pulmonar.
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

