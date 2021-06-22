from random import randrange
from functools import reduce

"""
solution 2. 
Using functools to use reduce function (implement functional programming)
The process is same with solution 1 but it's code readability is lower than solution 1

This answer is not pure random function because it's binomial distribution.
So median values appear mostly.
"""


def get_random(max_number):
    get_zero_or_one = lambda: randrange(2)
    return reduce(lambda ans, rand: ans + rand, [get_zero_or_one() for _ in range(max_number)])


# answer
# input_max_number = 10
# test_cases = 1000
# answers = [get_random(input_max_number) for _ in range(test_cases)]
# print("Solution 2")
# print("-" * 50)
# for i in range(input_max_number):
#     print("{} : {}".format(i, answers.count(i)))
# print("-" * 50)
