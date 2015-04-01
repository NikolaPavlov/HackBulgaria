import unittest

from p03_pandaSocialNetwork import Panda, PandaSocialNetwork


class TestPandaSocialNetwork(unittest.TestCase):

    def setUp(self):
        self.panda1 = Panda("Gogo", "gogo@mail.bg", "male")
        self.panda2 = Panda("Pepa", "pepa@mail.bg", "female")
        self.panda3 = Panda("Uruspia", "omg@mail.bg", "female")
        #self.socialNetwork = PandaSocialNetwork()
        #self.socialNetwork.pandasInTheNetwork = {}
        #self.socialNetwork.add_panda(self.panda1)

    def test_add_panda(self):
        pass

if __name__ == "__main__":
    unittest.main()