# Guía de sesión - Tema 4

## Minuto 0-5
Conectar Tema 3 con Tema 4: del Pull Request al pipeline.

## Minuto 5-12
Explicar qué es un pipeline:
- Fases encadenadas.
- Automatización.
- Feedback al desarrollador.
- Detención ante fallo.

## Minuto 12-20
Buenas prácticas:
- Compilar o empaquetar una vez.
- Usar el mismo proceso en todos los entornos.
- Ejecutar smoke tests.
- Detener el pipeline ante fallos.

## Minuto 20-38
Práctica:
1. Clonar repo.
2. Crear rama.
3. Ejecutar pruebas locales.
4. Hacer cambio.
5. Push.
6. Abrir PR.
7. Revisar Actions.

## Minuto 38-45
Fallo intencional:
```bash
python scripts/romper_test.py
python -m pytest -q
```

Luego corregir:
```bash
python scripts/restaurar_codigo.py
python -m pytest -q
```

## Minuto 45-50
Cierre:
- Qué fase se ejecutó.
- Qué falló.
- Qué información entregó el log.
- Por qué no se debe fusionar un PR con pipeline rojo.
