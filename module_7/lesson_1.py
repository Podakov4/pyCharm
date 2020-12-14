# Задача 1. Тайны археологии

cipher = 114, 12, 14, 10605, 4907, 450

for number in cipher:
    if number % 2 == 0 and number % 3 > 0:
        print('Число', number, 'делится на два и не делится на три')