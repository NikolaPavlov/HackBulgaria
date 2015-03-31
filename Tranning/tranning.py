class Animal:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

# Inheritance
# class Panda(Animal):
# super().__init__(name, age, weight)
# self.skill = skill

class Panda:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

        def eat(self):
            self._weight += 1

        def sleep(self):
            self._weight -= 1

        #private method
        def __set_name(self):
            self.name = name

        # __eq__
        def __eq__(self, other):
            return self.name == other.name

        # __str__
        def __str__(self):
            return self.name








# Tests
ivan = Panda("Ivan", 20, 200)
print(ivan)