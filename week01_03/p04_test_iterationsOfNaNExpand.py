import unittest

from p04_iterationsOfNaNExpand import iterations_of_nan_expand


class TestIterationOfNanExpand(unittest.TestCase):

    def test_iteration(self):
        self.assertEqual(iterations_of_nan_expand("Not a NaN"), 1)

    def test_iteration_false(self):
        self.assertFalse(iterations_of_nan_expand("Show these people!"))


if __name__ == "__main__":
    unittest.main()
