my_dict = {}
with open('my_text6.txt', 'r', encoding='utf-8') as my_file:
    for line in my_file:
        name, stats = line.split(':')
        name_sum = sum(map(int, ''.join([i for i in stats if i == ' ' or ('0' <= i <= '9')]).split()))
        my_dict[name] = name_sum
    print(f"{my_dict}")