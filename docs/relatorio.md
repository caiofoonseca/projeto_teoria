# Relatório - Quick Sort

## 1. Identificação

- Disciplina: Teoria da Computação
- Professor: Daniel Bezerra
- Grupo:
  - Caio Fonseca
  - Gabriel Belo
  - Jarbas Esteves
- Algoritmo analisado: Quick Sort
- Linguagens utilizadas: C e Python

## 2. Descrição do Algoritmo

O Quick Sort é um algoritmo de ordenação baseado na estratégia de divisão e conquista. Ele escolhe um elemento chamado pivô, reorganiza a lista de modo que os menores elementos fiquem antes do pivô e os maiores fiquem depois, e repete o processo recursivamente nas sublistas geradas.

## 3. Problema Resolvido

O problema resolvido é a ordenação de uma sequência de números inteiros em ordem crescente.

## 4. Pseudocódigo

```text
QUICKSORT(vetor, inicio, fim)
    se inicio < fim então
        pivô = PARTICIONAR(vetor, inicio, fim)
        QUICKSORT(vetor, inicio, pivô - 1)
        QUICKSORT(vetor, pivô + 1, fim)

PARTICIONAR(vetor, inicio, fim)
    pivô = vetor[fim]
    i = inicio - 1

    para j de inicio até fim - 1 faça
        se vetor[j] <= pivô então
            i = i + 1
            trocar vetor[i] com vetor[j]

    trocar vetor[i + 1] com vetor[fim]
    retornar i + 1
```

## 5. Análise de Complexidade

| Caso | Complexidade | Explicação |
| --- | --- | --- |
| Melhor caso | Big-Omega: Omega(n log n) | O pivô divide o vetor em partes aproximadamente iguais. |
| Caso médio | Big-Theta: Theta(n log n) | Em entradas aleatórias, as partições tendem a ser razoavelmente balanceadas. |
| Pior caso | Big-O: O(n^2) | O pivô gera partições muito desbalanceadas, como pode ocorrer em vetor já ordenado nesta implementação. |

## 6. Aplicabilidade

O Quick Sort é eficiente para ordenação em memória principal, especialmente quando as partições são bem balanceadas. Suas principais limitações aparecem no pior caso, quando a escolha do pivô produz divisões muito desiguais, e no uso de recursão, que pode aumentar o consumo de pilha.

## 7. Metodologia Experimental

Os experimentos devem ser executados com:

- 30 rodadas por cenário.
- Três tamanhos de entrada: pequena, média e grande.
- Três cenários: melhor caso, caso médio e pior caso.
- As duas linguagens escolhidas: C e Python.
- Medição de tempo com temporizadores de alta precisão.

## 8. Ambiente de Execução

Ambiente usado na execução dos experimentos registrados em `data/resultados.csv`:

- Computador: Dell Latitude 5511
- Arquitetura: PC baseado em x64
- Processador: Intel(R) Core(TM) i7-10850H CPU @ 2.70GHz
- Núcleos: 6
- Núcleos lógicos informados pelo sistema: 12
- Memória RAM instalada: 32,0 GB
- Memória física total: 31,6 GB
- Sistema operacional: Microsoft Windows 10 Pro
- Versão do sistema operacional: 10.0.19045, compilação 19045
- Compilador C: gcc.exe 16.1.0, MSYS2 UCRT64
- Python: 3.14.0
- Biblioteca de gráficos: matplotlib 3.10.9

## 9. Resultados Experimentais

Os resultados foram gerados com:

```bash
python scripts/run_benchmarks.py
```

O arquivo gerado será:

```text
data/resultados.csv
```

Resumo dos dados coletados:

| Linguagem | Caso | Tamanho | Rodadas | Média (ms) | Desvio-padrão (ms) |
| --- | --- | ---: | ---: | ---: | ---: |
| Python | melhor | 100 | 30 | 0.040343 | 0.009717 |
| Python | médio | 100 | 30 | 0.051723 | 0.004462 |
| Python | pior | 100 | 30 | 0.361187 | 0.035525 |
| Python | melhor | 1000 | 30 | 0.643863 | 0.011291 |
| Python | médio | 1000 | 30 | 0.979733 | 0.232886 |
| Python | pior | 1000 | 30 | 37.844777 | 1.124157 |
| Python | melhor | 3000 | 30 | 2.378267 | 0.112871 |
| Python | médio | 3000 | 30 | 3.219307 | 0.235365 |
| Python | pior | 3000 | 30 | 352.578220 | 9.665588 |
| C | melhor | 100 | 30 | 0.001833 | 0.000130 |
| C | médio | 100 | 30 | 0.006463 | 0.006439 |
| C | pior | 100 | 30 | 0.021747 | 0.000411 |
| C | melhor | 1000 | 30 | 0.027297 | 0.000234 |
| C | médio | 1000 | 30 | 0.070773 | 0.001708 |
| C | pior | 1000 | 30 | 2.507270 | 0.497418 |
| C | melhor | 3000 | 30 | 0.114330 | 0.006240 |
| C | médio | 3000 | 30 | 0.289300 | 0.010202 |
| C | pior | 3000 | 30 | 21.690007 | 0.795643 |

Os resultados mostram que a implementação em C apresentou tempos menores em todos os cenários. Também fica visível que o pior caso cresce de forma muito mais acentuada, coerente com a complexidade O(n^2) da implementação com pivô fixo no último elemento.

## 10. Gráficos

Os gráficos podem ser gerados com:

```bash
python scripts/generate_plots.py
```

Os arquivos serão salvos em:

```text
plots/
```

Gráficos gerados:

- `plots/quicksort_c.png`
- `plots/quicksort_python.png`

## 11. Reflexão sobre Classe P e NP

O problema de ordenação pertence à classe P, pois existe algoritmo que resolve o problema em tempo polinomial. O Quick Sort, mesmo em seu pior caso, executa em O(n^2), que ainda é polinomial.

O problema de ordenação não é tratado como problema NP-completo. Problemas NP-completos envolvem, em geral, decisões combinatórias cuja verificação de uma solução é polinomial, mas para os quais não se conhece algoritmo polinomial determinístico. Um problema semelhante no uso de ordenação como etapa auxiliar pode aparecer em otimizações combinatórias, mas a ordenação em si permanece em P.

## 12. Conclusão

Os experimentos confirmam a diferença esperada entre as linguagens: C executa o algoritmo com menor sobrecarga, enquanto Python apresenta tempos maiores por ser interpretado e possuir maior custo por operação. Ainda assim, ambas as implementações seguem o mesmo comportamento assintótico: melhor caso e caso médio próximos de n log n, e pior caso com crescimento quadrático.
