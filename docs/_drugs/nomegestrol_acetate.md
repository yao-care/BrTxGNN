---
layout: default
title: Nomegestrol Acetate
parent: Apenas Predição do Modelo (L5)
nav_order: 476
evidence_level: L5
indication_count: 10
---

# Nomegestrol Acetate
{: .fs-9 }

Nível de evidência: **L5** | Indicações previstas: **10** 
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

# Acetato de nomegestrol: De anticoncepcional a candidíase (previsão do modelo, sem evidências de suporte)

## Resumo em Uma Frase

O acetato de nomegestrol é um progestágeno originalmente usado como anticoncepcional.
O modelo TxGNN prevê que pode ser eficaz para **candidíase (candidiasis)**, mas atualmente há **0 ensaios clínicos** e **0 publicações** apoiando esta direção. A previsão baseia-se apenas na pontuação do modelo.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Anticoncepcionais |
| Nova Indicação Prevista | Candidíase (Candidiasis) |
| Pontuação de Previsão TxGNN | 98,78% |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | Apenas registros cancelados |
| Número de Registros | 2 |
| Decisão Recomendada | Hold |

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação. Segundo informações conhecidas, o acetato de nomegestrol é um progestágeno usado em contracepção hormonal. Sua eficácia como anticoncepcional é reconhecida, mas não há dados no material compilado que o conectem ao tratamento da candidíase.

Na prática, a relação aponta no sentido oposto: contraceptivos hormonais estão geralmente associados a **maior risco** de candidíase vulvovaginal, e não ao seu tratamento. A pontuação alta (98,78%) provavelmente reflete proximidade na rede do grafo de conhecimento, e não um mecanismo farmacológico demonstrado. Por isso, a previsão deve ser tratada com cautela.

### Outras indicações previstas (todas nível L5)

Além da candidíase, o modelo previu outras indicações, nenhuma com ensaios clínicos e todas sem mecanismo plausível identificado nos dados compilados:

| Posição | Doença prevista | Pontuação | Observação |
|------|------|------|------|
| 2 | Deficiência de antitrombina tipo 2 | 98,53% | Progestágenos não corrigem defeito funcional do gene SERPINC1; risco trombótico em trombofilia |
| 3 | Deficiência de cofator 2 da heparina | 98,49% | Provável proximidade na rede de coagulação; cautela pelo perfil trombótico |
| 4 | Excesso de fator 5 com trombose espontânea | 98,45% | Condição trombofílica em que hormônios exigem cautela; provável artefato de associação |
| 5 | Mieloma de plasmócitos | 97,75% | Racional apenas especulativo |
| 6 | Gota | 97,60% | Nenhuma via conhecida liga progestágeno à redução de urato |
| 7 | Mieloma de plasmócitos indolente | 97,53% | Mesma ausência de mecanismo do mieloma |
| 8 | Neoplasia cardíaca | 97,37% | Tumor raro sem conexão mecanística identificada |
| 9 | Doença trombótica | 97,37% | Única com literatura, mas trata de risco, não de benefício |
| 10 | Artrite reumatoide | 97,36% | Hormônios sexuais modulam imunidade, sem evidência direta |

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados.

## Evidências da Literatura

Para a indicação principal (candidíase), atualmente não há literatura relacionada.

Para fins de contexto, a única publicação identificada em todas as previsões refere-se a outra indicação (doença trombótica, 9ª posição) e trata de segurança:

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [36254131](https://pubmed.ncbi.nlm.nih.gov/36254131/) | 2022 | Estudo de coorte/observacional (inferido pelo título) | Przeglad Menopauzalny (Menopause Review) | Avalia o risco de tromboembolismo venoso com terapias hormonais orais de estrogênio-progestágeno, incluindo a combinação de estradiol e acetato de nomegestrol. É um dado de **risco**, não de benefício terapêutico. |

## Informações de Comercialização no Brasil

| Número de Registro | Nome Comercial | Forma Farmacêutica | Indicação Aprovada |
|---------|------|------|-----------|
| Registro nº 100330209 (cancelado) | IZIZ | Não informada | Anticoncepcionais |
| Registro nº 197110002 (cancelado) | STEZZA | Não informada | Anticoncepcionais |

## Considerações de Segurança

- **Risco trombótico**: a literatura identificada discute o risco de tromboembolismo venoso com terapias hormonais combinadas. Várias das doenças previstas (deficiência de antitrombina, deficiência de cofator 2 da heparina, excesso de fator 5) são trombofilias, nas quais agentes hormonais exigem cautela especial.
- **Candidíase**: contraceptivos hormonais estão geralmente associados a maior risco de candidíase vulvovaginal.

Para as demais informações de segurança (advertências, contraindicações e interações medicamentosas), consulte a bula.

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
A previsão baseia-se exclusivamente na pontuação do modelo (nível L5), sem ensaios clínicos nem literatura de suporte, e o conhecimento atual sugere associação inversa entre contraceptivos hormonais e candidíase. Além disso, todos os registros no Brasil estão cancelados.

**Para prosseguir, é necessário:**
- Obter e analisar a bula na ANVISA (advertências e contraindicações), etapa indispensável para a triagem de segurança
- Obter dados do mecanismo de ação (por exemplo, via DrugBank)
- Realizar revisão sistemática da literatura e estudos pré-clínicos que justifiquem uma hipótese mecanística plausível para candidíase
- Avaliar a viabilidade regulatória e comercial, dado que não há registros válidos no Brasil
- Avaliar a compatibilidade de vias de administração e a similaridade com a indicação original
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

