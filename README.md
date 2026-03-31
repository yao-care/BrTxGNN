# BrTxGNN - Brasil: Reposicionamento de Medicamentos

[![Website](https://img.shields.io/badge/Website-brtxgnn.yao.care-blue)](https://brtxgnn.yao.care)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Predicoes de reposicionamento de medicamentos (drug repurposing) para o Brasil utilizando o modelo TxGNN.

## Aviso Legal

- Os resultados deste projeto sao apenas para fins de pesquisa e nao constituem aconselhamento medico.
- Os candidatos a reposicionamento de medicamentos requerem validacao clinica antes da aplicacao.

## Visao Geral do Projeto

| Item | Quantidade |
|------|------------|
| **Relatorios de Medicamentos** | 256 |
| **Predicoes Totais** | 17,788,744 |

## Metodos de Predicao

### Metodo de Grafo de Conhecimento (Knowledge Graph)
Consulta direta de relacoes farmaco-doenca no grafo de conhecimento TxGNN, identificando candidatos potenciais para reposicionamento com base em conexoes existentes na rede biomedica.

### Metodo de Aprendizado Profundo (Deep Learning)
Utiliza o modelo de rede neural pre-treinado TxGNN para calcular pontuacoes de predicao, avaliando a probabilidade de novas indicacoes terapeuticas para medicamentos aprovados.

## Links

- Site: https://brtxgnn.yao.care
- Artigo TxGNN: https://doi.org/10.1038/s41591-023-02233-x
