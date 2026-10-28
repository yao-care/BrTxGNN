---
layout: default
title: Lidocaine
parent: Apenas Predição do Modelo (L5)
nav_order: 418
evidence_level: L5
indication_count: 10
monitor_inn: "Lidocaine"
predicted_indications: ["punctate epithelial keratoconjunctivitis", "papillary conjunctivitis", "rosacea conjunctivitis", "exposure keratitis", "atopic conjunctivitis", "conjunctival disorder", "nephrotic syndrome", "non-human animal disease", "tinea corporis", "sporadic idiopathic steroid-resistant nephrotic syndrome"]
last_modified_at: 2026-10-23
description: "Lidocaine: nova indicação prevista, Ceratoconjuntivite epitelial punctata (nível de evidência L5). Indicação original: Anestésicos locais"
---

# Lidocaine
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

## Lidocaína: De anestésico local para ceratoconjuntivite epitelial punctata
{: .text-alpha }

## Resumo em Uma Frase

A lidocaína é um anestésico local, registrado no Brasil com classificações como anestésicos locais e medicamentos com ação no miocárdio.
O modelo TxGNN prevê que pode ser eficaz para **ceratoconjuntivite epitelial punctata (punctate epithelial keratoconjunctivitis)**, mas **não há ensaios clínicos nem publicações** que sustentem essa previsão (apenas a previsão do modelo).

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Anestésicos locais |
| Nova Indicação Prevista | Ceratoconjuntivite epitelial punctata |
| Pontuação de Previsão TxGNN | 0,9999 |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | Comercializado (registros ativos: pelo menos 20) |
| Número de Registros | Pelo menos 20 (a lista pode estar incompleta) |
| Decisão Recomendada | Hold |

---

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação nos dados compilados para este relatório. Segundo informações conhecidas, a lidocaína é um bloqueador de canais de sódio com ação anestésica tópica, e sua eficácia como anestésico local está estabelecida.

Mecanisticamente, isso poderia aliviar a dor da superfície ocular. No entanto, não há evidência de que trate a ceratoconjuntivite subjacente. O uso prolongado de anestésicos tópicos pode, inclusive, lesar o epitélio da córnea, o que é uma preocupação de segurança em doenças epiteliais.

A pontuação elevada do TxGNN (0,9999) reflete uma previsão do modelo TxGNN (aprendizado profundo), sem confirmação em estudos reais. A relação entre a indicação original (anestesia) e a nova (doença inflamatória ocular) é, no máximo, sintomática.

### Outras indicações previstas (todas com evidência fraca)

| Posição | Doença prevista | Pontuação | Nível | Observação |
|---|---|---|---|---|
| 2 | Conjuntivite papilar | 0,9998 | L5 | Apenas previsão; benefício, se houver, seria sintomático |
| 3 | Conjuntivite da rosácea | 0,9992 | L5 | Apenas previsão; sem efeito conhecido sobre a disfunção das glândulas meibomianas |
| 4 | Ceratite de exposição | 0,9987 | L5 | Único artigo trata de ceratite em usuários de metanfetamina; anestésicos tópicos podem prejudicar a cicatrização da córnea |
| 5 | Conjuntivite atópica | 0,9986 | L5 | Estudos indiretos (mecanismo e reflexo neural), sem estudo direto de tratamento |
| 6 | Doença da conjuntiva | 0,9984 | L5 | Ensaios sobre anestesia em cirurgia, não tratamento da doença |
| 7 | Síndrome nefrótica | 0,9983 | L5 | Literatura trata de farmacocinética e segurança |
| 8 | Doença animal não humana | 0,9982 | L5 | Relato de convulsões em macacos; sinal de segurança |
| 9 | Tinea corporis | 0,9982 | L5 | Sem atividade antifúngica |
| 10 | Síndrome nefrótica esteroide-resistente idiopática esporádica | 0,9979 | L5 | Apenas previsão |

---

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados para a ceratoconjuntivite epitelial punctata.

---

## Evidências da Literatura

Atualmente não há literatura relacionada para a ceratoconjuntivite epitelial punctata.

---

## Informações de Comercialização no Brasil

Foram listados 20 registros válidos, todos de medicamentos de ingrediente único (lista possivelmente parcial). Os principais:

| Número de Registro | Nome Comercial | Forma Farmacêutica | Indicação Aprovada |
|---------|------|------|-----------|
| Registro nº 155840162 | LIDOGEL | Não informada | Anestésicos locais |
| Registro nº 104400188 | LIDIAL | Não informada | Anestésicos locais |
| Registro nº 105730589 | DERMOMAX | Não informada | Anestésicos |
| Registro nº 102980365 | XYLESTESIN ISOBÁRICO | Não informada | Medicamentos com ação no miocárdio |
| Registro nº 165070015 | CLORIDRATO DE LIDOCAÍNA | Não informada | Anestésicos locais |

---

## Considerações de Segurança

- **Contraindicações (relações registradas no grafo de conhecimento, não texto de bula):** hipertensão, insuficiência hepática, cirrose, epilepsia, doença renal, insuficiência adrenocortical, hipotireoidismo, glaucoma de ângulo aberto, ceratite por herpes simples, transtornos psicóticos, osteoporose, gastrite, entre outras.
- **Interações medicamentosas (100 registradas; principais):**
  - Maior gravidade: bupropiona (Major).
  - Moderadas: aprepitanto, cimetidina, morfina lipossomal, ácido obeticólico, polietilenoglicol com eletrólitos, picossulfato de sódio, sulfato de sódio.
  - Leves: dexametasona, canamicina, neomicina, omeprazol, estreptomicina, troglitazona.
- **Sinais de segurança na literatura:** efeitos neuropsiquiátricos e cardiológicos da lidocaína sistêmica; metemoglobinemia em criança com síndrome nefrótica; risco de dano ao epitélio corneano com anestésicos tópicos prolongados.

Consulte a bula para advertências e contraindicações formais, pois não estavam disponíveis nos dados compilados.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
- A previsão vem do modelo TxGNN (deep learning) e pode refletir semelhanças que o modelo aprendeu entre doenças relacionadas, não evidência biológica (L5), sem ensaios ou publicações sobre a ceratoconjuntivite epitelial punctata. O efeito esperado seria apenas sintomático, com risco potencial de toxicidade epitelial corneana.

**Para prosseguir, é necessário:**
- Obter e analisar a bula da ANVISA (advertências e contraindicações).
- Obter dados do mecanismo de ação a partir do DrugBank.
- Realizar estudos pré-clínicos ou clínicos que avaliem a lidocaína diretamente nessa doença, incluindo a segurança da superfície ocular.
- Definir a via de administração e a formulação oftálmica compatíveis.
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

