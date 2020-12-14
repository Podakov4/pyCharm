# Задача 5. Антошка, пора копать картошку

performed = int(input('Сколько метров уже вскопали?: '))
space = int(input('Через сколько метров другт от друга растёт картофель?: '))
potato_tuber = 0

for meter in range(performed, 101, space):
    potato_tuber += 3
    print('Картофеля выкопано:', potato_tuber, 'на', str(meter) + '-м метре')

print()
print('Картофеля выкопано всего:', potato_tuber, 'клубней картофеля')
