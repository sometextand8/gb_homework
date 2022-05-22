# 3. Узнайте у пользователя число n. Найдите сумму чисел
# n + nn + nnn. Например, пользователь ввёл число 3.
# Считаем 3 + 33 + 333 = 369.

input_user = input('enter number n: ')

first = int(input_user)
second = int(input_user * 2)
third = int(input_user * 3)
print(first + second + third)
