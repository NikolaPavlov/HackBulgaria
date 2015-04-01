from p01_aBankAccountTheTDDway import *

import unittest


class BankAccTests(unittest.TestCase):

    def setUp(self):
        self.acc = BankAcc("GoGo!", 512, '$')

    def testConstructor(self):
        self.assertTrue(isinstance(self.acc, BankAcc))

    def testDepositMoney(self):
        with self.assertRaises(ValueError):
            self.acc.deposit_money(-111)

    def testShowBalance(self):
        self.assertTrue(self.acc.balance(), self.acc.balance)

    def testWithdrawMoney(self):
        with self.assertRaises(ValueError):

    def test_to_str(self):
        self.assertEqual(str(self.acc), "Bank account for GoGo with balance of 512$")

    def test_int_value(self):
        self.assertEqual(int(self.acc), 512)


if __name__ == "__main__":
    unittest.main()