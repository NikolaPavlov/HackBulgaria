import unittest

from p10_ReduceFilePath import reduce_file_path


class TestReduceFilePath(unittest.TestCase):

    def test_reduce_file_path(self):
        self.assertEqual(reduce_file_path("/etc/../etc/../etc/../"), '/')


if __name__ == "__main__":
    unittest.main()
