# Задача 4. Калькулятор скидки

chair_1 = int(input('Введите стоимость стула'
                    ' из первого магазина: '))
chair_2 = int(input('Введите стоимость стула'
                    ' из второго магазина: '))
chair_3 = int(input('Введите стоимость стула'
                    ' из третьего магазина: '))

sum_of_check = chair_1 + chair_2 + chair_3

if sum_of_check > 10000:
    sum_of_check -= sum_of_check * 10 / 100
    print('Итоговая стоимость:', sum_of_check, 'рублей')
else:
    print('Итоговая стоимость:', sum_of_check, 'рублей')