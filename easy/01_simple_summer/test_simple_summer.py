import pytest
from simple_summer import add_numbers

def test_add_numbers_positive():
    assert add_numbers(10, 5) == 15

def test_add_numbers_negative():
    assert add_numbers(-1, -1) == -2

def test_add_numbers_zero():
    assert add_numbers(0, 0) == 0

def test_type_hints():
    # Verifica se as dicas de tipo foram implementadas
    hints = add_numbers.__annotations__
    assert hints['a'] == int
    assert hints['b'] == int
    assert hints['return'] == int