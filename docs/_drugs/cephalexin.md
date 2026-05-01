---
layout: default
title: Cephalexin
parent: 僅模型預測 (L5)
nav_order: 184
evidence_level: L5
indication_count: 10
---

# Cephalexin
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

O skill `txgnn-pipeline` não tem instruções específicas para geração de relatórios — as instruções já estão completas no system prompt. Prossigo diretamente com o relatório.

---

# Cefalexina: Das infecções bacterianas à otite média crônica

## Resumo em Uma Frase

Cefalexina é uma cefalosporina de primeira geração utilizada no tratamento de infecções bacterianas como infecções de pele, do trato urinário e respiratório.
O modelo TxGNN prevê que pode ser eficaz para **Otite Média Crônica (Chronic Otitis Media)**, com **0 ensaios clínicos** registados e **20 publicações** apoiando essa direção.
Contudo, a maioria das publicações refere-se a outros antibióticos da classe cefalosporínica, e Cefalexina apresenta limitações de cobertura para os principais patógenos causadores da doença.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|----------|
| Indicação Original | Infecções bacterianas (nenhum registro ANVISA disponível para extração) |
| Nova Indicação Prevista | Otite Média Crônica (Chronic Otitis Media) |
| Pontuação de Previsão TxGNN | 98,55% |
| Nível de Evidência | L3 |
| Situação no Mercado Brasileiro | ✗ Não comercializado |
| Número de Registros | 0 |
| Decisão Recomendada | Hold |

---

## Por que Esta Previsão é Razoável?

Atualmente, não há dados formais sobre o mecanismo de ação disponíveis no banco de dados consultado. Com base no conhecimento farmacológico estabelecido, Cefalexina é uma cefalosporina de primeira geração que inibe a síntese da parede celular bacteriana ao se ligar às proteínas de ligação à penicilina (PBPs). Esse mecanismo bactericida é eficaz contra organismos gram-positivos frequentemente implicados na otite média crônica, como *Staphylococcus aureus* e *Streptococcus* spp.

A relação entre o uso original de Cefalexina em infecções bacterianas e a otite média crônica é direta: ambas são condições infecciosas bacterianas nas quais antibióticos beta-lactâmicos têm papel terapêutico reconhecido. Existe inclusive evidência clínica direta — um ensaio controlado duplo-cego de 1983 (PMID 6361325) demonstrou que Cefalexina produziu desfechos clínicos comparáveis a cefroxadina no tratamento da otite média supurativa aguda e de exacerbações da otite média supurativa crônica. Um estudo laboratorial de 1981 (PMID 6798820) avaliou diretamente Cefalexina em pacientes com otite média crônica, comparando a via oral com gotas auriculares.

Há, porém, uma limitação mecanística relevante: Cefalexina apresenta cobertura insuficiente para *Haemophilus influenzae* e *Moraxella catarrhalis*, dois dos patógenos mais prevalentes na otite média crônica. Isso restringe seu papel como opção de primeira linha, em comparação com alternativas de espectro mais amplo como amoxicilina-clavulanato, recomendadas pelas diretrizes clínicas atuais.

---

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados para Cefalexina na indicação de otite média crônica.

---

