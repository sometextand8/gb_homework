# 4. Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе. Для решения используйте
# цикл while и арифметические операции.

input_num = int(input('enter number: '))
look = 0
while input_num > 0:

    max_number = input_num % 10
    input_num = input_num // 10
    if max_number > look:
        look = max_number

print(look)
