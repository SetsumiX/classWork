import unittest

class Calculator:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def subtract(a, b):
        return a - b

    @staticmethod
    def multiply(a, b):
        return a * b

    @staticmethod
    def division(a, b):
        if b == 0:
            raise ValueError("Делить на ноль нельзя")
        return a / b

    @staticmethod
    def power(a, b):
        return a**b

    @staticmethod
    def maximum(a, b):
        return a if a > b else b

    @staticmethod
    def minimum(a, b):
        return a if a < b else b

    @staticmethod
    def percentage(number, percent):
        if percent < 0 or percent > 100:
            raise ValueError("Процент должен быть от 0 до 100")
        return (number * percent)/100

class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(Calculator.add(2, 3), 5)
        self.assertEqual(Calculator.add(-1, 1), 0)
        self.assertEqual(Calculator.add(0, 0), 0)

    def test_sub(self):
        self.assertEqual(Calculator.subtract(5, 3), 2)
        self.assertEqual(Calculator.subtract(3, 5), -2)

    def test_mult(self):
        self.assertEqual(Calculator.multiply(2,5), 10)
        self.assertEqual(Calculator.multiply(-2, 10), -20)
        self.assertEqual(Calculator.multiply(0, 2), 0)

    def test_div(self):
        self.assertEqual(Calculator.division(10, 5), 2)
        self.assertEqual(Calculator.division(-6, 2), -3)
        self.assertAlmostEqual(Calculator.division(1, 3), 0.333333, places=6)
        with self.assertRaises(ValueError):
            Calculator.division(1, 0)

    def test_max(self):
        self.assertEqual(Calculator.maximum(6, 3), 6)
        self.assertEqual(Calculator.maximum(3, 6), 6)
        self.assertEqual(Calculator.maximum(2, 2), 2)
        self.assertEqual(Calculator.maximum(-1, -2), -1)

    def test_min(self):
        self.assertEqual(Calculator.minimum(2, 3), 2)
        self.assertEqual(Calculator.minimum(3, 2), 2)
        self.assertEqual(Calculator.minimum(2, 2), 2)

    def test_per(self):
        self.assertEqual(Calculator.percentage(100, 5), 5)
        self.assertEqual(Calculator.percentage(200, 25), 50)
        with self.assertRaises(ValueError):
            Calculator.percentage(100, -10)
        with self.assertRaises(ValueError):
            Calculator.percentage(100, 120)

    def test_pow(self):
        self.assertEqual(Calculator.power(2, 3), 8)
        self.assertEqual(Calculator.power(5, 0), 1)
        self.assertEqual(Calculator.power(4, 0.5), 2)

# print(Calculator.add(1, 1))
if __name__ == "__main__":
    unittest.main()