from __future__ import annotations

import sys


def partition(values: list[int], low: int, high: int) -> int:
    pivot = values[high]
    i = low - 1

    for j in range(low, high):
        if values[j] <= pivot:
            i += 1
            values[i], values[j] = values[j], values[i]

    values[i + 1], values[high] = values[high], values[i + 1]
    return i + 1


def quicksort(values: list[int], low: int = 0, high: int | None = None) -> None:
    if high is None:
        high = len(values) - 1

    if low < high:
        pivot_index = partition(values, low, high)
        quicksort(values, low, pivot_index - 1)
        quicksort(values, pivot_index + 1, high)


def parse_input(text: str) -> list[int]:
    tokens = text.split()
    if not tokens:
        raise ValueError("Informe o tamanho da lista.")

    size = int(tokens[0])
    values = [int(token) for token in tokens[1:]]

    if size < 0:
        raise ValueError("O tamanho da lista nao pode ser negativo.")

    if len(values) != size:
        raise ValueError("A quantidade de elementos nao corresponde ao tamanho informado.")

    return values


def main() -> int:
    try:
        values = parse_input(sys.stdin.read())
    except ValueError as error:
        print(f"Entrada invalida: {error}", file=sys.stderr)
        return 1

    quicksort(values)
    print(" ".join(str(value) for value in values))
    return 0


if __name__ == "__main__":
    sys.exit(main())
