import unittest

from p11_wordFrom_anbn import is_an_bn


class TestIsAnBn(unittest.TestCase):

    def test_is_an_bn_empty(self):
        self.assertTrue(is_an_bn(''))

    def test_is_an_bn(self):
        self.assertTrue(is_an_bn('aaabbb'))

    def test_isnot_an_bn(self):
        self.assertFalse(is_an_bn('rado'))


if __name__ == "__main__":
    unittest.main()
