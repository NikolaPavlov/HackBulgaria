# Fractions where is the fucking pandas?


class Fraction:

    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def __str__(self):
        return "{} / {}".format(self.numerator, self.denominator)

    def __repr__(self):
        return self.__str__()

# ########################################################################
    def addition(self, other):
        return Fraction(self.numerator + other.numerator,\
            self.denominator + other.denominator)

    def subtraction(self, other):
        pass

    def multiplication(self, other):
        pass

    def division(self, other):
        pass


# Tests
frac1 = Fraction(1, 2)
frac2 = Fraction(2, 4)
print(Fraction.addition(frac1, frac2))
