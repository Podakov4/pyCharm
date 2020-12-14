# Задача 1. Калькулятор опыта

experience = int(input('Введите количество опыта: '))
level = 1


if experience < 2499 and experience > 999:
    level += 1
elif experience < 4999 and experience > 2499:
    level += 2
elif 5000 <= experience:
    level += 3
else:
    print('Ошибка, вы ввели неверное число')
print('Ваш уровень: ', level)