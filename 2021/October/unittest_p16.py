import unittest
import random

import program16 as p

class Program16TC(unittest.TestCase):
    def test_no(self):
        self.assertTrue(p.is_number(111))
        self.assertFalse(p.is_number("pigeon"))
        self.assertTrue(p.is_number(3.11))

    def test_sort(self):
        lst = [random.randrange(1, 1000) for i in range(1, 100)]

        self.assertEqual(sorted(lst), p.bubble_sort(lst))

if __name__=="__main__":
    unittest.main(verbosity=2)