import unittest

from p04_anImmutableFraction import Fraction


class TestFraction(unittest.TestCase):

    def setUp(self):
        self.a = Fraction(1, 2)
        self.b = Fraction(2, 4)
        self.c = Fraction(1, 2)
        self.d = Fraction(5, 6)
        self.a_plus_b = self.a + self.b

    def test_constructor(self):
        self.assertIsInstance(self.a, Fraction)

    def test_to_str(self):
        self.assertEqual(str(self.a), "1 / 2")

    def test_eq(self):
        self.assertTrue(self.a == self.c)

    def test_eq_false(self):
        self.assertFalse(self.a == self.d)

    # 1 / 2 + 2 / 4 =
    def test_add1(self):
        self.assertEqual(self.a + self.b, Fraction(1, 1))

    # 1 / 2 + 5 / 6 =
    def test_add2(self):
        self.assertEqual(self.a + self.d, Fraction(4, 3))

    # 1 / 2 - 1 / 2 =
    def test_sub1(self):
        self.assertTrue(self.a - self.b, Fraction(6, 6))

    # 1 / 2 - 5 / 6 =
    def test_sub2(self):
        self.assertEqual(self.a - self.d, Fraction(1, 3))

    # 1 / 2 * 1 / 2 =
    def test_multiplication1(self):
        self.assertEqual((self.a * self.b), Fraction(1, 4))

    # 1 / 2 * 5 / 6 =
    def test_multiplication2(self):
        self.assertEqual((self.a * self.d), Fraction(5, 12))


if __name__ == "__main__":
    unittest.main()
