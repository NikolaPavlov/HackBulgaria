import re


class Panda:

    def validate_email(self, email):
        if re.match(
            r"^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$", email):
            return True
        else:
            return False

    def __init__(self, name, email, gender):
        if self.validate_email(email):
            self.email = email
        else:
            raise ValueError("Email is not real!")

        self.name = name
        self.gender = gender

    def get_name(self):
        return self.name

    def get_email(self):
        return self.email

    def get_gender(self):
        return self.gender

    def __str__(self):
        return "I am {}-Panda, with email: {}, {}". \
        format(self.name, self.email, self.gender)

    def __repr__(self):
        return "{} - {} - {}".format(self.name, self.email, self.gender)

    def __hash__(self):
        return hash((self.name, self.email, self.gender))

    def __eq__(self, other):
        return (self.name, self.email, self.gender) == \
        (other.name, other.email, other.gender)

    def is_male(self):
        return str.lower(self.gender) == "male"

    def is_female(self):
        return str.lower(self.gender) == "female"
