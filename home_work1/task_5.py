# 5. Запросите у пользователя значения выручки и издержек фирмы. Определите, с каким
# финансовым результатом работает фирма. Например, прибыль — выручка больше издержек,
# или убыток — издержки больше выручки. Выведите соответствующее сообщение.
# Если фирма отработала с прибылью, вычислите рентабельность выручки. Это отношение
# прибыли к выручке. Далее запросите численность сотрудников фирмы и определите прибыль
# фирмы в расчёте на одного сотрудника.


revenue = int(input('Введите прибыль фирмы: '))
costs = int(input('Введите убыток фирмы: '))

if revenue > costs:
    rentab = revenue / costs
    if rentab > 0:
        number_of_costumer = int(input('enter number of coustomer: '))
        result = revenue / number_of_costumer
        print(f'Прибыль на сотпудника - {result}')
    print('Прибыль у фирмы')
else:
    print('Убытки у фирмы')
