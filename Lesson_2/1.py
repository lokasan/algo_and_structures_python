"""
1.	Написать программу, которая будет складывать, вычитать, умножать или делить
два числа. Числа и знак операции вводятся пользователем. После выполнения
вычисления программа не должна завершаться, а должна запрашивать новые данные
для вычислений. Завершение программы должно выполняться при вводе символа '0'
в качестве знака операции. Если пользователь вводит неверный знак
(не '0', '+', '-', '*', '/'), то программа должна сообщать ему об ошибке и
снова запрашивать знак операции.
Также сообщать пользователю о невозможности деления на ноль,
если он ввел 0 в качестве делителя.
"""
while True:
    sign = input("Введите знак оператора для выполнения действия над числами ('+', '-', '*', '/') для выхода введите 0")
    if sign == '0':
        print("До свидания")
        break
    elif sign != '+' and sign != '-' and sign != '*' and sign != '/':
        print("Вы ввели неверный знак оператора, повторите ввод.")
    else:
        num1 = float(input("Введите первое число: "))
        num2 = float(input("Введите второе число: "))
        if sign == '+':
            print(f'{num1}{sign}{num2} = {num1 + num2}')
        elif sign == '-':
            print(f'{num1}{sign}{num2} = {num1 - num2}')
        elif sign == '*':
            print(f'{num1}{sign}{num2} = {num1 * num2}')
        else:
            if num2 == 0 and sign == '/':
                print("Деление на 0 невозможно")
            else:
                print(f'{num1}{sign}{num2} = {num1 / num2}')
