from random import randint
def num(l):
    enum = []
    for n in l:
        if n % 2 == 0:
           enum.append(n)
    return enum
print(num([randint(1,100) for i in range(10)]))