## Evidências da Literatura

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|-----------|-------------------|
| [6361325](https://pubmed.ncbi.nlm.nih.gov/6361325/) | 1983 | RCT (duplo-cego) | The Japanese Journal of Antibiotics | Ensaio duplo-cego comparando cefroxadina 250 mg 3×/dia vs. Cefalexina 250 mg 4×/dia em otite supurativa aguda e exacerbação aguda de otite supurativa crônica; eficácia clínica comparável entre os dois fármacos, sem diferença estatisticamente significativa |
| [6798820](https://pubmed.ncbi.nlm.nih.gov/6798820/) | 1981 | Laboratorial | Acta Oto-Laryngologica | Cefalexina oral vs. gotas auriculares em pacientes com otite média crônica (COM); a redução da contagem bacteriana foi maior com uso tópico do que oral, indicando melhor penetração local |
| [8177625](https://pubmed.ncbi.nlm.nih.gov/8177625/) | 1994 | Estudo Clínico | Pediatric Infectious Disease Journal | Estudo retrospectivo em 69 crianças com otite média supurativa crônica; 54% apresentavam flora mista aeróbica-anaeróbica; terapia eficaz contra anaeróbios (ex: metronidazol + cefalosporina) obteve resolução mais rápida do que monoterapia |
| [22737435](https://pubmed.ncbi.nlm.nih.gov/22737435/) | 2011 | Observacional/Laboratorial | Iranian Red Crescent Medical Journal | Perfil de microrganismos aeróbicos e padrão de susceptibilidade antimicrobiana em pacientes com CSOM no Irã; caracteriza os agentes causadores predominantes relevantes para seleção antibiótica |
| [11838568](https://pubmed.ncbi.nlm.nih.gov/11838568/) | 2001 | Revisão | Indian Journal of Pediatrics | Infecções do trato respiratório superior; otite média compõe 87,5% dos episódios de infecção respiratória superior; maioria de origem viral — antimicrobianos indicados apenas em complicações bacterianas |
| [7200999](https://pubmed.ncbi.nlm.nih.gov/7200999/) | 1982 | Farmacocinética | Journal of Infectious Diseases | Penetração de amoxicilina, cefaclor, eritromicina-sulfisoxazol e TMP-SMX no fluido do ouvido médio de 83 crianças com otite média serosa crônica; dados de referência para comparação com Cefalexina |
| [1920724](https://pubmed.ncbi.nlm.nih.gov/1920724/) | 1991 | Observacional | JAMA | Estudo bacteriológico da otite média aguda em adultos nos EUA; levanta dados sobre prevalência de *H. influenzae* como agente causador — um patógeno com cobertura limitada pela Cefalexina |
| [12017394](https://pubmed.ncbi.nlm.nih.gov/12017394/) | 2002 | Revisão | Clinical Therapeutics | Revisão de cefdinir, cefalosporina de geração avançada aprovada para otite média bacteriana aguda; contextualiza o espectro de cobertura superior de cefalosporinas mais recentes frente à Cefalexina de 1ª geração |
| [2685215](https://pubmed.ncbi.nlm.nih.gov/2685215/) | 1989 | Estudo Clínico | Nihon Jibiinkoka Gakkai Kaiho | Fatores associados à recuperação tardia de OME em crianças; culturas positivas em 30% dos casos; papel do tratamento antibiótico prolongado no manejo de crianças com patógenos respiratórios identificados |
| [15212560](https://pubmed.ncbi.nlm.nih.gov/15212560/) | 2004 | Revisão | Drugs | Revisão abrangente de cefdinir; atividade contra *H. influenzae*, *M. catarrhalis* e *S. pneumoniae* — os três principais patógenos da otite média — evidenciando lacuna da Cefalexina de 1ª geração nesses dois primeiros |

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
Embora exista uma base mecanística plausível e evidências históricas diretas de eficácia de Cefalexina em otite média supurativa (incluindo um RCT duplo-cego de 1983), a cobertura antimicrobiana insuficiente para *H. influenzae* e *M. catarrhalis*, a ausência de ensaios clínicos contemporâneos, a falta de registro na ANVISA e a indisponibilidade de dados de segurança formais impedem o avanço do reposicionamento neste momento.

**Para prosseguir, é necessário:**
- Obter dados formais de mecanismo de ação (MOA) via DrugBank API (gap de alta severidade)
- Levantar advertências e contraindicações via bula registrada (gap bloqueante)
- Verificar situação regulatória atual na ANVISA (o resultado "não comercializado" com 0 registros pode refletir limitação de consulta)
- Avaliar perfil de susceptibilidade dos patógenos prevalentes em CSOM na população brasileira frente à Cefalexina
- Caso haja interesse em prosseguir, desenhar ensaio clínico prospectivo comparativo — as únicas evidências diretas datam de 1970–1983 e não atendem aos padrões contemporâneos de evidência
---

