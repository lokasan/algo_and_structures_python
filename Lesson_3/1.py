# 1.	В диапазоне натуральных чисел от 2 до 99 определить,
# сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
digits = [i for i in range(2, 10)]
digits2 = [j for j in range(2, 100)]
count = 0
for i in range(len(digits)):
    for j in range(len(digits2)):
        if digits2[j] % digits[i] == 0:
            count += 1
    print(f'{digits[i]} - {count}')
    count = 0
