class Fraction:

    def __init__(self, nominator, denominator):
        self.nomi = nominator
        self.denomi = denominator

    def __str__(self):
        if self.nomi % self.denomi == 0:
            return str(int(self.nomi / self.denomi))
        else:
            return "{} / {}".format(self.nomi, self.denomi)

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        if self.nomi / self.denomi == other.nomi / other.denomi:
            return True
        return False

    @staticmethod
    def reduce_fraction(fraction):
        for i in range(fraction.nomi, 0, -1):
            if fraction.nomi % i == 0 and fraction.denomi % i == 0:
                fraction.nomi /= i
                fraction.denomi /= i
        return Fraction(int(fraction.nomi), int(fraction.denomi))

    def __add__(self, other):
        if isinstance(self, int):
            self = Fraction(self, 1)

        if isinstance(other, int):
            other = Fraction(other, 1)

        new_nominator = self.nomi * other.denomi + self.denomi * other.nomi
        new_denominator = self.denomi * other.denomi
        new_fraction = Fraction(new_nominator, new_denominator)
        return Fraction.reduce_fraction(new_fraction)

    def __sub__(self, other):
        if isinstance(self, int):
            self = Fraction(self, 1)

        if isinstance(other, int):
            other = Fraction(other, 1)

        new_nominator = self.nomi * other.denomi - self.denomi * other.nomi
        new_denominator = self.denomi * other.denomi
        new_fraction = Fraction(new_nominator, new_denominator)
        return Fraction.reduce_fraction(new_fraction)

    def __mul__(self, other):
        if isinstance(self, int):
            self = Fraction(self, 1)

        if isinstance(other, int):
            other = Fraction(other, 1)

        new_nominator = self.nomi * other.nomi
        new_denominator = self.denomi * other.denomi
        new_fraction = Fraction(new_nominator, new_denominator)
        return Fraction.reduce_fraction(new_fraction)
