a, b, c = int(input()), int(input()), int(input())
if a > b + c or b > a + c or c > a + b:
    print('Треугольник невозможен')
else:
    if a == b == c:
        print('Равносторонний треугольник')
    elif a == b or b == c or a == c:
        print('Равнобедренный треугольник')
    else:
        print('Разносторонний треугольник')