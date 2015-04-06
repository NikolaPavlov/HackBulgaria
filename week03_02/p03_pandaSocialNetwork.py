# Fucking pandas everywhere. Where the fuck am I dude?

import json
from p03_pandaClass import Panda


class PandaSocialNetwork:

    def __init__(self):
        self.pandasInTheNetwork = {}

    def add_panda(self, panda):
        if str(panda) not in self.pandasInTheNetwork:
            self.pandasInTheNetwork[str(panda)] = []
        else:
            pass

    def has_panda(self, panda):
        if str(panda) in self.pandasInTheNetwork:
            return True
        else:
            return False

    def make_frends(self, panda1, panda2):
        if panda1 not in self.pandasInTheNetwork:
            self.add_panda(panda1)
        if panda2 not in self.pandasInTheNetwork:
            self.add_panda(panda2)

        self.pandasInTheNetwork[str(panda1)].append(str(panda2))
        self.pandasInTheNetwork[str(panda2)].append(str(panda1))

    def are_frends(self, panda1, panda2):
        if str(panda1) in self.pandasInTheNetwork[str(panda2)] and \
            str(panda2) in self.pandasInTheNetwork[str(panda1)]:
            return True
        return False

    def frends_of(self, panda):
        if str(panda) not in self.pandasInTheNetwork:
            return False
        return self.pandasInTheNetwork[str(panda)]

    def connection_level(self, panda1, panda2):
        pass

    def are_connected(self, panda1, panda2):
        pass

    def how_many_gender_in_network(self, level, panda, gender):
        pass

###############################################