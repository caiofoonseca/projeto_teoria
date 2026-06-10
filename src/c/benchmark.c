#define _POSIX_C_SOURCE 199309L

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

#ifdef _WIN32
#include <windows.h>
#else
#include <time.h>
#endif

#define ROUNDS 30
#define SIZE_COUNT 3
#define CASE_COUNT 3

static const int SIZES[SIZE_COUNT] = {100, 1000, 3000};
static const char *CASES[CASE_COUNT] = {"melhor", "medio", "pior"};

static double now_seconds(void) {
#ifdef _WIN32
    LARGE_INTEGER frequency;
    LARGE_INTEGER counter;
    QueryPerformanceFrequency(&frequency);
    QueryPerformanceCounter(&counter);
    return (double)counter.QuadPart / (double)frequency.QuadPart;
#else
    struct timespec ts;
    clock_gettime(CLOCK_MONOTONIC, &ts);
    return (double)ts.tv_sec + (double)ts.tv_nsec / 1000000000.0;
#endif
}

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

static int fill_best_case(int values[], int index, int start, int end) {
    if (start > end) {
        return index;
    }

    int middle = (start + end) / 2;
    int right_start;
    int right_end;

    index = fill_best_case(values, index, start, middle - 1);
    right_start = index;
    index = fill_best_case(values, index, middle + 1, end);
    right_end = index - 1;

    if (right_start <= right_end) {
        int last = values[right_end];
        for (int i = right_end; i > right_start; i--) {
            values[i] = values[i - 1];
        }
        values[right_start] = last;
    }

    values[index] = middle;
    return index + 1;
}

static unsigned int next_random(unsigned int *seed) {
    *seed = (*seed * 1103515245u + 12345u) & 0x7fffffffu;
    return *seed;
}

static void shuffle(int values[], int size, unsigned int seed) {
    for (int i = size - 1; i > 0; i--) {
        int j = (int)(next_random(&seed) % (unsigned int)(i + 1));
        swap(&values[i], &values[j]);
    }
}

static void generate_values(int values[], int size, const char *case_name, int round_index) {
    if (strcmp(case_name, "melhor") == 0) {
        fill_best_case(values, 0, 0, size - 1);
        return;
    }

    for (int i = 0; i < size; i++) {
        values[i] = i;
    }

    if (strcmp(case_name, "medio") == 0) {
        shuffle(values, size, (unsigned int)(2026 + size + round_index));
    }
}

static double mean(const double values[], int size) {
    double total = 0.0;
    for (int i = 0; i < size; i++) {
        total += values[i];
    }
    return total / size;
}

static double standard_deviation(const double values[], int size, double avg) {
    double total = 0.0;
    for (int i = 0; i < size; i++) {
        double diff = values[i] - avg;
        total += diff * diff;
    }
    return sqrt(total / (size - 1));
}

int main(void) {
    printf("linguagem,caso,tamanho,rodadas,media_ms,desvio_padrao_ms\n");

    for (int size_index = 0; size_index < SIZE_COUNT; size_index++) {
        int size = SIZES[size_index];
        int *values = malloc((size_t)size * sizeof(int));
        if (values == NULL) {
            fprintf(stderr, "Erro ao alocar memoria.\n");
            return 1;
        }

        for (int case_index = 0; case_index < CASE_COUNT; case_index++) {
            const char *case_name = CASES[case_index];
            double times[ROUNDS];

            for (int round_index = 0; round_index < ROUNDS; round_index++) {
                generate_values(values, size, case_name, round_index);

                double start = now_seconds();
                quicksort(values, 0, size - 1);
                double end = now_seconds();

                times[round_index] = (end - start) * 1000.0;
            }

            double avg = mean(times, ROUNDS);
            double stdev = standard_deviation(times, ROUNDS, avg);
            printf("C,%s,%d,%d,%.6f,%.6f\n", case_name, size, ROUNDS, avg, stdev);
        }

        free(values);
    }

    return 0;
}
