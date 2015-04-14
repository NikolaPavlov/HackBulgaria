import unittest

from p09_VowelsInAString import count_vowels


class TestCountVowels(unittest.TestCase):

    def test_count_vowels(self):
        self.assertTrue(count_vowels("Python"), 2)


if __name__ == "__main__":
    unittest.main()
