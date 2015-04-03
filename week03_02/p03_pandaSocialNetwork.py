# Fucking pandas everywhere. Where the fuck am I dude?
from p03_pandaClass import Panda


class PandaSocialNetwork:

    def __init__(self):
        self.pandasInTheNetwork = {}

    def getAllPandasInTheNetwork(self):
        for panda in self.pandasInTheNetwork:
            print(panda)

    def add_panda(self, panda):
        self.pandasInTheNetwork[panda] = []

    def has_panda(self, panda):
        if panda in self.pandasInTheNetwork:
            return True
        else:
            return False

    def make_frends(self, panda1, panda2):
        if panda1 not in self.pandasInTheNetwork:
            self.add_panda(panda1)
        if panda2 not in self.pandasInTheNetwork:
            self.add_panda(panda2)

        self.pandasInTheNetwork[panda1].append(panda2)
        self.pandasInTheNetwork[panda2].append(panda1)

    def are_frends(self, panda1, panda2):
        if self.pandasInTheNetwork[panda1] == panda2:
            if self.pandasInTheNetwork[panda2] == panda1:
                return True
        else:
            return False

    def frends_of(self, panda):
        return self.pandasInTheNetwork[panda]

    def connection_level(self, panda1, panda2):
        pass

    def are_connected(self, panda1, panda2):
        pass

    def how_many_gender_in_network(self, level, panda, gender):
        pass

###############################################

# Tests the old way (the gold way)
gogo = Panda("Gogo", "gogo@mail.bg", "male")
pepa = Panda("Pepa", "pepa@mail.bg", "female")
network = PandaSocialNetwork()
network.add_panda(gogo)
network.add_panda(pepa)
network.make_frends(pepa, gogo)
print(network.are_frends(pepa, gogo))

network.getAllPandasInTheNetwork()


