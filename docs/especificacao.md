# Especificacao do Trabalho

Resumo da especificacao do projeto da disciplina de Teoria da Computacao.

## Dados Gerais

- Disciplina: Teoria da Computacao
- Professor: Daniel Bezerra
- Tema: Teoria da Complexidade e Analise de Tempo de Algoritmos
- Algoritmo do grupo: Quick Sort
- Linguagens escolhidas: C e Python
- Entrega do projeto: 16/06/2026
- Apresentação: 17/06/2026

## Grupo

- Caio Fonseca
- Gabriel Belo
- Jarbas Esteves

## Entregaveis

- Slides da apresentacao.
- PDF do relatorio.
- Link do GitHub na entrega do Classroom ou em uma secao do relatorio.

## Itens Obrigatorios da Analise

- Descricao do algoritmo: problema resolvido, logica geral e pseudocodigo.
- Classificacao assintotica: Big-O, Big-Omega e Big-Theta.
- Discussao sobre aplicabilidade: contextos de eficiencia e limitacoes.
- Simulacao com dados: entrada pequena, media e grande.
- Graficos e tabelas: comparacao entre tempos medidos, complexidade teorica e desempenho entre linguagens.
- Analise de casos: melhor caso, pior caso e caso medio.
- Reflexao final: classe P, versao NP e problemas semelhantes NP-completos.

## Metodologia Experimental

- Descrever o hardware utilizado: processador, memoria RAM e sistema operacional.
- Fechar programas em segundo plano durante os testes.
- Usar funcoes de alta precisao para medir tempo.
- Executar 30 rodadas por tamanho de entrada e por caso.
- Repetir as 30 rodadas para entradas pequena, media e grande.
- Repetir os testes nas duas linguagens escolhidas.

## Cenarios de Teste

| Cenario | Descricao | Rodadas por tamanho |
| --- | --- | --- |
| Melhor caso | Entrada que favorece a logica do algoritmo | 30 |
| Caso medio | Entrada aleatoria ou tipica | 30 |
| Pior caso | Entrada que forca o maior numero de operacoes | 30 |

## Graficos

- Eixo X: tamanho da entrada `n`.
- Eixo Y: tempo de execucao.
- Plotar a curva da complexidade teorica esperada sobre os dados reais.
- Usar escala logaritmica quando necessario.
