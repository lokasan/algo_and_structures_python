# 6.	Пользователь вводит номер буквы в алфавите. Определить, какая это буква.
number = int(input('Введите порядкрвый номер буквы английского алфавита: '))
if number < 1 or number > 26:
    exit(-1)
else:
    unicode_first_symb = 96
    print(chr(unicode_first_symb + number))
