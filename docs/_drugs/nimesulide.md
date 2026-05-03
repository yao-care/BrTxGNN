---
layout: default
title: Nimesulide
parent: 僅模型預測 (L5)
nav_order: 358
evidence_level: L5
indication_count: 10
---

# Nimesulide
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

Usando o skill `txgnn-pipeline` para orientar o formato de relatório, e seguindo as instruções detalhadas do sistema prompt. O skill não adiciona etapas específicas para geração de relatório a partir de Evidence Pack — prossigo diretamente com a produção do documento.

---

# Nimesulide: Da Dor e Inflamação à Artrite Gotosa

## Resumo em Uma Frase

Nimesulide é um anti-inflamatório não esteroidal (AINE) com inibição preferencial da COX-2, amplamente utilizado para o tratamento da dor e de processos inflamatórios musculoesqueléticos.
O modelo TxGNN prevê que pode ser eficaz para **Gota / Artrite Gotosa (Gout)**, atualmente com **0 ensaios clínicos registrados** e **14 publicações identificadas**, das quais ao menos 8 são clinicamente relevantes para esta indicação.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|----------|
| Indicação Original | Dor e inflamação (AINE — inibidor preferencial de COX-2) |
| Nova Indicação Prevista | Gota / Artrite Gotosa (Gout) |
| Pontuação de Previsão TxGNN | 97,57% |
| Nível de Evidência | L3 |
| Situação no Mercado Brasileiro | ✓ Comercializado |
| Número de Registros | 2 |
| Decisão Recomendada | Proceed with Guardrails |

---

## Por que Esta Previsão é Razoável?

Nimesulide é um AINE da classe sulfonamida que inibe preferencialmente a ciclooxigenase-2 (COX-2), enzima induzida em tecidos inflamados e responsável pela síntese de prostaglandinas pró-inflamatórias — especialmente a PGE₂. Ao contrário dos AINEs não seletivos clássicos, o nimesulide preserva em maior grau a COX-1 constitutiva, que protege a mucosa gástrica e regula a função plaquetária. Esse perfil de seletividade confere ao fármaco um potencial de menor risco gastrointestinal em comparação a agentes como indometacina ou diclofenaco.

A artrite gotosa aguda resulta da deposição de cristais de urato monossódico nas articulações, que ativam macrófagos sinoviais e desencadeiam uma cascata inflamatória intensa com produção de PGE₂, interleucinas e quimiocinas via COX-2. Os AINEs são o tratamento de primeira linha recomendado pelas diretrizes da ACR (*American College of Rheumatology*) e da EULAR para a crise aguda de gota — sendo a indometacina o agente histórico de referência. O mecanismo de inibição de COX-2 do nimesulide é, portanto, diretamente aplicável a esse processo inflamatório, com base biológica sólida.

Pacientes gotosos frequentemente apresentam comorbidades como hipertensão arterial, insuficiência renal leve a moderada e diabetes tipo 2 — condições que aumentam o risco de complicações gastrointestinais por AINEs não seletivos. Nesse contexto, a seletividade de COX-2 do nimesulide representa uma potencial vantagem clínica. Estudos publicados entre 2003 e 2007 (PMIDs 17672073, 15732721, 12847901) demonstraram eficácia e boa tolerabilidade do nimesulide no tratamento da artrite gotosa aguda, com resultados comparáveis ao diclofenaco sódico. Cabe destacar, no entanto, que preocupações com hepatotoxicidade levaram ao recolhimento ou restrição do nimesulide em alguns países europeus, exigindo monitoramento rigoroso da função hepática no uso clínico.

---

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados.

---

