# optional parameters with = sign
# class Student:
#     def __init__(self, name, id = 1):
#         self.name = name
#         self.id = id

# pero = Student("Pepa")
# print(pero.name)
# print(pero.id)

class People:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        print(self.name)

class Dude(People):
    def __init__(self, super):
        self.money = money

    def __str__(self):
        print("Name: " + self.name)
        print("Balance: " + self.money)


dude1 = Dude("Stamat", 999)
print(dude1)