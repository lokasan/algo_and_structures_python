# 4.	Определить, какое число в массиве встречается чаще всего.
arr1 = [1, 1, 1, 1, 6, 4, 3, 6, 3, 6, 6, 6, 7, 8, 9, 3, 3]
sum_elements = [0 for i in range(max(arr1) + 1)]
for i in range(len(arr1)):
    sum_elements[arr1[i]] += 1
for i in range(len(sum_elements)):
    if sum_elements[i] == max(sum_elements):
        print(f'Число {i} встречается {max(sum_elements)} раз ')
        break
