import unittest

from p07_CountingSubstrings import count_substrings


class TestCountSubstrings(unittest.TestCase):

    def test_count_substrings(self):
        self.assertEqual(count_substrings("Python is an awesome language to program in!", "o"), 4)


if __name__ == "__main__":
    unittest.main()
