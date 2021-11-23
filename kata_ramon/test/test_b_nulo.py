from src.ecuacion_2grado import ecuacion_segundo_grado
import pytest


@pytest.mark.b_nulo
def test_b_nulo_solucion_real():
    assert ecuacion_segundo_grado(1, 0, -1) == (1, -1)
    assert ecuacion_segundo_grado(-1, 0, 1) == (1, -1)

@pytest.mark.b_nulo
def test_b_nulo_solucion_imaginaria():
    assert ecuacion_segundo_grado(1, 0, 1) == None
    assert ecuacion_segundo_grado(-1, 0, -1) == None