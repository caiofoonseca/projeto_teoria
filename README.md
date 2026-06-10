# Projeto de Teoria da Computacao

Repositorio do trabalho de Teoria da Computacao desenvolvido pelo grupo:

- Caio Fonseca
- Eduardo Malheiros
- Gabriel Belo
- Jarbas

## Tema

O projeto tera como base o algoritmo **Quick Sort**, um algoritmo de ordenacao eficiente que utiliza a estrategia de divisao e conquista.

## Algoritmo Escolhido: Quick Sort

O Quick Sort funciona escolhendo um elemento como pivo e reorganizando os demais elementos de forma que:

- elementos menores ou iguais ao pivo fiquem antes dele;
- elementos maiores fiquem depois dele;
- o mesmo processo seja aplicado recursivamente as sublistas geradas.

Em media, o Quick Sort possui complexidade de tempo `O(n log n)`, mas pode chegar a `O(n^2)` no pior caso, dependendo da escolha do pivo e da organizacao inicial dos dados.

## Objetivo do Projeto

Implementar e analisar o funcionamento do Quick Sort conforme as especificacoes do trabalho, relacionando a implementacao com os conceitos estudados em Teoria da Computacao.

## Linguagens

O projeto usa:

- **C** para a implementacao principal do Quick Sort.
- **Python** para automatizar testes e facilitar a validacao dos resultados.

## Estrutura do Projeto

| Caminho | Descricao |
| --- | --- |
| `src/c/quicksort.c` | Implementacao do Quick Sort em C. |
| `scripts/run_tests.py` | Script em Python para compilar e testar o programa em C. |
| `examples/entrada.txt` | Exemplo de entrada. |
| `examples/saida.txt` | Saida esperada para o exemplo. |
| `docs/especificacao.md` | Espaco para registrar a especificacao completa do trabalho. |

## Formato de Entrada

O programa em C espera:

1. Um numero inteiro `n`, indicando a quantidade de elementos.
2. `n` numeros inteiros que serao ordenados.

Exemplo:

```text
6
8 3 1 7 0 10
```

Saida:

```text
0 1 3 7 8 10
```

## Como Compilar e Executar

Compilacao manual:

```bash
mkdir build
gcc src/c/quicksort.c -Wall -Wextra -std=c11 -o build/quicksort
```

Execucao usando o exemplo:

```bash
./build/quicksort < examples/entrada.txt
```

No Windows, o executavel pode ficar como `build/quicksort.exe`.

## Como Rodar os Testes

```bash
python scripts/run_tests.py
```

O script compila o codigo em C com `gcc` e executa alguns casos de teste.

Caso o comando informe que `gcc` nao foi encontrado, sera necessario instalar um compilador C antes de rodar a validacao automatica.

## Proximos Passos

- Ler e interpretar o arquivo de especificacoes do trabalho.
- Ajustar o projeto ao formato de entrada e saida exigido pelo professor.
- Adicionar comentarios teoricos sobre funcionamento, complexidade e casos do Quick Sort.
- Preparar exemplos para a apresentacao.
- Adicionar testes extras, se necessario.

## Repositorio

Este projeto sera versionado no GitHub:

<https://github.com/caiofoonseca/projeto_teoria.git>
