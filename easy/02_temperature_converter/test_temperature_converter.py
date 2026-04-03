import pytest
from solution import celsius_to_fahrenheit

def test_freezing_point():
    assert celsius_to_fahrenheit(0.0) == 32.0

def test_boiling_point():
    assert celsius_to_fahrenheit(100.0) == 212.0

def test_negative_temp():
    # -40 Celsius é igual a -40 Fahrenheit
    assert celsius_to_fahrenheit(-40.0) == -40.0

def test_body_temp():
    # Usando approx para lidar com precisão de float se necessário
    assert celsius_to_fahrenheit(37.0) == pytest.approx(98.6)

def test_type_hints():
    hints = celsius_to_fahrenheit.__annotations__
    assert hints['celsius'] == float
    assert hints['return'] == float