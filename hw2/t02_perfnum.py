from unittest import TestCase, main


def is_perfect_number(inp_num):
    if type(inp_num) != int or inp_num < 1:
        raise ValueError("Input number must be natural")
    sum_of_dividers = 0
    for i in range(1, inp_num):
        if inp_num % i == 0:
            sum_of_dividers += i
    if sum_of_dividers == inp_num:
        return True
    return False


class Validator(TestCase):
    def test_false(self):
        self.assertFalse(is_perfect_number(1))

    def test_true_1(self):
        self.assertTrue(is_perfect_number(6))

    def test_true_2(self):
        self.assertTrue(is_perfect_number(28))

    def test_list(self):
        self.assertRaises(ValueError, is_perfect_number, [6])

    def test_negative_num(self):
        self.assertRaises(ValueError, is_perfect_number, -28)


main()
