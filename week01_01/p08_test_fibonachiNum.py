import unittest

from p08_fibonachiNum import fib_number


class TestFibNumber(unittest.TestCase):

    def test_fib_number(self):
        self.assertEqual(fib_number(3), 112)

if __name__ == "__main__":
    unittest.main()
