from Solution_1 import get_random as sol1
from Solution_2 import get_random as sol2
from Solution_3 import get_random as sol3
from Solution_4 import get_random as sol4
import time


input_number = 100  # set max_number
test_cases = 1000  # set the number of times to test

solutions = [] # put all solutions

print("Test Time")
start_time = time.time()
solutions.append([sol1(input_number) for _ in range(test_cases)])
end_time = time.time()
print("WorkingTime[test {}]: {} sec".format(1, end_time-start_time))


start_time = time.time()
solutions.append([sol2(input_number) for _ in range(test_cases)])
end_time = time.time()
print("WorkingTime[test {}]: {} sec".format(2, end_time-start_time))


start_time = time.time()
solutions.append([sol3(input_number) for _ in range(test_cases)])
end_time = time.time()
print("WorkingTime[test {}]: {} sec".format(3, end_time-start_time))


start_time = time.time()
solutions.append([sol4(input_number) for _ in range(test_cases)])
end_time = time.time()
print("WorkingTime[test {}]: {} sec".format(4, end_time-start_time))


print("\nend the time test \n")


def test_ret(answers, idx):
    print("Solution " + str(idx))
    print("-" * 50)
    for i in range(input_number):
        print("{} : {}".format(i, answers.count(i)))
    print("-" * 50 + "\n")


for solution, idx in zip(solutions, range(1, 5)):
    test_ret(solution, idx)

