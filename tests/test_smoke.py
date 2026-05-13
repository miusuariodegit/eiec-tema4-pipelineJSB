import pytest


@pytest.mark.smoke
def test_smoke_import_app():
    import app.calculadora

    assert app.calculadora is not None
