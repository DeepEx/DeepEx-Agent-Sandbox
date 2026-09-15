import unittest

from calculator import add, divide


class CalculatorTests(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)

    def test_divide_positive_numbers(self):
        self.assertEqual(divide(6, 3), 2)

    def test_divide_returns_negative_result(self):
        self.assertEqual(divide(-6, 3), -2)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            divide(6, 0)


if __name__ == "__main__":
    unittest.main()
