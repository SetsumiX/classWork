import math, unittest

class Fraction:
    def __init__(self, numerator, denominator=1):
        if denominator == 0:
            raise ValueError("Знаменатель не может быть нулём")
        common_division = math.gcd(numerator, denominator)
        self.numerator = numerator // common_division
        self.denominator = denominator // common_division

        if self.denominator < 0:
            self.numerator *= -1
            self.denominator *= -1

    def __add__(self, other):
        new_denominator = self.denominator * other.denominator
        new_numerator = self.numerator * other.denominator + other.numerator * self.denominator
        return Fraction(new_numerator, new_denominator)

    def __sub__(self, other):
        new_denominator = self.denominator * other.denominator
        new_numinator = self.numerator * other.denominator - other.numerator * self.denominator
        return Fraction(new_numinator, new_denominator)

    def __mul__(self, other):
        new_denominator = self.denominator * other.denominator
        new_numinator = self.numerator * other.numerator
        return Fraction(new_numinator, new_denominator)

    def __truediv__(self, other):
        if other.numerator == 0:
            raise ValueError("Нельзя делить на ноль")
        new_denominator = self.denominator * other.numerator
        new_numinator = self.numerator * other.denominator
        return Fraction(new_numinator, new_denominator)

    def __eq__(self, other):
        return self.numerator == other.numerator and self.numerator == other.denominator

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

class TestFraction(unittest.TestCase):
    def test_init(self):
        f = Fraction(2, 4)
        self.assertEqual(f.numerator, 1)
        self.assertEqual(f.denominator, 2)

        f = Fraction(-1, -2)
        self.assertEqual(f.numerator, 1)
        self.assertEqual(f.denominator, 2)

        with self.assertRaises(ValueError):
            Fraction(1, 0)

    def test_add(self):
        f1 = Fraction(1, 2)
        f2 = Fraction(1, 3)
        result = f1 + f2
        self.assertEqual(result.numerator, 5)
        self.assertEqual(result.denominator, 6)

        f3 = Fraction(3)
        result = f1 + f3
        self.assertEqual(result.numerator, 7)
        self.assertEqual(result.denominator, 2)

    def test_sub(self):
        f1 = Fraction(1, 2)
        f2 = Fraction(1, 3)
        result = f1 - f2
        self.assertEqual(result.numerator, 1)
        self.assertEqual(result.denominator, 6)

    def test_mul(self):
        f1 = Fraction(1, 2)
        f2 = Fraction(1, 3)
        result = f1 * f2
        self.assertEqual(result.numerator, 1)
        self.assertEqual(result.denominator, 3)

    def test_div(self):
        f1 = Fraction(1, 2)
        f2 = Fraction(1, 3)
        result = f1 / f2
        self.assertEqual(result.numerator, 3)
        self.assertEqual(result.denominator, 4)
        with self.assertRaises(ValueError):
            f1 / Fraction(0, 1)

if __name__ == "__main__":
    unittest.main()
