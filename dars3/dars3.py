"""GENERATOR"""
import datetime
import random
from datetime import timedelta
from random import randint

# def is_polindrom(n: int) -> bool:
#     x = n
#     z = 0
#     while x > 0:
#         z = z * 10 + x % 10
#         x //= 10
#     return z == n
# def polindrom_generator(a, b):
#     while a < b:
#         if is_polindrom(a):
#             yield a
#         a += 1
#
# if __name__ == '__main__':
#     x,y = map(int, input(": ").split(" "))
#     for val in polindrom_generator(x, y):
#         print(val)


"""RANDOM"""


# print(datetime.datetime.now())
# print(random.randint(1, 15))


def get_num(a: int, b: int) -> int:
    return randint(a, b)


if __name__ == '__main__':
    a, b = map(int, input("Ikkita son kiriting: ").split())
    print("Men bitta son oyladim, topishga harakat qiling")
    num = int(input("Son kiriting: "))
    guest = get_num(a, b)
    end = datetime.datetime.now() + timedelta(seconds=10)

    while end >= datetime.datetime.now():
        if num > guest:
            print(f"Men o'ylagan son {num} dan kichik")
        elif num < guest:
            print(f"Men o'ylagan son {num} dan katta")
        else:
            print(f"Tabriklayman men o'ylagan son {num} edi")
            break
        num = input("Qayta urunib ko'ring: ")
        