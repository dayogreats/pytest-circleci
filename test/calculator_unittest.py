import unittest

import calc.calculator


class CalculatorUnittest(unittest.TestCase):

    def setUp(self):
        print('--------setting up testing ---------')

    def test_greetings(self):
        self.assertEqual(calc.calculator.greetings("Good Morning"), "Good Morning")


    def test_add(self):
        self.assertEqual(calc.calculator.add(1, 2), 3) 
    
    def test_subtract(self):
        self.assertEqual(calc.calculator.subtract(1, 2), -1)
    
    def test_multiply(self):
        self.assertEqual(calc.calculator.multiply(1, 2), 2)

    def test_divide(self):
        self.assertEqual(calc.calculator.divide(12, 4), 3)
    
    def test_square(self):
        self.assertEqual(calc.calculator.square(3), 9)
    
    def test_square_root(self):
        self.assertEqual(calc.calculator.square_root(9), 3)
    
    def test_cube(self):
        self.assertEqual(calc.calculator.cube(3), 27)
    
    def test_cube_root(self):
        self.assertEqual(calc.calculator.cube_root(27), 3)

    def test_power(self):
        self.assertEqual(calc.calculator.power(2, 3), 8)

    def test_mod(self):
        self.assertEqual(calc.calculator.mod(6, 3), 0)
    
    def test_floor(self):
        self.assertEqual(calc.calculator.floor(3.5), 3)
    
    def test_ceiling(self):
        self.assertEqual(calc.calculator.ceiling(3.5), 4)

    def test_truncate(self):
        self.assertEqual(calc.calculator.truncate(3.5), 3)
    
    def test_round(self):
        self.assertEqual(calc.calculator.round(3.5), 4)
    
    def test_absolute(self):
        self.assertEqual(calc.calculator.absolute(-3.5), 3)
    
    def test_cube(self):
        self.assertEqual(calc.calculator.cube(3), 27)

    def test_cube_root(self):
        self.assertEqual(calc.calculator.cube_root(27), 3)

    def test_power(self):
        self.assertEqual(calc.calculator.power(2, 3), 8)
    

if __name__ == '__main__':
    unittest.main()

