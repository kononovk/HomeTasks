from math import factorial
from copy import deepcopy
from unittest import TestCase, main


def pascal_triangle(n):
    if type(n) != int or n < 0:
        raise ValueError("n must be natural")
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
        if not self.assertRaises(ValueError, pascal_triangle, "abc"):
            print("Test passed")
        else:
            print("Test failed")
        if not self.assertEqual(pascal_triangle(0), [[1]]):
            print("Test passed")
        else:
            print("Test failed")
        if not self.assertEqual(pascal_triangle(2), [[1], [1, 1], [1, 2, 1]]):
            print("Test passed")
        else:
            print("Test failed")
        if not self.assertRaises(ValueError, pascal_triangle, -3):
            print("Test passed")
        else:
            print("Test failed")
        if not self.assertEqual(pascal_triangle(4), [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]):
            print("Test passed")
        else:
            print("Test failed")


main()
