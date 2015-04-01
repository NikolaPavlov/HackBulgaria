import unittest

from p07_turnAlistOfDigitsIntoNum import to_number


class TestToNumber(unittest.TestCase):

    def test_to_number1(self):
        self.assertEqual(to_number([1, 2, 3]), 123)


    def test_to_number2(self):
        self.assertEqual(to_number([1, 2, 3, 0, 2, 3]), 123023)

if __name__ == "__main__":
    unittest.main()
