# Задача 6. Игра в кубики

cube_of_Kostia = int(input('Кубик Кости: '))
cube_of_owner = int(input('Кубик Владельца: '))

if cube_of_Kostia >= cube_of_owner:
    kostia_pay = cube_of_Kostia - cube_of_owner
    print('Сумма:', kostia_pay)
    print('Костя платит')
else:
    owner_pay = cube_of_Kostia + cube_of_owner
    print('Сумма:', owner_pay)
    print('Владелец платит')
print('Игра окончена')