import pytest

from app.calculadora import dividir, multiplicar, restar, sumar


@pytest.mark.unit
def test_sumar():
    assert sumar(2, 2) == 4


@pytest.mark.unit
def test_restar():
    assert restar(5, 3) == 2


@pytest.mark.unit
def test_multiplicar():
    assert multiplicar(3, 4) == 12


@pytest.mark.unit
def test_dividir():
    assert dividir(8, 2) == 4


@pytest.mark.unit
def test_dividir_entre_cero():
    with pytest.raises(ValueError):
        dividir(8, 0)
