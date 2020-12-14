number = int(input('Сколько нужно считать?: '))


for _ in range(number // 2 * 2 + number % 2 - number % 2, 0, -2):
    print(_)