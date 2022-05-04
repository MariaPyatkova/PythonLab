import math
print ('Введите значение x')
x = float(input())
if -7<=x<=-6:
    res = 1
elif -6<x<=-4:
    res = -0.5*x-2
elif -4<x<=0:
    res = math.sqrt(-(x+2)**2+4)
elif 0<x<=2:
    res = - math.sqrt(1-(x-1)**2)
elif 2<x<=3:
    res = 2-x
else:
    res ='Функция не определена в этой точке'

print('Ответ:', res)
