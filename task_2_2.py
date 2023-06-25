a, b, c = int(input()), int(input()), int(input())
max_el = max(a, b, c)
min_el = min(a, b, c)
middle_el = a + b + c - max_el - min_el
if min_el >= 1 and min_el % 2 == 0:
    print('Самое маленькое число больше 1 и четное')
else:
    print('Самое маленькое число меньше 1 и нечетное')


if max_el > (middle_el + min_el) / 2 or max_el < middle_el * min_el:
    print('Самое большое число больше полусуммы среднего и маленького или меньше их произведения')
else:
    print('...')


if middle_el % 3 == 0 and middle_el % 2 == 0:
    print('Среднее число делится на 3 и четное')
else:
    print('...')