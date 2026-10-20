---
layout: default
title: Lidocaine
parent: Apenas Predição do Modelo (L5)
nav_order: 418
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Lidocaine: nova indicação prevista, Ceratoconjuntivite epitelial punctata (punctate epithelial keratoconj… (nível de evidência L5). Indicação original: Anestésicos locais"
monitor_inn: "Lidocaine"
predicted_indications: ["punctate epithelial keratoconjunctivitis", "papillary conjunctivitis", "rosacea conjunctivitis", "exposure keratitis", "atopic conjunctivitis", "conjunctival disorder", "nephrotic syndrome", "non-human animal disease", "sporadic idiopathic steroid-resistant nephrotic syndrome"]
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

# Lidocaína: De anestésico local à ceratoconjuntivite epitelial punctata

## Resumo em Uma Frase

A lidocaína é um anestésico local (bloqueador de canais de sódio), originalmente registrado na ANVISA como anestésico local.
O modelo TxGNN prevê que pode ser eficaz para **ceratoconjuntivite epitelial punctata (punctate epithelial keratoconjunctivitis)**, mas, até o momento, **não há ensaios clínicos nem publicações** que apoiem diretamente esta previsão: ela se baseia apenas na pontuação computacional.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Anestésicos locais |
| Nova Indicação Prevista | Ceratoconjuntivite epitelial punctata (punctate epithelial keratoconjunctivitis) |
| Pontuação de Previsão TxGNN | 99,99% |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | Somente registros cancelados |
| Número de Registros | 20 (todos cancelados) |
| Decisão Recomendada | Hold |

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação nos dados compilados para este relatório. Segundo informações conhecidas, a lidocaína é um bloqueador de canais de sódio com ação anestésica local, e sua eficácia como anestésico está bem estabelecida.

Mecanisticamente, a anestesia da superfície ocular poderia aliviar a dor associada à ceratoconjuntivite epitelial punctata. Trata-se, porém, de um efeito sintomático, e não modificador da doença. A pontuação TxGNN muito alta (0,9999) é uma previsão computacional, sem respaldo de ensaios ou literatura nesta condição.

**Outras indicações previstas (resumo):** a previsão de maior suporte é a de **distúrbio conjuntival** (nível L3), com dois ensaios clínicos e literatura sobre uso em cirurgia de pterígio, mas tratando-se de anestesia procedimental, que se sobrepõe ao uso original. A **conjuntivite atópica** (L4) tem apoio mecanístico indireto (via de sinalização nervosa). As demais previsões (conjuntivite papilar, conjuntivite rosácea, ceratite por exposição, síndrome nefrótica, doença animal não humana, tinea corporis, síndrome nefrótica esteroide-resistente) permanecem em L5, sem evidência de benefício. Na ceratite por exposição, anestésicos tópicos costumam ser desaconselhados por prejudicarem a cicatrização epitelial.

## Informações de Comercialização no Brasil

Todos os 20 registros estão cancelados; não há produto de lidocaína com registro válido nos dados compilados. Principais registros:

| Número de Registro | Nome Comercial | Forma Farmacêutica | Indicação Aprovada |
|---------|------|------|-----------|
| Registro 155840162 | LIDOGEL | Não informada | Anestésicos locais |
| Registro 104400188 | LIDIAL | Não informada | Anestésicos locais |
| Registro 105730589 | DERMOMAX | Não informada | Anestésicos |
| Registro 102980365 | XYLESTESIN ISOBÁRICO | Não informada | Medicamentos com ação no miocárdio |
| Registro 165070015 | Cloridrato de Lidocaína | Não informada | Anestésicos locais |

## Considerações de Segurança

- **Contraindicações segundo o grafo de conhecimento (não é texto de bula):** o grafo de conhecimento associa a lidocaína a contraindicações em doenças como hipertensão, insuficiência hepática, epilepsia, doença renal, cirrose, insuficiência adrenocortical, hipotireoidismo, glaucoma de ângulo aberto, osteoporose, transtornos psicóticos, infecções fúngicas e gastrite, entre outras. Devem ser verificadas na bula.
- **Interações medicamentosas (100 registradas):** entre as principais, a interação **Maior** com **bupropiona**; interações **Moderadas** com aprepitanto, cimetidina, morfina lipossomal, ácido obeticólico, polietilenoglicol (3350 com eletrólitos), ácido picossulfúrico e sulfato de sódio; interações Menores com dexametasona, canamicina, neomicina, omeprazol, estreptomicina e troglitazona.
- **Sinais de segurança na literatura:** metemoglobinemia em criança com síndrome nefrótica com uso tópico de lidocaína, benzocaína e cotrimoxazol (PMID 41995267); convulsões em macacos após ceftriaxona dissolvida em lidocaína 1% (PMID 19858165); efeitos neuropsiquiátricos e cardiológicos da lidocaína intravenosa (PMID 19250287); alteração da ligação a proteínas plasmáticas na doença renal (PMID 7037263).

Para as advertências e contraindicações oficiais, consulte a bula.

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
- Para a indicação principal prevista (ceratoconjuntivite epitelial punctata), não há ensaios clínicos nem literatura. A previsão é apenas computacional (L5), e todos os registros no Brasil estão cancelados.

**Para prosseguir, é necessário:**
- Obter e analisar a bula oficial da ANVISA (advertências e contraindicações), uma lacuna que impede a triagem de segurança.
- Obter dados do mecanismo de ação (por exemplo, via DrugBank).
- Realizar revisão da literatura e estudos pré-clínicos específicos para ceratoconjuntivite epitelial punctata, avaliando o risco de toxicidade epitelial corneana com anestésicos tópicos.
- Definir via de administração e formulação oftálmica, já que a compatibilidade de via ainda está pendente.
- Como alternativa, priorizar a linha de **distúrbio conjuntival** (L3) ou **conjuntivite atópica** (L4, hipótese neural), tratadas como questões de pesquisa.
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

