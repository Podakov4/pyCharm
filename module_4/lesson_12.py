# Задача 12. Ленивый бизнес


number_of_machines = int(input('Введите количество станков: '))
room_area = int(input('Введите площадь помещения: '))

if number_of_machines > 4 and room_area > 99:
    print("Всё отлично, это наш вариант!")
else:
    print('Не подходит. Нужно искать дальше')