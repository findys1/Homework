weight, height, old  = float(input('Введите свой вес: ')), float(input('Введите свой рост: ')), int(input('Введите свой возраст: '))
i = weight / height ** 2
if old < 45:
    if i < 18.5:
        print('Недостаточная масса тела')
    elif 18.5 < i < 24.99:
        print('Норма')
    elif 25 < i < 29.99:
        print('Избыточная масса тела')
    else:
        print('Ожирение')
else:
    if i < 22:
        print('Недостаточная масса тела')
    elif 22 < i < 26.99:
        print('Норма')
    elif 27 < i < 31.99:
        print('Избыточная масса тела')
    else:
        print('Ожирение')