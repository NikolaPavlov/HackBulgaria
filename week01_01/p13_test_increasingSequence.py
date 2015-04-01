import unittest

from p13_increasingSequence import is_increasing


class TestIsIncreasing(unittest.TestCase):

    def test_is_increasing1(self):
        self.assertTrue(is_increasing([1, 2, 3, 4, 5]))


    def test_is_increasing2(self):
        self.assertFalse(is_increasing([5, 6, -10]))


if __name__ == "__main__":
    unittest.main()
