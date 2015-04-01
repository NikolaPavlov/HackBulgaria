import unittest

from p03_sumAllDigitsOfNum import sum_of_digits


class TestSumOfDigits(unittest.TestCase):

    def test_sum_of_digits_value1(self):
        self.assertEqual(sum_of_digits(123), 6)

    def test_sum_of_digits_value2(self):
        self.assertEqual(sum_of_digits(-10), 1)


if __name__ == "__main__":
    unittest.main()
