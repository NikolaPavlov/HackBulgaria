import unittest

from p03_nanExpand import nan_expand


class TestNanExpand(unittest.TestCase):

    def test_nan_expand(self):
        self.assertEqual(nan_expand(3), "Not a Not a Not a NaN")


if __name__ == "__main__":
    unittest.main()
