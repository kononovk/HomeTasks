from unittest import TestCase, main
import time
import memory_profiler

t1_start = time.perf_counter()


def fact_rec(n):
    if type(n) != int:
        return "ValueError"
    if n < 0:
        return "ValueError"
    if n == 0:
        return 1
    return n * fact(n - 1)


def fact(n):
    factorial = 1
    if type(n) != int:
        return "ValueError"
    if n < 0:
        return "ValueError"
    try:
        for i in range(1, int(n + 1)):
            factorial *= i
        return factorial
    except ValueError:
        return "ValueError"


class Validator(TestCase):
    def test_correct_values(self):
        self.assertEqual(fact("10"), "ValueError")
        self.assertEqual(fact("abc"), "ValueError")
        self.assertEqual(fact(10.0), "ValueError")
        self.assertEqual(fact(10), 3628800)
        self.assertEqual(fact(0), 1)
        self.assertEqual(fact(-4), "ValueError")
        self.assertEqual(fact(11.75), "ValueError")
        self.assertEqual(fact([3]), "ValueError")

        self.assertEqual(fact_rec("10"), "ValueError")
        self.assertEqual(fact_rec("abc"), "ValueError")
        self.assertEqual(fact_rec(10.0), "ValueError")
        self.assertEqual(fact_rec(10), 3628800)
        self.assertEqual(fact_rec(0), 1)
        self.assertEqual(fact_rec(-4), "ValueError")
        self.assertEqual(fact_rec(11.75), "ValueError")
        self.assertEqual(fact_rec([3]), "ValueError")


t1_stop = time.perf_counter()
print("Time = ".format((t1_stop - t1_start)/60))
main()
