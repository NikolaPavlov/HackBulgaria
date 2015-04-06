import re


class Panda:

    def validate_email(self, email):
        return re.match(r"^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$", email)

    def __init__(self, name, email, gender):
        self.name = name

        if self.validate_email(email):
            self.email = email
        else:
            raise ValueError("Email is not real!")

        self.gender = gender

    def get_name(self):
        return str(self.name)

    def get_email(self):
        return self.email

    def get_gender(self):
        return self.gender

    def __str__(self):
        return self.name

    def __repr__(self):
        return "{} - {} - {}".format(self.name, self.email, self.gender)

    def __hash__(self):
        return hash(self.name + self.email + self.gender)

    def __eq__(self, other):
        # first Kpk way (my way)
        if self.name == other.name:
            if self.email == other.email:
                if self.gender == other.gender:
                    return True
                return False
            return False
        return False

        '''
        # second Kpk way (Ivo way)
        names = self.name == other.name
        emails = self.email == other.email
        genders = self.gender == other.gender

        return names and emails and genders
        '''

    def is_male(self):
        return str.lower(self.gender) == "male"

    def is_female(self):
        return str.lower(self.gender) == "female"
