# 9.Вводятся три разных числа. Найти, какое из них
# является средним (больше одного, но меньше другого).
num1 = float(input("Введите 1 число: "))
num2 = float(input("Введите 2 число: "))
num3 = float(input("Введите 3 число: "))

if num3 > num1 > num2 or num2 > num1 > num3 :
    print(f'{num1} является средним')
elif  num3 > num2 > num1 or num1 > num2 > num3:
    print(f'{num2} является средним')
elif num2 > num3 > num1 or num1 > num3 > num2:
    print(f'{num3} является средним')
