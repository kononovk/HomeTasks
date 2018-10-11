from math import factorial
from copy import deepcopy
from unittest import TestCase, main


def pascal_triangle(n):
    if type(n) != int or n < 0:
        return "ValueError"
    triangle = []
    curr_string = []
    for i in range(0, n + 1):
        for k in range(0, i + 1):
            curr_string.append(int(factorial(i) / (factorial(k) * factorial(i - k))))
        tmp_str = deepcopy(curr_string)
        triangle.append(tmp_str)
        curr_string.clear()
    return triangle


class Validator(TestCase):
    def test_correct_values(self):
        self.assertEqual(pascal_triangle('abc'), "ValueError")
        self.assertEqual(pascal_triangle(0), [[1]])
        self.assertEqual(pascal_triangle(2), [[1], [1, 1], [1, 2, 1]])
        self.assertEqual(pascal_triangle(-3), "ValueError")
        self.assertEqual(pascal_triangle(4), [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]])


main()
