from unittest import TestCase, main


def fact_rec(n):
    if type(n) != int or n < 0:
        return "ValueError"
    if n == 0:
        return 1
    return n * fact(n - 1)


def fact(n):
    factorial = 1
    if type(n) != int or n < 0:
        return "ValueError"
    try:
        for i in range(1, int(n + 1)):
            factorial *= i
        return factorial
    except ValueError:
        return "ValueError"


class Validator(TestCase):
    def test_correct_values(self):
        if not self.assertEqual(fact("10"), "ValueError"):
            print("Test passed")
        else:
            print("Test failed")
        if not self.assertEqual(fact("abc"), "ValueError"):
            print("Test passed")
        else:
            print("Test failed")
        if not self.assertEqual(fact(10.0), "ValueError"):
            print("Test passed")
        else:
            print("Test failed")
        if not self.assertEqual(fact(10), 3628800):
            print("Test passed")
        else:
            print("Test failed")
        if not self.assertEqual(fact(0), 1):
            print("Test passed")
        else:
            print("Test failed")
        if not self.assertEqual(fact(-4), "ValueError"):
            print("Test passed")
        else:
            print("Test failed")
        if not self.assertEqual(fact(11.75), "ValueError"):
            print("Test passed")
        else:
            print("Test failed")
        if not self.assertEqual(fact([3]), "ValueError"):
            print("Test passed")
        else:
            print("Test failed")
        if not self.assertEqual(fact_rec("10"), "ValueError"):
            print("Test passed")
        else:
            print("Test failed")
        if not self.assertEqual(fact_rec("abc"), "ValueError"):
            print("Test passed")
        else:
            print("Test failed")
        if not self.assertEqual(fact_rec(10.0), "ValueError"):
            print("Test passed")
        else:
            print("Test failed")
        if not self.assertEqual(fact_rec(10), 3628800):
            print("Test passed")
        else:
            print("Test failed")
        if not self.assertEqual(fact_rec(0), 1):
            print("Test passed")
        else:
            print("Test failed")
        if not self.assertEqual(fact_rec(-4), "ValueError"):
            print("Test passed")
        else:
            print("Test failed")
        if not self.assertEqual(fact_rec(11.75), "ValueError"):
            print("Test passed")
        else:
            print("Test failed")
        if not self.assertEqual(fact_rec([3]), "ValueError"):
            print("Test passed")
        else:
            print("Test failed")


main()
