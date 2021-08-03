def my_func(a,b):
    return 1 / a ** abs(b)
print(f'Результат - {my_func(int(input("Введите число: ")), int(input("Введите отрицательное число, для возведения в степень: ")))}')