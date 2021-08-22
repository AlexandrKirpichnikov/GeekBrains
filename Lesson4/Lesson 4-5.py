from functools import reduce

def my_func(a, b):
    return a * b
print(f'Список четных значений: {[a for a in range(100, 1001) if a % 2 == 0]}')
print(f'Результат перемножения всех элементов списка: {reduce(my_func, [a for a in range (99, 1001) if a % 2 == 0])}')