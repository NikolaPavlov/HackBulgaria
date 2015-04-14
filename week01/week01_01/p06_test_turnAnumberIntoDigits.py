import unittest

from p06_turnAnumberIntoDigits import to_digits


class TestNumberToDigits(unittest.TestCase):

    def test_to_digits(self):
        self.assertEqual(to_digits(123023), [1, 2, 3, 0, 2, 3])

if __name__ == "__main__":
    unittest.main()
