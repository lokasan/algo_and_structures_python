"""
1. Проанализировать скорость и сложность одного любого алгоритма,
разработанных в рамках домашнего задания первых трех уроков.
Примечание: попробуйте написать несколько реализаций алгоритма и сравнить их.
"""
from timeit import timeit
import cProfile


def memorize(func):
    def g(n, memory={}):
        r = memory.get(n)
        if r is None:
            r = func(n)
            memory[n] = r
        return r
    return g


def f(n):
    summary = 0
    for i in range(1, n+1):
        summary += i
    return summary


@memorize
def test_digits(n):
    if n == 1:
        return 1
    else:
        return n + test_digits(n - 1)


n = 10
print(test_digits(n) == n*(n+1)//2)
print(f(n) == n*(n+1)//2)
print(timeit("test_digits(n)", setup="from __main__ import test_digits, n"))
print(timeit("f(n)", setup="from __main__ import f, n"))


# функция def f(n) имеет сложность O(n) и выполняется за 0.74-0.84
# рекурсия без мемоизации имеет сложность O(n) и выполняется за 1.55-1.6
# рекурсия с мемоизацией имеет сложность O(n) и выполняется за 0.19
# В итоге наиболее эффективным алгоритмом является рекурсия с мемоизация, которая выполняется за 0.19 из-за того, что
# данные сохраняются в словарь и извлекаются из него, что не требует избыточного заполнения стека вызовов


