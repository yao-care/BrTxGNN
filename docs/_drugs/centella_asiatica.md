---
layout: default
title: Centella Asiatica
parent: Apenas Predição do Modelo (L5)
nav_order: 214
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Centella Asiatica: nova indicação prevista, Insônia (insomnia) (nível de evidência L5). Indicação original: Não há indicação registrada"
monitor_inn: "Centella asiatica"
predicted_indications: ["insomnia (disease)", "anxiety", "sleep disorder, initiating and maintaining sleep", "agoraphobia", "rheumatoid arthritis", "anxiety disorder", "alcohol withdrawal delirium", "benign paroxysmal torticollis of infancy", "acute encephalopathy with biphasic seizures and late reduced diffusion", "colobomatous microphthalmia-rhizomelic dysplasia syndrome"]
---

# Centella Asiatica
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

## Centella asiatica: De uso sem indicação registrada no Brasil para insônia
{: .text-alpha }

## Resumo em Uma Frase

Centella asiatica (centela asiática, também conhecida como gotu kola) é uma planta medicinal tradicional que não possui indicação original registrada na ANVISA e não é comercializada no Brasil como medicamento.
O modelo TxGNN prevê que ela pode ser eficaz para **insônia (insomnia)**, com pontuação muito alta, mas o único suporte é **1 publicação** pré-clínica (modelo em larvas de peixe-zebra) e **nenhum ensaio clínico** registrado.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Não há indicação registrada (sem registros na ANVISA) |
| Nova Indicação Prevista | Insônia (insomnia) |
| Pontuação de Previsão TxGNN | 99,94% |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | Não comercializado |
| Número de Registros | 0 |
| Decisão Recomendada | Hold |

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação. Segundo informações conhecidas, a Centella asiatica é uma erva usada há muito tempo na medicina ayurvédica e em outras medicinas tradicionais asiáticas, sobretudo para cicatrização, saúde da pele e, tradicionalmente, ansiedade e memória. Seus principais constituintes são triterpenos (ácido asiático, madecassosídeo, asiaticosídeo).

A relação com a insônia é indireta. O único estudo disponível indica que um extrato etanólico da planta reduziu a sinalização de orexina, ERK, Akt e p38 em larvas de peixe-zebra com modelo de insônia. A orexina (hipocretina) participa do sistema de vigília, de modo que a inibição dessa via seria compatível com um efeito sedativo. Também se especula uma ligação com efeitos ansiolíticos ou sobre receptores GABA-A, mas isso é hipótese.

É preciso cautela: o estudo é pré-clínico, em organismo não mamífero, sem dados em humanos. A pontuação alta do TxGNN (0,999) é uma previsão computacional e não equivale a evidência de eficácia.

### Outras indicações previstas (para contexto)

| Indicação | Pontuação TxGNN | Nível de Evidência | Observação |
|------|------|------|------|
| Ansiedade / transtorno de ansiedade | 99,08% / 98,03% | L3 | Um pequeno estudo clínico em transtorno de ansiedade generalizada (33 participantes, sem grupo controle documentado) e revisões; um estudo de 2025 sugere que os constituintes testados não explicam o efeito ansiolítico |
| Artrite reumatoide | 98,05% | L4 | Estudos consistentes em modelos animais; sem dados em humanos |
| Distúrbio do sono (iniciar e manter o sono) | 99,03% | L5 | Mesmo estudo em peixe-zebra |
| Agorafobia | 98,07% | L5 | Apenas revisão geral sobre ansiedade |
| Demais (delirium por abstinência alcoólica, torcicolo paroxístico benigno da infância, encefalopatia aguda bifásica, síndrome colobomatosa) | 97,5% a 97,9% | L5 | Sem literatura; provavelmente artefatos do grafo |

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados.

## Evidências da Literatura

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [38812527](https://pubmed.ncbi.nlm.nih.gov/38812527/) | 2024 | Pré-clínico (peixe-zebra) | F1000Research | Extrato etanólico de C. asiatica em modelo de insônia em larvas de peixe-zebra, com inibição das vias de orexina, ERK, Akt e p38 |

Para as indicações vizinhas, a literatura mais relevante é a seguinte (ansiedade, relacionada ao sono):

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [20677602](https://pubmed.ncbi.nlm.nih.gov/20677602/) | 2010 | Estudo clínico pequeno | Nepal Med Coll J | 33 participantes com transtorno de ansiedade generalizada receberam extrato hidroetanólico (500 mg, duas vezes ao dia) |
| [23653088](https://pubmed.ncbi.nlm.nih.gov/23653088/) | 2013 | Revisão | CNS Drugs | Revisão de medicamentos à base de plantas para ansiedade, com evidências clínicas e pré-clínicas |
| [26848139](https://pubmed.ncbi.nlm.nih.gov/26848139/) | 2016 | Pré-clínico (camundongo) | Phytother Res | Efeito neuroprotetor contra ansiedade, dano oxidativo e neuroinflamação induzidos por privação de sono, com envolvimento do óxido nítrico |
| [27062315](https://pubmed.ncbi.nlm.nih.gov/27062315/) | 2016 | Pré-clínico (in vitro) | Chem Biol Drug Des | Triterpenos (ácidos asiático e madecássico) mostraram modulação negativa seletiva de subtipos de receptores GABA-A |
| [41097248](https://pubmed.ncbi.nlm.nih.gov/41097248/) | 2025 | Pré-clínico (camundongo) | Nutrients | Triterpenos e ácidos cafeoilquínicos contribuem para a cognição, mas não para o efeito ansiolítico |

## Considerações de Segurança

- **Interações medicamentosas**: não foram encontradas interações registradas nos dados compilados.
- **Outros dados de segurança**: as advertências e contraindicações da bula não estão disponíveis nos dados compilados. Consulte a bula para informações de segurança.

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
- Para insônia, a previsão tem nível de evidência L5: um único estudo em larvas de peixe-zebra, sem dados em mamíferos ou humanos, e nenhum ensaio clínico. A alta pontuação do TxGNN é apenas computacional.
- A planta não tem registro na ANVISA, e a ausência dos dados de bula impede a triagem de segurança.
- Entre as indicações previstas, ansiedade (L3) e artrite reumatoide (L4) têm suporte um pouco maior, mas ainda como questões de pesquisa, e não como candidatas a avanço clínico.

**Para prosseguir, é necessário:**
- Obter advertências e contraindicações de bulas ou monografias oficiais, para a triagem de segurança.
- Obter dados de mecanismo de ação (por exemplo, no DrugBank).
- Replicar o efeito sobre o sono em modelos de mamíferos.
- Se houver interesse clínico, conduzir ensaio randomizado e controlado, com padronização do extrato, em ansiedade ou insônia.
- Definir a categoria regulatória no Brasil (fitoterápico, medicamento ou suplemento), já que não há registros atualmente.
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

