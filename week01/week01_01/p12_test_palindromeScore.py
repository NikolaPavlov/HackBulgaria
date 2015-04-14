import unittest

from p12_palindromeScore import p_score


class TestPalindromeScope(unittest.TestCase):

    def test_p_scope(self):
        self.assertEqual(p_score(198), 6)

if __name__ == "__main__":
    unittest.main()
