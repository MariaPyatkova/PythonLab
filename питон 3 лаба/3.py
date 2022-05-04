print ('Введите стороны прямоугольника')
a = int(input())
b = int(input())
n = 0
while a != 0:
    if b > a:
        a, b = b, a
    k = a // b
    a = a % b
    print(k, 'квадратов', b, 'x', b)
    n += k
print ('Всего квадратов: ', n)
