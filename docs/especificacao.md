# Especificação do Trabalho

Resumo da especificação do projeto da disciplina de Teoria da Computação.

## Dados Gerais

- Disciplina: Teoria da Computação
- Professor: Daniel Bezerra
- Tema: Teoria da Complexidade e Análise de Tempo de Algoritmos
- Algoritmo do grupo: Quick Sort
- Linguagens escolhidas: C e Python
- Entrega do projeto: 16/06/2026
- Apresentação: 17/06/2026

## Grupo

- Caio Fonseca
- Gabriel Belo
- Jarbas Esteves

## Entregáveis

- Slides da apresentação.
- PDF do relatório.
- Link do GitHub na entrega do Classroom ou em uma seção do relatório.

## Itens Obrigatórios da Análise

- Descrição do algoritmo: problema resolvido, lógica geral e pseudocódigo.
- Classificação assintótica: Big-O, Big-Omega e Big-Theta.
- Discussão sobre aplicabilidade: contextos de eficiência e limitações.
- Simulação com dados: entrada pequena, média e grande.
- Gráficos e tabelas: comparação entre tempos medidos, complexidade teórica e desempenho entre linguagens.
- Análise de casos: melhor caso, pior caso e caso médio.
- Reflexão final: classe P, versão NP e problemas semelhantes NP-completos.

## Metodologia Experimental

- Descrever o hardware utilizado: processador, memória RAM e sistema operacional.
- Fechar programas em segundo plano durante os testes.
- Usar funções de alta precisão para medir tempo.
- Executar 30 rodadas por tamanho de entrada e por caso.
- Repetir as 30 rodadas para entradas pequena, média e grande.
- Repetir os testes nas duas linguagens escolhidas.

## Cenários de Teste

| Cenário | Descrição | Rodadas por tamanho |
| --- | --- | --- |
| Melhor caso | Entrada que favorece a lógica do algoritmo | 30 |
| Caso médio | Entrada aleatória ou típica | 30 |
| Pior caso | Entrada que força o maior número de operações | 30 |

## Gráficos

- Eixo X: tamanho da entrada `n`.
- Eixo Y: tempo de execução.
- Plotar a curva da complexidade teórica esperada sobre os dados reais.
- Usar escala logarítmica quando necessário.
