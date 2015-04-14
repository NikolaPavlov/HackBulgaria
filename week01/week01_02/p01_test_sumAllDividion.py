import unittest

from p01_sumAllDividion import sum_of_divisors


class TestSumOfDivisors(unittest.TestCase):

    def test_sum_of_divisors(self):
        self.assertEqual(sum_of_divisors(8), 15)


if __name__ == "__main__":
    unittest.main()
