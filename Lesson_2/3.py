"""
3.	Сформировать из введенного числа обратное по порядку входящих в него
цифр и вывести на экран. Например, если введено число 3486,
 то надо вывести число 6843.
"""


def my_reverse(number):
    if number < 0:
        exit(-1)
    if len(str(number)) == 1:
        return str(number % 10)
    else:
        return str(number % 10) + ' ' + str(my_reverse(number // 10))


number = int(input("Введите число: "))
print(my_reverse(number))
