---
layout: default
title: Acetylcysteine
parent: 僅模型預測 (L5)
nav_order: 21
evidence_level: L5
indication_count: 10
---

# Acetylcysteine
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

# Acetylcysteine: Do agente mucolítico à doença trombótica

## Resumo em Uma Frase

Acetylcysteine (NAC) é amplamente utilizado como agente mucolítico no tratamento de doenças respiratórias com hipersecreção mucosa e como antídoto na intoxicação por paracetamol.
O modelo TxGNN prevê que pode ser eficaz para **Doença Trombótica (Thrombotic Disease)**, com destaque para microangiopatia trombótica associada a transplante (TA-TMA) e púrpura trombocitopênica trombótica (TTP), atualmente com **9 ensaios clínicos** e **20 publicações** apoiando esta direção.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Agente mucolítico (doenças respiratórias com hipersecreção mucosa) e antídoto para intoxicação por paracetamol |
| Nova Indicação Prevista | Doença Trombótica (Thrombotic Disease) |
| Pontuação de Previsão TxGNN | 99.96% |
| Nível de Evidência | L1 |
| Situação no Mercado Brasileiro | Não comercializado |
| Número de Registros | 0 |
| Decisão Recomendada | Proceed with Guardrails |

---

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação no Evidence Pack. Com base no conhecimento farmacológico estabelecido, o NAC é um precursor direto da glutationa (GSH), com propriedades antioxidantes e mucolíticas derivadas da sua capacidade de reduzir e clivar ligações dissulfeto em macromoléculas. É essa mesma propriedade química que fundamenta sua atuação no sistema de coagulação.

No contexto da doença trombótica, o NAC exerce um mecanismo triplo especialmente relevante para microangiopatias: **(1) degradação de multímeros ultra-grandes de von Willebrand Factor (ULVWF)** — o NAC cliva diretamente as ligações dissulfeto N-terminais do VWF, reduzindo a forma patologicamente agregadora responsável pela trombose microvascular; **(2) redução do estresse oxidativo endotelial** que amplifica a ativação plaquetária; e **(3) modulação do sistema complemento**, mecanismo especialmente relevante na TA-TMA pós-transplante. Na TTP, onde a deficiência de ADAMTS13 leva ao acúmulo de ULVWF, o NAC oferece uma via de clivagem auxiliar independente da enzima deficiente.

A progressão das evidências clínicas é substancial: dois ensaios de Phase 3 centrados em TA-TMA (um concluído com n=170 e outro em andamento com n=260), somados a um RCT prospectivo como profilaxia para TA-TMA, sustentam a plausibilidade biológica e clínica desta previsão. O guardrail central é que a evidência L1 é específica para o subtipo TA-TMA, não cobrindo uniformemente toda a categoria genérica de "doença trombótica", e a droga não substitui anticoagulantes padrão nem plasmaférese nas indicações estabelecidas.

---

## Evidências de Ensaios Clínicos

