"""
6.	В одномерном массиве найти сумму элементов, находящихся
между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать.
"""
from random import randint
array = [randint(0, 100) for i in range(15)]
print(array)
minimum = float('inf')
maximum = 0
minimum_index = 0
maximum_index = 0
summary = 0
for i in range(len(array)):
    if array[i] > maximum:
        maximum = array[i]
        maximum_index = i
    elif array[i] < minimum:
        minimum = array[i]
        minimum_index = i
if minimum_index > maximum_index:
    for i in range(minimum_index + 1, len(array)):
        summary += array[i]
    for i in range(maximum_index):
        summary += array[i]
elif len(array) - 1 == minimum_index and maximum_index == 0:
    summary = 0
elif maximum_index > minimum_index:
    for i in range(minimum_index + 1, maximum_index):
        summary += array[i]

print(f'Сумма между наименьшим и наибольшим элементами = {summary}')
