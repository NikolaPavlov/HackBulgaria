import unittest

from p07_LongestSubsequenceOfEqualConsecutiveElements import max_consecutive


class TestMaxConsecutive(unittest.TestCase):

    def test_max_consecutive(self):
        self.assertEqual(max_consecutive([1, 2, 3, 3, 3, 3, 4, 3, 3]), 4)


if __name__ == "__main__":
    unittest.main()
