---
layout: default
title: Latanoprost
parent: Apenas Predição do Modelo (L5)
nav_order: 393
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Latanoprost: nova indicação prevista, Glaucoma Hereditário Primário (Primary Hereditary Glaucoma) (nível de evidência L5). Indicação original: Glaucoma de ângulo aberto e hipertensão ocular"
monitor_inn: "LATANOPROST"
predicted_indications: ["visceral calciphylaxis", "hypotrichosis simplex of the scalp", "venous thoracic outlet syndrome", "arterial thoracic outlet syndrome", "neurogenic thoracic outlet syndrome", "congenital hypotrichosis milia", "angiodysplasia of stomach", "blue toe syndrome", "lymphangiectasis"]
---

# Latanoprost
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

## Latanoprosta: Do glaucoma de ângulo aberto ao glaucoma hereditário primário
{: .text-alpha }

## Resumo em Uma Frase

A latanoprosta é um análogo da prostaglandina F2-alfa, originalmente usado no tratamento do glaucoma de ângulo aberto e da hipertensão ocular.
O modelo TxGNN prevê que ela pode ser eficaz para **Glaucoma Hereditário Primário (Primary Hereditary Glaucoma)**,
mas, até o momento, **não há ensaios clínicos nem publicações** nos dados compilados para este relatório que apoiem esta direção; a previsão se baseia apenas no modelo.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Glaucoma de ângulo aberto e hipertensão ocular (conforme a base de conhecimento do TxGNN, pois não há registros no Brasil) |
| Nova Indicação Prevista | Glaucoma Hereditário Primário (Primary Hereditary Glaucoma) |
| Pontuação de Previsão TxGNN | 99,88% |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | Não comercializado (nos dados compilados) |
| Número de Registros | 0 |
| Decisão Recomendada | Hold |

## Por que Esta Previsão é Razoável?

A latanoprosta é um análogo da prostaglandina F2-alfa que reduz a pressão intraocular ao aumentar o escoamento uveoscleral do humor aquoso. Esse é o mecanismo que sustenta seu uso no glaucoma de ângulo aberto e na hipertensão ocular. Atualmente, não há dados detalhados sobre o mecanismo de ação nos dados compilados; a descrição acima baseia-se em conhecimento farmacológico geral.

O glaucoma hereditário primário (congênito ou juvenil) pertence à mesma área de doença da indicação original, e o objetivo terapêutico, reduzir a pressão intraocular, é o mesmo. Isso torna a pontuação elevada do modelo plausível do ponto de vista mecanístico.

Há, porém, uma ressalva importante: os glaucomas pediátricos e do desenvolvimento costumam envolver malformações da malha trabecular ou do ângulo da câmara anterior, e os análogos de prostaglandinas são frequentemente menos eficazes nesses casos. A previsão deve, portanto, ser tratada como hipótese de pesquisa.

## Outras Indicações Previstas (para contexto)

| Posição | Doença | Pontuação TxGNN | Avaliação |
|------|------|------|------|
| 2 | Calcifilaxia visceral | 99,83% | Hold, sem vínculo mecanístico claro |
| 3 | Hipotricose simples do couro cabeludo | 99,81% | Pergunta de pesquisa; plausível pelo efeito de prostaglandinas no ciclo do folículo piloso (fase anágena) |
| 4 | Síndrome do desfiladeiro torácico venosa | 99,78% | Hold |
| 5 | Síndrome do desfiladeiro torácico arterial | 99,78% | Hold |
| 6 | Síndrome do desfiladeiro torácico neurogênica | 99,72% | Hold |
| 7 | Hipotricose congênita com milia | 99,71% | Pergunta de pesquisa; mesma lógica da hipotricose |
| 8 | Angiodisplasia do estômago | 99,70% | Hold |
| 9 | Síndrome do dedo azul | 99,69% | Hold |
| 10 | Linfangiectasia | 99,67% | Hold |

Todas estão no nível L5, sem ensaios clínicos nem literatura nos dados compilados. A pontuação idêntica das formas venosa e arterial da síndrome do desfiladeiro torácico sugere que a previsão vem de vizinhos compartilhados no grafo, e não de evidência específica da doença.

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados.

## Evidências da Literatura

Atualmente não há literatura relacionada.

## Considerações de Segurança

- **Contraindicações segundo a base de conhecimento (TxGNN/PrimeKG, não é texto de bula)**: uveíte, doença da íris, doença do corpo ciliar, panuveíte, edema macular da retina, edema macular cistoide, irite, conjuntivite e conjuntivite contagiosa aguda. Esses itens indicam condições oculares inflamatórias em que o uso exige cautela.
- **Interações Medicamentosas**: foram identificadas 100 interações potenciais na consulta, mas todas com nível de gravidade "Desconhecido". Exemplos: calcitriol, glimepirida, doxiciclina, clotrimazol, lansoprazol, cimetidina, atropina, pantoprazol, mesalazina, acarbose, morfina, metformina, omeprazol, sucralfato, rosiglitazona, vancomicina, lactulose, triancinolona, prednisona e sinvastatina. A relevância clínica não pôde ser classificada.

As advertências e contraindicações da bula não estão disponíveis; consulte a bula para informações de segurança completas.

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
A previsão para glaucoma hereditário primário tem pontuação alta e plausibilidade mecanística, mas não há ensaios clínicos nem literatura (nível L5), o fármaco não tem registro no Brasil, e a eficácia dos análogos de prostaglandinas em glaucomas do desenvolvimento é duvidosa. As demais indicações previstas têm vínculo mecanístico fraco ou inexistente.

**Para prosseguir, é necessário:**
- Revisão sistemática da literatura sobre análogos de prostaglandinas em glaucoma congênito e juvenil, e busca de ensaios em registros internacionais
- Dados formais de mecanismo de ação (consulta ao DrugBank)
- Obtenção e análise da bula (advertências e contraindicações) no site da ANVISA
- Avaliação da situação regulatória: o fármaco não possui registro no Brasil
- Avaliação de segurança e de formulação para a população pediátrica
- Classificação clínica das interações medicamentosas de gravidade desconhecida
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

