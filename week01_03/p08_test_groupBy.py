import unittest

from p08_groupBy import groupby


class TestGroupBy(unittest.TestCase):

    def test_group_by(self):
        self.assertEqual(groupby(lambda x: x % 2, [0,1,2,3,4,5,6,7]),
            {0: [0, 2, 4, 6], 1: [1, 3, 5, 7]})


if __name__ == "__main__":
    unittest.main()
