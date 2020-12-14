# Задача 15. (*необязательная)

N = int(input('Введите количество карточек: '))
n_sum = 0
i_sum = 0

for i in range(1, N):
    card = int(input('Введите значение карточки: '))
    n_sum += card
    i_sum += i

card = i_sum + N - n_sum

print('Потерянная карточка:', card)