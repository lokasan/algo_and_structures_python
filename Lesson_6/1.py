"""
1. Подсчитать, сколько было выделено памяти под переменные в ранее
разработанных программах в рамках первых трех уроков. Проанализировать
результат и определить программы с наиболее эффективным использованием памяти.
Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько
вариантов кода для одной и той же задачи. Результаты анализа вставьте в виде
комментариев к коду. Также укажите в комментариях версию Python
и разрядность вашей ОС.
"""
from memory_profiler import profile
import cProfile
from random import randint


@profile
def sum_min_and_max():
    array = [randint(0, 100) for i in range(150000)]
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


def memorize(func):
    def g(n, memory={}):
        r = memory.get(n)
        if r is None:
            r = func(n)
            memory[n] = r
        return r
    return g

@profile
def f(n):
    summary = 0
    for i in range(1, n+1):
        summary += i
    return summary

@profile
# @memorize
def test_digits(n):
    if n == 1:
        return 1
    else:
        return n + test_digits(n - 1)


n = 100
print(test_digits(n) == n*(n+1)//2)
print(f(n) == n*(n+1)//2)

if __name__ == '__main__':
    f(n)               # инкремент 0 мб, всего используется 28 мб

    test_digits(n)     # инкремент 0 мб, 28.4 мб | разница между данными реализациями в занимаемом объеме памяти отсутст
                       # вует из-за такого, что неиспользуются объекты, которые бы занимали много ресурсов.

    sum_min_and_max()  # инкремент на строке 17 "array = [randint(0, 100) for i in range(150000)]" 0.3 мб только
                       # почему-то стало использоваться 29.7 мб, было выделено изначально 28.4, затем используемая
                       # память понизилась до 29.3 мб и осталось такой до конца выполнения программного кода.
                       # память занята объектом словаря.
