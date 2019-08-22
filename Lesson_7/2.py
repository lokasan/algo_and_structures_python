"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный
и отсортированный массивы.
"""
import random


def merged_list(a):
    if len(a) > 1:
        center = len(a) // 2
        left = a[:center]
        right = a[center:]
        merged_list(left)
        merged_list(right)
        i, j, k = 0, 0, 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                a[k] = left[i]
                i += 1
            else:
                a[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            a[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            a[k] = right[j]
            j += 1
            k += 1
        return a


a = [round(random.uniform(0, 50), 2) for i in range(20)]
print(a)
print(merged_list(a))
