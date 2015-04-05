import unittest

from p03_pandaClass import Panda


class TestPandaClass(unittest.TestCase):

    def setUp(self):
        self.panda1 = Panda('Gogo', 'gogo@email.com', 'male')
        self.panda2 = Panda('Pepa', 'pepa@maiil.bgbg', 'female')

    def test_constructor(self):
        self.assertIsInstance(self.panda1, Panda)

    def test_get_name(self):
        self.assertEqual(self.panda1.get_name(), "Gogo")

    def test_get_email(self):
        self.assertTrue(self.panda1.get_email(), "gogo@email.com")

    def test_get_gender(self):
        self.assertTrue(self.panda1.get_gender(), "male")

    def test_eq(self):
        self.assertTrue(self.panda1 == self.panda1)

    def test_eq_false(self):
        self.assertFalse(self.panda1 == self.panda2)

    def test_to_str(self):
        self.assertEqual(str(self.panda1), "Gogo")

    def test_hash(self):
        self.assertIsNotNone(hash(self.panda1))

    def test_is_male_true(self):
        self.assertTrue(self.panda1.is_male())

    def test_is_male_fail(self):
        self.assertFalse(self.panda2.is_male())

    def test_is_female_true(self):
        self.assertTrue(self.panda2.is_female())

if __name__ == "__main__":
    unittest.main()
