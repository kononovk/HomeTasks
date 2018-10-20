from unittest import TestCase, main
import balls_collide


class Validator(TestCase):
    def test_false_1(self):
        self.assertFalse(balls_collide((0, 0, 0, 1), (0, 10, 0, 5)))
    """
    def test_false_2(self):

    def test_true_1(self):

    def test_true_2(self):

    def test_negative_num(self):
    """


main()
