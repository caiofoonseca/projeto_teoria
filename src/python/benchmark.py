from __future__ import annotations

import csv
import random
import statistics
import sys
from time import perf_counter

from quicksort import quicksort


ROUNDS = 30
SIZES = [100, 1000, 3000]
CASES = ["melhor", "medio", "pior"]


def best_case_values(start: int, end: int) -> list[int]:
    if start > end:
        return []

    middle = (start + end) // 2
    left = best_case_values(start, middle - 1)
    right = best_case_values(middle + 1, end)

    if right:
        right = [right[-1]] + right[:-1]

    return left + right + [middle]


def generate_values(size: int, case_name: str, round_index: int) -> list[int]:
    if case_name == "melhor":
        return best_case_values(0, size - 1)

    if case_name == "medio":
        values = list(range(size))
        random.Random(2026 + size + round_index).shuffle(values)
        return values

    if case_name == "pior":
        return list(range(size))

    raise ValueError(f"Caso desconhecido: {case_name}")


def measure_case(size: int, case_name: str) -> list[float]:
    times: list[float] = []

    for round_index in range(ROUNDS):
        values = generate_values(size, case_name, round_index)

        start = perf_counter()
        quicksort(values)
        end = perf_counter()

        times.append((end - start) * 1000)

    return times


def main() -> int:
    sys.setrecursionlimit(max(10000, max(SIZES) * 2))
    writer = csv.writer(sys.stdout)
    writer.writerow(["linguagem", "caso", "tamanho", "rodadas", "media_ms", "desvio_padrao_ms"])

    for size in SIZES:
        for case_name in CASES:
            times = measure_case(size, case_name)
            writer.writerow(
                [
                    "Python",
                    case_name,
                    size,
                    ROUNDS,
                    f"{statistics.mean(times):.6f}",
                    f"{statistics.stdev(times):.6f}",
                ]
            )

    return 0


if __name__ == "__main__":
    sys.exit(main())
