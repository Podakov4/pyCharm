# Задача 8. Перемена

number_1 = int(input('Загадайте первое число: '))
number_2 = int(input('Загадайте второе число число: '))

#number_1 %= 2
#number_2 %= 2

if (number_1 % 2 and number_2 % 2) == 0:
    print('Одно из чисел чётное. Учитель заслужил конфету!')
else:
    print('Оба числа нечётные. Детям положена конфета.')

# Тут два варианта решения, какое лучше для программиста, сначала решить, а потом сравнивать или сразу
# сравнивать решая попутно? (Надеюсь корректно задал вопрос :) )