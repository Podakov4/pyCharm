# Задача 3. Долги

sum_debtor = int(input('Введите количество должников: '))
debt = 0

for debtor in range(0, sum_debtor + 1, 5):
    print('Должник с номером:', debtor)
    debt += int(input('Сколько должны?: '))
print('Общая сумма долга:', debt)