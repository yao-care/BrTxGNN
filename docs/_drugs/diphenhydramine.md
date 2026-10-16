---
layout: default
title: Diphenhydramine
parent: Apenas Predição do Modelo (L5)
nav_order: 272
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Diphenhydramine: nova indicação prevista, Conjuntivite da rosácea (rosacea conjunctivitis) (nível de evidência L5). Indicação original: Anti-histamínicos sistêmicos"
monitor_inn: "Diphenhydramine"
predicted_indications: ["rosacea conjunctivitis", "rhinitis", "allergic urticaria", "cold urticaria", "cauda equina syndrome", "nasopharyngitis", "viral conjunctivitis", "neuralgia", "trigeminal autonomic cephalalgia", "glossodynia"]
---

# Diphenhydramine
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

# Difenidramina: De anti-histamínico sistêmico para rinite

## Resumo em Uma Frase

A difenidramina é um anti-histamínico de primeira geração, registrado no Brasil em produtos para alergia, náusea, tosse e orofaringe.
O modelo TxGNN classifica como primeira previsão a **conjuntivite da rosácea (rosacea conjunctivitis)**, sem nenhuma evidência clínica. A indicação com maior suporte entre as previstas é a **rinite (rhinitis)**, com **5 ensaios clínicos** e **18 publicações** nos dados compilados. Ela é, na prática, um uso já estabelecido da classe, e não um reposicionamento genuíno.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Anti-histamínicos sistêmicos |
| Nova Indicação Prevista (primeira do ranking) | Conjuntivite da rosácea (rosacea conjunctivitis) |
| Pontuação de Previsão TxGNN | 99,20% |
| Nível de Evidência | L5 (para a primeira do ranking) |
| Situação no Mercado Brasileiro | Somente registros cancelados |
| Número de Registros | 6 (todos cancelados) |
| Decisão Recomendada | Hold (para a primeira do ranking) |

**Observação:** a primeira indicação prevista (conjuntivite da rosácea) tem apenas a previsão do modelo. O restante deste relatório detalha a **rinite** (2ª colocada, pontuação de 98,35%, nível L1, decisão *Proceed with Guardrails*), por ser a única com ensaios clínicos e literatura substanciais. Também são resumidas as demais candidatas.

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação nos dados compilados. Segundo informações conhecidas, a difenidramina é um antagonista (agonista inverso) do receptor H1 de primeira geração, com atividade anticolinérgica marcante e efeitos sobre o sistema nervoso central (sedação).

**Conjuntivite da rosácea (1ª do ranking):** o bloqueio de H1 poderia, em tese, reduzir a inflamação da superfície ocular mediada por histamina. Porém, a doença é causada principalmente por disfunção das glândulas meibomianas, ativação imune inata e fatores microbianos ou de *Demodex*. Não há ensaios nem literatura que sustentem a relação.

**Rinite:** o bloqueio de H1 reduz espirros, coriza e prurido na rinite alérgica, e a ação anticolinérgica diminui as secreções nasais. Trata-se de um uso que se sobrepõe à classe anti-histamínica original, portanto não é um reposicionamento verdadeiro.

## Evidências de Ensaios Clínicos

Ensaios para **rinite**:

