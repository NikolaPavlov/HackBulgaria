import unittest

from p04_factorialDigits import fact_digits


class TestFactorialDigits(unittest.TestCase):
    def test_fact_digits_value1(self):
        self.assertEqual(fact_digits(145), 145)


    def test_fact_digits_value2(self):
        self.assertEqual(fact_digits(999), 1088640)

if __name__ == "__main__":
    unittest.main()