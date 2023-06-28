A, B = float(input('Введите число A: ')), float(input('Введите число B: '))
if  A == 0 and B == 1:
    print('X любое число')
elif A == 0 or A == B + 1:
    print('Решений у уравнения нет')
else:
    print('X = ', (B - 1) / A - 1)