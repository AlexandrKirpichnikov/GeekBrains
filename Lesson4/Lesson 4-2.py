my_list = [40, 2, 5, 10, 1, 100, 99, 235, 20]
new_list = [a for i, a in enumerate(my_list) if i != 0 and my_list[i - 1] < my_list[i]]
print(f'Основной список: {my_list}')
print(f'Новый список: {new_list}')