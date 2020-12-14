# Задача 5. Ресторан

day_of_week = int(input('Введите номер дня недели: '))
time_left = int(input('Введите количество часов до конца рабочего дня: '))
clock = 'час'

if 1 < time_left < 5:
    clock = 'часа'
elif time_left > 4:
    clock = 'часов'

if day_of_week == 1:
    print('Сегодня понедельник.')
    print('Осталось работать', time_left, clock)
elif day_of_week == 2:
    print('Сегодня вторник.')
    print('Осталось работать', time_left, clock)
elif day_of_week == 3:
    print('Сегодня среда.')
    print('Осталось работать', time_left, clock)
elif day_of_week == 4:
    print('Сегодня Четверг.')
    print('Осталось работать', time_left, clock)
elif day_of_week == 5:
    print('Сегодня пятница.')
    print('Осталось работать', time_left, clock)
    if time_left < 2:
        print('Можно уйти пораньше!')
elif day_of_week == 6:
    print('Сегодня суббота.')
    print('Осталось работать', time_left, clock)
elif day_of_week == 7:
    print('Сегодня воскресенье')
    print('Осталось работать', time_left, clock)