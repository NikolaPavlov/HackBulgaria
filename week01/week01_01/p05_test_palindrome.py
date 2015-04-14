import unittest

from p05_palindrome import palindrome


class TestPalindrome(unittest.TestCase):

    def test_palindrome1(self):
        self.assertTrue(palindrome("kapak"))

    def test_palindrome2(self):
        self.assertTrue(palindrome("121"))

    def test_palindrome3(self):
        self.assertFalse(palindrome("baba"))


if __name__ == "__main__":
    unittest.main()
