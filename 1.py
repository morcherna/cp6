print('Введите элементы массива')
array = []
try:
    for x in input().split():
        array.append(int(x))
except ValueError:
    print('Ошибка, неправильно введены элементы массива ')
else:
    print('Введите значение delta')
    try:
        delta = int(input())
    except ValueError:
        print('Ошибка, неправильно введено значение delta ')
    else:
        a = array.count(min(array) + delta)
        print(a)