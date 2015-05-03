class Calculator:

    def __init__(self, num1, num2):
        self.a = num1
        self.b = num2

    def add(self):
        return self.a + self.b

    def multi(self):
        return self.a * self.b

class Scientific(Calculator):

    def power(self):
        return(pow(self.a, self.b))


my_calculator = Calculator(2, 3)
print(my_calculator.add())
print(my_calculator.multi())
my_sci_calculator = Scientific(2, 3)
print(my_sci_calculator.power())
