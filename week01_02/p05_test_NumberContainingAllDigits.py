import unittest

from p05_NumberContainingAllDigits import contains_digits


class TestContainsDigit(unittest.TestCase):

    def test_contains_digit(self):
        self.assertTrue(contains_digits(402123, [0, 3, 4]))

    def test_not_contains_digit(self):
        self.assertFalse(contains_digits(666, [6, 4]))



if __name__ == "__main__":
    unittest.main()
