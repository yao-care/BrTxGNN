---
layout: default
title: Pyridoxine
parent: Apenas Predição do Modelo (L5)
nav_order: 556
evidence_level: L5
indication_count: 10
---

# Pyridoxine
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

# Piridoxina: De monovitamina à uretrite por Ureaplasma

## Resumo em Uma Frase

A piridoxina (vitamina B6) foi originalmente registrada no Brasil como monovitamina e como componente de associações antieméticas e vitamínicas.
O modelo TxGNN prevê que ela possa ser eficaz para **uretrite por Ureaplasma (Ureaplasma urethritis)**, mas **não há ensaios clínicos nem publicações** que apoiem essa direção. É uma previsão puramente computacional.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Monovitaminas, exceto vitamina K |
| Nova Indicação Prevista | Uretrite por Ureaplasma (Ureaplasma urethritis) |
| Pontuação de Previsão TxGNN | 93,87% |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | ✗ Somente registros cancelados |
| Número de Registros | 20 (todos cancelados) |
| Decisão Recomendada | Hold |

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação nos dados compilados para este relatório. Segundo informações conhecidas, a piridoxina é a forma de vitamina B6 que o organismo converte em fosfato de piridoxal (PLP), coenzima do metabolismo de aminoácidos, neurotransmissores e unidades de um carbono. Sua eficácia na reposição vitamínica e, em associações, no controle de náuseas é conhecida.

**A previsão não se sustenta do ponto de vista mecanístico.** A piridoxina não tem atividade antimicrobiana conhecida contra *Ureaplasma*, e o tratamento padrão da uretrite é feito com antibióticos. A pontuação alta (93,87%) parece refletir apenas associações no grafo de conhecimento, sem respaldo clínico ou na literatura. A análise de similaridade com a indicação original não foi concluída.

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados.

## Evidências da Literatura

Atualmente não há literatura relacionada.

## Informações de Comercialização no Brasil

Todos os 20 registros encontrados estão cancelados. A tabela mostra os 5 principais.

| Número de Registro | Nome Comercial | Forma Farmacêutica | Indicação Aprovada |
|---------|------|------|-----------|
| Registro nº 107150060 | NEURI - B6 | Não informada | Monovitaminas, exceto vitamina K |
| Registro nº 115600078 | NAUSILON B6 | Não informada | Antieméticos e antinauseantes |
| Registro nº 103920092 | DIMENIDRIN | Não informada | Antieméticos e antinauseantes |
| Registro nº 103920210 | DRIVOM B6 | Não informada | Antieméticos e antinauseantes |
| Registro nº 178170907 | DRAMIN B6 | Não informada | Antieméticos e antinauseantes |

## Considerações de Segurança

As informações de bula sobre advertências e contraindicações não estavam disponíveis nos dados compilados. Consulte a bula para esses itens.

- **Contraindicações sugeridas pelo grafo de conhecimento** (não provêm do texto de bula e devem ser tratadas como sinais a verificar): insuficiência e doença hepática, doença renal e comprometimento da função renal, úlcera péptica, doenças da vesícula biliar, diabetes mellitus e cetoacidose diabética, gota, lúpus eritematoso sistêmico e doenças autoimunes, neuropatia periférica e doenças do sistema nervoso periférico, transtornos de ansiedade e neuróticos, dependência de substâncias, rabdomiólise, hemocromatose e doenças do metabolismo do ferro, doença de Wilson, doença diarreica, deficiência de potássio e acetilação lenta.
- **Interações medicamentosas** (13 registradas):
  - **Moderadas**: altretamina, fenobarbital, levodopa e fenitoína.
  - **Leves**: amobarbital, butabarbital, butalbital, metoexital, pentobarbital, secobarbital, tiopental, metilfenobarbital e primidona.

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
- A previsão tem nível de evidência L5: não há ensaios, não há literatura e não há mecanismo plausível. Além disso, todos os registros brasileiros estão cancelados.
- Os demais candidatos de maior pontuação (gonorreia, infecção urinária, doença inflamatória uterina, pielonefrite xantogranulomatosa) também ficam em Hold, por falta de fundamento mecanístico.
- O candidato **"distúrbio por deficiência vitamínica"** (pontuação de 85,50%) é uma exceção. Tem nível L2, com um ensaio de Fase 2/3 concluído (NCT01128244, 13 participantes, efeitos da vitamina B6 no metabolismo de um carbono) e revisões sobre epilepsias dependentes de B6.
  - Esse candidato é mais bem descrito como uso nutricional próprio da vitamina do que como reposicionamento.
  - Sua recomendação preliminar é *Proceed with Guardrails*, com cautela quanto à neuropatia sensorial em doses altas e crônicas, às interações (como levodopa sem inibidor de descarboxilase) e à situação regulatória.

**Para prosseguir, é necessário:**
- Obter as advertências e contraindicações da bula na ANVISA.
- Obter dados de mecanismo de ação da piridoxina, por exemplo no DrugBank.
- Para uretrite por Ureaplasma, realizar estudos pré-clínicos ou observacionais que demonstrem algum efeito antimicrobiano ou adjuvante. Sem isso, a previsão não deve avançar.
- Considerar priorizar a avaliação do candidato "distúrbio por deficiência vitamínica", verificando a disponibilidade regulatória, já que os registros atuais estão cancelados.
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

