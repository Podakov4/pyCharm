N = int(input('Введите число: '))
check = 0
compilated = 0
natural_number = 0

for number in range(1,  N + 1):
    check = N % number
    if check == 0:
        compilated += 1
        print('Делитель:', number)
if compilated > 2:
    print('Это сложное число!')
else:
    print('Это простое число')
print('Количество делителей', compilated)