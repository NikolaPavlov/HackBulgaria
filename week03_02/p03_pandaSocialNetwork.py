#fucking pandas everywhere. Where the fuck am I dude?
###############################################


class PandaSocialNetwork:

    def __init__(self):
        self.pandasInTheNetwork = {}

    def add_panda(self, Panda):
        self.pandasInTheNetwork[Panda] = 1

    def has_panda(self, Panda):
        if Panda in self.pandasInTheNetwork:
            return True
        else:
            return False
### dosen't work shit happened
    def make_frends(self, Panda1, Panda2):
        if Panda1 in self.pandasInTheNetwork:
            self.pandasInTheNetwork[Panda1] = [Panda2]
        if Panda2 in self.pandasInTheNetwork:
            self.pandasInTheNetwork[Panda2] = [Panda1]

        self.pandasInTheNetwork[Panda1].append(Panda2)
        self.pandasInTheNetwork[Panda2].append(Panda1)


    def are_frends(self, Panda1, Panda2):
        pass

    def frends_of(self, Panda):
        pass

    def connection_level(self, Panda1, Panda2):
        pass

    def are_connected(self, Panda1, Panda2):
        pass

    def how_many_gender_in_network(self, level, Panda, gender):
        pass

###############################################

# Test 
gogo = Panda("Gogo", "gogo@mail.bg", "male")
pepa = Panda("Pepa", "pepa@mail.bg", "female")
network = PandaSocialNetwork()
network.add_panda(gogo)
print(network.has_panda(gogo))
network.make_frends(gogo, pepa)
