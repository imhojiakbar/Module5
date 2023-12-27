Class FileManager:
    def __init__(self, path, mode):
        self.path = path
        self.mode = mode
    def __enter__(self):
        file = open(file=self.path, mode=self.mode)
        self.file = file
        return file
    def __exit__(self):
        self.file.close()

def description_data():
    with FileManager("../exam/005.txt", "r") as f:
        pprint(f)



def desriptions_request():
    url = 'http://164.92.64.76/desc/'
    response = requests.post(url).json()
    pprint(response)




 if __name__ == '__main__':
     desriptions_request()
     description_data()
