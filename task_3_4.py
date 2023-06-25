str = input('Введите строку: ')
a = str[len(str) // 2]
print(a)
if a == str[0]:
    lst = list(str)
    lst = lst[1:len(lst)]
    print(''.join(lst))