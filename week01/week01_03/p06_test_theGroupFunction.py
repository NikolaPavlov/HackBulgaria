import unittest

from p06_theGroupFunction import group


class TestGroup(unittest.TestCase):

    def test_group(self):
        self.assertEqual(group([1, 1, 1, 2, 3, 1, 1, 1]), [[1, 1, 1], [2], [3], [1, 1, 1]])


if __name__ == "__main__":
    unittest.main()
