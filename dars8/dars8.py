import asyncio

import requests


# async def print_numbers():
#     for i in range(10):
#         print(i)
#
# async def get_data(url):
#     response = requests.get(url)
#     return response.status_code
#
# def run():
#     await print_numbers()
#     await get_data()
#
# if __name__ == '__main__':
#     run()

async def tub(n1):
    s = []
    for num in range(2, n1 + 1):
        if num > 1:
            for i in range(2, int(num ** 0.5) + 1):
                if (num % i) == 0:
                    break
            else:
                s.append(num)
    print(s)

async def tub_2(n2):
    s = []
    for num in range(2, n2 + 1):
        if num > 1:
            for i in range(2, int(num ** 0.5) + 1):
                if (num % i) == 0:
                    break
            else:
                s.append(num)
    print(s)

async def tub_3(n3):
    s = []
    for num in range(2, n3 + 1):
        if num > 1:
            for i in range(2, int(num ** 0.5) + 1):
                if (num % i) == 0:
                    break
            else:
                s.append(num)
    print(s)

async def tub_4(n4):
    s = []
    for num in range(2, n4 + 1):
        if num > 1:
            for i in range(2, int(num ** 0.5) + 1):
                if (num % i) == 0:
                    break
            else:
                s.append(num)
    print(s)

async def run():
    tasks = (asyncio.create_task(tub(n1)), asyncio.create_task(tub_2(n2)),
             asyncio.create_task(tub_3(n3)), asyncio.create_task(tub_4(n4)))
    await asyncio.gather(*tasks)

if __name__ == '__main__':
    n1, n2, n3, n4 = map(int, input("Son kiriting: ").split())
    asyncio.run(run())

