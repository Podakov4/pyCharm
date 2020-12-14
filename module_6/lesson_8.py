# Задача 8. Продолжаем бегать

run_km = int(input('Сколько километров в первый день спортсмен?: '))
day_count = 0
required_mileage = int(input('Какого результата нужно добиться спортсмену?(км): '))
day = 'дней'
while run_km < required_mileage:
    if run_km > required_mileage:
        break
    run_km = run_km * 1.1
    day_count += 1

if day_count == 1:
    day = 'день'
elif day_count < 5:
    day = 'дня'

print('Через', day_count, day, 'спортсмен пробежал больше', required_mileage, 'км, а именно:', run_km, 'км')