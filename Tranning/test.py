class TestClass:

    def __init__(self):
        self__name = 'this is a name'

    def first_print(self):
        print('this is a first_print')

    def second_print(self):
        print('this is a second print')
        self.first_print()



# Tests
tc = TestClass()
tc.second_print()
