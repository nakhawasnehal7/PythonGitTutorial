import pytest
import calculator

def test_add():
    result = calculator.add(2,3)
    assert result == 5

def test_subtract_pos():
    result = calculator.subtract(5,3)
    assert result == 2

def test_subtract_neg():
    result = calculator.subtract(3, 5)
    assert result == -2

def test_multiply():
    assert calculator.multiply(2,3) == 6

def test_divide_int():
    result = calculator.divide(6,2)
    assert result == 3

def test_divide_float():
    result = calculator.divide(7, 2)
    assert result == 3.5

