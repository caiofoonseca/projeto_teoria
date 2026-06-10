from __future__ import annotations

from pathlib import Path
import csv
import subprocess
import sys

from toolchain import environment_for_tool, find_gcc


ROOT = Path(__file__).resolve().parents[1]
BUILD_DIR = ROOT / "build"
DATA_DIR = ROOT / "data"
RESULTS_FILE = DATA_DIR / "resultados.csv"
PYTHON_BENCHMARK = ROOT / "src" / "python" / "benchmark.py"
C_BENCHMARK = ROOT / "src" / "c" / "benchmark.c"
C_EXECUTABLE = BUILD_DIR / "benchmark.exe"


def run_python_benchmark() -> list[dict[str, str]]:
    result = subprocess.run(
        [sys.executable, str(PYTHON_BENCHMARK)],
        text=True,
        capture_output=True,
        check=True,
    )
    return list(csv.DictReader(result.stdout.splitlines()))


def run_c_benchmark() -> list[dict[str, str]]:
    gcc = find_gcc()
    if gcc is None:
        print("[AVISO] gcc nao encontrado. Benchmark em C foi pulado.")
        return []

    BUILD_DIR.mkdir(exist_ok=True)
    subprocess.run(
        [gcc, str(C_BENCHMARK), "-Wall", "-Wextra", "-std=c11", "-lm", "-o", str(C_EXECUTABLE)],
        check=True,
        env=environment_for_tool(gcc),
    )
    result = subprocess.run(
        [str(C_EXECUTABLE)],
        text=True,
        capture_output=True,
        check=True,
        env=environment_for_tool(gcc),
    )
    return list(csv.DictReader(result.stdout.splitlines()))


def save_results(rows: list[dict[str, str]]) -> None:
    DATA_DIR.mkdir(exist_ok=True)
    fieldnames = ["linguagem", "caso", "tamanho", "rodadas", "media_ms", "desvio_padrao_ms"]

    with RESULTS_FILE.open("w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def main() -> int:
    rows = []
    rows.extend(run_python_benchmark())
    rows.extend(run_c_benchmark())
    save_results(rows)

    print(f"Resultados salvos em {RESULTS_FILE}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
