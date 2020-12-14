# Задача 7.

a = int(input('Введите начало отрезка: '))
b = int(input('Введите конец отрезка: '))
c = int(input('Введите промежуток между числами: '))
number_count = 0
number_sum = 0

for number in range(a, b+1, c):
    number_count += 1
    number_sum += number

arithmetic_mean = number_sum / number_count
print('Средняя арифметическая суммы чисел из отрезка кратных', c, 'равна: ', arithmetic_mean)