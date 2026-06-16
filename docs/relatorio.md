# Relatorio - Quick Sort

## 1. Identificacao

- Disciplina: Teoria da Computacao
- Professor: Daniel Bezerra
- Grupo:
  - Caio Fonseca
  - Gabriel Belo
  - Jarbas Esteves
- Algoritmo analisado: Quick Sort
- Linguagens utilizadas: C e Python

## 2. Descricao do Algoritmo

O Quick Sort e um algoritmo de ordenacao baseado na estrategia de divisao e conquista. Ele escolhe um elemento chamado pivo, reorganiza a lista de modo que os menores elementos fiquem antes do pivo e os maiores fiquem depois, e repete o processo recursivamente nas sublistas geradas.

## 3. Problema Resolvido

O problema resolvido e a ordenacao de uma sequencia de numeros inteiros em ordem crescente.

## 4. Pseudocodigo

```text
QUICKSORT(vetor, inicio, fim)
    se inicio < fim entao
        pivo = PARTICIONAR(vetor, inicio, fim)
        QUICKSORT(vetor, inicio, pivo - 1)
        QUICKSORT(vetor, pivo + 1, fim)

PARTICIONAR(vetor, inicio, fim)
    pivo = vetor[fim]
    i = inicio - 1

    para j de inicio ate fim - 1 faca
        se vetor[j] <= pivo entao
            i = i + 1
            trocar vetor[i] com vetor[j]

    trocar vetor[i + 1] com vetor[fim]
    retornar i + 1
```

## 5. Analise de Complexidade

| Caso | Complexidade | Explicacao |
| --- | --- | --- |
| Melhor caso | Big-Omega: Omega(n log n) | O pivo divide o vetor em partes aproximadamente iguais. |
| Caso medio | Big-Theta: Theta(n log n) | Em entradas aleatorias, as particoes tendem a ser razoavelmente balanceadas. |
| Pior caso | Big-O: O(n^2) | O pivo gera particoes muito desbalanceadas, como pode ocorrer em vetor ja ordenado nesta implementacao. |

## 6. Aplicabilidade

O Quick Sort e eficiente para ordenacao em memoria principal, especialmente quando as particoes sao bem balanceadas. Suas principais limitacoes aparecem no pior caso, quando a escolha do pivo produz divisoes muito desiguais, e no uso de recursao, que pode aumentar o consumo de pilha.

## 7. Metodologia Experimental

Os experimentos devem ser executados com:

- 30 rodadas por cenario.
- Tres tamanhos de entrada: pequena, media e grande.
- Tres cenarios: melhor caso, caso medio e pior caso.
- As duas linguagens escolhidas: C e Python.
- Medicao de tempo com temporizadores de alta precisao.

## 8. Ambiente de Execucao

Ambiente usado na execucao dos experimentos registrados em `data/resultados.csv`:

- Computador: Dell Latitude 5511
- Arquitetura: PC baseado em x64
- Processador: Intel(R) Core(TM) i7-10850H CPU @ 2.70GHz
- Nucleos: 6
- Nucleos logicos informados pelo sistema: 12
- Memoria RAM instalada: 32,0 GB
- Memoria fisica total: 31,6 GB
- Sistema operacional: Microsoft Windows 10 Pro
- Versao do sistema operacional: 10.0.19045, compilacao 19045
- Compilador C: gcc.exe 16.1.0, MSYS2 UCRT64
- Python: 3.14.0
- Biblioteca de graficos: matplotlib 3.10.9

## 9. Resultados Experimentais

Os resultados foram gerados com:

```bash
python scripts/run_benchmarks.py
```

O arquivo gerado sera:

```text
data/resultados.csv
```

Resumo dos dados coletados:

| Linguagem | Caso | Tamanho | Rodadas | Media (ms) | Desvio-padrao (ms) |
| --- | --- | ---: | ---: | ---: | ---: |
| Python | melhor | 100 | 30 | 0.040343 | 0.009717 |
| Python | medio | 100 | 30 | 0.051723 | 0.004462 |
| Python | pior | 100 | 30 | 0.361187 | 0.035525 |
| Python | melhor | 1000 | 30 | 0.643863 | 0.011291 |
| Python | medio | 1000 | 30 | 0.979733 | 0.232886 |
| Python | pior | 1000 | 30 | 37.844777 | 1.124157 |
| Python | melhor | 3000 | 30 | 2.378267 | 0.112871 |
| Python | medio | 3000 | 30 | 3.219307 | 0.235365 |
| Python | pior | 3000 | 30 | 352.578220 | 9.665588 |
| C | melhor | 100 | 30 | 0.001833 | 0.000130 |
| C | medio | 100 | 30 | 0.006463 | 0.006439 |
| C | pior | 100 | 30 | 0.021747 | 0.000411 |
| C | melhor | 1000 | 30 | 0.027297 | 0.000234 |
| C | medio | 1000 | 30 | 0.070773 | 0.001708 |
| C | pior | 1000 | 30 | 2.507270 | 0.497418 |
| C | melhor | 3000 | 30 | 0.114330 | 0.006240 |
| C | medio | 3000 | 30 | 0.289300 | 0.010202 |
| C | pior | 3000 | 30 | 21.690007 | 0.795643 |

Os resultados mostram que a implementacao em C apresentou tempos menores em todos os cenarios. Tambem fica visivel que o pior caso cresce de forma muito mais acentuada, coerente com a complexidade O(n^2) da implementacao com pivo fixo no ultimo elemento.

## 10. Graficos

Os graficos podem ser gerados com:

```bash
python scripts/generate_plots.py
```

Os arquivos serao salvos em:

```text
plots/
```

Graficos gerados:

- `plots/quicksort_c.png`
- `plots/quicksort_python.png`

## 11. Reflexao sobre Classe P e NP

O problema de ordenacao pertence a classe P, pois existe algoritmo que resolve o problema em tempo polinomial. O Quick Sort, mesmo em seu pior caso, executa em O(n^2), que ainda e polinomial.

O problema de ordenacao nao e tratado como problema NP-completo. Problemas NP-completos envolvem, em geral, decisoes combinatorias cuja verificacao de uma solucao e polinomial, mas para os quais nao se conhece algoritmo polinomial deterministico. Um problema semelhante no uso de ordenacao como etapa auxiliar pode aparecer em otimizacoes combinatorias, mas a ordenacao em si permanece em P.

## 12. Conclusao

Os experimentos confirmam a diferenca esperada entre as linguagens: C executa o algoritmo com menor sobrecarga, enquanto Python apresenta tempos maiores por ser interpretado e possuir maior custo por operacao. Ainda assim, ambas as implementacoes seguem o mesmo comportamento assintotico: melhor e caso medio proximos de n log n, e pior caso com crescimento quadratico.
