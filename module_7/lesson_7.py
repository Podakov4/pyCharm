# Задача 7. Трёхзначные числа

n = int(input('Введите число: '))

for i in range(100, 1000):
    i_1 = i % 10
    i_2 = (i // 10) % 10
    i_3 = i // 100
    if i_1 + i_2 + i_3 == n:
        print('Сумма цифр числа', i, 'равна числу', n)