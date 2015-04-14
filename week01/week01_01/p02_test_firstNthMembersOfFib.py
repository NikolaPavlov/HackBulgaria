import unittest

from p02_firstNthMembersOfFib import fibonacci


class Test_Fibonachi(unittest.TestCase):
    def test_fib_value1(self):
        self.assertEqual(fibonacci(1), [1])

    def test_fib_value2(self):
        self.assertEqual(fibonacci(10), [1, 1, 2, 3, 5, 8, 13, 21, 34, 55])


if __name__ == "__main__":
    unittest.main()