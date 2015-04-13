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
        self = self.reducer(self.nominator, self.denominator)
        other = self.reducer(other.nominator, other.denominator)

        if self.nominator == other.nominator:
            if self.denominator == other.denominator:
                return True
            return False
        return False

    def reducer(self, a, b):
        for i in range(a, 0, -1):
            if b % i == 0 and a % i == 0:
                a /= i
                b /= i
                return Fraction(a, b)

    def __add__(self, other):
        # reduce the two fraction
        self = self.reducer(self.nominator, self.denominator)
        other = other.reducer(other.nominator, other.denominator)

        new_nominator = self.nominator * other.denominator + self.denominator * other.nominator
        new_denominator = self.denominator * other.denominator
        return Fraction(int(new_nominator), int(new_denominator))

    def __sub__(self, other):
        # reduce the two fraction
        self = self.reducer(self.nominator, self.denominator)
        other = other.reducer(other.nominator, other.denominator)

        new_nominator = self.nominator * other.denominator - self.denominator * other.nominator
        new_denominator = self.denominator * other.denominator
        return Fraction(int(new_nominator), int(new_denominator))


    def __mul__(self, other):
        self = self.reducer(self.nominator, self.denominator)
        other = other.reducer(other.nominator, other.denominator)

        new_nominator = self.nominator * other.nominator
        new_denominator = self.denominator * other.denominator
        return Fraction(int(new_nominator), int(new_denominator))

a = Fraction(1, 2)
b = Fraction(2, 4)
c = Fraction(5, 6)
print(a - b)
print(a - c)
print(a == b)
