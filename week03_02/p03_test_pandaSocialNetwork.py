import unittest

from p03_pandaSocialNetwork import Panda, PandaSocialNetwork


class TestPandaSocialNetwork(unittest.TestCase):

    def setUp(self):
        self.socialNetwork = PandaSocialNetwork()
        self.panda1 = Panda("Gogo", "gogo@mail.bg", "male")
        self.panda2 = Panda("Pepa", "pepa@mail.bg", "female")
        self.panda3 = Panda("Uruspia", "omg@mail.bg", "female")

    def test_constructor_network(self):
        self.assertTrue(isinstance(self.socialNetwork, PandaSocialNetwork))

    def test_add_panda(self):
        self.socialNetwork.add_panda(self.panda1)

    def test_has_panda(self):
        self.assertTrue(self.socialNetwork.has_panda(self.panda1))

    def test_hasnot_panda(self):
        self.assertFalse(self.socialNetwork.has_panda(self.panda3))
        self.assertFalse(self.panda3 in self.socialNetwork)


if __name__ == "__main__":
    unittest.main()
