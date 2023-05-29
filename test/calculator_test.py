import pytest
import calc.calcculator

@pytest.fixture

def test_greetings():
    assert calc.calcculator.greetings("Good Morning") == "Good Morning"

def test_add():
    assert calc.calcculator.add(2,3) == 5

def test_subtract():
    assert calc.calcculator.subtract(3,2) == 1

def test_multiply():
    assert calc.calcculator.multiply(2,3) == 6

def test_divide():
    assert calc.calcculator.divide(6,3) == 2

def test_square():
    assert calc.calcculator.square(3) == 9

def test_square_root():
    assert calc.calcculator.square_root(9) == 3

