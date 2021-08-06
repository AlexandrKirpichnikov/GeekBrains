from itertools import count

my_list = [3, 3, 3, 69, 54, 2, 2, 2, 100, 1, 42]
new_list = [el for el in my_list if my_list.count(el) == 1]
print(my_list)
print(new_list)
