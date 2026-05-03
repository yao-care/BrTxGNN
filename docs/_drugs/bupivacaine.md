---
layout: default
title: Bupivacaine
parent: 僅模型預測 (L5)
nav_order: 140
evidence_level: L5
indication_count: 4
---

# Bupivacaine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Bupivacaína: Da Anestesia Regional à Acrodermatite Crónica Atrófica

## Resumo em Uma Frase

Bupivacaína é um anestésico local de longa duração da classe das amidas, amplamente utilizado em bloqueios de nervos periféricos, anestesia epidural e analgesia regional. O modelo TxGNN prevê que pode ser eficaz para **Acrodermatite Crónica Atrófica (Acrodermatitis chronica atrophicans)**, com pontuação de 99,23%, porém **sem ensaios clínicos** e **sem publicações** específicas apoiando esta direção — a previsão baseia-se exclusivamente no modelo de IA, sem respaldo empírico disponível.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Anestesia regional e bloqueio de nervos periféricos |
| Nova Indicação Prevista | Acrodermatite Crónica Atrófica (*Acrodermatitis chronica atrophicans*) |
| Pontuação de Previsão TxGNN | 99,23% |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | Não comercializado |
| Número de Registros | 0 |
| Decisão Recomendada | Hold |

---

## Por que Esta Previsão é Razoável?

Bupivacaína é um anestésico local da classe das amidas que atua bloqueando os canais de sódio voltagem-dependentes (Nav1.x), impedindo a geração e propagação de impulsos nervosos. É reconhecida pela sua longa duração de ação em comparação com outros anestésicos locais. Embora o MOA detalhado não esteja disponível neste Evidence Pack (Data Gap DG002), o perfil farmacológico geral do fármaco é bem estabelecido na literatura médica.

Além do efeito anestésico primário, estudos in vitro mostram que a bupivacaína possui propriedades imunomoduladoras não específicas: inibe a quimiotaxia de neutrófilos, reduz a produção de citocinas pró-inflamatórias (IL-6, TNF-α) e suprime a ativação da via NF-κB. A acrodermatite crónica atrófica (ACA) é uma manifestação cutânea tardia da doença de Lyme (terceira fase), caracterizada por inflamação crônica local persistente na pele das extremidades.

O raciocínio mecanístico do TxGNN seria que os efeitos anti-inflamatórios locais da bupivacaína poderiam, em tese, modular a resposta inflamatória crônica da ACA. Contudo, a causa primária da ACA é a persistência de *Borrelia burgdorferi* no tecido cutâneo, e a bupivacaína **não possui atividade antibacteriana contra espiroquetas**. Sem eliminar o agente causal, a modulação inflamatória isolada não seria suficiente para tratar a doença. A associação representa uma inferência distal do grafo de conhecimento, com relevância mecanística muito limitada.

---

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados.

---

## Evidências da Literatura

Atualmente não há literatura relacionada.

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
Apesar da pontuação elevada do TxGNN (99,23%), não existe nenhuma evidência clínica ou pré-clínica publicada que sustente o uso de bupivacaína para acrodermatite crónica atrófica. O mecanismo proposto é biologicamente implausível para tratar a causa primária da doença, que é de natureza infecciosa, e a bupivacaína carece completamente de atividade antimicrobiana.

**Para prosseguir, é necessário:**
- Obter dados de segurança da bula oficial (corrigir Data Gap DG001 via ANVISA)
- Confirmar o MOA detalhado via consulta ao DrugBank API (corrigir Data Gap DG002)
- Identificar estudos pré-clínicos que demonstrem algum efeito sobre *B. burgdorferi* ou sobre a inflamação tecidual específica da ACA
- Verificar diretamente na ANVISA se há registros de bupivacaína no Brasil não capturados por este Evidence Pack
- Caso avanços pré-clínicos sejam identificados, reclassificar para L4 e reavaliar a decisão
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

