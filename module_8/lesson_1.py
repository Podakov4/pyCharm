# Задача 1. Космическая еда

buckwheat = 100
monthly_rate = 4

for month in range(1, 26):
    buckwheat -= 4
    print('Сейчас,', month, 'месяц, запас гречки в следующем месяце составит:', buckwheat, 'кг')
