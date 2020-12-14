# Задача 9. Поставьте оценку!

review = None
rating_positive = 0
rating_negative = 0

while review != 0:
    review = int(input('Введите рейтинг: '))
    if review > 0:
        rating_positive += 1
    else:
        rating_negative += 1

print('Положительных отзывов:',  rating_positive)
print('Негативных отзывов:',  rating_negative)