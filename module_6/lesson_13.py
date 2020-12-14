# Задача 13. Игра «Угадай число»

number = int(input('Загадайте число: '))
attempt = int(input('Введите число для разгадки: '))
attempt_count = 0

while attempt != number:

    if attempt > number:
        print('Число больше, чем нужно. Попробуйте ещё раз!')
    else:
        print('Число меньше, чем нужно. Попробуйте ещё раз!')
    attempt = int(input('Введите число для разгадки: '))
    attempt_count += 1
print('Вы угадали! Количество попыток:', attempt_count)

