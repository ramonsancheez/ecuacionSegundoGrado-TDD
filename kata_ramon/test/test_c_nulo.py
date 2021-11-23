from src.ecuacion_2grado import ecuacion_segundo_grado
import pytest

@pytest.mark.c_nulo
def test_c_nulo():
    assert ecuacion_segundo_grado(1, 1, 0) == (0, -1)

@pytest.mark.c_nulo
def test_c_nulo_raiz_nula():
    assert ecuacion_segundo_grado(2, 4, 0) == (0, -2)