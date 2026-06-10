from pathlib import Path
import subprocess
import sys


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "src" / "c" / "quicksort.c"
BUILD_DIR = ROOT / "build"
EXECUTABLE = BUILD_DIR / "quicksort.exe"

TEST_CASES = [
    ("lista desordenada", "6\n8 3 1 7 0 10\n", "0 1 3 7 8 10\n"),
    ("lista ja ordenada", "5\n1 2 3 4 5\n", "1 2 3 4 5\n"),
    ("lista invertida", "5\n5 4 3 2 1\n", "1 2 3 4 5\n"),
    ("valores repetidos", "7\n4 2 4 1 2 9 1\n", "1 1 2 2 4 4 9\n"),
    ("lista vazia", "0\n", "\n"),
]


def compile_program() -> None:
    BUILD_DIR.mkdir(exist_ok=True)
    command = ["gcc", str(SOURCE), "-Wall", "-Wextra", "-std=c11", "-o", str(EXECUTABLE)]
    subprocess.run(command, check=True)


def run_case(name: str, input_data: str, expected_output: str) -> bool:
    result = subprocess.run(
        [str(EXECUTABLE)],
        input=input_data,
        text=True,
        capture_output=True,
        check=False,
    )

    if result.returncode != 0:
        print(f"[ERRO] {name}: programa retornou codigo {result.returncode}")
        print(result.stderr)
        return False

    if result.stdout != expected_output:
        print(f"[FALHA] {name}")
        print(f"Esperado: {expected_output!r}")
        print(f"Obtido:   {result.stdout!r}")
        return False

    print(f"[OK] {name}")
    return True


def main() -> int:
    try:
        compile_program()
    except FileNotFoundError:
        print("gcc nao encontrado. Instale um compilador C para rodar os testes.")
        return 1
    except subprocess.CalledProcessError as error:
        print(f"Falha ao compilar o programa: {error}")
        return 1

    passed = 0
    for name, input_data, expected_output in TEST_CASES:
        if run_case(name, input_data, expected_output):
            passed += 1

    total = len(TEST_CASES)
    print(f"\nResultado: {passed}/{total} testes passaram.")
    return 0 if passed == total else 1


if __name__ == "__main__":
    sys.exit(main())
