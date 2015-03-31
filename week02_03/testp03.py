import unittest
from p03_theCashDeskProblem import Bill

class BillTest(unittest.TestCase):
    #boilerplate for init test (variabeles here bitch!!!!)
    def setUp(self):
        self.my_bill = Bill(5)

    def test_create_new_instance_bill(self):
        self.assertTrue(isinstance(self.my_bill, Bill))


    def test_valid_amaout(self):
        self.assertEqual(self.my_bill.num, 4)


    def test_int_cast(self):
        self.assertEqual(int(self.my_bill), 5)

if __name__ == "__main__":
    unittest.main()



#how to test one variable with multipale values
#use send email with test for bgcoder

#hacking automatic unit testing system




#-----------
with self.assertRaises(ValueError)