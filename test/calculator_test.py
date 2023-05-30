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

def test_cube():
    assert calc.calcculator.cube(3) == 27

def test_cube_root():
    assert calc.calcculator.cube_root(27) == 3

def test_power():
    assert calc.calcculator.power(2,3) == 8

def test_mod():
    assert calc.calcculator.mod(6,3) == 0

def test_mod_2():
    assert calc.calcculator.mod(7,3) == 1
        
def test_floor():
    assert calc.calcculator.floor(3.5) == 3
def test_ceiling():
    assert calc.calcculator.ceiling(3.5) == 4
def test_truncate():
    assert calc.calcculator.truncate(3.5) == 3
def test_round():
    assert calc.calcculator.round(3.5) == 4
def test_absolute():
    assert calc.calcculator.absolute(-3.5) == 3
def test_cube():
    assert calc.calcculator.cube(3) == 27
def test_cube_root():
    assert calc.calcculator.cube_root(27) == 3
def test_power():
    assert calc.calcculator.power(2,3) == 8




