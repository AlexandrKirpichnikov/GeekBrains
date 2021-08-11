a = int(input('В первый день км: '))
b = int(input('Я должен пробежать: '))
day = 1
print('1 -й день:', a)
while a < b:
    a *= 1.1
    day += 1
    print(day,'-й день:', a)