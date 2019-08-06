"""
4.	Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.
"""


def my_range(n, c=1):
    if n == c:
        return str(1 / pow(-2, n - 1))
    else:
        return str(1 / pow(-2, c - 1)) + ' ' + my_range(n, c + 1)


n = int(input("Введите количество элементов ряда: "))

elements_range = my_range(n)
elements_range = elements_range.split()
summary = 0

for elements in elements_range:
    summary += float(elements)

print(f'Сумма ряда {elements_range} = {summary}')
