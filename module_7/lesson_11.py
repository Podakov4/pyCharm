# Задача 11. Биолаборатория

test_tube = int(input('Сколько бактерий в пробирке?: '))
a = int(input('Стартовая температура в первой пробирке: '))
b = int(input('Конечная температура в первой пробирке: '))
population_1 = test_tube
for temp_1 in range(a, b + 1):
    if population_1 == test_tube:
        population_1 *= temp_1
    else:
        population_1 *= temp_1

print('Популяция в первой пробирке:', population_1)

c = int(input('Стартовая температура во второй пробирке: '))
d = int(input('Конечная температура во второй пробирке: '))
population_2 = test_tube

for temp_2 in range(c, d + 1):
    if population_2 == test_tube:
        population_2 *= temp_2
    else:
        population_2 *= temp_2

print('Популяция во второй пробирке:', population_1)

difference_populations = population_1 - population_2
if difference_populations < 0:
    difference_populations *= -1

print('Разность популяции:', difference_populations)