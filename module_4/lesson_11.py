# Задача 11. Костя хочет выигрывать

number_1 = int(input('Введите первое выпавшее число: '))
number_2 = int(input('Введите второе выпавшее число: '))
number_3 = int(input('Введите третье выпавшее число: '))

if number_1 == number_2 == number_3:
    print('Совпало 3 числа')
elif number_1 == number_2 or number_1 == number_3 or number_2 == number_3:
    print('Совпало 2 числа')
else:
    print('Все числа разные, 0 очков')


# Задача 12. Ленивый бизнес

number_of_machines = int(input('Введите количество станков: '))
room_area = int(input('Введите площадь помещения: '))

if number_of_machines > 4 and room_area > 99:
    print('Всё отлично, это наш вариант!')
else:
    print('Не подходит. Нужно искать дальше')
