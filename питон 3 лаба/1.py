print ('Введите x и точность')
x = float(input())
e = float(input())
c = x
y = c
Max = 500
for n in range (1, Max):
    c = -c*((x*x)/(2*n*(2*n+1)))
    y += c
    if abs(c) <= e:
        print ('Ответ: значение функции sin = ', y, 'Вычислено с точностью ', e, 'за ', n, ' итераций')
        break
else :
    print ('Решение не найдено')


