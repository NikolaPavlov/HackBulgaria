import unittest

from p03_CheckIfANumberHasAPrimeNumberOfDivisors import prime_number_of_divisiors


class TestPrimeNumOfDivisiors(unittest.TestCase):

    def test_prime_number_of_divisors(self):
        self.assertTrue(prime_number_of_divisiors(7))

    def test_not_prime_number_of_divisors(self):
        self.assertFalse(prime_number_of_divisiors(8))


if __name__ == "__main__":
    unittest.main()
