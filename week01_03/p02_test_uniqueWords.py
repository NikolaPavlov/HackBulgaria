import unittest

from p02_uniqueWords import unique_words_count


class TestUniqueWordsCount(unittest.TestCase):

    def test_unique_words_count(self):
        self.assertEqual(unique_words_count(["apple", "banana", "apple", "pie"]), 3)


if __name__ == "__main__":
    unittest.main()
