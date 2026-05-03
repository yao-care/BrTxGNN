---
layout: default
title: Megestrol Acetate
parent: 僅模型預測 (L5)
nav_order: 340
evidence_level: L5
indication_count: 10
---

# Megestrol Acetate
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

O skill `txgnn-pipeline` é focado em operações de pipeline e deploy multi-país — não altera o fluxo de escrita de relatório. Prossigo diretamente com a geração do relatório conforme as instruções do sistema.

---

# Megestrol Acetate: Da Caquexia Oncológica ao Carcinoma Endometrial do Corpo Uterino

## Resumo em Uma Frase

Megestrol acetate é um progestagênio sintético utilizado internacionalmente no tratamento do câncer de mama avançado, caquexia/anorexia associada ao câncer e, em vários países, no carcinoma endometrial — porém **sem registro ativo no Brasil**. O modelo TxGNN prevê que pode ser eficaz para **Carcinoma Endometrial do Corpo Uterino (Uterine Corpus Endometrial Carcinoma)**, com previsão de altíssima confiança suportada por **3 ensaios clínicos** — e o mecanismo de agonismo do receptor de progesterona (PR) fornece base mecanística diretamente compatível com esta indicação.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Não registrado no Brasil (uso internacional: câncer de mama avançado, caquexia oncológica, carcinoma endometrial) |
| Nova Indicação Prevista | Carcinoma Endometrial do Corpo Uterino (Uterine Corpus Endometrial Carcinoma) |
| Pontuação de Previsão TxGNN | 99.94% |
| Nível de Evidência | L2 |
| Situação no Mercado Brasileiro | ✗ Não comercializado |
| Número de Registros | 0 |
| Decisão Recomendada | Proceed with Guardrails |

---

## Por que Esta Previsão é Razoável?

Megestrol acetate é um progestagênio sintético de alta potência que atua como **agonista do receptor de progesterona (PR)**. Seu mecanismo antitumoral central envolve a ligação ao PR, resultando em downregulation da expressão do receptor de estrogênio α (ERα) e inibição direta da proliferação celular induzida pelo estradiol (E2). Adicionalmente, suprime a secreção hipofisária de LH e FSH, reduzindo indiretamente os níveis circulantes de estrogênio — o principal hormônio promotor do crescimento endometrial.

O carcinoma endometrial do corpo uterino, especialmente o subtipo endometrioide de baixo e médio grau, é um dos tumores mais frequentemente PR-positivos do sistema reprodutor feminino. Neste contexto, a terapia progestagênica representa o pilar do tratamento conservador com preservação de fertilidade e uma opção estabelecida para doença recorrente/metastática PR+. A compatibilidade mecanística é, portanto, direta e biologicamente sólida: o alvo molecular do fármaco (PR) está amplamente expresso no tumor-alvo.

É importante situar esta previsão no contexto regulatório: o megestrol acetate **já possui aprovação do FDA norte-americano** para o tratamento do carcinoma endometrial avançado, sendo utilizado há décadas em oncologia ginecológica. Para o Brasil, este resultado configura uma oportunidade de **introdução formal de uma indicação oncológica clinicamente madura**, sem a necessidade de construir evidências do zero — mas com a exigência de submissão regulatória à ANVISA.

---

## Evidências de Ensaios Clínicos

| Número do Ensaio | Fase | Status | Participantes | Principais Achados |
|---------|------|------|------|---------|
| [NCT00729586](https://clinicaltrials.gov/study/NCT00729586) | Phase 2 | Concluído | 73 | Temsirolimus com ou sem a combinação de megestrol acetate + tamoxifeno em carcinoma endometrial avançado, persistente ou recorrente — avalia se a adição de terapia hormonal potencializa a inibição de mTOR |
| [NCT00503581](https://clinicaltrials.gov/study/NCT00503581) | Phase 2 | Encerrado precocemente | 9 | Megestrol acetate em regime contínuo vs. sequencial para neoplasia intraepitelial endometrial (EIN) e hiperplasia endometrial atípica em pacientes que desejam preservar o útero — estrogênio pode estimular crescimento de células endometriais anômalas, e megestrol pode bloqueá-lo |
| [NCT04046185](https://clinicaltrials.gov/study/NCT04046185) | Early Phase 1 | Desconhecido | 60 | Inibidor de PD-1 combinado com progestagênio vs. progestagênio isolado em câncer endometrial inicial com preservação de fertilidade — evidência indireta do papel do progestagênio em regime combinado |

---

## Evidências da Literatura

Atualmente não há literatura relacionada indexada para esta indicação específica nos dados do Evidence Pack.

---

## Informações de Comercialização no Brasil

Megestrol acetate **não possui registro ativo na ANVISA**. Nenhum produto com esta substância ativa se encontra comercializado no Brasil. Não há histórico de licenças ou registros anteriores.

---

## Citotoxicidade

| Item | Conteúdo |
|------|------|
| Classificação de Citotoxicidade | Terapia hormonal — progestagênio sintético (não é citotóxico convencional; mecanismo antitumoral mediado por receptor hormonal) |
| Risco de Mielossupressão | Baixo (progestagênios não causam mielossupressão direta; sem efeito sobre células hematopoiéticas) |
| Classificação de Emetogenicidade | Baixa |
| Itens de Monitoramento | Peso corporal (ganho de peso frequente), pressão arterial, glicemia (risco de hiperglicemia), parâmetros de coagulação (risco tromboembólico), função adrenal (supressão adrenal secundária documentada com uso prolongado em doses altas) |
| Proteção no Manuseio | Precauções padrão de manipulação farmacêutica — não requer medidas especiais de citotóxico convencional |

---

## Considerações de Segurança

Consulte a bula aprovada internacionalmente (FDA/EMA) para informações completas de segurança, incluindo advertências, contraindicações e interações medicamentosas — esses dados não estão disponíveis no registro brasileiro (fármaco sem registro na ANVISA).

---

## Conclusão e Próximos Passos

**Decisão: Proceed with Guardrails**

**Justificativa:**
Megestrol acetate possui aprovação regulatória do FDA para carcinoma endometrial avançado, mecanismo de ação diretamente compatível com o tumor-alvo (agonismo do PR), e suporte de ensaio clínico Phase 2 concluído (NCT00729586, n=73). A principal barreira não é de evidência científica, mas de **acesso regulatório e comercial no Brasil**.

**Para prosseguir, é necessário:**
- Submissão de dossiê de registro à ANVISA (categoria de medicamento novo ou por equivalência a registro internacional existente)
- Obtenção e análise da bula completa FDA/EMA para mapeamento completo de advertências, contraindicações e interações medicamentosas
- Confirmação formal do mecanismo de ação completo via DrugBank (DG002) para suportar análise de DDI
- Avaliação de segurança específica para populações brasileiras, com foco em risco tromboembólico e supressão adrenal em uso prolongado
- Definição do regime de dosagem-alvo (doses altas de 160–800 mg/dia são usadas em oncologia; doses menores para outras indicações)
- Avaliação de viabilidade comercial considerando a ausência total de presença de mercado no Brasil
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

