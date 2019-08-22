"""
1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы. Сортировка должна быть реализована в
виде функции. По возможности доработайте алгоритм (сделайте его умнее).
"""
import random


def bubble(a):
    n = 1
    flag = False
    while n < len(a):
        for i in range(len(a) - n):
            if a[i] < a[i + 1]:
                a[i], a[i + 1] = a[i + 1], a[i]
                flag = True
        if not flag:
            break
        else:
            n += 1
    return a


a = [random.randint(-100, 100) for i in range(20)]
n = 1

print(a)
print(bubble(a))
