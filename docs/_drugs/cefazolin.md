---
layout: default
title: Cefazolin
parent: Evidência Moderada (L3-L4)
nav_order: 204
evidence_level: L4
indication_count: 10
---

# Cefazolin
{: .fs-9 }

Nível de evidência: **L4** | Indicações previstas: **10** 
{: .fs-6 .fw-300 }

---

## Índice
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Relatório de avaliação farmacêutica

</div>

# Cefazolina: De pneumonia bacteriana e outras infecções para otite média infecciosa

## Resumo em Uma Frase

Cefazolina é uma cefalosporina de primeira geração, originalmente usada em infecções bacterianas como pneumonia bacteriana (estreptocócica e estafilocócica), colangite, endocardite e artrite bacteriana.
O modelo TxGNN prevê que pode ser eficaz para **otite média infecciosa (infectious otitis media)**,
mas atualmente há **0 ensaios clínicos** e **2 publicações** (um relato de caso e uma revisão com pouca relação direta com o tema), ou seja, a previsão se apoia essencialmente no modelo.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Pneumonia bacteriana (os textos de indicação aprovados no Brasil não estão disponíveis; a informação vem das relações de indicação do grafo de conhecimento do TxGNN) |
| Nova Indicação Prevista | Otite média infecciosa (infectious otitis media) |
| Pontuação de Previsão TxGNN | 99,44% |
| Nível de Evidência | L4 |
| Situação no Mercado Brasileiro | ✗ Não comercializado (nos dados compilados) |
| Número de Registros | 0 |
| Decisão Recomendada | Hold |

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação no registro do fármaco. Segundo conhecimento geral, a cefazolina é uma cefalosporina de primeira geração que inibe a síntese da parede celular bacteriana ao se ligar às proteínas ligadoras de penicilina (PBP). Tem boa atividade contra estreptococos e *Staphylococcus aureus* sensível à meticilina.

A indicação original (pneumonias estreptocócica e estafilocócica, endocardite, artrite bacteriana) envolve os mesmos tipos de bactérias gram-positivas que também podem causar otite média. Essa sobreposição de patógenos explica a pontuação alta do modelo.

Há limitações importantes: a atividade contra *H. influenzae* e *M. catarrhalis*, patógenos frequentes na otite média, é limitada, e a cefazolina só existe em forma parenteral, o que é pouco prático para uma infecção geralmente tratada por via oral. Não há dados clínicos diretos que sustentem a previsão.

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados.

## Evidências da Literatura

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [3742953](https://pubmed.ncbi.nlm.nih.gov/3742953/) | 1986 | Revisão | Clinical Pharmacy | Descrição de um caso de síndrome de Stevens-Johnson em uma menina de 2,5 anos tratada por otite média e outras condições com vários antibióticos, com revisão da literatura sobre a síndrome. Não avalia a eficácia da cefazolina |
| [39567876](https://pubmed.ncbi.nlm.nih.gov/39567876/) | 2025 | Relato de caso | Annals of Otology, Rhinology, and Laryngology | Terapia empírica com ceftazidima-cefazolina na síndrome de Gradenigo pediátrica, complicação rara de otite média aguda. Evidência de caso isolado |

Nota: a literatura recuperada para as indicações vizinhas (otite média supurativa, crônica e outras) inclui um estudo comparativo japonês de 1982 entre cefmetazol e cefazolina na otite média supurativa (PMID 6752467, 172 pacientes avaliados), o único sinal clínico direto relacionado à cefazolina, mas antigo e sem validação moderna.

## Considerações de Segurança

- **Contraindicações (relações do grafo de conhecimento, não texto de bula)**: doença de coagulação do sangue, colite por *Clostridium difficile*, enterocolite necrosante perinatal e deficiência congênita de protrombina.
- **Interações Medicamentosas**: foram identificadas 100 interações na consulta. As de nível **moderado** incluem os aminoglicosídeos canamicina, neomicina e estreptomicina, além do ácido picossulfúrico. Outras (nível desconhecido) incluem calcitriol, epinefrina, anfotericina B, manitol, ácido acetilsalicílico, amoxicilina, bupropiona, budesonida, pantoprazol, glimepirida, clotrimazol, acarbose, morfina, metformina, omeprazol e sucralfato.

As advertências e contraindicações da bula da ANVISA não estavam disponíveis; consulte a bula para as informações completas de segurança.

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
- A previsão tem pontuação alta, mas está no nível L4 de evidência, sem ensaios clínicos e com apenas literatura indireta. O espectro limitado contra os principais patógenos da otite média e a via exclusivamente parenteral reduzem a plausibilidade prática. Além disso, o fármaco não tem registro comercializado no Brasil nos dados compilados.

**Para prosseguir, é necessário:**
- Obter e analisar a bula da ANVISA (advertências e contraindicações), pois a triagem de segurança está bloqueada
- Obter os dados de mecanismo de ação no DrugBank
- Verificar a situação regulatória da cefazolina no Brasil (nenhum registro foi encontrado)
- Avaliar a viabilidade de uso parenteral na otite média e comparar com alternativas orais já estabelecidas
- Obter e revisar o estudo de 1982 (PMID 6752467) e buscar estudos clínicos modernos
- Considerar, como alternativa de menor risco, indicações com racional mais forte, como a otite média supurativa (única com sinal clínico direto, nível L3)
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

