# Задача 5. Календари

day_of_calendar = None
calendar_count = 0
compare = 0

while True:
    day_of_calendar = int(input('Число месяца: '))
    if day_of_calendar == 0:
        break
    compare = day_of_calendar % 2
    if compare == 0:
        calendar_count += 1

print('В этом календаре:', calendar_count, 'четных дней')