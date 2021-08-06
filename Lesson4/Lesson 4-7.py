from itertools import count
from math import factorial

def fact():
    for el in count(1):
        yield factorial(el)
n = int(input('Введите число: '))
i = 0
for el in fact():
    if i <= n:
        print(el)
        i += 1
    else:
        break