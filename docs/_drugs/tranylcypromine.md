---
layout: default
title: Tranylcypromine
parent: Apenas Predição do Modelo (L5)
nav_order: 650
evidence_level: L5
indication_count: 7
last_modified_at: 2026-10-28
description: "Tranylcypromine: nova indicação prevista, Torcicolo paroxístico benigno da infância (benign paroxysmal torticol… (nível de evidência L5). Indicação original: Antidepressivos"
monitor_inn: "tranylcypromine"
predicted_indications: ["benign paroxysmal torticollis of infancy", "Ohdo syndrome and variants", "agoraphobia", "blepharophimosis - intellectual disability syndrome, Ohdo type", "neurotic disorder", "ligneous conjunctivitis", "Keppen-Lubinsky syndrome"]
---

# Tranylcypromine
{: .fs-9 }

Nível de evidência: **L5** | Indicações previstas: **7** 
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

## Tranilcipromina: De antidepressivo a torcicolo paroxístico benigno da infância
{: .text-alpha }

## Resumo em Uma Frase

Tranilcipromina (nome comercial PARNATE) é um inibidor irreversível da monoamina oxidase (IMAO), originalmente registrado no Brasil como antidepressivo.
O modelo TxGNN (deep learning) prevê que pode ser eficaz para **torcicolo paroxístico benigno da infância (benign paroxysmal torticollis of infancy)**, mas **não há ensaios clínicos nem publicações** que apoiem essa previsão. A pontuação vem do modelo TxGNN e pode refletir semelhanças que o modelo aprendeu entre doenças relacionadas, não evidência biológica.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Antidepressivos |
| Nova Indicação Prevista | Torcicolo paroxístico benigno da infância (benign paroxysmal torticollis of infancy) |
| Pontuação de Previsão TxGNN | 0,9967 |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | Comercializado (registros ativos: 1 de 1) |
| Número de Registros | 1 (ativos: 1) |
| Decisão Recomendada | Hold |

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação nos dados compilados para este relatório. Segundo informações conhecidas, a tranilcipromina é um inibidor não seletivo e irreversível da MAO, que aumenta os níveis de serotonina, noradrenalina e dopamina. Sua eficácia como antidepressivo é estabelecida, e ela também inibe a LSD1 (KDM1A), uma desmetilase de histonas.

Para o torcicolo paroxístico benigno da infância, **não foi estabelecida nenhuma ligação mecanística**. Trata-se de um distúrbio pediátrico, autolimitado e associado a canalopatia (gene CACNA1A). A pontuação alta do TxGNN vem do modelo de deep learning e pode refletir semelhanças que o modelo aprendeu entre doenças relacionadas, não evidência biológica. Além disso, um IMAO irreversível, com risco de crise hipertensiva e de interação com tiramina, dificilmente seria apropriado para lactentes.

Por isso, a previsão de maior pontuação deve ser vista com cautela. Entre as demais previstas, as que têm alguma literatura (agorafobia, melancolia, depressão neurótica, transtorno neurótico) estão, em geral, próximas da indicação original ou são categorias diagnósticas antigas, o que as torna menos um reposicionamento genuíno.

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados.

## Evidências da Literatura

Atualmente não há literatura relacionada.

## Informações de Comercialização no Brasil

| Número de Registro | Nome Comercial | Forma Farmacêutica | Indicação Aprovada |
|---------|------|------|-----------|
| Registro nº 101070146 (cancelado) | PARNATE | Não informada | Antidepressivos |

## Citotoxicidade

Não se aplica: a tranilcipromina não é um antineoplásico, portanto esta seção foi omitida.

*(Observação: pelas regras do modelo, esta seção deve ser omitida; mantida apenas esta nota para transparência.)*

## Considerações de Segurança

- **Contraindicações previstas pelo grafo de conhecimento (não provenientes da bula)**: hipertensão e transtornos hipertensivos, hipotensão ortostática, doenças cardiovasculares (doença arterial coronariana, parada cardíaca súbita, doença do sistema de condução), feocromocitoma e paraganglioma, hipertireoidismo/doença de Graves, epilepsia, doença renal, doença hepática, doença da vesícula biliar, diabetes mellitus e cetoacidose diabética, transtorno bipolar, abuso/dependência de substâncias, entre outras.
- **Interações medicamentosas**: foram identificadas 151 interações. Entre as de gravidade **maior** estão isometepteno, bupropiona, morfina, lorcasserina, dietilpropiona, dolasetrona, palonosetrona e fentermina. Entre as de gravidade **moderada** estão epinefrina, clorpropamida, glimepirida, repaglinida, insulina asparte, dronabinol e alguns laxantes (picossulfato, sulfato de sódio, polietilenoglicol). Entre as **menores** estão atropina, hioscina e diciclomina.
- **Risco clássico dos IMAO**: relato de 1964 documenta óbito associado à tranilcipromina e queijo (crise hipertensiva por tiramina).

As advertências e contraindicações da bula não estavam disponíveis; consulte a bula para informações de segurança completas.

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
A previsão de maior pontuação (torcicolo paroxístico benigno da infância) não tem nenhum ensaio, publicação ou ligação mecanística plausível, e o perfil de risco do fármaco é incompatível com o uso em lactentes. O único registro no Brasil está cancelado.

**Para prosseguir, é necessário:**
- Obter a bula da ANVISA com advertências e contraindicações oficiais
- Complementar os dados de mecanismo de ação (DrugBank)
- Priorizar, se houver interesse, indicações com literatura (por exemplo, agorafobia e transtorno de pânico refratário), que hoje têm apenas revisões e relatos de caso (nível L4) e exigiriam estudos controlados
- Confirmar a situação regulatória atual do fármaco no Brasil, já que o registro está cancelado
- Elaborar um plano de segurança específico para crise hipertensiva, síndrome serotoninérgica e interações medicamentosas antes de qualquer desenvolvimento
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

