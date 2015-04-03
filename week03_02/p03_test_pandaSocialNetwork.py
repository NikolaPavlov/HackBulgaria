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

    def test_hasnot_panda(self):
        self.assertFalse(self.socialNetwork.has_panda(self.panda3))

    def test_eq(self):
        self.assertTrue(self.panda1 == self.panda1)
    #BooM!
    # def test_make_frends(self):
        # self.socialNetwork.make_frends(self.panda1, self.panda2)

    def test_are_frends(self, other):
        self.assertTrue(self.socialNetwork.are_frends(self.panda1, self.panda2))

if __name__ == "__main__":
    unittest.main()