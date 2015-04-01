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
        self.assertTrue(self.bill1, self.bill3)

    def test_can_hash(self):
        self.assertIsNotNone(hash(self.bill1))

    def test_negative_bill_err(self):
        with self.assertRaises(ValueError):
            bill = Bill(-10)

    def test_zero_bill_err(self):
        with self.assertRaises(ValueError):
            bill = Bill(0)

    def test_float_bill_err(self):
        with self.assertRaises(ValueError):
            bill = Bill(0.999)

    def test_batch(self):
        values = [10, 20, 50, 100]
        bills = [Bill(value) for value in values]
        batch = BatchBill(bills)

        self.assertIsInstance(batch, BatchBill)


if __name__ == "__main__":
    unittest.main()

