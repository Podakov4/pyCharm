# Задача 8. Функция 2

x_1 = int(input('Введите начальное значение X: '))
x_2 = int(input('Введите конечное значение X: '))
s = int(input('Введите шаг с которым X будет скакать по точкам: '))

for x in range(x_2, x_1 - 1, s):
    y = x ** 3 + 2 * x ** 2 - 4 * x + 1
    print('В точке', x, 'y равен: ', y)