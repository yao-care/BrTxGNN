---
layout: default
title: Bacitracin
parent: Apenas Predição do Modelo (L5)
nav_order: 104
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Bacitracin: nova indicação prevista, Ceratoconjuntivite epitelial punctata (punctate epithelial keratoconj… (nível de evidência L5). Indicação original: Ceratite, ceratoconjuntivite e blefaroconjunti…"
monitor_inn: "Bacitracin"
predicted_indications: ["punctate epithelial keratoconjunctivitis", "exposure keratitis", "non-human animal disease", "otitis externa", "postinfectious vasculitis", "post-bacterial disorder", "infective urethral stricture", "post-infectious syndrome", "infection-related hemolytic uremic syndrome", "Chagas cardiomyopathy"]
---

# Bacitracin
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

# Bacitracina: Da ceratite à ceratoconjuntivite epitelial punctata

## Resumo em Uma Frase

A bacitracina é um antibiótico polipeptídico de uso tópico, originalmente utilizado em afecções oculares como ceratite, ceratoconjuntivite e blefaroconjuntivite.
O modelo TxGNN prevê que ela pode ser eficaz para a **Ceratoconjuntivite Epitelial Punctata (punctate epithelial keratoconjunctivitis)**, mas atualmente há **0 ensaios clínicos** e **0 publicações** apoiando esta direção específica.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Ceratite, ceratoconjuntivite e blefaroconjuntivite (conforme o grafo de conhecimento; não há texto de indicação de registro no Brasil) |
| Nova Indicação Prevista | Ceratoconjuntivite epitelial punctata (punctate epithelial keratoconjunctivitis) |
| Pontuação de Previsão TxGNN | 99,999% |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | Não comercializado |
| Número de Registros | 0 |
| Decisão Recomendada | Hold |

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação nos dados compilados para este relatório. Segundo informações conhecidas, a bacitracina é um antibiótico polipeptídico tópico que atua sobre bactérias Gram-positivas por meio da inibição da síntese da parede celular. Sua utilidade em infecções oculares superficiais é conhecida, e mecanisticamente ela poderia ser aplicável a quadros da mesma família.

A nova indicação prevista está próxima das indicações originais (ceratite e ceratoconjuntivite), de modo que a previsão do TxGNN é plausível como extensão dentro da mesma família de doenças. Contudo, a ceratoconjuntivite epitelial punctata costuma ser de origem viral (por exemplo, adenovírus) ou não infecciosa, situações em que um antibacteriano tem benefício limitado. Portanto, a pontuação elevada pode refletir mais a proximidade no grafo de conhecimento do que um mecanismo terapêutico comprovado.

Entre as demais previsões, a de **otite externa** é a única com alguma literatura (veja abaixo), mas fica fora do escopo da indicação principal avaliada neste relatório.

## Considerações sobre Outras Indicações Previstas

| Indicação prevista | Pontuação TxGNN | Nível | Comentário |
|------|------|------|------|
| Ceratite por exposição | 99,99% | L5 | Vínculo indireto (profilaxia de infecção secundária e veículo lubrificante); sem evidências |
| Otite externa | 99,97% | L4 | Há literatura, mas sobretudo com combinações de produtos; evidência específica da bacitracina é limitada |
| Doença animal não humana | 99,97% | L5 | Categoria inespecífica da ontologia, provável artefato do grafo; não perseguir |
| Vasculite pós-infecciosa, transtorno pós-bacteriano e síndrome pós-infecciosa | 99,96–99,97% | L5 | Sequelas imunomediadas; sem papel mecanístico claro |
| Estenose uretral infecciosa | 99,97% | L5 | Condição fibrótica; a bacitracina não tem ação antifibrótica |
| Síndrome hemolítico-urêmica associada a infecção | 99,96% | L5 | Desfavorável: antibióticos geralmente são evitados e a bacitracina é nefrotóxica se absorvida |
| Cardiomiopatia chagásica | 99,96% | L5 | Causada por protozoário; sem atividade antiprotozoária conhecida |

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados.

## Evidências da Literatura

Atualmente não há literatura relacionada para a ceratoconjuntivite epitelial punctata.

Para referência, a literatura disponível na indicação prevista de otite externa (não é a indicação principal deste relatório):

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [17503066](https://pubmed.ncbi.nlm.nih.gov/17503066/) | 2007 | Estudo clínico comparativo (duplo-cego, 151 pacientes) | Eur Arch Otorhinolaryngol | Pomada de polimixina B + bacitracina isolada versus associada a acetato de hidrocortisona na otite externa bacteriana aguda; avalia a contribuição do corticoide |
| [9820118](https://pubmed.ncbi.nlm.nih.gov/9820118/) | 1998 | Estudo in vitro (veterinário) | Zentralbl Veterinarmed B | Suscetibilidade a 20 antibióticos de 46 cepas isoladas de otite externa canina crônica; resistência aumentada em relação ao relatado antes |
| [14055264](https://pubmed.ncbi.nlm.nih.gov/14055264/) | 1963 | Artigo de prática clínica/revisão | Md State Med J | Tratamento prático da otite externa (sem resumo disponível) |
| [14048629](https://pubmed.ncbi.nlm.nih.gov/14048629/) | 1963 | Relato clínico histórico (produto combinado) | Z Laryngol Rhinol Otol | Tratamento local de processos inflamatórios e secretores do ouvido com bastões de Nebacetin (sem resumo disponível) |

## Considerações de Segurança

- **Contraindicações no grafo de conhecimento** (não provenientes de bula): o grafo associa o fármaco a contraindicações em condições como doença renal, doença hepática, epilepsia, diabetes, cetoacidose diabética, miastenia gravis e doenças da junção neuromuscular, insuficiência respiratória, bloqueio atrioventricular, doença vascular periférica, glaucoma de ângulo aberto e hipertensão ocular, ceratite por herpes simplex, infecções oculares fúngicas e virais, conjuntivite, insuficiência adrenocortical/doença de Addison, atrofia da pele e telangiectasia. Esses dados devem ser verificados com a bula, pois alguns itens podem refletir outros fármacos ou classes.
- **Interações medicamentosas**: foram identificadas 84 interações, sendo as de gravidade **maior** com:
  - aminoglicosídeos: canamicina, neomicina e estreptomicina (risco aditivo de nefrotoxicidade e neurotoxicidade);
  - deferasirox;
  - contrastes iodados: diatrizoato, iodipamida, iodixanol e ioexol.
- Interações de gravidade **moderada** incluem mesalazina, balsalazida, olsalazina, sulfassalazina, exenatida, vancomicina e ácido picossulfúrico.
- A nefrotoxicidade da bacitracina em exposição sistêmica limita usos não tópicos.

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
- A previsão tem pontuação TxGNN muito alta, mas não há ensaios clínicos nem literatura que a sustentem (L5). Além disso, a doença é frequentemente viral ou não infecciosa, o que reduz o benefício esperado de um antibacteriano. O fármaco não está comercializado no Brasil.

**Para prosseguir, é necessário:**
- Obter e analisar a bula aprovada (advertências e contraindicações), pois a triagem de segurança está bloqueada por essa lacuna.
- Obter os dados do mecanismo de ação a partir do DrugBank.
- Revisar sistematicamente a literatura sobre a etiologia da ceratoconjuntivite epitelial punctata e o papel de antibacterianos tópicos.
- Verificar a viabilidade regulatória e de via de administração (formulação oftálmica) para o Brasil, já que não há registros vigentes.
- Se houver interesse em outra direção, avaliar otite externa como pergunta de pesquisa, com revisão da evidência específica da bacitracina separada dos produtos combinados.
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

