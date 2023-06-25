str_1 = list(input('Ввести строку: '))
if len(str_1) > 10:
    str_2 = str_1
    str_2.append('!!!')
    print(''.join(str_2))
else:
    print(str_1[1])
