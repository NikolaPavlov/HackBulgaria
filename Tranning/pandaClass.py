class Panda:

    def __init__(self, name, email, gender):
        self.name = name
        self.email = email
        self.gender = gender

    def __str__(self):
        return ("{} - {} - {}".format(self.name, self.email, self.gender))

    def __eq__(self, other):
        if self.name == other.name and \
            self.email == other.email and \
            self.gender == other.gender:
            return True
        return False

    def __hash__(self):
        return hash(self.name)


class Network:

    def __init__(self):
        self.pandas = {}

    def add_panda(self, panda):
        self.pandas[str(panda)] = []

    def make_frends(self, panda1, panda2):
        if str(panda1) not in self.pandas:
            self.pandas[str(panda1)] = []
        if str(panda2) not in self.pandas:
            self.pandas[str(panda2)] = []

        self.pandas[str(panda1)].append(str(panda2))
        self.pandas[str(panda2)].append(str(panda1))

    def are_frends(self, panda1, panda2):
        return str(panda2) in self.pandas[str(panda1)] and \
        str(panda1) in self.pandas[str(panda2)] 





# Tests
net = Network()
p1 = Panda("GoGo", "email", "m")
p2 = Panda("rados", "email", "m")
p3 = Panda("nino", "email", "m")
net.add_panda(p1)
net.add_panda(p2)
net.make_frends(p1, p2)
print(net.are_frends(p1, p2))
print(net.are_frends(p1, p3))
print(net.pandas)