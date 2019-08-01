"""
4.	Написать программу, которая генерирует в указанных пользователем границах
●	случайное целое число,
●	случайное вещественное число,
●	случайный символ.
Для каждого из трех случаев пользователь задает свои границы диапазона.
Например, если надо получить случайный символ от 'a' до 'f',
то вводятся эти символы. Программа должна вывести на экран любой
символ алфавита от 'a' до 'f' включительно.
"""
import random


print('Введите диапазон целых чисел')
start = int(input('start: '))
end = int(input('end: '))
if start > end:
    exit(-1)
else:
    print(f'Результат: {random.randint(start, end)}')

print('Введите диапазон вещественных чисел')
start = float(input('start: '))
end = float(input('end: '))
if start > end:
    exit(-1)
else:
    print(f'Результат: {random.uniform(start, end)}')

print('Введите диапазон символов английского алфавита')
start = input('start: ')
end = input('end: ')
if ord(start) > ord(end):
    exit(-1)
else:
    print(f'Результат: {chr(random.randint(ord(start), ord(end)))}')
