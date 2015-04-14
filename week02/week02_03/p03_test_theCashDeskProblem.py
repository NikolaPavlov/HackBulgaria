import unittest

from p03_theCashDeskProblem import Bill, BatchBill, CashDesk


class TestCashDesk(unittest.TestCase):

    def setUp(self):
        self.bill1 = Bill(10)
        self.bill2 = Bill(5)
        self.bill3 = Bill(10)
        self.money_holder = {}

# Class Bill Tests
    def test_constructor(self):
        self.assertIsInstance(self.bill1, Bill)

    def test_to_str(self):
        self.assertEqual(str(self.bill1), "A 10$ bill")

    def test_int(self):
        self.assertEqual(int(self.bill1), 10)

    def test_eq(self):
        self.assertTrue(self.bill1 == self.bill3)

    def test_eq_false(self):
        self.assertFalse(self.bill1 == self.bill2)

    def test_can_hash(self):
        self.assertIsNotNone(hash(self.bill1))
        self.assertIsInstance(hash(self.bill1), int)

    def test_negative_bill_err(self):
        with self.assertRaises(ValueError):
            Bill(-10)

    def test_zero_bill_err(self):
        with self.assertRaises(ValueError):
            Bill(0)

    def test_float_bill_err(self):
        with self.assertRaises(ValueError):
            Bill(0.999)

    def test_batch(self):
        values = [10, 20, 50, 100]
        bills = [Bill(value) for value in values]
        batch = BatchBill(bills)

        self.assertIsInstance(batch, BatchBill)

    def test_batch_as_str(self):
        values = [10, 20, 50, 100]
        bills = [Bill(value) for value in values]
        batch = BatchBill(bills)
        self.assertEqual(str(batch[0]), "A 10$ bill")
        self.assertEqual(str(batch[2]), "A 50$ bill")

    def test_cash_desk(self):
        values = [10, 20, 50, 100, 100, 100]
        bills = [Bill(value) for value in values]
        batch = BatchBill(bills)
        desk = CashDesk()
        desk.take_money(batch)
        desk.take_money(Bill(10))

        self.assertEqual(desk.total(), 390)

    def test_inspect_cash_desk(self):
        pass
        # values = [10, 20, 50, 100, 100, 100]
        # bills = [Bill(value) for value in values]
        # batch = BatchBill(bills)
        # desk = CashDesk()
        # desk.take_money(batch)
        # desk.take_money(Bill(10))

        # self.assertEqual(desk.inspect(), '{A 100$ bill: 3, A 10$ bill: 2, A 20$ bill: 1, A 50$ bill: 1}')

if __name__ == "__main__":
    unittest.main()

