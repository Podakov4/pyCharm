# Задача 2. Сумма нечетных

num_stop = int(input('Подсчет суммы закончится на числе: '))
num_summ = 0
for number in range(1, num_stop // 2 * 2 + num_stop % 2 + 1, 2):
    print(number)
    num_summ += number
print('Сумма всех нечетных чисел равна:', num_summ)