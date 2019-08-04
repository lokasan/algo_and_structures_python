"""
9. Среди натуральных чисел, которые были введены, найти
наибольшее по сумме цифр. Вывести на экран это число и сумму его цифр.
"""
count = int(input("Введите количество вводимых натуральных чисел: "))
maximum = 0
summary_number = 0
maximum_number = 0
while count != 0:
    number = input("Введите натуральное число:")
    save_number = int(number)
    for i in range(len(number) + 1):
        summary_number += int(number) % 10
        number = int(number) // 10
    if summary_number > maximum:
        maximum = summary_number
        maximum_number = save_number
    count -= 1
    summary_number = 0
print(f'Наибольшее число по сумме цифр: {maximum_number} его сумма: {maximum}')
