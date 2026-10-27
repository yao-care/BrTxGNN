---
layout: default
title: Brompheniramine
parent: Apenas Predição do Modelo (L5)
nav_order: 159
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-13
description: "Brompheniramine: nova indicação prevista, Urticária alérgica (allergic urticaria) (nível de evidência L5). Indicação original: Produto para terapia sintomática da gripe (descongestionantes e antia…"
---

# Brompheniramine
{: .fs-9 }

Nível de evidência: **L5** | Indicações previstas: **2** 
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

## Bronfeniramina: De descongestionante e antialérgico para urticária alérgica
{: .text-alpha }

## Resumo em Uma Frase

Bronfeniramina é um anti-histamínico, usado em associações com fenilefrina, originalmente indicado como descongestionante e antialérgico e na terapia sintomática da gripe.
O modelo TxGNN prevê que pode ser eficaz para **urticária alérgica (allergic urticaria)**,
atualmente com **0 ensaios clínicos** e **0 publicações** nos dados compilados para este relatório; a previsão se apoia apenas no modelo e na farmacologia da classe.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Produto para terapia sintomática da gripe (descongestionantes e antialérgicos) |
| Nova Indicação Prevista | Urticária alérgica (allergic urticaria) |
| Pontuação de Previsão TxGNN | 99,87% |
| Nível de Evidência | L5 (apenas previsão do modelo, sem estudos específicos para este par fármaco-indicação) |
| Situação no Mercado Brasileiro | ✗ Somente registros cancelados |
| Número de Registros | 19 (todos cancelados) |
| Decisão Recomendada | Hold |

> Observação: a avaliação interna dos dados classificou o par como L4 (questão de pesquisa). Como não há estudos pré-clínicos ou de mecanismo fornecidos, aplicando estritamente os critérios deste relatório o nível é L5. Em ambos os casos, a evidência é apenas indireta.

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação nos dados compilados. Segundo o conhecimento farmacológico geral, a bronfeniramina é um anti-histamínico H1 de primeira geração (classe das alquilaminas), que age como antagonista/agonista inverso do receptor H1. Esta descrição é inferida da farmacologia geral da classe, não dos dados fornecidos.

Na urticária alérgica, a liberação de histamina pelos mastócitos provoca urticas (placas) e prurido. O bloqueio do receptor H1 é, portanto, um encaixe mecanístico direto. A indicação original (descongestionante e antialérgico) já envolve o componente alérgico mediado por histamina, o que apoia a plausibilidade biológica da previsão.

Vale ressaltar que o suporte é indireto (classe do fármaco e uso antialérgico aprovado), e não evidência clínica direta para este par fármaco-indicação.

Uma segunda indicação prevista também foi identificada: **urticária ao frio (cold urticaria)**, com pontuação de 99,55%, igualmente de nível L4/L5 e sem ensaios ou publicações. Qualquer expectativa de eficácia seria extrapolada de outros anti-histamínicos H1.

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados.

## Evidências da Literatura

Atualmente não há literatura relacionada.

## Informações de Comercialização no Brasil

Todos os 19 registros encontram-se cancelados. Principais registros (5 de 19):

| Número de Registro | Nome Comercial | Forma Farmacêutica | Indicação Aprovada |
|---------|------|------|-----------|
| Registro nº 178170957 | BENEDESC PLUS | Não informada | Produto para terapia sintomática da gripe |
| Registro nº 155840646 | Maleato de bronfeniramina + cloridrato de fenilefrina | Não informada | Produto para terapia sintomática da gripe |
| Registro nº 103850005 | BIALERGE | Não informada | Produto para terapia sintomática da gripe |
| Registro nº 178170960 | DESCON | Não informada | Descongestionantes e antialérgicos |
| Registro nº 178170955 | CORISTINA D CONGEST | Não informada | Descongestionantes e antialérgicos |

## Considerações de Segurança

- **Contraindicações segundo o grafo de conhecimento (TxGNN/PrimeKG, não texto de bula)**: hipertensão e distúrbios hipertensivos, doença coronariana, infarto do miocárdio, insuficiência e doenças hepáticas, doença renal, epilepsia, DPOC, úlcera gástrica/péptica, hipotireoidismo, diabetes mellitus e cetoacidose diabética, hiperplasia prostática benigna, hipertensão ocular, pancreatite, doença da vesícula biliar, doença inflamatória intestinal, colite por *Clostridium difficile*, abuso/dependência de substâncias, hemoglobinopatia, entre outras. Esses itens são sinais do grafo e devem ser confirmados na bula.
- **Interações Medicamentosas**: foram identificadas 290 interações. Entre as listadas:
  - **Graves (Major)**: cloreto de potássio e citrato de potássio.
  - **Moderadas**: anticolinérgicos (atropina, hiosciamina, escopolamina, diciclomina, glicopirrônio, propantelina, metescopolamina, clidínio, mepenzolato), opioides e correlatos (morfina, ópio, loperamida, eluxadolina), canabinoides (dronabinol, nabilona) e metoclopramida.

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
- A previsão do TxGNN é alta (99,87%) e o mecanismo anti-histamínico H1 é plausível para urticária alérgica, mas não há ensaios nem literatura para este par, e todos os registros no Brasil estão cancelados. Além disso, os dados de segurança da bula estão ausentes, o que impede a triagem de segurança.

**Para prosseguir, é necessário:**
- Obter e analisar a bula (advertências e contraindicações) no site da ANVISA.
- Confirmar o mecanismo de ação em fonte oficial (DrugBank).
- Realizar revisão sistemática da literatura sobre bronfeniramina e anti-histamínicos H1 em urticária.
- Avaliar a viabilidade regulatória, dado que não há registro válido no Brasil, e a existência de alternativas anti-histamínicas de segunda geração, com melhor perfil de segurança.
- Avaliar o perfil de segurança considerando as contraindicações do grafo e o número elevado de interações.
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

