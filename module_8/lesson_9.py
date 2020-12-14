# Задача 9. Письмо

weight_letter = int(input('Введите ширину письма: '))
height_letter = int(input('Введите длину письма: '))

folding_weight = weight_letter // 13
folding_height = height_letter // 13
folding = folding_height + folding_weight

print('Письмо нужно свернуть', folding, 'раз')