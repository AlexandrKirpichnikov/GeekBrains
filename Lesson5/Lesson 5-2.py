f = open(r"C:\Users\Alex\PycharmProjects\GeekBrains\Lesson5\my_text2.txt", "w")
str_text = ['Купить мощный компьютер в компьютерном магазине''\n''Установить на компьютер основные программы''\n']
f.writelines(str_text)
f.close()

with open('my_text2.txt') as r:
    line_count = 0
    for line in r:
        line_count += 1
print('Колличество строк в тексте: ', line_count)

with open('my_text2.txt') as r:
    for line in r.readlines():
        words: int = len(line.split())
        print('Колличество слов в строке: ', words)
