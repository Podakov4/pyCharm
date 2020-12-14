# Задача 5. Модуль числа

number = int(input('Введите число: '))

if number < 0:
    number_1 = number * -1
    print('Ввели', str(number) + ', ответ', number_1)
else:
    print('Ввели', str(number) + ', ответ', number)