# Задача 11. Рекорд температуры

temperature = None
temp_max = 0

while temperature != 0:
    temperature = int(input('Введите температуру на экваторе: '))
    if temperature > temp_max:
        temp_max = temperature

print('Максимальная температура: ', temp_max)