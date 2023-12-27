import os
from multiprocessing import Process


def wrapper(func):
    def inner(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"{func.name} result is {result}")
        return result

    return inner


@wrapper
def show_number():
    summa = 0
    os.chdir('descriptions')
    for text in os.listdir():
        print(text)
        with open(f"{os.getcwd()}/{text}", "r") as f:
            data = f.read()
            for i in data:
                if i.isdigit():
                    summa += int(i)
            print(summa)


if __name__ == '__main__':
    p1 = Process(target=show_number)
    p1.start()
    p1.join()