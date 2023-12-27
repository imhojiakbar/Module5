import time
from math import factorial
from multiprocessing import Process


# def square(nums: list):
#     result = []
#     time.sleep(10)
#     for v in nums:
#         result.append(v ** 2)
#     print("result square : ", result)
#
#
# def cube(nums: list):
#     result = []
#     time.sleep(5)
#     for v in nums:
#         result.append(v ** 3)
#     print("result cube: ", result)
#
#
# # fact(3) -> 1*2*3 -> 6
# # fib(5) -> 01123 -> 3
#
# if __name__ == '__main__':
#     nums = [2, 3, 4, 6]
#     time.sleep(10)
#     p1 = Process(target=square, args=(nums,))
#     p2 = Process(target=cube, args=(nums,))
#     p1.start()
#     p2.start()
#     p1.join()
#     p2.join()
#     time.sleep(10)


def fact(nums: int):
    return factorial(nums)

def fib(nums: int):
    if nums <= 1:
        return nums
    else:
        return fib(nums-1) + fib(nums-2)
nums = int(input("Nechta: "))
if nums <= 0:
    print("Error")
else:
    # print("Fibanachchi")
    for i in range(nums):
        print(fib(i))


if __name__ == '__main__':
    nums = int(input(": "))
    f = fact(nums)
    fi = fib(nums)
    print("Factorial: ", f)
    print("Fibanatchi: ", fi)

