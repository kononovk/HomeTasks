from memory_profiler import profile, time
from unittest import TestCase, main
from sys import setrecursionlimit
from termcolor import colored
from math import factorial


#  Recursion factorial function #
def fact_rec(n):
    if type(n) != int or n < 0:
        raise ValueError("n must be natural")
    if n == 0:
        return 1
    return n * fact(n - 1)


@profile
def recursion_fact(n):
    setrecursionlimit(1000000)
    return fact_rec(n)


#  Cycle factorial function #
def fact(n):
    curr_fact = 1
    if type(n) != int or n < 0:
        raise ValueError("n must be natural")
    try:
        for i in range(1, int(n + 1)):
            curr_fact *= i
        return curr_fact
    except ValueError:
        return "ValueError"


@profile
def cycle_fact(n):
    return fact(n)


#  Test processing main class  #
class Validator(TestCase):
    def test_correct_values(self):
        if not self.assertRaises(ValueError, fact, "10"):
            print("Test passed")
        else:
            print("Test failed")
        if not self.assertRaises(ValueError, fact, "abc"):
            print("Test passed")
        else:
            print("Test failed")
        if not self.assertRaises(ValueError, fact, 10.0):
            print("Test passed")
        else:
            print("Test failed")
        if not self.assertEqual(fact(30000), factorial(30000)):
            print("Test passed")
        else:
            print("Test failed")
        if not self.assertEqual(fact(0), 1):
            print("Test passed")
        else:
            print("Test failed")
        if not self.assertRaises(ValueError, fact, -4):
            print("Test passed")
        else:
            print("Test failed")
        if not self.assertRaises(ValueError, fact, 11.75):
            print("Test passed")
        else:
            print("Test failed")
        if not self.assertRaises(ValueError, fact, [3]):
            print("Test passed")
        else:
            print("Test failed")
        if not self.assertRaises(ValueError, fact_rec, "10"):
            print("Test passed")
        else:
            print("Test failed")
        if not self.assertRaises(ValueError, fact_rec, "abc"):
            print("Test passed")
        else:
            print("Test failed")
        if not self.assertRaises(ValueError, fact_rec, 10.0):
            print("Test passed")
        else:
            print("Test failed")
        if not self.assertEqual(fact_rec(30000), factorial(30000)):
            print("Test passed")
        else:
            print("Test failed")
        if not self.assertEqual(fact_rec(0), 1):
            print("Test passed")
        else:
            print("Test failed")
        if not self.assertRaises(ValueError, fact_rec, -4):
            print("Test passed")
        else:
            print("Test failed")
        if not self.assertRaises(ValueError, fact_rec, 11.75):
            print("Test passed")
        else:
            print("Test failed")
        if not self.assertRaises(ValueError, fact_rec, [3]):
            print("Test passed")
        else:
            print("Test failed")


#  Time and memory measuring for different variable values  #
fact_of = 10000
int_time = time.process_time()
recursion_fact(fact_of)
print(colored("Recursion factorial function time for {} = {}".format(fact_of, time.process_time() - int_time), 'yellow'))
int_time = time.process_time()
cycle_fact(fact_of)
print(colored("Cycle factorial function time for {} = {}".format(fact_of, time.process_time() - int_time), 'yellow'))
print(colored("____________________________________________________________________________________________", 'yellow'))
fact_of = 20000
int_time = time.process_time()
recursion_fact(fact_of)
print(colored("Recursion factorial function time for {} = {}".format(fact_of, time.process_time() - int_time), 'yellow'))
int_time = time.process_time()
cycle_fact(fact_of)
print(colored("Cycle factorial function time for {} = {}".format(fact_of, time.process_time() - int_time), 'yellow'))
print(colored("____________________________________________________________________________________________", 'yellow'))
fact_of = 30000
int_time = time.process_time()
recursion_fact(fact_of)
print(colored("Recursion factorial function time for {} = {}".format(fact_of, time.process_time() - int_time), 'yellow'))
int_time = time.process_time()
cycle_fact(fact_of)
print(colored("Cycle factorial function time for {} = {}".format(fact_of, time.process_time() - int_time), 'yellow'))
print(colored("____________________________________________________________________________________________", 'yellow'))

'# test processing #'
print(colored("TESTS:", 'green'))
main()
