# Задача 2. Максимум из трёх чисел 2

x = int(input('Число 1: '))
y = int(input('Число 2: '))
z = int(input('Число 3: '))

if x > y and x > z:
    print('Максимальное из введенных чисел:', x)
elif x < y > z:
    print('Максимальное из введенных чисел:', y)
else:
    print('Максимальное из введенных чисел:', z
          )