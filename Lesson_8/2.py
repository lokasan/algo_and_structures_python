"""
2*. Определение количества различных подстрок с использованием хэш-функции.
Пусть дана строка S длиной N, состоящая только из маленьких латинских букв.
Требуется найти количество различных подстрок в этой строке.
"""
import hashlib
string = input("Введите строку только из маленьких латинских букв: ")
count = len(string)
save = set()
for i in range(count):
    if i == 0:
        count = len(string) - 1
    else:
        count = len(string)
    for j in range(count, i, - 1):
        save.add(hashlib.sha1(string[i:j].encode('utf8')).hexdigest())
print(save)
print(f'Количество подстрок в строке "{string}" = {len(save)}')
