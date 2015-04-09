import unittest

from p09_spamAndEggs import prepare_meal


class TestSpamAndEggs(unittest.TestCase):

    def test_spam_and_egg1(self):
        self.assertEqual(prepare_meal(3), "spam ")

    def test_spam_and_egg2(self):
        self.assertEqual(prepare_meal(45), "spam spam and eggs")

if __name__ == "__main__":
    unittest.main()
