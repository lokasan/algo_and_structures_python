# 3.	По введенным пользователем координатам двух точек вывести
# уравнение прямой вида y = kx + b, проходящей через эти точки.
x1 = int(input('Введите x1: '))
y1 = int(input('Введите y1: '))
x2 = int(input('Введите x2: '))
y2 = int(input('Введите y2: '))

if x2 - x1 == 0 or y2 - y1 == 0:
    exit()
else:
    x = y1 - y2
    y = x2 - x1
    b = x1 * y2 - x2 * y1
    if y > 0 and b > 0:
        print(f'{x}x + {y}y + {b} = 0')
    elif y < 0 and b < 0:
        print(f'{x}x {y}y {b} = 0')
    elif y < 0 and b > 0:
        print(f'{x}x {y}y + {b} = 0')
    elif y > 0 and b < 0:
        print(f'{x}x + {y}y {b} = 0')
