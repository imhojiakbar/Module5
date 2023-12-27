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

