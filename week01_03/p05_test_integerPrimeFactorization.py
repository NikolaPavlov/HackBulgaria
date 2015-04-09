import unittest

from p05_integerPrimeFactorization import prime_factorization


class TestPrimeFactorization(unittest.TestCase):

    def test_prime_fact1(self):
        self.assertEqual(prime_factorization(10), ((2, 1), (5, 1)))

    def test_prime_fact2(self):
        self.assertEqual(prime_factorization(1000), ((2, 3), (5, 3)))


if __name__ == "__main__":
    unittest.main()
