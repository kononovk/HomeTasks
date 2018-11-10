from hw4.t01.smile_logic import bracket_correct
from unittest import TestCase, main


class Validator(TestCase):
    def test_1(self):
        self.assertTrue(bracket_correct("[]{}([{}])"))

    def test_2(self):
        self.assertTrue(bracket_correct("({gf[sdfg]}sdfg)sdfg     {}{}"))

    def test_3(self):
        self.assertFalse(bracket_correct("[{]}"))

    def test_4(self):
        self.assertFalse(bracket_correct("()[}"))

    def test_5(self):
        self.assertFalse(bracket_correct("{}())"))


main()
