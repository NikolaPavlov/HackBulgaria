import unittest

from p14_decreasingSequence import is_decreasing


class TestIsDecreasing(unittest.TestCase):

    def test_is_decreasing(self):
        self.assertTrue(is_decreasing([5, 4, 3, 2, 1]))


if __name__ == "__main__":
    unittest.main()
