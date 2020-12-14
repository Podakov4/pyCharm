# Задача 9. Опять двойка

rating = int(input('Что получил по математике? '))
if rating == 2 or rating == 3:
 print('Плохо. Марш учиться!')
elif rating == 4 or rating == 5:
 print('Молодец! Можешь отдохнуть.')

 # почему не работает способы
 # if rating == (2 or 3)
 # if rating == (4 or 5)
 # Или так нельзя сокращать?