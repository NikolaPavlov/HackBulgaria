#fucking pandas everywhere. Where the fuck am I dude?
import re


class Panda:

    def email_validator(email):
        EMAIL_REGEX = re.compile(r"^[\w\.\+\-]+\@[\w]+\.[a-z]{2,3}$")
        if not EMAIL_REGEX.match(email):
            return False
        else:
            return True

    def __init__(self, name, email, gender):
        self.name = name
        self.email = email
        self.gender = gender

    def nameOfThePanda(self):
        return self.name

    def email(self):
        return self.email

    def gender(self):
        return self.gender

    def __str__(self):
        return str(self.name + ' ' + self.email + ' ' + self.gender)

    def __hash__(self):
        return hash(self.name.__str__())

    def __eq__(self, other):
        # first Kpk way (my way)
        if self.name == other.name:
            if self.email == other.email:
                if self.gender == other.gender:
                    return True
        return False

        # second Kpk way (Ivo way)
        '''
        names = self.name == other.name
        emails = self.email == other.email
        genders = self.gender == other.gender

        return names and emails and genders
        '''

    def is_male(self):
        return str.lower(self.gender) == "male"

    def is_female(self):
        return str.lower(self.gender) == "female"

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
