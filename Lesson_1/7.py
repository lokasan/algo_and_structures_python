"""
7.	По длинам трех отрезков, введенных пользователем, определить возможность
существования треугольника, составленного из этих отрезков. Если такой
треугольник существует, то определить, является ли он
разносторонним, равнобедренным или равносторонним.
"""
a = int(input("Введите сторону a "))
b = int(input("Введите сторону b "))
c = int(input("Введите сторону c "))
if (a < b + c) and (b < a + c) and (c < a + b):
    if a == b and a == c and b == c:
        print("Треугольник равносторонний")
    elif a != b and a != c and b != c:
        print("Треугольник разносторонний")
    elif a == b or a == c or b == c:
        print("Треугольник равнобедренный")
else:
    print("Треугольник не существует")
