from random import randrange

"""
1. By using format function, convert int number to string type of binary number such as 5 -> 101, and get the 
value of length of binary number. 
2. make random binary number that length is same with binary number of max_number. 
3. In this case all number probability is same as 1/n. (n = len of binary number of max number, in code binary_digit) 
4. This is because all results are different depending on the order in which get_zero_or_one() is executed. The 
number of Solution1 and 2 is determined according to the number of 1s regardless of the order in which 
get_zero_or_one() is executed, resulting in a binomial distribution. However, in Sol3, all probabilities are 
independent. 
5. Since the binary number has the same number of digits and can be greater than max_number, 
only a value less than max_number is returned. This results in unnecessary calculations. 
"""


def get_random(max_number):
    get_zero_or_one = lambda: randrange(2)
    binary_digit = len(format(max_number, 'b'))  # find length of binary number of max_number to reduce calculation.
    while True:
        ans = int("".join([str(get_zero_or_one()) for _ in range(binary_digit)]), 2)
        if ans < max_number: return ans


# answer
# input_number = 10
# test_cases = 1000
# answers = [get_random(input_number) for _ in range(test_cases)]
# print("Solution 3")
# print("-" * 50)
# for i in range(input_number):
#     print("{} : {}".format(i, answers.count(i)))
# print("-" * 50)
