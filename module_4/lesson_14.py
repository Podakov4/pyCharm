# Задача 14. Прогрессивный налог 2

profit = int(input('Введите прибыль: '))
tax_1 = 13
tax_2 = 20
tax_3 = 30

if profit < 10000:
    profit = profit * tax_1 / 100
    print('Ваш доход после вычета налога: ', profit)
elif profit > 9999 and profit < 50000:
    profit = (profit - 10000) * tax_2 / 100 + 10000 * tax_1 / 100
    print('Ваш доход после вычета налога: ', profit)
elif profit > 49999:
    profit = (profit - 50000) * tax_3 / 100\
             + (50000 - 10000) * tax_2 / 100 + 10000 * tax_1 / 100
    print('Ваш доход после вычета налога: ', profit)


# задачка сложноватая в том плане, что можно легко запутаться, вопрос в чем,
# проще ли будет создать переменные для сумм-границ (10000, 50000)