---
layout: default
title: Política de Privacidade
nav_order: 99
description: "Política de privacidade do BrTxGNN."
permalink: /privacy-policy/
---

# Política de Privacidade

**Última atualização**: 5 de novembro de 2026

---

## Visão Geral

O BrTxGNN (brtxgnn.yao.care) é um projeto de pesquisa de código aberto que fornece previsões de reposicionamento de medicamentos. Esta política descreve como tratamos informações.

---

## Dados Coletados

### Dados que NÃO Coletamos

- **Dados pessoais**: Não coletamos nomes, e-mails nem dados de cadastro (o site não tem contas nem formulários)
- **Dados de saúde**: Não coletamos informações médicas de usuários
- **Dados de pacientes**: O aplicativo SMART não envia a identidade do paciente nem os dados do prontuário aos servidores deste site (é um site estático, sem backend); para identificar os medicamentos, envia apenas os códigos RxNorm (sem identificadores do paciente) ao serviço RxNav da Biblioteca Nacional de Medicina dos EUA e, quando você solicita ensaios clínicos, os nomes do medicamento e da indicação ao ClinicalTrials.gov

### Dados de Acesso

O GitHub Pages pode registrar automaticamente:
- Endereços IP
- Informações do navegador
- Páginas visitadas

O GitHub trata esses registros conforme a própria política de privacidade.

Além disso, o site usa o Google Analytics 4, que coleta, por meio de cookies de análise definidos ao carregar a página, as páginas visitadas, o site de origem, a profundidade de rolagem e o tempo na página. Usamos esses dados apenas para estatísticas agregadas de acesso. Termos de busca, conteúdo de formulários e parâmetros da URL não são enviados.

---

## Uso de Dados

Os dados do BrTxGNN são:

1. **Públicos**: Todos os dados do projeto são de acesso público
2. **Para pesquisa**: Destinados exclusivamente a fins de pesquisa acadêmica
3. **Não comerciais**: Não vendemos ou comercializamos dados

---

## Terceiros

### GitHub Pages

O site é hospedado no GitHub Pages. Consulte a [Política de Privacidade do GitHub](https://docs.github.com/en/site-policy/privacy-policies/github-privacy-statement).

### Recursos de terceiros carregados pelas páginas

As páginas carregam os seguintes recursos de terceiros, que podem registrar os acessos conforme suas próprias políticas:

| Serviço | Finalidade | Política de privacidade |
|---------|---------|----------------|
| Google Analytics 4 (www.googletagmanager.com, google-analytics.com) | Estatísticas de visitas (páginas vistas, origem); usa cookies de análise. Termos de busca, conteúdo de formulários e parâmetros da URL não são enviados. | [Política de Privacidade do Google](https://policies.google.com/privacy) |
| cdn.jsdelivr.net | Bibliotecas de scripts: gráficos d3 em todas as páginas; Fuse.js para comparar nomes e o cliente SMART on FHIR nas páginas SMART | [Política de Privacidade do jsDelivr](https://www.jsdelivr.com/terms/privacy-policy-jsdelivr-net) |
| clinicaltrials.gov | Busca de ensaios clínicos nas páginas SMART: somente quando você solicita, os nomes do medicamento e da indicação são enviados à API do ClinicalTrials.gov | [Políticas web da NLM](https://www.nlm.nih.gov/web_policies.html) |
| rxnav.nlm.nih.gov | Aplicativo SMART: os códigos RxNorm dos medicamentos lidos do seu prontuário eletrônico são enviados à API RxNav da NLM para obter o nome do princípio ativo (sem identificadores do paciente) | [Políticas web da NLM](https://www.nlm.nih.gov/web_policies.html) |

### Fontes de Dados

Utilizamos dados públicos de:
- ANVISA (dados.anvisa.gov.br)
- ClinicalTrials.gov
- PubMed
- DrugBank

---

<!-- privacy-law:start（母目錄 .claude/gen_local_pages_20261119.py 產生，勿手改；法規與連結見 .claude/privacy_text_20261119.py）-->
## Legislação aplicável

Para visitantes no Brasil, a lei aplicável é a [Lei Geral de Proteção de Dados Pessoais (LGPD, Lei nº 13.709/2018)](https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm), fiscalizada pela [Autoridade Nacional de Proteção de Dados (ANPD)](https://www.gov.br/anpd/pt-br). Os únicos dados pessoais envolvidos são os dados de uso coletados pelo Google Analytics 4 por meio de cookies, tratados pelo Google fora do Brasil (transferência internacional, arts. 33 a 36).

## Seus direitos e como exercê-los

- Confirmação da existência de tratamento e acesso aos dados (art. 18, I e II).
- Correção de dados incompletos, inexatos ou desatualizados (art. 18, III).
- Eliminação dos dados e revogação do consentimento, por exemplo bloqueando os cookies (art. 18, VI e IX).
- Petição à ANPD (art. 18, § 1º).

Solicitações e dúvidas: service@yao.care. Como o site não tem contas, só podemos agir sobre os dados do Google Analytics se você fornecer detalhes suficientes (por exemplo, a data e as páginas da visita); você também pode bloquear ou apagar os cookies de análise no navegador.

## Direitos autorais e fontes de dados

Os textos do site são protegidos pela [Lei de Direitos Autorais (Lei nº 9.610/1998)](https://www.planalto.gov.br/ccivil_03/leis/l9610.htm). O código do site é publicado sob a licença MIT no [repositório do GitHub](https://github.com/yao-care/BrTxGNN); os textos dos relatórios são © 藥提醒科技有限公司 (yao.care).

Fontes de dados deste site e seus termos:

- Dados de previsão do **TxGNN** (Harvard Dataverse): dedicação ao domínio público CC0 1.0; cite Huang et al., *Nature Medicine* 2024.
- **ClinicalTrials.gov** e **PubMed**: Biblioteca Nacional de Medicina dos EUA; veja os [termos do ClinicalTrials.gov](https://clinicaltrials.gov/about-site/terms-conditions) e as [políticas do NCBI](https://www.ncbi.nlm.nih.gov/home/about/policies/) (alguns resumos do PubMed continuam protegidos pelo editor).
- Identificadores e dados do **DrugBank**: conforme os termos de licença do [DrugBank](https://go.drugbank.com/) (uso não comercial).
- **Conjunto de dados local**: [ANVISA: DADOS_ABERTOS_MEDICAMENTOS.csv](https://dados.anvisa.gov.br/dados/DADOS_ABERTOS_MEDICAMENTOS.csv), publicado por Agência Nacional de Vigilância Sanitária (ANVISA); a reutilização segue os termos do editor, e este site não concede direitos adicionais.

<!-- privacy-law:end -->

---

## Contato

Para questões sobre privacidade:

- **GitHub Issues**: [github.com/yao-care/BrTxGNN/issues](https://github.com/yao-care/BrTxGNN/issues)

---

## Alterações

Esta política pode ser atualizada. Alterações serão publicadas nesta página com a data de atualização.

---

## Isenção de Responsabilidade Médica

<div class="disclaimer">
O BrTxGNN fornece informações de pesquisa e <strong>não constitui aconselhamento médico</strong>. Consulte profissionais de saúde para decisões médicas.
</div>
