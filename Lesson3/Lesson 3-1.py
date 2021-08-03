def my_func():
    try:
        a = int(input('Введите делимое: '))
        b = int(input('Введите делитель: '))
    except ValueError:
        return
    if b == 0:
        print('На ноль делить нельзя!')
    else:
        s_full = a/b
        return s_full
print(my_func())
