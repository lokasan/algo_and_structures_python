#5.	В массиве найти максимальный отрицательный элемент.
# Вывести на экран его значение и позицию (индекс) в массиве.
from random import randint
array = [randint(-100, 100) for i in range(20)]
maximum_negative = float('-inf')
save_index = 0
for i in range(len(array)):
    if maximum_negative < array[i] < 0:
        maximum_negative = array[i]
        save_index = i
print(array)
print(f'значение = {maximum_negative} позиция = {save_index}')
