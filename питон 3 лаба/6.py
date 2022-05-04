import math

print ('Введите значения х и у, чтобы узнать попадает ли точка в заштрихованную область : ')
for i in range (10):
    x = float(input())
    y = float(input())
    if (x*x + y*y <= 1) or (x <= 0) and (y <= 0) and (y>=-x-2):
        print('Точка попадает в область')
    else:
        print ('Точка не попадает в область')
