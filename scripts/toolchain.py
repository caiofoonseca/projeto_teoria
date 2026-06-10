from __future__ import annotations

from pathlib import Path
import os
import shutil


def find_gcc() -> str | None:
    gcc = shutil.which("gcc")
    if gcc is not None:
        return gcc

    candidates = [
        Path("C:/msys64/ucrt64/bin/gcc.exe"),
        Path("C:/msys64/mingw64/bin/gcc.exe"),
        Path("C:/msys64/clang64/bin/gcc.exe"),
    ]

    for candidate in candidates:
        if candidate.exists():
            return str(candidate)

    return None


def environment_for_tool(tool_path: str) -> dict[str, str]:
    env = os.environ.copy()
    tool_dir = str(Path(tool_path).resolve().parent)
    env["PATH"] = tool_dir + os.pathsep + env.get("PATH", "")
    return env
