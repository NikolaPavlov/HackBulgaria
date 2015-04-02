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