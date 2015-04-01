import unittest

from p15_hackNumbers import next_hack


class TestNextHack(unittest.TestCase):

    def test_next_hack1(self):
        self.assertEqual(next_hack(8031), 8191)

    def test_next_hack2(self):
        self.assertEqual(next_hack(10), 21)


if __name__ == "__main__":
    unittest.main()
