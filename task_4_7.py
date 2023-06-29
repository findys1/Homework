import math
a, b, c = float(input('Введите коэффицент a: ')), float(input('Введите коэффицент b: ')), float(input('Введите коэффицент c: '))
D = b ** 2 - 4 * a * c
if D < 0:
    print('Корней у уравнения нет')
elif D == 0:
    print('X = ', -b / (2 * a))
else:
    print('X1 = ', (-b + math.sqrt(D)) / (2 * a))
    print('X2 = ', (-b - math.sqrt(D)) / (2 * a))