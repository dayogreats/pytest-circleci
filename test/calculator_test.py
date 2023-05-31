import pytest
import calc.calculator

@pytest.fixture

def test_greetings():
    assert calc.calculator.greetings("Good Morning") == "Good Morning"

def test_add():
    assert calc.calculator.add(2,3) == 5

def test_subtract():
    assert calc.calculator.subtract(3,2) == 1

def test_multiply():
    assert calc.calculator.multiply(2,3) == 6

def test_divide():
    assert calc.calculator.divide(6,3) == 2

def test_square():
    assert calc.calculator.square(3) == 9

def test_square_root():
    assert calc.calculator.square_root(9) == 3

def test_cube():
    assert calc.calculator.cube(3) == 27

def test_cube_root():
    assert calc.calculator.cube_root(27) == 3

def test_power():
    assert calc.calculator.power(2,3) == 8

def test_mod():
    assert calc.calculator.mod(6,3) == 0
        
def test_floor():
    assert calc.calculator.floor(3.5) == 3

def test_ceiling():
    assert calc.calculator.ceiling(3.5) == 4

def test_truncate():
    assert calc.calculator.truncate(3.5) == 3

def test_round():
    assert calc.calculator.round(3.5) == 4

def test_absolute():
    assert calc.calculator.absolute(-3.5) == 3

def test_cube():
    assert calc.calculator.cube(3) == 27

def test_cube_root():
    assert calc.calculator.cube_root(27) == 3
    
def test_power():
    assert calc.calculator.power(2,3) == 8




