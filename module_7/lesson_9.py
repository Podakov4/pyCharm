# Задача 9. Успеваемость в классе

N = int(input('Введите количество учеников сегодня в классе: '))

excellent = 0
good = 0
c_grade = 0
text = ''

for i in range(N):
    i = int(input('Введите оценку ученика: '))
    if i == 5:
        excellent += 1
    elif i == 4:
        good += 1
    else:
        c_grade += 1

if excellent < c_grade > good:
    text = 'Количество троечников преобладало на уроке'
elif good < excellent > c_grade:
    text = 'На уроке было больше всех отличников'
else:
    text = 'Хорошистов было больше всех'

print('Сегодня на уроке присутствовали:')
print(text)