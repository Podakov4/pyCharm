#Задача 2. Поступление

quantity_of_russian = int(input('Введите кол-во баллов по русскому языку: '))
quantity_of_mathematics = int(input('Введите кол-во баллов по математике: '))
quantity_of_informatics = int(input('Введите кол-во баллов по информатике: '))

total_quantity = quantity_of_russian \
                 + quantity_of_mathematics \
                 + quantity_of_informatics
min_points = 270
if total_quantity >= min_points:
    print('Поздравляю, ты поступил на бюджет!')
else:
    print('К сожалению, ты не прошёл на бюджет')
    print('Не расстраивайся. Всё к лучшему!')