import unittest

from p01_countWords import count_words


class TestCountWords(unittest.TestCase):

    def test_count_words(self):
        self.assertEqual(count_words(["apple", "banana", "apple", "pie"]),
        {'banana': 1, 'apple': 2, 'pie': 1})


if __name__ == "__main__":
    unittest.main()
