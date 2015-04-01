# WTF is python doctest?
# why not use py.test

import unittest

class FooTest(unittest.TestCase):
    def testFoo(self):
        self.assertTrue(True)

if __name__ == "__main__":
    unittest.main()