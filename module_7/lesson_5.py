# Задача 5. С заботой о природе

disturbance_count = 0

for sector in range(30, 36):
    amount_peoples = int(input('Людей в секторе ' + str(sector) + ': '))
    if amount_peoples > 10:
        print('Нарушение! Слишком много людей в секторе!')
        disturbance_count += 1
    else:
        print("Всё спокойно.")

print("Количество нарушений:", disturbance_count)