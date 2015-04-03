import unittest

from p01_aBankAccountTheTDDway import BankAcc


class BankAccTests(unittest.TestCase):

    def setUp(self):
        self.acc = BankAcc("GoGo", 512, '$')

    def test_constructor(self):
        self.assertTrue(isinstance(self.acc, BankAcc))

    def test_show_balance(self):
        self.assertEqual(self.acc.get_balance(), 512)

    def test_deposit_money_negative_amount(self):
        with self.assertRaises(ValueError):
            self.acc.deposit_money(-1)

    def test_deposit_money(self):
        oldBalance = self.acc.get_balance()
        self.acc.deposit_money(111)
        newBalance = self.acc.get_balance()
        self.assertTrue(oldBalance + 111, newBalance)

    def test_withdraw_negative_amount(self):
        with self.assertRaises(ValueError):
            self.acc.withdraw(-1)

    def test_withdraw(self):
        oldBalance = self.acc.get_balance()
        self.acc.withdraw(100)
        newBalance = self.acc.get_balance()
        self.assertTrue(oldBalance - 1, newBalance)

    def test_transfer_to_acc(self):
        account2 = BankAcc('PePa', 256, '$')
        self.acc.transfer_to_acc(account2, 1)
        self.assertEqual(self.acc.get_balance(), 511)
        self.assertEqual(account2.get_balance(), 257)

    def test_transfet_to_acc_negative(self):
        account2 = BankAcc('Pepa', 256, '$')
        with self.assertRaises(ValueError):
            self.acc.transfer_to_acc(account2, -1)

    def test_transfer_to_acc_Usd_to_E(self):
        account3 = BankAcc('Shavrantia', 32, 'E')
        with self.assertRaises(ValueError):
            self.acc.transfer_to_acc(account3, 1)

    def test_to_string(self):
        self.assertEqual(str(self.acc), "Bank account for GoGo with balance of 512$")

    def test_to_int(self):
        self.assertEqual(int(self.acc), 512)


if __name__ == "__main__":
    unittest.main()
