def sal():
    try:
        time = float(input('Введите вашу выработку в часах: '))
        salary = int(input('Введите вашу ставку в долларах: '))
        prize = int(input('Введите вашу премию: '))
        res = time * salary + prize
        print(f'Ваша заработная плата составляет: {res}', '$')
    except ValueError:
        return print('Введите число еще раз: ')
sal()