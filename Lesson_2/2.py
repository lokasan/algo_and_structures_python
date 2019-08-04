"""
2.	Посчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, то у него 3 четные цифры
(4, 6 и 0) и 2 нечетные (3 и 5).
"""


number = int(input("Введите натуральное число: "))
odd = 0
even = 0
save_odd_number = ''
save_even_number = ''
if number == 0:
    print(f'1 четное - ({number})')
    exit()
while number != 0:
    if number % 10 % 2 == 0:
        even += 1
        save_even_number += str(number % 10) + ' '
        number //= 10
    elif number % 10 % 2 != 0:
        odd += 1
        save_odd_number += str(number % 10) + ' '
        number //=10
print(f'{save_even_number} - {even} четн')
print(f'{save_odd_number}- {odd} нечетн ')