| Número do Ensaio | Fase | Status | Participantes | Principais Achados |
|---------|------|------|------|---------|
| [NCT00648973](https://clinicaltrials.gov/study/NCT00648973) | Phase 4 | Concluído | 1021 | Difenidramina 25 mg e 50 mg vs. placebo e pseudoefedrina para congestão nasal na rinite alérgica sazonal (duplo-cego, randomizado) |
| [NCT00762749](https://clinicaltrials.gov/study/NCT00762749) | Phase 1 | Concluído | 36 | Farmacocinética de dose única em crianças e adolescentes; apoia dose e segurança, não eficácia |
| [NCT05586477](https://clinicaltrials.gov/study/NCT05586477) | Phase 4 | Concluído | 20 | Efeito sobre a termorregulação durante exercício; foco em fisiologia de segurança |
| [NCT06217367](https://clinicaltrials.gov/study/NCT06217367) | Phase 4 | Desconhecido | 16 | Anti-histamínicos de venda livre e termorregulação durante estresse térmico passivo |
| [NCT01177852](https://clinicaltrials.gov/study/NCT01177852) | Phase 3 | Retirado | 0 | Combinação difenidramina + dropropizina + pseudoefedrina em crianças de 2 a 12 anos com tosse e rinite aguda; sem participantes, sem evidência |

Ensaios de outras indicações previstas:

| Número do Ensaio | Fase | Status | Participantes | Indicação | Principais Achados |
|---------|------|------|------|------|---------|
| [NCT02023164](https://clinicaltrials.gov/study/NCT02023164) | Phase 3 | Concluído | 36 | Urticária alérgica | Piloto de viabilidade comparando cetirizina IV com difenidramina IV (comparador); não tem poder para avaliar eficácia |
| [NCT01406860](https://clinicaltrials.gov/study/NCT01406860) | NA | Terminado | 19 | Cefaleia autonômica trigeminal | Droperidol vs. metoclopramida + difenidramina em cefaleias primárias no pronto-socorro; não isola o efeito da difenidramina |
| [NCT01669967](https://clinicaltrials.gov/study/NCT01669967) | NA | Concluído | 34 | Neuralgia | Lidocaína IV em dor neuropática; não testa difenidramina |
| [NCT00837941](https://clinicaltrials.gov/study/NCT00837941) | Phase 2 | Retirado | 0 | Neuralgia | Estudo analgésico de dose única; sem participantes |

Para conjuntivite da rosácea, urticária ao frio, síndrome da cauda equina, nasofaringite, conjuntivite viral e glossodinia não há ensaios clínicos registrados.

## Evidências da Literatura

Literatura para **rinite** (principais):

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [16680933](https://pubmed.ncbi.nlm.nih.gov/16680933/) | 2006 | RCT | Ann Allergy Asthma Immunol | Difenidramina vs. desloratadina e placebo em rinite alérgica sazonal moderada a grave |
| [10691585](https://pubmed.ncbi.nlm.nih.gov/10691585/) | 2000 | RCT | Ann Intern Med | Fexofenadina, difenidramina e álcool sobre o desempenho ao dirigir em simulador; anti-histamínicos sedativos podem prejudicar a direção tanto quanto o álcool |
| [14582817](https://pubmed.ncbi.nlm.nih.gov/14582817/) | 2003 | RCT | Ann Allergy Asthma Immunol | Difenidramina vs. desloratadina sobre vigilância e função cognitiva na rinite alérgica por ambrósia |
| [8634878](https://pubmed.ncbi.nlm.nih.gov/8634878/) | 1996 | RCT | Ann Allergy Asthma Immunol | Efeitos de Semprex-D e difenidramina sobre o aprendizado na rinite alérgica sazonal |
| [36420548](https://pubmed.ncbi.nlm.nih.gov/36420548/) | 2022 | Estudo piloto | Tokai J Exp Clin Med | Aplicação transdérmica de difenidramina na asa nasal em rinite alérgica e asma |
| [31582993](https://pubmed.ncbi.nlm.nih.gov/31582993/) | 2019 | Posicionamento | Allergy Asthma Clin Immunol | A CSACI recomenda anti-histamínicos de nova geração como primeira linha, por serem mais seguros que os de primeira geração |
| [12113226](https://pubmed.ncbi.nlm.nih.gov/12113226/) | 2002 | Revisão | Clin Allergy Immunol | Anti-histamínicos H1 são úteis na rinoconjuntivite alérgica em crianças; uso em infecções respiratórias não tem forte respaldo |
| [12743547](https://pubmed.ncbi.nlm.nih.gov/12743547/) | 2003 | Consenso de especialistas | J Allergy Clin Immunol | Manejo do comprometimento causado por anti-histamínicos na rinite alérgica |
| [16278258](https://pubmed.ncbi.nlm.nih.gov/16278258/) | 2005 | Revisão | Ann Pharmacother | Eficácia e segurança de anti-histamínicos de primeira e nova geração em rinite alérgica e urticária crônica idiopática |
| [40152721](https://pubmed.ncbi.nlm.nih.gov/40152721/) | 2025 | Revisão | Med Lett Drugs Ther | Tratamento de rinite e conjuntivite alérgicas |

Literatura de outras indicações previstas (destaques):

| PMID | Ano | Tipo | Indicação | Principais Achados |
|------|-----|------|------|---------|
| [34862952](https://pubmed.ncbi.nlm.nih.gov/34862952/) | 2022 | Revisão | Urticária alérgica | O papel da cetirizina IV frente à difenidramina IV, único anti-histamínico IV de primeira geração ainda aprovado nos EUA |
| [40717751](https://pubmed.ncbi.nlm.nih.gov/40717751/) | 2025 | Revisão | Urticária alérgica | Aplicações clínicas e perfil de efeitos adversos da difenidramina |
| [475987](https://pubmed.ncbi.nlm.nih.gov/475987/) | 1979 | Relato clínico | Urticária ao frio | Em um único paciente, os antagonistas H1 suprimiram a formação de vergões |
| [17560664](https://pubmed.ncbi.nlm.nih.gov/17560664/) | 2007 | RCT (combinação) | Nasofaringite | Paracetamol vs. combinação anti-histamínico + descongestionante + paracetamol em crianças; não isola a difenidramina |
| [14909468](https://pubmed.ncbi.nlm.nih.gov/14909468/) | 1952 | Relato histórico | Cefaleia autonômica trigeminal | Benadryl na cefaleia histamínica; evidência histórica e anedótica |
| [23494529](https://pubmed.ncbi.nlm.nih.gov/23494529/) | 2013 | Pré-clínico (animal) | Neuralgia | A histamina modula a dor neuropática espontânea após axotomia; vínculo especulativo |

## Informações de Comercialização no Brasil

Todos os 6 registros estão **cancelados**; não há produto vigente com difenidramina isolada.

| Número de Registro | Nome Comercial | Forma Farmacêutica | Indicação Aprovada |
|---------|------|------|-----------|
| Registro nº 102980170 | Difenidrin | Não informada | Anti-histamínicos sistêmicos |
| Registro nº 101180653 | Lenix | Não informada | Antieméticos e antinauseantes |
| Registro nº 102350421 | Endcoff | Não informada | Antitussígenos |
| Registro nº 157211204 | Benalet | Não informada | Antitussígenos - associações medicamentosas |
| Registro nº 155840134 | Calamyn | Não informada | Antialérgicos tópicos |

(Há ainda o registro nº 115600099, Benatux, para produtos de orofaringe, também cancelado.)

## Considerações de Segurança

- **Interações medicamentosas:** foram identificadas 100 interações; as de maior gravidade são **Major**, com **citrato de potássio** e **eliglustate**. As demais listadas são de gravidade Moderate, em geral com anticolinérgicos e depressores do SNC, como hiosciamina, atropina, glicopirrônio, diciclomina, clidínio, mepenzolato, metescopolamina, loperamida, morfina, bupropiona, lorcaserina, dronabinol, nabilona, eluxadoline, metoclopramida e fenilbutirato de glicerol.
- **Riscos observados na literatura:** sedação, comprometimento cognitivo e psicomotor (incluindo direção), carga anticolinérgica e preferência por anti-histamínicos de segunda geração, sobretudo em crianças e idosos. Também há preocupação com toxicidade em doses altas ou na administração IV rápida.

Para advertências e contraindicações formais, consulte a bula.

## Conclusão e Próximos Passos

**Decisão: Proceed with Guardrails (rinite); Hold (conjuntivite da rosácea, a primeira do ranking)**

**Justificativa:**
- A rinite tem ensaios e RCTs concluídos (incluindo um estudo de fase 4 com 1021 participantes), mas é um uso já estabelecido da classe, não um reposicionamento novo, e as diretrizes preferem anti-histamínicos de segunda geração.
- A conjuntivite da rosácea, de maior pontuação, tem apenas previsão do modelo (L5), sem mecanismo plausível nem estudos, e por isso fica em *Hold*.

**Outras candidatas:**
- Urticária alérgica (L3, *Proceed with Guardrails*): a evidência direta é limitada a dados de comparador.
- Urticária ao frio e cefaleia autonômica trigeminal (L4, *Research Question*): evidência apenas histórica, de relatos de caso ou narrativa.
- Nasofaringite e neuralgia (L4, *Hold*): sem evidência direta sobre a difenidramina.
- Síndrome da cauda equina, conjuntivite viral e glossodinia (L5, *Hold*): somente previsão do modelo.

**Para prosseguir, é necessário:**
- Obter e analisar a bula na ANVISA para advertências e contraindicações, hoje ausentes.
- Obter dados do mecanismo de ação (por exemplo, via DrugBank).
- Considerar que não há registro vigente no Brasil: avaliar a viabilidade regulatória e as formas farmacêuticas e vias de administração antes de qualquer desenvolvimento.
- Para a rinite, comparar com anti-histamínicos de segunda geração e definir restrições por população (crianças, idosos).
- Para as candidatas L4/L5, gerar evidência clínica direta antes de qualquer avanço.
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

