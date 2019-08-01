# 1.	Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.
num = int(input("give me please three figures: "))
summary = (num % 10) + (num // 10 % 10 ) + (num // 100 % 10)
comp = (num % 10) * (num // 10 % 10 ) * (num // 100 % 10)
print(f'сумма = {summary} произведение = {comp}')

