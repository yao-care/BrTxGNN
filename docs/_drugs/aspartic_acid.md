---
layout: default
title: Aspartic Acid
parent: Apenas Predição do Modelo (L5)
nav_order: 82
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-28
description: "Aspartic Acid: nova indicação prevista, Acidose Tubular Renal (Renal Tubular Acidosis) (nível de evidência L5). Indicação original: Nutrientes parenterais"
monitor_inn: "ASPARTIC ACID"
predicted_indications: ["renal tubular acidosis"]
---

# Aspartic Acid
{: .fs-9 }

Nível de evidência: **L5** | Indicações previstas: **1** 
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

## Ácido Aspártico: De nutriente parenteral para acidose tubular renal
{: .text-alpha }

## Resumo em Uma Frase

O ácido aspártico é um aminoácido não essencial, originalmente usado como nutriente parenteral (reposição hidroeletrolítica e alimentação parenteral).
O modelo TxGNN prevê que pode ser eficaz para **Acidose Tubular Renal (Renal Tubular Acidosis)**,
mas atualmente há **0 ensaios clínicos** e **4 publicações** de relevância indireta, sem evidência clínica que sustente diretamente esta previsão.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Nutrientes parenterais |
| Nova Indicação Prevista | Acidose Tubular Renal (Renal Tubular Acidosis) |
| Pontuação de Previsão TxGNN | 0,9947 |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | Comercializado (registros ativos: 9 de 9) |
| Número de Registros | 9 (ativos: 9) |
| Decisão Recomendada | Hold |

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação. Segundo informações conhecidas, o ácido aspártico faz parte de soluções de nutrição parenteral (como componente de misturas de aminoácidos), sua função como nutriente foi estabelecida, e a conexão com a acidose tubular renal é apenas teórica.

Uma possível ligação envolveria o metabolismo renal de amônia e o equilíbrio ácido-base, já que células do túbulo proximal manejam aminoácidos e produzem amônia (amoniogênese). Entretanto, nenhuma das publicações encontradas mostra o ácido aspártico tratando a acidose tubular renal.

Essa doença é principalmente um defeito de transporte, frequentemente genético (por exemplo, mutações no trocador aniônico SLC4A1), e o tratamento padrão é a suplementação de álcalis, não a administração de aminoácidos. A pontuação alta do TxGNN (0,9947) é apenas uma previsão computacional, sem respaldo clínico.

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados.

## Evidências da Literatura

Nenhuma publicação testa o ácido aspártico como tratamento da acidose tubular renal. Os trabalhos abaixo são de relevância indireta.

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [26208211](https://pubmed.ncbi.nlm.nih.gov/26208211/) | 2015 | Estudo diagnóstico | Jornal de Pediatria | Sequenciamento completo do exoma para diagnóstico genético de quatro crianças com acidose tubular renal distal |
| [6422151](https://pubmed.ncbi.nlm.nih.gov/6422151/) | 1983 | Relato de caso | J Inherit Metab Dis | Recém-nascido com deficiência de piruvato carboxilase, acidose tubular renal proximal e cistinúria; a criança passou a se desenvolver após suplementação dietética com aspartato, asparagina e outros aminoácidos (resumo incompleto) |
| [20068363](https://pubmed.ncbi.nlm.nih.gov/20068363/) | 2010 | Série de casos genética | Nephron Physiology | Descrição clínica e genética da acidose tubular renal distal em crianças filipinas, causada por mutações em SLC4A1 |
| [14301365](https://pubmed.ncbi.nlm.nih.gov/14301365/) | 1965 | Fisiologia básica | Am J Physiol | Relação do pH/NH3 das células tubulares com a produção renal de amônia (sem resumo disponível) |

## Informações de Comercialização no Brasil

Os 9 registros estão válidos (9 de 9); o medicamento está comercializado.

| Número de Registro | Nome Comercial | Forma Farmacêutica | Indicação Aprovada |
|---------|------|------|-----------|
| Registro 100850145 | AMIXAL | Não informada | Nutrientes parenterais |
| Registro 100850109 | NUTRIFLEX PLUS | Não informada | Nutrientes parenterais |
| Registro 100850246 | NUTRIFLEX LIPID | Não informada | Nutrientes parenterais |
| Registro 100850124 | NUTRIFLEX LIPID | Não informada | Nutrientes parenterais |
| Registro 100850247 | NUTRIFLEX | Não informada | Nutrientes parenterais |

## Considerações de Segurança

- **Contraindicações associadas no grafo de conhecimento** (relações fármaco-doença do TxGNN/PrimeKG, não texto de bula): doença renal, piureter, doença diarreica (incluindo diarreia crônica), bloqueio atrioventricular, paralisia periódica hipercalêmica, paralisia periódica, hipoaldosteronismo, miotonia congênita e gastroparesia.
- Chama atenção a presença de doença renal e hipoaldosteronismo entre essas condições, pois guardam relação com o contexto da nova indicação.
- Não foram encontradas interações medicamentosas nos dados compilados.

Consulte a bula para advertências e contraindicações formais.

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
A previsão se baseia apenas no modelo (L5): não há ensaios clínicos, a literatura é indireta, não há ligação mecanística comprovada, e o tratamento padrão da acidose tubular renal (álcalis) é distinto. Além disso, o medicamento está comercializado, com 9 registros válidos de 9.

**Para prosseguir, é necessário:**
- Obter o mecanismo de ação (consulta à API do DrugBank)
- Obter advertências e contraindicações da bula na ANVISA
- Estudos pré-clínicos ou de mecanismo sobre aspartato, amoniogênese renal e equilíbrio ácido-base
- Avaliar a viabilidade regulatória, dado que não há registro válido no Brasil, e a compatibilidade de vias de administração
- Revisão de segurança renal, considerando que a previsão do modelo TxGNN (deep learning) para acidose tubular renal pode refletir similaridades aprendidas entre doenças relacionadas, não evidência biológica
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

