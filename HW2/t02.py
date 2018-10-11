from unittest import TestCase, main


def is_perfect_number(inp_num):
    if type(inp_num) != int or inp_num < 1:
        return "ValueError"
    sum_of_dividers = 0
    for i in range(1, inp_num):
        if inp_num % i == 0:
            sum_of_dividers += i
    if sum_of_dividers == inp_num:
        return True
    return False


class Validator(TestCase):
    def test_correct_values(self):
        self.assertFalse(is_perfect_number(1), False)
        self.assertTrue(is_perfect_number(33550336), True)
        self.assertTrue(is_perfect_number(28), True)
        self.assertEqual(is_perfect_number([6]), "ValueError")
        self.assertEqual(is_perfect_number(-28), "ValueError")


main()

