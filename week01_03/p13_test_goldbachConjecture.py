import unittest

from p13_goldbachConjecture import formatTheResult


class TestGoldbach(unittest.TestCase):

    def test_goldbach1(self):
        self.assertEqual(formatTheResult(10), [(3, 7), (5, 5)])

    def test_goldbach2(self):
        self.assertEqual(formatTheResult(100),
            [(3, 97), (11, 89), (17, 83), (29, 71), (41, 59), (47, 53)])


if __name__ == "__main__":
    unittest.main()
