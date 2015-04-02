class Panda:

    def __init__(self, name, email, gender):
        self.name = name
        self.email = email
        self.gender = gender
        self.pandasInTheNetwork = {}

    def make_frends(self, panda1, panda2):
        self.pandasInTheNetwork[panda1] = panda2
        self.pandasInTheNetwork[panda2] = panda1
        print(self.pandasInTheNetwork)



p1 = Panda('gogo', 'email', 'male')
p2 = Panda('pepa', 'email', 'female')
p3 = Panda('rossy', 'email', 'female')
p3.make_frends(p1, p2)
