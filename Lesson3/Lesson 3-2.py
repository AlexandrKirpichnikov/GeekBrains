def my_func(name, surname, birth, city, email, phone):
    name = str(input('Введите ваше имя: '))
    surname = str(input('Введите вашу фамилию: '))
    birth = int(input('Введите ваш год рождения: '))
    city = str(input('Введите ваш город проживания: '))
    email = str(input('Введите ваш электронный адрес: '))
    phone = int(input('Введите ваш телефон: '))
    return(name, surname, birth, city, email, phone)
print(my_func('name', 'surname', 'birth', 'city', 'email', 'phone'))