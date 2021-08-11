def my_func(a, b, c):
  if a >= b and b >= c:
    return a + b
  elif a <= b and b <= c:
    return b + c
  elif a >= c and b >= c:
    return a + b
  else:
    return a + c
print(f'Результат - {my_func(int(input("Введите первое число: ")), int(input("Введите второе число: ")), int(input("Введите третье число: ")))}')