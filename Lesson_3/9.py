# 9.	Найти максимальный элемент среди минимальных элементов столбцов матрицы.
from random import randint
m = int(input('Введите количество строк '))
n = int(input('Введите количество столбцов'))
array = [[randint(0, 100) for j in range(n)] for i in range(m)]
array_min = list()
array_min_result = list()
print(array)
for j in range(n):
    for i in range(m):
        array_min.append(array[i][j])
    array_min_result.append(min(array_min))
    array_min = []
print(f'Минимальные элементы стобцов матрицы : {array_min_result}')
print(f'Максимальный элемент среди минимальных = {max(array_min_result)}')
