# Ghost fail in this test WTF dude! ( False assertFalse dosen't work correct! )
import unittest

from p02_checkIfNumberIsPrime import is_prime


class TestIsPrime(unittest.TestCase):

    def test_is_prime1(self):
        self.assertFalse(1)

    def test_is_prime2(self):
        self.assertTrue(2)

    def test_is_prime3(self):
        self.assertFalse(8)

    def test_is_prime4(self):
        self.assertTrue(11)

    def test_is_prime5(self):
        self.assertFalse(-10)

if __name__ == "__main__":
    unittest.main()
