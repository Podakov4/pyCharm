# Задача 10. Стипендия

educational_grant = int(input('Стипендия студента составляет (руб.мес.): '))
expenses = int(input('Расходы составляют (руб.мес.): '))
total_expenses = 0
total_educational_grant = educational_grant

for _ in range(9):
    total_educational_grant += educational_grant
    total_expenses += expenses * .03 + expenses
need_money = (total_educational_grant - total_expenses) * -1

print('Студенту необходимо попросить у родителей', int(need_money), 'рублей')