---
layout: default
title: Darunavir
parent: 僅模型預測 (L5)
nav_order: 211
evidence_level: L5
indication_count: 4
---

# Darunavir
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

A seguir, o relatório gerado a partir do Evidence Pack fornecido:

---

# Darunavir: Do HIV-1 à Síndrome de Imunodeficiência Adquirida Felina

## Resumo em Uma Frase

Darunavir é um inibidor de protease antirretroviral originalmente desenvolvido para o tratamento da infecção por HIV-1 em adultos e pacientes pediátricos. O modelo TxGNN prevê que pode ser eficaz para a **Síndrome de Imunodeficiência Adquirida Felina (Feline Acquired Immunodeficiency Syndrome / FIV)**, com **1 ensaio clínico identificado** — porém reclassificado como não relevante por erro de mapeamento — e **nenhuma publicação direta** apoiando esta aplicação em felinos, situando a hipótese como mecanisticamente plausível, mas ainda sem respaldo empírico específico.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Infecção por HIV-1 (inibidor de protease antirretroviral) |
| Nova Indicação Prevista | Síndrome de Imunodeficiência Adquirida Felina (Feline AID / FIV) |
| Pontuação de Previsão TxGNN | 99,97% |
| Nível de Evidência | L4 |
| Situação no Mercado Brasileiro | ✓ Comercializado |
| Número de Registros | 6 |
| Decisão Recomendada | Hold |

---

## Por que Esta Previsão é Razoável?

Os dados detalhados de mecanismo de ação não estão disponíveis no Evidence Pack atual. Com base no conhecimento publicado, o darunavir é um inibidor de protease de segunda geração que atua bloqueando a enzima protease viral do HIV-1 — essencial para a clivagem das poliproteínas precursoras e a maturação das partículas virais infecciosas. Seu perfil de inibição é mais robusto que inibidores de primeira geração, com menor propensão ao desenvolvimento de resistência.

O FIV (vírus da imunodeficiência felina) e o HIV-1 pertencem ambos à família *Lentivirus*, compartilhando homologia estrutural relevante na protease viral. Estudos de bioquímica estrutural demonstraram que alguns inibidores de protease desenvolvidos para HIV apresentam atividade cruzada in vitro sobre a protease do FIV, o que justifica biologicamente a conexão feita pelo grafo de conhecimento TxGNN. A elevada pontuação do modelo (99,97%) reflete essa proximidade vetorial entre os nós de HIV e FIV.

Contudo, a analogia tem limitações importantes: os sítios de ligação da protease diferem de forma significativa entre HIV-1 e FIV, e o darunavir foi otimizado especificamente para a conformação do HIV-1. A ausência de qualquer estudo publicado específico para felinos e o fato de o único ensaio clínico identificado ser um caso de mapeamento incorreto (ensaio humano de HIV) reduzem substancialmente a confiança na previsão. O alto score do TxGNN é provavelmente resultado do efeito de vizinhança vetorial (agrupamento de doenças lentivirais no grafo), e não de uma conexão mecanística direta bem estabelecida.

---

## Evidências de Ensaios Clínicos

> ⚠️ **Alerta de qualidade:** O ensaio abaixo foi identificado pela busca automatizada, mas classificado como **Grau C — não relevante** após análise de pertinência. Trata-se de um estudo realizado em seres humanos com HIV-1, mapeado incorretamente para FIV pelo agrupamento de doenças lentivirais no grafo de conhecimento. **Não constitui evidência clínica para imunodeficiência felina.**

| Número do Ensaio | Fase | Status | Participantes | Principais Achados |
|---------|------|------|------|---------|
| [NCT02770508](https://clinicaltrials.gov/study/NCT02770508) | Phase 4 | Concluído | 145 | ⚠️ **Mapeamento incorreto.** Estudo em humanos HIV-1 naïve: darunavir/ritonavir + lamivudina vs. darunavir/ritonavir + tenofovir/emtricitabina ou tenofovir/lamivudina. Avalia esquema de dois fármacos (2-DR) versus três fármacos. Não é ensaio veterinário nem investiga FIV. |

---

## Informações de Comercialização no Brasil

O darunavir possui **6 registros ativos** no Brasil. Os detalhes individuais de cada registro (número de registro, nome comercial, forma farmacêutica e indicação aprovada) não estão disponíveis neste Evidence Pack devido a lacunas nos dados regulatórios coletados. Para informações completas e atualizadas, consulte diretamente o sistema **DATAVISA/ANVISA** em [consultas.anvisa.gov.br](https://consultas.anvisa.gov.br).

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
A homologia estrutural entre as proteases de FIV e HIV-1 oferece uma base mecanística plausível para a previsão, mas o único ensaio clínico identificado é um caso de mapeamento incorreto (estudo de HIV humano sem relação com felinos), e não há nenhuma publicação científica que avalie o uso de darunavir diretamente em FIV — tornando a base de evidências insuficiente para qualquer avanço clínico ou regulatório.

**Para prosseguir, é necessário:**
- Realizar busca direcionada em literatura veterinária especializada (ex.: *Journal of Feline Medicine and Surgery*, *Veterinary Immunology and Immunopathology*, *Antiviral Research*)
- Encomendar ou identificar estudos in vitro de atividade inibitória do darunavir sobre a protease do FIV (ensaios enzimáticos e de cultura celular)
- Complementar o mecanismo de ação (MOA) via consulta à API do DrugBank (DB01264) para análise de similaridade de sítio de ligação
- Obter o perfil farmacocinético do darunavir em espécie felina (biodisponibilidade oral, distribuição, metabolismo hepático e eliminação)
- Recuperar advertências, contraindicações e interações medicamentosas a partir da bula aprovada pela ANVISA (download do PDF no DATAVISA)
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

