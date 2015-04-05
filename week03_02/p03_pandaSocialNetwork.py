# Fucking pandas everywhere. Where the fuck am I dude?
from p03_pandaClass import Panda


class PandaSocialNetwork:

    def __init__(self):
        self.pandasInTheNetwork = {}

    def add_panda(self, panda):
        self.pandasInTheNetwork[str(panda)] = []

    def has_panda(self, panda):
        if panda in self.pandasInTheNetwork:
            return True
        else:
            return False

    def make_frends(self, panda1, panda2):
        if panda1 not in self.pandasInTheNetwork:
            self.add_panda(str(panda1))
        if panda2 not in self.pandasInTheNetwork:
            self.add_panda(str(panda2))

        self.pandasInTheNetwork[str(panda1)].append(str(panda2))
        self.pandasInTheNetwork[str(panda2)].append(str(panda1))

    def are_frends(self, panda1, panda2):
        if str(panda1) in self.pandasInTheNetwork[str(panda2)] and \
            str(panda2) in self.pandasInTheNetwork[str(panda1)]:
            return True
        return False

    def frends_of(self, panda):
        return self.pandasInTheNetwork[str(panda)]

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
rado = Panda("rado", "gg@mail.bg", "male")
network = PandaSocialNetwork()
network.add_panda(gogo)
network.add_panda(pepa)
network.add_panda(rado)
network.make_frends(gogo, pepa)
print(network.are_frends(gogo, pepa))
print(network.frends_of(gogo))