import json

import requests


async def get_data(n):
    url = "https://api.agify.io?name=meelad"
    response = await requests.get(url)
    return response(n)

if __name__ == '__main__':
    n = input(": ").split()
    with open("names.json", "w") as f:
        json.dump(n, f, indent=4)