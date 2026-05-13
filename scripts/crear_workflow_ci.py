"""Genera el workflow de GitHub Actions para la fase de commit.

Uso:
    python scripts/crear_workflow_ci.py
"""

from pathlib import Path

WORKFLOW = """name: Fase de commit - Python

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  commit-stage:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout del codigo
        uses: actions/checkout@v4

      - name: Preparar Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.11"

      - name: Instalar dependencias
        run: pip install -r requirements.txt

      - name: Analisis estatico
        run: flake8 app tests scripts

      - name: Ejecutar pruebas
        run: python -m pytest -q --cov=app --cov-report=term-missing
"""


def main() -> None:
    workflow_path = Path(".github/workflows/ci.yml")
    workflow_path.parent.mkdir(parents=True, exist_ok=True)
    workflow_path.write_text(WORKFLOW, encoding="utf-8")
    print(f"Workflow creado en: {workflow_path}")


if __name__ == "__main__":
    main()
