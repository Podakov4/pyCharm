# Задача 14. ...Теперь можно посчитать и свою

a_years_wage = 0
decrease = 0
wage_month_2 = 0
for month in range(1, 11):
    wage_month_1 = int(input('Введите зарплату за ' + str(month) + ' месяц: '))
    if wage_month_2 == 0:
        wage_month_2 = 0
    elif wage_month_1 < wage_month_2:
        decrease += 1
        decline = wage_month_2 - wage_month_1
        print('Зарплата стала ниже на', decline, 'руб.')
    wage_month_2 = wage_month_1


print('Снижалась:', decrease, "раз")