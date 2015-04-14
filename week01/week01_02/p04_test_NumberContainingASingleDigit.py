import unittest

from p04_NumberContainingASingleDigit import contains_digit


class TestContainsDigit(unittest.TestCase):

    def test_contains_digit(self):
        self.assertTrue(contains_digit(1000, 0))

    def test_not_contains_digit(self):
        self.assertFalse(contains_digit(123, 4))


if __name__ == "__main__":
    unittest.main()
