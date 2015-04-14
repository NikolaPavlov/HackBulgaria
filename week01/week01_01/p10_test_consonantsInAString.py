import unittest

from p10_consonantsInAString import count_consonants


class TestCountConsonants(unittest.TestCase):

    def test_count_consonants(self):
        self.assertEqual(count_consonants("Python"), 4)

if __name__ == "__main__":
    unittest.main()
