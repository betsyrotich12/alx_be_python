import unittest
from simple_calculator import SimpleCalculator
class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the addition method."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(1, 0), 1)
        # Add more assertions to thoroughly test the add method.

    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(3, 2), 1)
        self.assertEqual(self.calc.subtract(5, 2), 3)
        self.assertEqual(self.calc.subtract(7, 4), 3)
        self.assertEqual(self.calc.subtract(-3, 2), -5)
        self.assertEqual(self.calc.subtract(6, 1), 5)

    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(6, 1), 6)
        self.assertEqual(self.calc.multiply(2, 2), 4)
        self.assertEqual(self.calc.multiply(6, 3), 18)
        self.assertEqual(self.calc.multiply(3, 2), 6)
        self.assertEqual(self.calc.multiply(4, 1), 4)

    def test_division(self):
         
         self.assertEqual(self.calc.divide(6, 3), 2)
         self.assertEqual(self.calc.divide(-6, 3), -2)
         self.assertEqual(self.calc.divide(-6, -3), 2)
         self.assertEqual(self.calc.divide(5, 2), 2.5)
         self.assertIsNone(self.calc.divide(5, 0), "Expected None when dividing by zero")
         self.assertEqual(self.calc.divide(0, 5), 0)
        

if __name__ == "__main__":
    unittest.main()
