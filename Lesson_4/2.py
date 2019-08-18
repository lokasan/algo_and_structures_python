"""
2. Написать два алгоритма нахождения i-го по счёту простого числа.
Без использования «Решета Эратосфена»;
Используя алгоритм «Решето Эратосфена»
"""
import timeit

def simple_position(n):
    count = 1
    simple = 2
    while count <= n:
        temp = 1
        is_simple = True
        while temp <= simple:
            if simple % temp == 0 and temp != simple and temp != 1:
                is_simple = False
                break
            temp += 1
        if is_simple:
            if count == n:
                break
            count += 1
        simple += 1

    return simple


def simple_era(n):
    simple = 2
    limit = 10000
    array = [i for i in range(limit)]
    array[1] = 0
    while simple < limit:
        if array[simple] != 0:
            m = simple * 2
            while m < limit:
                array[m] = 0
                m += simple
        simple += 1
    return [p for p in array if p != 0][n-1]


n = int(input('Введите позицию простого числа: '))
print(simple_position(n))
print(simple_era(n))
print(timeit.timeit('simple_position(n)', setup='from __main__ import simple_position, n', number=100))
print(timeit.timeit('simple_era(n)', setup='from __main__ import simple_era, n', number=100))
