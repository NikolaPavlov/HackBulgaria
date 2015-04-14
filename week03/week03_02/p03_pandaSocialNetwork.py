# Fucking pandas everywhere. Where the fuck am I dude?

import json
from p03_pandaClass import Panda


class PandaSocialNetwork:

    def __init__(self):
        self.pandasInTheNetwork = {}

    def add_panda(self, panda):
        if panda not in self.pandasInTheNetwork:
            self.pandasInTheNetwork[panda] = []
        else:
            pass

    def has_panda(self, panda):
        if panda in self.pandasInTheNetwork:
            return True
        else:
            return False

    def make_friends(self, panda1, panda2):
        if panda1 not in self.pandasInTheNetwork:
            self.add_panda(panda1)
        if panda2 not in self.pandasInTheNetwork:
            self.add_panda(panda2)

        self.pandasInTheNetwork[panda1].append(panda2)
        self.pandasInTheNetwork[panda2].append(panda1)

    def are_friends(self, panda1, panda2):
        if panda1 in self.pandasInTheNetwork[panda2] and \
            panda2 in self.pandasInTheNetwork[panda1]:
            return True
        return False

    def frends_of(self, panda):
        if panda not in self.pandasInTheNetwork:
            return False
        return self.pandasInTheNetwork[panda]

    def connection_level(self, panda1, panda2):
        pass

    def are_connected(self, panda1, panda2):
        pass

    def how_many_gender_in_network(self, level, panda, gender):
        pass

    def __repr__(self):
        content = {}

        for panda in self.pandasInTheNetwork:
            friends = [repr(panda_friend) for panda_friend in self.pandasInTheNetwork[panda]]
            content[repr(panda)] = friends

        return json.dumps(content, indent=True)

    def save(self, filename):
        with open(filename, 'w') as f:
            f.write(self.__repr__())


if __name__ == "__main__":
    # A -> B -> C -> D -> A
    p1 = Panda("A", "asda@mail.bg", "male")
    p2 = Panda("B", "asdasd@mail.bg", "female")
    p3 = Panda("C", "asdads@mail.bg", "male")
    p4 = Panda("D", "asdada@mail.bg", "female")
    network = PandaSocialNetwork()
    network.make_friends(p1, p2)
    network.make_friends(p2, p3)
    network.make_friends(p3, p4)
    network.make_friends(p4, p1)
    network.save("network.json")
