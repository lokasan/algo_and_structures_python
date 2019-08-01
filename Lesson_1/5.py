#5.	Пользователь вводит две буквы. Определить, на каких местах
# алфавита они стоят, и сколько между ними находится букв.
symb1 = input('Введите первую букву английского алфавита: ')
symb2 = input('Введите вторую букву английского алфавита: ')
alp_count = 26
unicode_last_pos = 122
print(f'{symb1} - позиция {alp_count - (unicode_last_pos - ord(symb1))}')
print(f'{symb2} - позиция {alp_count - (unicode_last_pos - ord(symb2))}')
print(f'количество букв между введенными = {abs(ord(symb1) - ord(symb2))-1}')
