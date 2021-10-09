import unittest

import program13 as p

class Program13TC(unittest.TestCase):
    def test_capitalize(self):
        str_ = "The quick brown fox jumped over the lazy dog."

        self.assertEqual(str_.title(), p.capitalize_word(str_))

    def test_capitalize_nos(self):
        # failed??
        str_ = "The quick 32-bit fox jumped over the lazy edge."

        self.assertEqual(str_.title(), p.capitalize_word(str_))


if __name__=="__main__":
    unittest.main(verbosity=2)