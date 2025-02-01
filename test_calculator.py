import unittest
from calculator import Calculator  # Import the Calculator class from calculator.py


class TestCalculator(unittest.TestCase):
    def setUp(self):
        """Set up a Calculator instance for testing."""
        self.calc = Calculator()

    def test_add(self):
        """Test addition functionality."""
        self.assertEqual(self.calc.add(10, 5), 15)  # 10 + 5 = 15
        self.assertEqual(self.calc.add(-1, 1), 0)   # -1 + 1 = 0
        self.assertEqual(self.calc.add(-1, -1), -2) # -1 + (-1) = -2

    def test_subtract(self):
        """Test subtraction functionality."""
        self.assertEqual(self.calc.subtract(10, 5), 5)  # 10 - 5 = 5
        self.assertEqual(self.calc.subtract(-1, 1), -2) # -1 - 1 = -2
        self.assertEqual(self.calc.subtract(-1, -1), 0) # -1 - (-1) = 0

    def test_multiply(self):
        """Test multiplication functionality."""
        self.assertEqual(self.calc.multiply(10, 5), 50)  # 10 * 5 = 50
        self.assertEqual(self.calc.multiply(-1, 1), -1)  # -1 * 1 = -1
        self.assertEqual(self.calc.multiply(-1, -1), 1)  # -1 * (-1) = 1

    def test_divide(self):
        """Test division functionality."""
        self.assertEqual(self.calc.divide(10, 5), 2)  # 10 / 5 = 2
        self.assertEqual(self.calc.divide(-1, 1), -1) # -1 / 1 = -1
        self.assertEqual(self.calc.divide(-1, -1), 1) # -1 / (-1) = 1

        # Test division by zero
        with self.assertRaises(ValueError):
            self.calc.divide(10, 0)  # Division by zero should raise ValueError

    def test_exponent(self):
        """Test exponentiation functionality."""
        self.assertEqual(self.calc.exponent(2, 3), 8)   # 2^3 = 8
        self.assertEqual(self.calc.exponent(5, 0), 1)   # 5^0 = 1
        self.assertEqual(self.calc.exponent(-2, 2), 4)  # (-2)^2 = 4
        self.assertEqual(self.calc.exponent(-2, 3), -8) # (-2)^3 = -8


# Run the tests
if __name__ == "__main__":
    unittest.main()
