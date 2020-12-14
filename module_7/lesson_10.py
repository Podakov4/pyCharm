# Задача 10. Отрезок

a = int(input('Введите начало отрезка: '))
b = int(input('Введите конец отрезка: '))
i_summ = 0
i_count = 0

for i in range(a, b + 1):
    if i % 3 == 0:
        i_summ += i
        i_count += 1

arithmetical_mean = i_summ / i_count

print('Средняя арифметическая из отрезка равна: ', arithmetical_mean)