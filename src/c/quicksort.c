#include <stdio.h>
#include <stdlib.h>

static void swap(int *a, int *b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}

static int partition(int values[], int low, int high) {
    int pivot = values[high];
    int i = low - 1;

    for (int j = low; j < high; j++) {
        if (values[j] <= pivot) {
            i++;
            swap(&values[i], &values[j]);
        }
    }

    swap(&values[i + 1], &values[high]);
    return i + 1;
}

static void quicksort(int values[], int low, int high) {
    if (low < high) {
        int pivot_index = partition(values, low, high);

        quicksort(values, low, pivot_index - 1);
        quicksort(values, pivot_index + 1, high);
    }
}

static void print_values(const int values[], int size) {
    for (int i = 0; i < size; i++) {
        if (i > 0) {
            printf(" ");
        }
        printf("%d", values[i]);
    }
    printf("\n");
}

int main(void) {
    int size;

    if (scanf("%d", &size) != 1 || size < 0) {
        fprintf(stderr, "Entrada invalida. Informe o tamanho da lista.\n");
        return 1;
    }

    int *values = malloc((size_t)size * sizeof(int));
    if (size > 0 && values == NULL) {
        fprintf(stderr, "Erro ao alocar memoria.\n");
        return 1;
    }

    for (int i = 0; i < size; i++) {
        if (scanf("%d", &values[i]) != 1) {
            fprintf(stderr, "Entrada invalida. Informe todos os elementos.\n");
            free(values);
            return 1;
        }
    }

    quicksort(values, 0, size - 1);
    print_values(values, size);

    free(values);
    return 0;
}
