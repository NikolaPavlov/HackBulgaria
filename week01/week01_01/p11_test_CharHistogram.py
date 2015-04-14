import unittest

from p11_CharHistogram import char_histogram


class TestCharHistogram(unittest.TestCase):

    def test_char_histogram(self):
        self.assertEqual(char_histogram("Python!"),
            {'t': 1, '!': 1, 'o': 1, 'n': 1, 'y': 1, 'P': 1, 'h': 1})

if __name__ == "__main__":
    unittest.main()
