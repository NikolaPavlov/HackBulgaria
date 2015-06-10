import unittest
from histogram import Histogram


class TestHistogram(unittest.TestCase):

    def setUp(self):
        self.h = Histogram()
        self.h.add('Apache')

    def test_add_to(self):
        self.assertIn('Apache', self.h.histo_dict)

    def test_count(self):
        self.h.add('Apache')
        self.assertEqual(self.h.count('Apache'), 2)
        self.assertEqual(self.h.count('ISS'), None)

    def test_get_dict(self):
        z = self.h.get_dict()
        self.assertEqual(type(z), dict)

    def test_items(self):
        self.h.add('Apache')
        self.h.add('ngninx')
        self.h.add('asdasd')
        z = self.h.get_dict()
        for key, count in self.h.items():
            self.assertEqual(z[key], count)


if __name__ == '__main__':
    unittest.main()
