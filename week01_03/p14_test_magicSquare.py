import unittest

from p14_magicSquare import magic_square


class TestMagicSquare(unittest.TestCase):

    def test_magic_square1(self):
        self.assertFalse(magic_square([[1,2,3], [4,5,6], [7,8,9]]))

    def test_magic_square2(self):
        self.assertTrue(magic_square([[7,12,1,14], [2,13,8,11], [16,3,10,5], [9,6,15,4]]))

if __name__ == "__main__":
    unittest.main()
