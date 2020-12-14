# Задача 9. Плохой циферблат


mileage = int(input('Введите пробег: '))
number_of_day = int(input('Введите номер дня: '))

mileage_01 = mileage // 100
mileage_02 = mileage // 10 % 10
mileage_03 = mileage % 10

sum_of_numbers = mileage_01 + mileage_02 + mileage_03

# print(sum_of_numbers)

if sum_of_numbers > number_of_day:
    mileage = 0
    print('Сброс')
    print('Пробег:', mileage)
else:
    print('Сегодня не сломался')
    print('Пробег:', mileage)