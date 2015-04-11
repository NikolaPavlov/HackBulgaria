import unittest

from p15_fridayYears import friday_years


class TestFidayYears(unittest.TestCase):

    def test_fiday_years1(self):
        self.assertEqual(friday_years(1000, 2000), 178)

    def test_fiday_years2(self):
        self.assertEqual(friday_years(1753, 2000), 44)

    def test_fiday_years3(self):
        self.assertEqual(friday_years(1990, 2015), 4)


if __name__ == "__main__":
    unittest.main()
