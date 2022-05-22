# 1. Поработайте с переменными, создайте несколько, выведите на экран.
# Запросите у пользователя некоторые числа и строки
# и сохраните в переменные, затем выведите на экран.

some_num = 8
some_text = 'Hello'

print(some_num, some_text, sep='\n')
print()
input_from_user_text = input('Enter some text: ')
input_from_user_number = int(input('Enter some number: '))
print()
print(f'your text - {input_from_user_text}\nyour number - {input_from_user_number}')
