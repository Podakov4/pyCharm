# Задача 4. Это будет бомба

bomb_bang = 10

for remained_seconds in range(bomb_bang, -1, -1):
    if remained_seconds == 0:
        print('Бомба взорвалась')
    else:
        action = int(input('Хотите ли вы обезвредить бомбу сейчас?: '))
        if action == 0:
            print('До взрыва осталось', remained_seconds)
        else:
            print('Вы обезвредили бомбу!')
            break