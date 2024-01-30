from src.calc import Calculator
#WHITEBOX

def test_addition():
    calc = Calculator()
    assert calc.add(2, 3) == 5


def test_subtraction():
    calc = Calculator()
    assert calc.sub(2, 3) == -1


def test_multiplication():
    calc = Calculator()
    assert calc.mul(2, 3) == 6


def test_division():
    calc = Calculator()
    assert calc.div(4, 2) == 2
