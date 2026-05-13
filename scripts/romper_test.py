"""Introduce un fallo controlado para demostrar un pipeline rojo.

Uso:
    python scripts/romper_test.py
"""

from pathlib import Path

TEST_FILE = Path("tests/test_calculadora.py")


def main() -> None:
    content = TEST_FILE.read_text(encoding="utf-8")
    content = content.replace("assert sumar(2, 2) == 4", "assert sumar(2, 2) == 5")
    TEST_FILE.write_text(content, encoding="utf-8")
    print("Se introdujo un fallo intencional en tests/test_calculadora.py")


if __name__ == "__main__":
    main()
