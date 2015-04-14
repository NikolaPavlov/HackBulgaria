import unittest

from p09_sumNumbersInMatrix import sum_matrix


class TestSumMatrix(unittest.TestCase):

    def test_sum_matrix(self):
        self.assertEqual(sum_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), 45)


if __name__ == "__main__":
    unittest.main()
