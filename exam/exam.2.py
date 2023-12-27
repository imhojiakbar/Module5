import threading


def printer(func):
    def inner (n):
        result = func(n)
        return result
    return inner
@printer
def answer(n):
        reversed_num = int(str(n)[::-1])
        print(reversed_num)


if __name__ == '__main__':
    n = input(": ").split()
    answer(n)

# def reverse_numbers(numbers):
#     def reverse_number(number):
#         reversed_num = int(str(number)[::-1])
#         print(reversed_num)
#     threadlar = []

#     for number in numbers:
#         thread = threading.Thread(target=reverse_number, args=(number,))
#         thread.start()

#         for thread in threadlar:
#             thread.join()

# if __name__ == '__main__':

#     numbers = input("Enter: ")
#     numbers = [int(num) for num in numbers.split()]
#     reverse_numbers(numbers)

