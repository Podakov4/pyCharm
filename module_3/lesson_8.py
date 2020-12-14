# Задача 8. Тяжёлая жизнь

work_hours = int(input('Введите отработанные часы: '))
loan_balance = int(input('Введите остаток по кредиту: '))
spending_on_food = int(input('Введите траты на еду: '))

salary = (200 * work_hours) / (2 ** 3) + work_hours
expenses = loan_balance + spending_on_food

if salary > expenses:
    print('Часов хватает. Можно отдохнуть')
else:
    print("Часов не хватает. Придётся поработать!")
