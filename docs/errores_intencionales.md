# Errores intencionales

## Error 1: prueba fallida

```bash
python scripts/romper_test.py
python -m pytest -q
```

Resultado esperado: `test_sumar` falla.

## Error 2: error de estilo

Agregar una variable sin usar o una línea demasiado larga en `app/calculadora.py`.

Resultado esperado: `flake8` falla.

## Error 3: dependencia inexistente

Cambiar temporalmente `requirements.txt`:

```txt
paquete-inexistente-tema4==1.0.0
```

Resultado esperado: falla la instalación de dependencias en GitHub Actions.
