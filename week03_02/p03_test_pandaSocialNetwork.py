import unittest

from p03_pandaSocialNetwork import Panda, PandaSocialNetwork


class TestPandaSocialNetwork(unittest.TestCase):

    def setUp(self):
        self.socialNetwork = PandaSocialNetwork()
        self.panda1 = Panda("Gogo", "gogo@mail.bg", "male")
        self.panda2 = Panda("Pepa", "pepa@mail.bg", "female")
        self.panda3 = Panda("Uruspia", "omg@mail.bg", "female")
        #self.socialNetwork = PandaSocialNetwork()
        #self.socialNetwork.pandasInTheNetwork = {}
        #self.socialNetwork.add_panda(self.panda1)

    def test_add_panda(self):
        self.socialNetwork.add_panda(self.panda1)

    def test_has_panda(self):
        self.socialNetwork.has_panda(self.panda1)

    def test_make_frends(self):
        self.socialNetwork.make_frends(self.panda1, self.panda2)

    def test_frends_of(self):
        self.socialNetwork.frends_of(self.panda1)

if __name__ == "__main__":
    unittest.main()