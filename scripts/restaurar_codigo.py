"""Restaura el fallo controlado del test.

Uso:
    python scripts/restaurar_codigo.py
"""

from pathlib import Path

TEST_FILE = Path("tests/test_calculadora.py")


def main() -> None:
    content = TEST_FILE.read_text(encoding="utf-8")
    content = content.replace("assert sumar(2, 2) == 5", "assert sumar(2, 2) == 4")
    TEST_FILE.write_text(content, encoding="utf-8")
    print("Se restauro tests/test_calculadora.py")


if __name__ == "__main__":
    main()
