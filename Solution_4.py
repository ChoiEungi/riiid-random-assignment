from random import randrange

"""
This solution is similar to solution3 but compare origin number.
So there are almost no unnecessary calculation.

reference: https://stackoverflow.com/questions/13209162/creating-a-random-number-generator-from-a-coin-toss
"""


def get_random(max_number):
    reducer = (2**max_number)/max_number
    get_zero_or_one = lambda: randrange(2)
    while True:
        ans = int("".join([str(get_zero_or_one()) for _ in range(max_number)]), 2)
        if ans < max_number * reducer: return ans//reducer


# # answer
# input_number = 10
# test_cases = 1000
# answers = [get_random(input_number) for _ in range(test_cases)]
# print("Solution 4")
# print("-" * 50)
# for i in range(input_number):
#     print("{} : {}".format(i, answers.count(i)))
# print("-" * 50)