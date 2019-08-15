"""
1. Пользователь вводит данные о количестве предприятий, их наименования и
прибыль за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия..
Программа должна определить среднюю прибыль (за год для всех предприятий) и
вывести наименования предприятий, чья прибыль выше среднего и отдельно
вывести наименования предприятий, чья прибыль ниже среднего.
"""
import collections
Company = collections.namedtuple('Company', ['name', 'q1', 'q2', 'q3', 'q4'])
company_list = list()
count_company = int(input('Введите количество предприятий: '))
for i in range(count_company):
    name = input('Введите название предприятия: ')
    q1 = int(input('Введите прибыль за 1 квартал'))
    q2 = int(input('Введите прибыль за 2 квартал'))
    q3 = int(input('Введите прибыль за 3 квартал'))
    q4 = int(input('Введите прибыль за 4 квартал'))
    company_list.append(Company(name=name, q1=q1, q2=q2, q3=q3, q4=q4))
total_avg = 0
for objects in company_list:
    c = objects
    total_avg += (c.q1 + c.q2 + c.q3 + c.q4) / len(company_list)
for objects in company_list:
    c = objects
    if c.q1 + c.q2 + c.q3 + c.q4 > total_avg:
        print(f'У предприятия {c.name} прибыль выше среднего = {c.q1 + c.q2 + c.q3 + c.q4}')
    else:
        print(f'У предприятия {c.name} прибыль ниже среднего {c.q1 + c.q2 + c.q3 + c.q4}')

