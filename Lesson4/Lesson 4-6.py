from itertools import count
from itertools import cycle

for a in count(int(input('Введите целое число: '))):
    if a == 100:
        break
    print(a)

my_list = ['iphone', 'samsung', 'xiaomi', 'oppo']
b = 0
for el in cycle(my_list):
    if b == 10:
        break
    print(el)
    b += 1