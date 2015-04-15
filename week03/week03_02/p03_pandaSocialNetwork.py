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
            raise ValueError("panda already registered!")

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
        if panda1 in self.pandasInTheNetwork[panda2]:
            if panda2 in self.pandasInTheNetwork[panda1]:
                return True
            return False
        return False

    def friends_of(self, panda):
        if panda not in self.pandasInTheNetwork:
            return False
        return self.pandasInTheNetwork[panda]

    def connection_level(self, panda1, panda2):
        pass

    def are_connected(self, panda1, panda2):
        pass

    def how_many_gender_in_network(self, level, panda, gender):
        pass

    def save(self, filename):
        container = {}
        for panda in self.pandasInTheNetwork:
            if repr(panda) not in container:
                container[repr(panda)] = []
            for friend in self.pandasInTheNetwork[panda]:
                container[repr(panda)].append(repr(friend))

        json_string = json.dumps(container, indent=8)

        with open(filename, 'w') as f:
            f.write(json_string)

        print('The network is saved!')

    def load(self, filename):
        json_container = {}

        with open(filename, 'r') as f:
            json_container = json.load(f)

        for panda in json_container:
            split_panda = panda.split(' - ')
            temp_panda = Panda(
             name=split_panda[0], email=split_panda[1], gender=split_panda[2])
            self.add_panda(temp_panda)
            for friend in json_container[panda]:
                # print(friend)
                split_panda = panda.split(' - ')
                temp_friend = Panda(name=split_panda[0], \
                    email=split_panda[1], gender=split_panda[2])
                self.make_friends(temp_panda, temp_friend)


if __name__ == "__main__":
    # A -> B -> C -> D -> A
    # p1 = Panda("A", "asda@mail.bg", "male")
    # p2 = Panda("B", "asdasd@mail.bg", "female")
    # p3 = Panda("C", "asdads@mail.bg", "male")
    # p4 = Panda("D", "asdada@mail.bg", "female")
    network = PandaSocialNetwork()
    # network.make_friends(p1, p2)
    # network.make_friends(p2, p3)
    # network.make_friends(p3, p4)
    # network.make_friends(p4, p1)

    # network.save('gogo-net')
    network.load('gogo-net')
    print(network.pandasInTheNetwork)