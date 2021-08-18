f = open("my_text5.txt", 'w', encoding='utf-8')
str_text = ('10  8  5  30  66  14  3  87  26')
f.writelines(str_text)
f.close()

with open('my_text5.txt', 'r') as my_file:
    my_num = str_text.split()
    print(sum(map(int, my_num)))