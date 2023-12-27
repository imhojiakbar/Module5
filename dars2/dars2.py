# n = input(": ")
# s = []
# for i in n:
#     if i.isdigit():
#         s.append(i)
# print(*s[::-1])

# def reverse_numbers(s:str) -> None:
#     if s[-1].isdigit():
#         print(s[-1], end=" ")
#     if len(s)!=1:
#         reverse_numbers(s[:-1])
# if __name__ == '__main__':
#     s = input(": ")
#     reverse_numbers(s)


class FloatRange:
    def __init__(self, first, last, step=1):
        if last != 1:
            self.first = first
            self.last = last
            self.step = step
        else:
            self.first = 1
            self.last = first

        self.step = step
    def __iter__(self):
        return self

    def __next__(self):
        val = self.first
        self.first += self.step
        if self.first > self.last:
            raise StopIteration
        return val

if __name__ == '__main__':
    for i in FloatRange(12, 34):
        print(i)
