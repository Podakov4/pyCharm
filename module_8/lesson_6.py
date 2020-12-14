# Задача 6. Грустная история

tree_age = int(input('Сколько лет было дереву?: '))
planting_interval = int(input('Через какое количество лет, Алёна будет сажать деревья?: '))
planting_count = 0

for planting in range(6, tree_age, planting_interval):
    planting_count += int(input('Сколько посадить деревьев?: '))
print()
print('Деревье посажено:', planting_count)