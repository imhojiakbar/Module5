# 1
# def lengthOfLastword(n):
#     s = n[-1]
#     print(len(s))
#
# if __name__ == '__main__':
#     n = input(": ").split()
#     lengthOfLastword(n)
#
# # 2
# def strStr(a):
#     print(a[::-1])
#
# if __name__ == '__main__':
#     a = list(input(": "))
#     strStr(a)
#
#
# # 3
# def findTheDifference(a, b):
#     a = set(a)
#     a.symmetric_difference_update(b)
#     print(a)
#
# if __name__ == '__main__':
#     a = input(": ")
#     b = input(": ")
#     findTheDifference(a, b)
#
#
# def numJewelsInStones(jewels, stones):
#     s = 0
#     for i in jewels, stones:
#         if i == "A":
#             s += 1
#         print(s)
#
# if __name__ == '__main__':
#     jewels = input(": ").split()
#     stones = input(": ").split()
#     numJewelsInStones(jewels, stones)
import pprint
from pprint import pprint

import requests
import csv
import os

class FileManager:
    def __init__(self, path, mode):
        self.path = path
        self.mode = mode
    def __enter__(self):
        file = open(file=self.path, mode=self.mode)
        self.file = file
        return file
    def __exit__(self):
        self.file.close()

def get_data(url):
    response = requests.get(url)
    data = response.json()
    return data

os.mkdir('people.info')
os.chdir('people.info')

if __name__ == '__main__':
    url = 'https://randomuser.me/api/'
    data = get_data(url)
    if data['results'][0]['gender'] == 'female' or data['results'][0]['gender'] == 'male':
        id_name = data['results'][0]['id']['name']
        large_img = data['results'][0]['picture']['large']
        medium_img = data['results'][0]['picture']['medium']
        thumbnail_img = data['results'][0]['picture']['thumbnail']

        large = requests.get(large_img).content
        medium = requests.get(medium_img).content
        thumbnail = requests.get(thumbnail_img).content

        with open('emails.csv', 'a') as f:
            writer = csv.writer(f)
            writer.writerow('emails')
            writer.writerow(data['results'][0]['email'])

        with FileManager(f'people/{id_name}_large.jpg', 'wb') as f1, FileManager(f'people/{id_name}_medium.jpg', 'wb') as f2, FileManager(f'people/{id_name}_thumbnail.jpg', 'wb') as f3:
            f1.write(large)
            f2.write(medium)
            f3.write(thumbnail)

    else:
        print('Not normal person\nTry again!')
    pprint(data)


