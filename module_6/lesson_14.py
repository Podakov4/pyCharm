# Задача 14. Игра «Компьютер угадывает число» (необязательная)
right_border = 1
left_border = 101



while True:
    N = (left_border + right_border) // 2
    print('Твоё число больше, меньше или равно числу,', N)
    answer = int(input('1 - равно, 2 - больше, 3 - меньше: '))
    if answer == 1:
        print('Число отгадано!')
        break
    elif answer == 2:
        right_border = N

    else:

        left_border = N