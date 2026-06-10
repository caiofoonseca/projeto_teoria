from pathlib import Path
import shutil
import subprocess
import sys


ROOT = Path(__file__).resolve().parents[1]
SOURCE_C = ROOT / "src" / "c" / "quicksort.c"
SOURCE_PYTHON = ROOT / "src" / "python" / "quicksort.py"
BUILD_DIR = ROOT / "build"
EXECUTABLE = BUILD_DIR / "quicksort.exe"

TEST_CASES = [
    ("lista desordenada", "6\n8 3 1 7 0 10\n", "0 1 3 7 8 10\n"),
    ("lista ja ordenada", "5\n1 2 3 4 5\n", "1 2 3 4 5\n"),
    ("lista invertida", "5\n5 4 3 2 1\n", "1 2 3 4 5\n"),
    ("valores repetidos", "7\n4 2 4 1 2 9 1\n", "1 1 2 2 4 4 9\n"),
    ("lista vazia", "0\n", "\n"),
]


def compile_c_program() -> bool:
    if shutil.which("gcc") is None:
        print("[AVISO] gcc nao encontrado. Testes em C foram pulados.")
        return False

    BUILD_DIR.mkdir(exist_ok=True)
    command = ["gcc", str(SOURCE_C), "-Wall", "-Wextra", "-std=c11", "-o", str(EXECUTABLE)]
    subprocess.run(command, check=True)
    return True


def run_case(command: list[str], language: str, name: str, input_data: str, expected_output: str) -> bool:
    result = subprocess.run(
        command,
        input=input_data,
        text=True,
        capture_output=True,
        check=False,
    )

    if result.returncode != 0:
        print(f"[ERRO] {language} - {name}: programa retornou codigo {result.returncode}")
        print(result.stderr)
        return False

    if result.stdout != expected_output:
        print(f"[FALHA] {language} - {name}")
        print(f"Esperado: {expected_output!r}")
        print(f"Obtido:   {result.stdout!r}")
        return False

    print(f"[OK] {language} - {name}")
    return True


def run_language_tests(language: str, command: list[str]) -> tuple[int, int]:
    passed = 0
    for name, input_data, expected_output in TEST_CASES:
        if run_case(command, language, name, input_data, expected_output):
            passed += 1

    return passed, len(TEST_CASES)


def main() -> int:
    results: list[tuple[str, int, int]] = []

    results.append(("Python", *run_language_tests("Python", [sys.executable, str(SOURCE_PYTHON)])))

    try:
        if compile_c_program():
            results.append(("C", *run_language_tests("C", [str(EXECUTABLE)])))
    except subprocess.CalledProcessError as error:
        print(f"Falha ao compilar o programa em C: {error}")
        return 1

    print("\nResumo:")
    for language, passed, total in results:
        print(f"- {language}: {passed}/{total} testes passaram.")

    return 0 if all(passed == total for _, passed, total in results) else 1


if __name__ == "__main__":
    sys.exit(main())
