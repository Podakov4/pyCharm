# Задача 10. Обычный день на работе

call = 0
score = 0
number_of_tasks = 0
a_task = 0
hours_of_work = 1

print('Начался 8-часовй день')
while hours_of_work < 9:
    print( hours_of_work, 'час')
    a_task = int(input('Сколько задач решит Максим?: '))
    number_of_tasks += a_task
    call = int(input('Звонит Жена. Взять трубку?: '))
    if call == 1:
        score = 1
    hours_of_work += 1

print('Рабочий день закончился. Всего задач выполнено:', number_of_tasks)
if score == 1:
    print('Нужно зайти в магазин')

