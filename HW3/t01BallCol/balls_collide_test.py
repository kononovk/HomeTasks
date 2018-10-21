from math import sqrt
from unittest import TestCase, main
from HW3.t01BallCol.balls_collide import balls_collide


class Validator(TestCase):
    def test_false_1(self):
        self.assertFalse(balls_collide((0, 0, 0, 1), (0, 10, 0, 5)))

    def test_false_2(self):
        self.assertFalse(balls_collide((50.4, 3, 1, 0), (5, 3, 1, 10)))

    def test_true_1(self):
        self.assertTrue(balls_collide((5.4, 3, 1, 0), (5, 3, 1, 10)))

    def test_true_2(self):
        self.assertTrue(balls_collide((0, 0, 0, 1), (sqrt(3)/2, 1/2, 0, 0)))

    def test_negative_num(self):
        self.assertRaises(ValueError, balls_collide, (3, 3, 1, -2), (2, 1, 5, 1))


main()