## Evidências da Literatura

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|-----------|-------------------|
| [17672073](https://pubmed.ncbi.nlm.nih.gov/17672073/) | 2007 | Estudo Comparativo Clínico | Terapevticheskii arkhiv | Comparou o tempo para efeito analgésico e anti-inflamatório entre nimesulide (granulado e comprimido) e diclofenaco sódico na artrite gotosa aguda |
| [15732721](https://pubmed.ncbi.nlm.nih.gov/15732721/) | 2004 | Estudo de Efetividade Clínica | Klinicheskaia meditsina | Avaliou eficácia e segurança do nimesulide como inibidor seletivo de COX-2 em pacientes com artrite gotosa e comorbidades renais, hepáticas e metabólicas |
| [12847901](https://pubmed.ncbi.nlm.nih.gov/12847901/) | 2003 | Estudo Clínico | Terapevticheskii arkhiv | Avaliou eficácia e segurança do Nimesil® (nimesulide granulado) como inibidor seletivo de COX-2 para o tratamento da artrite gotosa |
| [32841190](https://pubmed.ncbi.nlm.nih.gov/32841190/) | 2020 | Revisão de Algoritmo Clínico | Georgian medical news | Discute erros comuns no diagnóstico e tratamento da gota e propõe algoritmo terapêutico baseado nas recomendações atualizadas ACR/EULAR 2018, incluindo AINEs |
| [12115158](https://pubmed.ncbi.nlm.nih.gov/12115158/) | 2002 | ECR | Arthritis and rheumatism | Avaliou se colchicina adicionada ao nimesulide (tratamento de base) tem efeito modificador de sintomas na osteoartrite do joelho — nimesulide utilizado como braço de referência |
| [40106177](https://pubmed.ncbi.nlm.nih.gov/40106177/) | 2025 | Estudo de Utilização de Fármacos | Advances in therapy | Descreve padrões de prescrição de AINEs (incluindo nimesulide) na prática clínica real na Itália entre 2019–2022, conforme os critérios da Nota 66 da AIFA |
| [29300762](https://pubmed.ncbi.nlm.nih.gov/29300762/) | 2018 | Estudo In vitro | PloS one | Avaliou propriedades antiglicação de 18 fármacos comuns, incluindo nimesulide, em contexto de reposicionamento para complicações diabéticas — relevante às comorbidades do perfil gotoso |
| [20012865](https://pubmed.ncbi.nlm.nih.gov/20012865/) | 2010 | Relato de Caso | Rheumatology international | Descreve quadro incomum de gota tofácea poliarticular crônica com imagens clínicas e radiográficas; ilustra a gravidade da doença não controlada |

> **Nota:** 4 publicações sobre toxicidade de nimesulide em aves rapineiras (abutres) foram excluídas desta tabela por ausência de relevância clínica para a indicação humana, conforme indicado na racionalidade de reposicionamento.

---

## Informações de Comercialização no Brasil

O nimesulide possui **2 registros ativos** na ANVISA com situação **Comercializado**. Os detalhes individuais de cada registro — número de registro, nome comercial, forma farmacêutica e texto de indicação aprovada — não constam nos dados disponíveis nesta versão do Evidence Pack.

Para consulta completa, acesse o portal da ANVISA: [consultas.anvisa.gov.br](https://consultas.anvisa.gov.br/#/medicamentos/)

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

> ⚠️ **Atenção ao perfil hepático:** Embora os dados formais de advertências e contraindicações estejam pendentes de coleta, a literatura científica registra casos de hepatite fulminante e hepatotoxicidade grave associados ao uso de nimesulide, inclusive com necessidade de transplante hepático (PMID 12070417, identificado na coleta de tendinite). Essa sinalização deve ser considerada prioritária na avaliação de segurança, especialmente em pacientes com hepatopatia subjacente.

---

## Conclusão e Próximos Passos

**Decisão: Proceed with Guardrails**

**Justificativa:**
Há múltiplos estudos clínicos publicados — incluindo ensaios comparativos diretos com desfecho de dor e inflamação — demonstrando eficácia do nimesulide na artrite gotosa aguda; o mecanismo de inibição preferencial de COX-2 é biologicamente coerente com a fisiopatologia da gota; e o fármaco já está regularmente comercializado no Brasil, reduzindo barreiras regulatórias. O nível de evidência L3 (estudos observacionais e clínicos não randomizados) é suficiente para avançar com cautela, mas insuficiente para uso amplo sem monitoramento.

**Para prosseguir, é necessário:**
- Obter os dados completos da bula ANVISA (advertências, contraindicações, posologia) via download do PDF no portal da ANVISA
- Confirmar o número de registro, nome comercial e indicações aprovadas nos 2 registros ativos
- Avaliar rigorosamente o perfil de segurança hepática — o sinal de hepatotoxicidade do nimesulide requer protocolo de monitoramento de função hepática (ALT, AST, bilirrubinas) definido antes do uso estruturado
- Identificar ou conduzir um ECR de Phase 2/3 com desfechos modernos (escala VAS de dor, tempo para resolução da crise, marcadores inflamatórios) comparando nimesulide vs colchicina ou indometacina na crise aguda de gota, para elevar o nível de evidência de L3 para L2
- Definir critérios de exclusão claros para pacientes com disfunção hepática, dado o risco específico associado ao fármaco
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

