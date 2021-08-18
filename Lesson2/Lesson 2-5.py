my_list = [7, 5, 3, 3, 2]
number = int(input('Введите любое число: '))
my_list.append(number)
print(sorted(my_list, reverse=True))