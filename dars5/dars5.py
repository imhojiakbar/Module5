"""DECORATORS"""
import json


# def wrapper(func):
#     def inner(*args, **kwargs):
#         print("Funksiya ishlashni boshladi")
#         result = func(args, kwargs)
#         print("Funksiya bajarib boldi")
#         return result
#     return inner
# @wrapper
# def add(x: int, y: int):
#     return x+y
#
# if __name__ == '__main__':
#     print(add(2, 4))
def logger(filename, data: dict):
    with open(filename, "r+") as f:
        transfers = json.load(f)
        transfers.append(data)

class Person:
    def __init__(self, full_name, balance):
        self.full_name = full_name
        self.balance = balance
    def __str__(self):
        return f"{self.full_name} balansingiz: {self.balance}"

def checker(func):
    def inner(*args, **kwargs):
        p1, p2, amount = args
        if p1.balance < amount:
            print("Hisobingizda yetarli mablag' mavjud emas")

        result = func(*args, **kwargs)
        print("Tranfer amalga oshirildi")
        return result
    return inner


@checker
def transfer(p1: Person, p2: Person, amont: float):
    p1.balance = p1.balance - amont
    p2.balance = p2.balance + amont


if __name__ == '__main__':
    p1 = Person("Hoshimjon", 400)
    p2 = Person("Azizjon", 150)
    print(p1)
    print(p2)
    value = float(input("Qancha yubormoqchisiz ?: "))
    transfer(p1, p2, value)
    print(p1)
    print(p2)
