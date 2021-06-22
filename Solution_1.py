from random import randrange

"""
Solution1. 
using sum function (implement functional programming)
At first, Repeat max_number times to put the list into the 0 or 1(it is created by get_zero_or_one function)
And then sum the list. 

This answer is not pure random function because it's binomial distribution.
So median values appear mostly.
"""


def get_random(max_number):
    get_zero_or_one = lambda: randrange(2)
    return sum([get_zero_or_one() for _ in range(max_number)])


# answer
# input_max_number = 10
# test_cases = 1000
# answers = [get_random(input_max_number) for _ in range(test_cases)]
# print("Solution 1")
# print("-"*50)
# for i in range(input_max_number):
#     print("{} : {}" .format(i, answers.count(i)))
# print("-"*50)


