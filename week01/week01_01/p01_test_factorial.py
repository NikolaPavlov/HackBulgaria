import unittest

from p01_factorial import factorial

class testFactorial(unittest.TestCase):
    def test_value_fact1(self):
        self.assertEqual(factorial(0), 1)

    def test_value_fact2(self):
        self.assertEqual(factorial(1), 1)

    def test_value_fact3(self):
        self.assertEqual(factorial(5), 120)

if __name__ == "__main__":
    unittest.main()
