import unittest

from p06_isNumberBalanced import is_number_balanced


class TestIsNumberBalanced(unittest.TestCase):

    def test_is_number_balanced(self):
        self.assertTrue(is_number_balanced(1238033))

    def test_is_number_not_balanced(self):
        self.assertFalse(is_number_balanced(28471))


if __name__ == "__main__":
    unittest.main()
