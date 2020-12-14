# Задача 6. Счастливый билетик


ticket = int(input('Введите номер билета: '))

start = ticket // 1000
finish = ticket % 1000

summ_of_start = 0
summ_of_finish = 0


while start > 0 or finish > 0:
    summ_of_start += start % 10
    start //= 10
    summ_of_finish += finish % 10
    finish //= 10

if summ_of_start != summ_of_finish:
    print('Ваш билет не счастливый')
else:
    print('Ваш билет счастливый!')