from src.ecuacion_2grado import ecuacion_segundo_grado
import pytest

@pytest.mark.b_c_nulo
def test_b_c_nulo_raiz_nula():
    assert ecuacion_segundo_grado(9, 0, 0) == 0

@pytest.mark.b_c_nulo
def test_b_c_nulo_raiz_nula():
    assert ecuacion_segundo_grado(2, 0, 0) == 0