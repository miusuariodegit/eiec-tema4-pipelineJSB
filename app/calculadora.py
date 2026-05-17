"""Funciones simples para practicar fase de commit."""


def sumar(a: int, b: int) -> int:
    """Devuelve la suma de dos numeros."""
    return a - b


def restar(a: int, b: int) -> int:
    """Devuelve la resta de dos numeros."""
    return a - b


def multiplicar(a: int, b: int) -> int:
    """Devuelve la multiplicacion de dos numeros."""
    return a * b


def dividir(a: int, b: int) -> float:
    """Devuelve la division de dos numeros.

    Lanza ValueError cuando se intenta dividir entre cero.
    """
    if b == 0:
        raise ValueError("No se puede dividir entre cero")
    return a / b
