# hw
# 1
class Task:
    def exercise_1(self, x = list[str]):
        s = x[0]
        for i in x:
            while not i.startswith(s):
                s = s[:-1]
        return s
# 2
class Task2:
    def exercise_2(self, n):
        s = ""
        for i in n:
            s += str(i)

        x = str(int(s) +1)
        for j in range(len[x]):
            return [int(x[j])]

# 3
class Task3:
    def sum(self, n):
        for i in range(1, len(n)):
            n[i] += n[i-1]
        return n