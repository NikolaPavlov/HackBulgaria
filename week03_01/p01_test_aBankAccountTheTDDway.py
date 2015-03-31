from p01_aBankAccountTheTDDway import *

import unittest

class BankAccTests(unittest.TestCase):
    def setUp(self):
        self.acc = BankAcc("GoGo!", 512, '$')


    def testConstructor(self):
        self.assertTrue(isinstance(self.acc, BankAcc))


    def testDepositMoney(self, money):
        with self.assertRaises(ValueError):
            self.acc.deposit_money(-111)

#    def testShowBalance(self):
#        return BankAcc.balance





if __name__ == "__main__":
    unittest.main()