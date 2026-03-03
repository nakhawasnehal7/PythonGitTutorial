import pytest
import calculator

@pytest.mark.slow
def exponent_test():
    result = calculator.exponentiate(2,3)
    assert result == 8

@pytest.mark.skip(reason="Function not implemented yet")
def test_root():
    result = calculator.root(4,2)
    assert result == 2

@pytest.mark.xfail(reason="Cannot divide by 0")
def test_divide():
    calculator.divide(7, 0)
