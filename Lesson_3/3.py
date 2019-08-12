#3.	В массиве случайных целых чисел поменять местами минимальный
# и максимальный элементы.
from random import randint
arr1 = [randint(i, 100) for i in range(10)]
maximum = 0
minimum = float('inf')
maximum_i = 0
minimum_i = 0
for i in range(len(arr1)):
    if arr1[i] > maximum:
        maximum = arr1[i]
        maximum_i = i
    elif arr1[i] < minimum:
        minimum = arr1[i]
        minimum_i = i

print(arr1)
arr1[minimum_i], arr1[maximum_i] = arr1[maximum_i], arr1[minimum_i]
print(arr1)
