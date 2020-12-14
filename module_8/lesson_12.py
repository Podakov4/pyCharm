# Задача 12. Выражение

x = int(input('Введите число X: '))
var = (x - 1) / (x - 2)

for a in range(3, 63, 2):
    var = var * (x - a) / (x - a + 1)
    print(var)