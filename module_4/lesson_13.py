# Задача 13. Новоселье

apartment_area = int(input("Введите площадь просторной квартиры (кв.м.): "))
apartment_cost = int(input("Введите стоимость просторной квартиры (тыс.руб.): "))

if apartment_area >= 100 and apartment_cost <= 10000000:
    print('Вам вы можете позволить себе эту квартиру!')
elif 100 > apartment_area >= 80 and apartment_cost <= 7000000:
        print('Смотрите, вам подходит второй вариант')
else:
    print('Вариантов пока нет')



#Первый вариант — они готовы взять квартиру попросторнее
#(не менее 100 квадратных метров), но стоимостью не более 10 млн.

#Второй вариант — немного расширить круг поиска, то есть взять
# квартиру поменьше (от 80 квадратный метров), но и стоимостью не более 7 млн.
