# Задача 13. Лесенка

amount_step = int(input('Введите количество ступеней: '))
step_sum = ''
for i in range(1,amount_step + 1):
    step_sum += str(i)
    print(step_sum)
    i += 1
