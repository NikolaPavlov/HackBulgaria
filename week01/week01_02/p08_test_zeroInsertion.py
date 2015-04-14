# TODO: More test for this problem
import unittest

from p08_zeroInsertion import zero_insert


class TestZeroInsert(unittest.TestCase):

    def test_zero_insert(self):
        self.assertEqual(zero_insert(116457), [1, 0, 1, 6, 0, 4, 5, 7])


if __name__ == "__main__":
    unittest.main()
