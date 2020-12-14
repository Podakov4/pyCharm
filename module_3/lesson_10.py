x = int(input('Число 1: '))
y = int(input('Число 2: '))
z = int(input('Число 3: '))

if x > y:
    a = x
else:
    a = y
if a > z:
    b = a
else:
    b = z

print('Максимальное из введенных чисел:', b)