| Número do Ensaio | Fase | Status | Participantes | Principais Achados |
|---------|------|------|------|---------|
| [NCT03252925](https://clinicaltrials.gov/study/NCT03252925) | Phase 3 | Concluído | 170 | Estudo prospectivo de segurança e eficácia do NAC em TA-TMA pós-transplante de células-tronco hematopoiéticas (HSCT); principal evidência L1 para este subtipo, com avaliação dentro dos primeiros 100 dias pós-transplante |
| [NCT05907486](https://clinicaltrials.gov/study/NCT05907486) | Phase 3 | Desconhecido | 260 | RCT avaliando eficácia e segurança do NAC para prevenção de eventos trombóticos após transplante alogênico de células-tronco hematopoiéticas; n=260 representa o maior ensaio nesta indicação |
| [NCT07279610](https://clinicaltrials.gov/study/NCT07279610) | Phase 2/3 | Ativo (sem recrutamento) | 44 | Ensaio multicêntrico prospectivo de braço único avaliando NAC para TA-TMA; motivado pela baixa resposta à plasmaférese (<10%) e pelo custo elevado de eculizumabe; estudo de acompanhamento ao NCT03252925 |
| [NCT03636932](https://clinicaltrials.gov/study/NCT03636932) | Phase 2 | Concluído | 40 | RENACTIF: RCT duplo-cego cruzado avaliando redução do fenótipo trombótico em insuficiência renal crônica com NAC; papel da toxina urêmica Indoxil Sulfato como mediador pró-trombótico |
| [NCT04368598](https://clinicaltrials.gov/study/NCT04368598) | Phase 2 | Desconhecido | 44 | Estudo aberto de braço único avaliando NAC + dexametasona em alta dose em adultos com púrpura trombocitopênica imune (PTI) recém-diagnosticada |
| [NCT03460808](https://clinicaltrials.gov/study/NCT03460808) | Phase 1/2 | Desconhecido | 200 | Estudo multicêntrico comparando atorvastatina + NAC + danazol versus danazol em monoterapia na PTI corticorresistente/recidivante; NAC como componente de terapia combinada |
| [NCT06518044](https://clinicaltrials.gov/study/NCT06518044) | Phase 2 | Não iniciado | 30 | Estudo prospectivo de braço único avaliando NAC na promoção de recuperação hematopoiética pós-transplante haploidêntico em anemia aplástica grave (SAA) |
| [NCT01808521](https://clinicaltrials.gov/study/NCT01808521) | Early Phase 1 | Concluído | 3 | Estudo piloto de NAC intravenoso em TTP suspeita durante plasmaférese terapêutica; primeiros dados de prova de conceito em TTP humana; hipótese de melhora da clivagem de VWF por ADAMTS13 |
| [NCT05551624](https://clinicaltrials.gov/study/NCT05551624) | Early Phase 1 | Concluído | 15 | Atorvastatina + NAC em PTI resistente a esteroide ou em recidiva; avaliação da elevação de contagem plaquetária como estratégia terapêutica alternativa |

---

## Evidências da Literatura

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [35940529](https://pubmed.ncbi.nlm.nih.gov/35940529/) | 2022 | RCT (prospectivo, controlado por placebo) | Transplantation and Cellular Therapy | NAC como terapia profilática para TA-TMA em HSCT; RCT aberto com grupo placebo, Universidade de Soochow; avalia redução de incidência de TA-TMA com NAC preventivo |
| [37311880](https://pubmed.ncbi.nlm.nih.gov/37311880/) | 2023 | Coorte Retrospectiva | Annals of Hematology | Associação entre tratamento com NAC e mortalidade hospitalar em PTT adquirida (aTTP); estudo de coorte retrospectivo; uso de NAC na aTTP ainda controverso, mas dados de sobrevida são sugestivos |
| [21266777](https://pubmed.ncbi.nlm.nih.gov/21266777/) | 2011 | Estudo Mecanístico (plasma humano + modelo murino) | Journal of Clinical Investigation | NAC reduz tamanho e atividade do VWF em plasma humano e camundongos; principal publicação definindo o mecanismo molecular de clivagem de ULVWF por NAC independente de ADAMTS13 |
| [28011677](https://pubmed.ncbi.nlm.nih.gov/28011677/) | 2017 | Pré-clínico (camundongo + babuíno) | Blood | NAC em modelos pré-clínicos de TTP; validação in vivo com modelo de camundongo e primata não-humano (babuíno); apoia translação clínica |
| [32243196](https://pubmed.ncbi.nlm.nih.gov/32243196/) | 2020 | Revisão Narrativa (foco em reposicionamento) | Expert Review of Hematology | Revisão de drogas reposicionadas em TTP, incluindo NAC, rituximabe, bortezomibe e caplacizumabe; contextualiza NAC como candidato de reposicionamento com mecanismo distinto |
| [33540569](https://pubmed.ncbi.nlm.nih.gov/33540569/) | 2021 | Revisão | Journal of Clinical Medicine | Fisiopatologia, diagnóstico e manejo da PTT; papel central do ADAMTS13 e lacuna terapêutica que justifica vias auxiliares como o NAC |
| [28416507](https://pubmed.ncbi.nlm.nih.gov/28416507/) | 2017 | Revisão | Blood | PTT: microangiopatia hemolítica trombótica com deficiência grave de ADAMTS13; fundamento para intervenções que reduzem ULVWF sem dependência da enzima deficiente |
| [39737637](https://pubmed.ncbi.nlm.nih.gov/39737637/) | 2025 | Relato de Caso | J Pediatric Hematology/Oncology | Plasmaférese + NAC em PTT congênita com insuficiência renal aguda; mutação nova de ADAMTS13 identificada; primeiro relato de uso pediátrico combinado |
| [28961512](https://pubmed.ncbi.nlm.nih.gov/28961512/) | 2018 | Estudo Animal | Redox Biology | NAC atenua ativação plaquetária sistêmica e trombose de vasos cerebrais em diabetes; elo entre glicação por metilglioxal, ROS e trombose revertido pelo NAC |
| [36410267](https://pubmed.ncbi.nlm.nih.gov/36410267/) | 2022 | Revisão Narrativa | Journal of Infection and Public Health | NAC para prevenção e tratamento de COVID-19; estado protrombótico como alvo terapêutico; revisão do papel do NAC no contexto de trombose associada a inflamação sistêmica |

---

## Informações de Comercialização no Brasil

Acetylcysteine **não possui registro na ANVISA** e não está comercializado no mercado brasileiro. Não há licenças ativas registradas no sistema regulatório nacional. Para uso clínico, seria necessária a solicitação de importação por excepcionalidade ou abertura de processo de registro junto à ANVISA.

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Proceed with Guardrails**

**Justificativa:**
Dois ensaios de Phase 3 centrados em TA-TMA (NCT03252925, concluído, n=170; NCT05907486, n=260) somados a um RCT prospectivo controlado por placebo (PMID 35940529) e a mecanismo molecular bem definido de clivagem de ULVWF estabelecem nível de evidência L1 para o subtipo TA-TMA da doença trombótica. Contudo, a evidência é subtipo-específica e o fármaco não está registrado no Brasil, exigindo salvaguardas regulatórias e clínicas antes de qualquer aplicação.

**Para prosseguir, é necessário:**
- Obter dados completos do mecanismo de ação (MOA) via DrugBank API (DG002)
- Obter informações de segurança da bula oficial (ANVISA/FDA): advertências, contraindicações e interações medicamentosas (DG001 — item bloqueante para avaliação de segurança S1)
- Confirmar status atualizado do ensaio NCT05907486 (Phase 3, status classificado como "desconhecido")
- Estratificar o nível de evidência por subtipo: TA-TMA (L1) vs. TTP adquirida (L2–L3) vs. doença trombótica geral (insuficiente)
- Avaliar viabilidade de registro na ANVISA ou uso via importação por excepcionalidade para contexto de HSCT/oncologia
- Definir via de administração preferencial: NAC intravenoso para formas agudas de TMA/TTP; oral para uso profilático
- Garantir que o uso não substitua anticoagulação padrão nem plasmaférese nas indicações estabelecidas
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

