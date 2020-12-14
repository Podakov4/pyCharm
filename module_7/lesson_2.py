# Задача 2. Должники

bank_client_count = 0

for bank_client in range(10):
    client_number = int(input('Введите номер клиента: '))
    if client_number % 2 == 0 and client_number > 0:
        bank_client_count += 1

print('По параметрам подходит следующее количество клиентов:', bank_client_count, 'человек')

