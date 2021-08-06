def my_sum():
    a = False
    sum_ = 0
    while a == False:
        number = input('Введите числа через проблел и $ чтобы закончить программу: ').split()
        z = 0
        for b in range(len(number)):
            if number[b] == '$':
                a = True
                break
            else:
                z = z + int(number[b])
        sum_ = sum_ + z
        print(f'Сумма введенных числе составляет: {sum_}')
    print(f'Общая сумма введеных числе составляет: {sum_}')
my_sum()