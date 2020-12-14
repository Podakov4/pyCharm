health_vally = 100

for way in range(1, int(health_vally / 5 * 2) + 1):
    print('Валли проехал', way * 4, 'м.')
    print('Осталось ехать: ', health_vally // 5 * 2 * 4 - way * 4, 'м.')
    print('Прочности осталось', health_vally - way * 5 / 2, 'м.')
    print()
