import unittest

from p12_creditCardValidation import is_credit_card_valid


class TestIsCreditCardValid(unittest.TestCase):

    def test_is_credit_card_valid(self):
        self.assertTrue(is_credit_card_valid(79927398713))

    def test_is_credit_card_not_valid(self):
        self.assertFalse(is_credit_card_valid(79927398715))


if __name__ == "__main__":
    unittest.main()
