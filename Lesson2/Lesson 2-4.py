words = str(input('Напишите любое предложение: '))
x = words.split()
y = 1
for i in x:
    print(y,'-', i[:10])
    y += 1