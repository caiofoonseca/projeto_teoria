# Projeto de Teoria da Computacao

Repositorio do trabalho de Teoria da Computacao desenvolvido pelo grupo:

- Caio Fonseca
- Gabriel Belo
- Jarbas Esteves

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
| `src/python/quicksort.py` | Implementacao do Quick Sort em Python. |
| `src/c/benchmark.c` | Benchmark do Quick Sort em C. |
| `src/python/benchmark.py` | Benchmark do Quick Sort em Python. |
| `scripts/run_tests.py` | Script em Python para compilar e testar o programa em C. |
| `scripts/run_benchmarks.py` | Executa os benchmarks e salva os resultados em CSV. |
| `scripts/generate_plots.py` | Gera graficos a partir dos resultados. |
| `examples/entrada.txt` | Exemplo de entrada. |
| `examples/saida.txt` | Saida esperada para o exemplo. |
| `docs/especificacao.md` | Resumo da especificacao completa do trabalho. |
| `docs/checklist_avaliacao.md` | Checklist dos requisitos para nota maxima. |
| `docs/relatorio.md` | Base do relatorio final. |
| `data/resultados.csv` | Resultados experimentais coletados. |
| `plots/` | Graficos gerados a partir dos resultados. |

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

Execucao usando o exemplo em Bash, Git Bash ou MSYS2:

```bash
./build/quicksort < examples/entrada.txt
```

No Windows, o executavel pode ficar como `build/quicksort.exe`.

Execucao usando o exemplo no PowerShell:

```powershell
Get-Content examples/entrada.txt | .\build\quicksort.exe
```

Execucao da versao em Python:

```bash
python src/python/quicksort.py < examples/entrada.txt
```

No PowerShell, a versao Python tambem pode ser executada assim:

```powershell
Get-Content examples/entrada.txt | python src/python/quicksort.py
```

## Como Rodar os Testes

```bash
python scripts/run_tests.py
```

O script executa os testes da versao em Python e tambem compila/testa a versao em C quando `gcc` esta instalado.

Caso o comando informe que `gcc` nao foi encontrado, sera necessario instalar um compilador C antes de rodar a validacao automatica.

## Como Rodar os Experimentos

Para gerar os dados experimentais exigidos na especificacao:

```bash
python scripts/run_benchmarks.py
```

O resultado sera salvo em:

```text
data/resultados.csv
```

Para gerar os graficos:

```bash
python scripts/generate_plots.py
```

Esse comando depende da biblioteca `matplotlib`.

Os graficos gerados ficam em:

```text
plots/quicksort_c.png
plots/quicksort_python.png
```

## Observacao sobre Arquivos de Entrada e Saida

A especificacao do projeto nao obriga, por si so, que o programa leia um arquivo chamado `entrada.txt` ou gere um arquivo chamado `saida.txt`.

Neste repositorio, os arquivos em `examples/` servem como exemplos de execucao e validacao. O programa le pela entrada padrao, entao o usuario pode digitar os dados manualmente ou redirecionar um arquivo.

Em Bash, Git Bash ou MSYS2:

```bash
./build/quicksort < examples/entrada.txt
```

Em PowerShell:

```powershell
Get-Content examples/entrada.txt | .\build\quicksort.exe
```

## Proximos Passos

- Ler e interpretar o arquivo de especificacoes do trabalho.
- Executar os benchmarks no computador usado na analise final.
- Preencher o ambiente de execucao no relatorio.
- Gerar tabelas e graficos finais.
- Exportar o relatorio para PDF.
- Preparar os slides da apresentacao.

## Repositorio

Este projeto sera versionado no GitHub:

<https://github.com/caiofoonseca/projeto_teoria.git>
