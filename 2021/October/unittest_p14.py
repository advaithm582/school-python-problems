import unittest

import program14 as p

class Program14TC(unittest.TestCase):
    def test_vowel_count(self):
        str_ = "Hay in June, JULY"

        self.assertEqual(5, p.count_vowels(str_))

    def test_vowel_count_lst(self):
        lst = [
            "AAAA EEEE IIII OOOO UUUU",
            "Hay in June, JULY",
            "Ae Eu I"
        ]

        self.assertEqual(p.swmv(lst), lst[0])


if __name__=="__main__":
    unittest.main(verbosity=2)