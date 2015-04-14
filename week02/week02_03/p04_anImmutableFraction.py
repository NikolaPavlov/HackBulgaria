# Fractions where is the fucking panda?


class Fraction:

    def __init__(self, nominator, denominator):
        self.nominator = nominator
        self.denominator = denominator

    def __str__(self):
        if self.nominator % self.denominator == 0:
            return str(int(self.nominator / self.denominator))
        else:
            return "{} / {}".format(self.nominator, self.denominator)

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        if self.nominator / self.denominator == \
        other.nominator / other.denominator:
            return True
        else:
            return False

    @staticmethod
    def reduce_fraction(fraction):
        for i in range(fraction.nominator, 0, -1):
            if fraction.nominator % i == 0 and \
            fraction.denominator % i == 0:
                fraction.nominator /= i
                fraction.denominator /= i
        return Fraction(int(fraction.nominator), int(fraction.denominator))

    def __add__(self, other):
        new_nominator = self.nominator * other.denominator + \
        self.denominator * other.nominator
        new_denominator = self.denominator * other.denominator
        new_fraction = Fraction(new_nominator, new_denominator)
        return Fraction.reduce_fraction(new_fraction)

    def __sub__(self, other):
        new_nominator = self.nominator * other.denominator - \
        self.denominator * other.nominator
        new_denominator = self.denominator * other.denominator
        new_fraction = Fraction(new_nominator, new_denominator)
        return Fraction.reduce_fraction(new_fraction)

    def __mul__(self, other):
        new_nominator = self.nominator * other.nominator
        new_denominator = self.denominator * other.denominator
        new_fraction = Fraction(new_nominator, new_denominator)
        return Fraction.reduce_fraction(new_fraction)
