"""
8.	Посчитать, сколько раз встречается определенная цифра в введенной
 последовательности чисел. Количество вводимых чисел и цифра,
 которую необходимо посчитать, задаются вводом с клавиатуры.
"""
count_numbers = int(input("Сколько чисел нужно? "))
search_digit = int(input("Какую цифру нужно посчитать?"))
count = 0

while count_numbers != 0:

    temp = input('Введите число: ')

    for i in range(len(temp) + 1):
        if int(temp) % 10 == search_digit:
            count += 1
        temp = int(temp) // 10

    count_numbers -= 1

print(f'Количество {search_digit} в последовательности = {count}')
