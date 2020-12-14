# Задача 8. Факториал

N = int(input('Введите число: '))
factorial = 1

for i in range(1, N + 1):
    factorial = factorial * i

print('Факториал числа', N, 'равен', factorial)