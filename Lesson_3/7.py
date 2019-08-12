"""
7.	В одномерном массиве целых чисел определить два наименьших элемента.
Они могут быть как равны между собой (оба являться минимальными),
 так и различаться.
"""
from random import randint
array = [randint(0, 100) for i in range(10)]
if array[0] > array[1]:
    min1 = 0
    min2 = 1
else:
    min1 = 1
    min2 = 0

for i in range(2, len(array)):
    if array[i] < array[min1]:
        buff = min1
        min1 = i
        if array[buff] < array[min2]:
            min2 = buff
    elif array[i] < array[min2]:
        min2 = i

print(array)
print(f'{array[min1]}, {array[min2]}')
