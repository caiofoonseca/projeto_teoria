# Projeto de Teoria da Computacao

Repositorio do trabalho de Teoria da Computacao desenvolvido pelo grupo:

- Caio Fonseca
- Gabriel Belo
- Jarbas Esteves

## Tema

O projeto tera como base o algoritmo **Quick Sort**, um algoritmo de ordenacao eficiente que utiliza a estratégia de divisão e conquista.

## Algoritmo Escolhido: Quick Sort

O Quick Sort funciona escolhendo um elemento como pivô e reorganizando os demais elementos de forma que:

- elementos menores ou iguais ao pivô fiquem antes dele;
- elementos maiores fiquem depois dele;
- o mesmo processo seja aplicado recursivamente as sublistas geradas.

Em média, o Quick Sort possui complexidade de tempo `O(n log n)`, mas pode chegar a `O(n^2)` no pior caso, dependendo da escolha do pivô e da organização inicial dos dados.

## Objetivo do Projeto

Implementar e analisar o funcionamento do Quick Sort conforme as especificações do trabalho, relacionando a implementacao com os conceitos estudados em Teoria da Computação.

## Linguagens

O projeto usa:

- **C** para a implementação principal do Quick Sort.
- **Python** para automatizar testes e facilitar a validação dos resultados.

## Estrutura do Projeto

| Caminho | Descricao |
| --- | --- |
| `src/c/quicksort.c` | Implementação do Quick Sort em C. |
| `src/python/quicksort.py` | Implementação do Quick Sort em Python. |
| `src/c/benchmark.c` | Benchmark do Quick Sort em C. |
| `src/python/benchmark.py` | Benchmark do Quick Sort em Python. |
| `scripts/run_tests.py` | Script em Python para compilar e testar o programa em C. |
| `scripts/run_benchmarks.py` | Executa os benchmarks e salva os resultados em CSV. |
| `scripts/generate_plots.py` | Gera gráficos a partir dos resultados. |
| `examples/entrada.txt` | Exemplo de entrada. |
| `examples/saida.txt` | Saida esperada para o exemplo. |
| `docs/especificacao.md` | Resumo da especificação completa do trabalho. |
| `docs/checklist_avaliacao.md` | Checklist dos requisitos para nota máxima. |
| `docs/relatorio.md` | Base do relatorio final. |
| `data/resultados.csv` | Resultados experimentais coletados. |
| `plots/` | Gráficos gerados a partir dos resultados. |

## Formato de Entrada

O programa em C espera:

1. Um número inteiro `n`, indicando a quantidade de elementos.
2. `n` números inteiros que serão ordenados.

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

Compilação manual:

```bash
mkdir build
gcc src/c/quicksort.c -Wall -Wextra -std=c11 -o build/quicksort
```

Execução usando o exemplo em Bash, Git Bash ou MSYS2:

```bash
./build/quicksort < examples/entrada.txt
```

No Windows, o executável pode ficar como `build/quicksort.exe`.

Execução usando o exemplo no PowerShell:

```powershell
Get-Content examples/entrada.txt | .\build\quicksort.exe
```

Execução da versao em Python:

```bash
python src/python/quicksort.py < examples/entrada.txt
```

No PowerShell, a versao Python também pode ser executada assim:

```powershell
Get-Content examples/entrada.txt | python src/python/quicksort.py
```

## Como Rodar os Testes

```bash
python scripts/run_tests.py
```

O script executa os testes da versao em Python e tambem compila/testa a versao em C quando `gcc` esta instalado.

Caso o comando informe que `gcc` nao foi encontrado, sera necessário instalar um compilador C antes de rodar a validação automática.

## Como Rodar os Experimentos

Para gerar os dados experimentais exigidos na especificação:

```bash
python scripts/run_benchmarks.py
```

O resultado será salvo em:

```text
data/resultados.csv
```

Para gerar os gráficos:

```bash
python scripts/generate_plots.py
```

Esse comando depende da biblioteca `matplotlib`.

Os gráficos gerados ficam em:

```text
plots/quicksort_c.png
plots/quicksort_python.png
```

## Observacao sobre Arquivos de Entrada e Saida

A especificação do projeto nao obriga, por si so, que o programa leia um arquivo chamado `entrada.txt` ou gere um arquivo chamado `saida.txt`.

Neste repositorio, os arquivos em `examples/` servem como exemplos de execução e validação. O programa lê pela entrada padrão, então o usuário pode digitar os dados manualmente ou redirecionar um arquivo.

Em Bash, Git Bash ou MSYS2:

```bash
./build/quicksort < examples/entrada.txt
```

Em PowerShell:

```powershell
Get-Content examples/entrada.txt | .\build\quicksort.exe
```
