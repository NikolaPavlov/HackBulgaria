import unittest

from p03_pandaSocialNetwork import Panda, PandaSocialNetwork


class TestPandaSocialNetwork(unittest.TestCase):

    def setUp(self):
        self.socialNetwork = PandaSocialNetwork()
        self.panda1 = Panda("Gogo", "gogo@mail.bg", "male")
        self.panda2 = Panda("Pepa", "pepa@mail.bg", "female")
        self.panda3 = Panda("Uruspia", "omg@mail.bg", "female")
        self.alone_panda = Panda("aloneOne", "mail@mail.bg", "female")
        self.socialNetwork.add_panda(self.panda1)
        self.socialNetwork.add_panda(self.panda2)
        self.socialNetwork.add_panda(self.panda3)
        self.socialNetwork.make_frends(self.panda1, self.panda2)
        self.socialNetwork.make_frends(self.panda2, self.panda3)

    def test_constructor_network(self):
        self.assertTrue(isinstance(self.socialNetwork, PandaSocialNetwork))

    def test_add_panda(self):
        self.socialNetwork.add_panda(self.panda1)
        self.assertTrue(self.panda1 in self.socialNetwork.pandasInTheNetwork)

    def test_has_panda(self):
        self.assertTrue(self.socialNetwork.has_panda(self.panda1))

    def test_hasnot_panda(self):
        self.assertFalse(self.socialNetwork.has_panda(self.alone_panda))

    def test_make_frends_and_are_frends(self):
        self.assertTrue(self.socialNetwork.are_frends(self.panda1, self.panda2))

    def test_frends_of(self):
        self.assertEqual(self.socialNetwork.frends_of(self.panda1), [self.panda2])

    def test_frends_of_invalid(self):
        self.assertFalse(self.socialNetwork.frends_of(self.alone_panda))


if __name__ == "__main__":
    unittest.main()
