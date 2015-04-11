import unittest

from p04_anImmutableFraction import Fraction


class TestFraction(unittest.TestCase):

    def setUp(self):
        self.a = Fraction(1, 2)
        self.b = Fraction(2, 4)
        self.c = Fraction(1, 2)

    def test_constructor(self):
        self.assertIsInstance(self.a, Fraction)

    def test_to_str(self):
        self.assertEqual(str(self.a), "1 / 2")

    def test_eq(self):
        self.assertTrue(self.a == self.c)

    def test_eq_false(self):
        self.assertFalse(self.a == self.b)

    def test_add(self):
        self.assertEqual((self.a + self.b), 1)

    def test_sub(self):
        self.assertEqual((self.a - self.b), 0)

    def test_multiplication(self):
        self.assertEqual((self.a * self.b), 1)



if __name__ == "__main__":
    unittest.main()
