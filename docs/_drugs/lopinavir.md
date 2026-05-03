---
layout: default
title: Lopinavir
parent: 僅模型預測 (L5)
nav_order: 329
evidence_level: L5
indication_count: 3
---

# Lopinavir
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

O skill `txgnn-pipeline` confirma o contexto do projeto. Agora vou gerar o relatório completo com base no Evidence Pack fornecido.

---

# Lopinavir: De HIV/AIDS para Síndrome de Imunodeficiência Adquirida Felina

## Resumo em Uma Frase

Lopinavir é um inibidor de protease antiretroviral, utilizado em co-formulação com ritonavir (Kaletra®) no tratamento da infecção por HIV-1/AIDS em adultos e crianças.
O modelo TxGNN prevê que pode ser eficaz para **Síndrome de Imunodeficiência Adquirida Felina (Feline Acquired Immunodeficiency Syndrome)**,
porém atualmente **não há ensaios clínicos** nem **publicações científicas** na base de dados apoiando esta direção.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Infecção por HIV-1/AIDS |
| Nova Indicação Prevista | Síndrome de Imunodeficiência Adquirida Felina (Feline Acquired Immunodeficiency Syndrome) |
| Pontuação de Previsão TxGNN | 99,90% |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | ✓ Comercializado |
| Número de Registros ANVISA | 4 |
| Decisão Recomendada | Hold |

---

## Por que Esta Previsão é Razoável?

Atualmente, o Evidence Pack não contém dados detalhados sobre o mecanismo de ação. Com base em informações farmacológicas conhecidas, Lopinavir é um inibidor competitivo da protease do HIV-1 — a enzima responsável pela clivagem da poliproteína Gag-Pol em proteínas estruturais e enzimáticas maduras. Sem essa clivagem, os vírions produzidos são imaturos e não infectantes. A co-administração obrigatória com ritonavir serve para inibir o CYP3A4 hepático, elevando a concentração plasmática do Lopinavir a níveis terapêuticos.

O FIV (Vírus da Imunodeficiência Felina), assim como o HIV-1, é um lentivírus que codifica uma Aspartil Protease para realizar a mesma clivagem Gag-Pol, constituindo o alvo molecular análogo. Há uma plausibilidade estrutural parcial: o bolso de ligação ao substrato das duas proteases compartilha similaridades topológicas. Contudo, a especificidade de substrato da protease do FIV difere substancialmente da do HIV-1, e os dados de atividade in vitro de inibidores de protease do HIV contra o FIV são escassos e em sua maioria negativos na literatura.

A alta pontuação TxGNN (99,90%) deriva principalmente da conectividade compartilhada no grafo de conhecimento entre nós HIV e FIV — especificamente os nós `viral_replication` e `retroviral_protease` — configurando uma **inferência topológica do grafo**, e não evidência experimental direta. Este é um caso em que a racionalidade mecanicista existe em nível conceitual, mas a ausência total de estudos publicados exige interpretação muito cautelosa.

---

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados.

---

## Evidências da Literatura

Atualmente não há literatura relacionada.

---

## Informações de Comercialização no Brasil

Lopinavir possui **4 registros** ativos na ANVISA. Os detalhes individuais (número de registro, nome comercial, forma farmacêutica e texto da indicação aprovada) não estão disponíveis no presente Evidence Pack. Consulte o portal da ANVISA em [consultas.anvisa.gov.br](https://consultas.anvisa.gov.br) para acessar as informações completas de cada registro.

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
A previsão baseia-se exclusivamente em inferência topológica do grafo de conhecimento (nível L5), sem qualquer ensaio clínico ou publicação científica de suporte. Embora exista plausibilidade estrutural parcial entre as proteases de HIV e FIV, a eficácia do Lopinavir contra o FIV não foi demonstrada em estudos publicados, e os dados in vitro disponíveis são majoritariamente negativos para inibidores de protease do HIV frente ao FIV.

**Para prosseguir, é necessário:**
- Conduzir ou identificar estudos in vitro de inibição da protease do FIV por Lopinavir
- Realizar busca ampliada na literatura veterinária sobre atividade de inibidores de protease do HIV contra FIV
- Recuperar os detalhes completos dos 4 registros ANVISA (número, indicação aprovada, forma farmacêutica)
- Obter dados de segurança completos da bula ANVISA (advertências, contraindicações, interações medicamentosas)
- Confirmar o mecanismo de ação (MOA) via DrugBank API (DB01601) para análise de relevância mecanística
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

