# Fractions where is the fucking pandas?
from fractions import gcd


class Fraction:

    def __init__(self, numerator, denominator):
        self.greatest_divisor = gcd(numerator, denominator)
        self.numerator = numerator
        self.denominator = denominator

    def __str__(self):
        return "{} / {}".format(self.numerator, self.denominator)

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return (self.numerator, self.denominator) == \
        (other.numerator, other.denominator)

# ########################################################################
    def __add__(self, other):
        numerator = (self.numerator * other.denominator) +\
         (other.numerator * self.denominator)
        denominator = self.denominator * other.denominator
        if numerator % denominator == 0:
            return int(numerator / denominator)
        else:
            return Fraction(numerator, denominator)

    def __sub__(self, other):
        numerator = (self.numerator * other.denominator) -\
         (other.numerator * self.denominator)
        denominator = self.denominator * other.denominator
        if numerator % denominator == 0:
            return int(numerator / denominator)
        else:
            return Fraction(numerator, denominator)

    def __mul__(self, other):
        numerator = self.numerator * other.numerator
        denominator = self.denominator * other.denominator
        if numerator % denominator == 0:
            return int(numerator / denominator)
        else:
            return Fraction(numerator / self.greatest_divisor, denominator / self.greatest_divisor)

    def division(self, other):
        pass

    def test(self, other):
        print(self.numerator)
        print(self.denominator)
        print(other.numerator)
        print(other.denominator)

a = Fraction(1, 2)
b = Fraction(2, 4)
print(a * b)