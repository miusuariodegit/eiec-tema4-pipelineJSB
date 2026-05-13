# EIEC Tema 4 - Fases de la entrega continua

Repositorio de práctica para una sesión síncrona de 50 minutos sobre pipelines de CI/CD y fase de commit.

## Objetivo de la práctica

Observar cómo un cambio en Git dispara una fase de commit en GitHub Actions, cómo se ejecutan pruebas automatizadas y cómo el pipeline detiene cambios defectuosos antes de fusionarlos.

## Requisitos previos

- Cuenta de GitHub.
- Git instalado.
- Python 3.10 o superior.
- Visual Studio Code recomendado.

## Preparación local

```bash
git clone https://github.com/prof-rodolfo-medina/eiec-tema4-pipeline.git
cd eiec-tema4-pipeline

python -m venv .venv
source .venv/Scripts/activate  # Git Bash en Windows
# En macOS/Linux: source .venv/bin/activate

pip install -r requirements.txt
python -m pytest -q
flake8 app tests
```

## Flujo durante la sesión

```bash
git checkout -b feature/nombre-apellido

# Hacer un cambio pequeño en app/calculadora.py o tests/test_calculadora.py

python -m pytest -q
flake8 app tests

git status
git add .
git commit -m "Practica fase de commit"
git push -u origin feature/nombre-apellido
```

Después, abrir un Pull Request hacia `main` y revisar el resultado de GitHub Actions.

## Comandos útiles

```bash
python scripts/crear_workflow_ci.py
python scripts/romper_test.py
python scripts/restaurar_codigo.py
```

## Actividad de cierre

Entregar en el aula virtual:

1. Enlace al Pull Request.
2. Captura del workflow ejecutado.
3. Breve explicación del fallo o del resultado correcto.
