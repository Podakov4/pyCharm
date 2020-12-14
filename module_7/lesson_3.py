# Задача 3. Посчитай чужую зарплату...

a_years_wage = 0

for month in range(1, 13):
    wage_month = int(input('Введите зарплату за ' + str(month) + ' месяц: '))
    a_years_wage += wage_month

average_wage = a_years_wage / 12
print('Средняя зарплата работника за 12 месяцев равна:', average_wage)