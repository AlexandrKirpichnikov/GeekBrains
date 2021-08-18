summa: int = 0
count: int = 0
persons = []
with open('my_text3.txt', 'r') as my_file:
    for line in my_file:
        tokens = line.split()
        if int(tokens[2]) <= 20000:
            persons.append(tokens[0])
        summa += int(tokens[2])
        count += 1
result = summa / count
print(f"Сотрудники имеющие оклад менее 20000: {persons}")
print(f"Средняя велична дохода: {result}")