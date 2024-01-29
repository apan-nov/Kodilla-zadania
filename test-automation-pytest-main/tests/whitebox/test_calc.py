from src.calc import Calculator

def test_addition():
    calc = Calculator()
    assert calc.add(2, 3) == 5

# TODO