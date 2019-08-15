"""
8.	Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк.
Программа должна вычислять сумму введенных элементов каждой строки и
записывать ее в последнюю ячейку строки.
В конце следует вывести полученную матрицу.
"""
from random import randint


rows = 5
columns = 4
array = [[0 for j in range(columns)] for i in range(rows)]
for i in range(rows):
    summary = 0

    for j in range(columns):
        if j != 3:
            rnd = randint(0, 100)
            array[i][j] = rnd
            summary += rnd
    array[i][3] = summary

for i in array:
    print(f'{i}')
