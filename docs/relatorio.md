# Relatorio - Quick Sort

## 1. Identificacao

- Disciplina: Teoria da Computacao
- Professor: Daniel Bezerra
- Grupo:
  - Caio Fonseca
  - Eduardo Malheiros
  - Gabriel Belo
  - Jarbas
- Algoritmo analisado: Quick Sort
- Linguagens utilizadas: C e Python
- Repositorio: <https://github.com/caiofoonseca/projeto_teoria.git>

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

Preencher antes da entrega final:

- Processador:
- Memoria RAM:
- Sistema operacional:
- Versao do compilador C:
- Versao do Python:

## 9. Resultados Experimentais

Os resultados devem ser gerados com:

```bash
python scripts/run_benchmarks.py
```

O arquivo gerado sera:

```text
data/resultados.csv
```

## 10. Graficos

Os graficos podem ser gerados com:

```bash
python scripts/generate_plots.py
```

Os arquivos serao salvos em:

```text
plots/
```

## 11. Reflexao sobre Classe P e NP

O problema de ordenacao pertence a classe P, pois existe algoritmo que resolve o problema em tempo polinomial. O Quick Sort, mesmo em seu pior caso, executa em O(n^2), que ainda e polinomial.

O problema de ordenacao nao e tratado como problema NP-completo. Problemas NP-completos envolvem, em geral, decisoes combinatorias cuja verificacao de uma solucao e polinomial, mas para os quais nao se conhece algoritmo polinomial deterministico. Um problema semelhante no uso de ordenacao como etapa auxiliar pode aparecer em otimizacoes combinatorias, mas a ordenacao em si permanece em P.

## 12. Conclusao

Preencher apos a execucao dos experimentos finais, comparando os tempos medidos em C e Python com a curva teorica esperada.
