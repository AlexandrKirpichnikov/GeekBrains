f = open('my_text.txt', 'w')
while True:
    text = input('Введите любую строку в текстовый фаил: ')
    if text == '':
        break
    f.write(text+'\n')
f.close()