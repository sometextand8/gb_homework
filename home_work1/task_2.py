# 2. Пользователь вводит время в секундах.
# Переведите время в часы, минуты, секунды
# и выведите в формате чч:мм:сс.
# Используйте форматирование строк.


input_sec = int(input('Enter time in seconds: '))

hours = input_sec // 3600
minuts = (input_sec - hours * 3600) // 60
seconds = (input_sec - hours * 3600) % 60


print('{} - seconds equals\n{}hh:{}mm:{}ss.'.format(input_sec, hours, minuts, seconds))
