from __future__ import annotations

from collections import defaultdict
from pathlib import Path
import csv
import math
import sys


ROOT = Path(__file__).resolve().parents[1]
DATA_FILE = ROOT / "data" / "resultados.csv"
PLOTS_DIR = ROOT / "plots"


def theoretical_curve(size: int, reference_size: int, reference_time: float) -> float:
    if size <= 1 or reference_size <= 1:
        return reference_time

    return reference_time * (size * math.log2(size)) / (reference_size * math.log2(reference_size))


def main() -> int:
    try:
        import matplotlib.pyplot as plt
    except ImportError:
        print("matplotlib nao encontrado. Instale matplotlib para gerar os graficos.")
        return 1

    if not DATA_FILE.exists():
        print("Arquivo data/resultados.csv nao encontrado. Rode primeiro: python scripts/run_benchmarks.py")
        return 1

    with DATA_FILE.open(encoding="utf-8") as file:
        rows = list(csv.DictReader(file))

    grouped: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in rows:
        grouped[row["linguagem"]].append(row)

    PLOTS_DIR.mkdir(exist_ok=True)

    for language, language_rows in grouped.items():
        plt.figure(figsize=(10, 6))

        for case_name in ["melhor", "medio", "pior"]:
            case_rows = [row for row in language_rows if row["caso"] == case_name]
            case_rows.sort(key=lambda row: int(row["tamanho"]))

            sizes = [int(row["tamanho"]) for row in case_rows]
            times = [float(row["media_ms"]) for row in case_rows]
            plt.plot(sizes, times, marker="o", label=f"{case_name} medido")

            if case_name == "medio" and sizes:
                reference_size = sizes[0]
                reference_time = times[0]
                theory = [theoretical_curve(size, reference_size, reference_time) for size in sizes]
                plt.plot(sizes, theory, linestyle="--", label="O(n log n) teorico")

        plt.title(f"Quick Sort em {language}")
        plt.xlabel("Tamanho da entrada (n)")
        plt.ylabel("Tempo medio (ms)")
        plt.legend()
        plt.grid(True, alpha=0.3)
        plt.tight_layout()
        output = PLOTS_DIR / f"quicksort_{language.lower()}.png"
        plt.savefig(output, dpi=160)
        plt.close()
        print(f"Grafico salvo em {output}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
