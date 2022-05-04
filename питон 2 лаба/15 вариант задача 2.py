import math
print ('Введите значение R')
R = float(input())
print ('Введите значение x')
x = float(input())
print ('Введите значение y')
y = float(input())
if (-R<=x<=0) and (0<=y<=R)and y<=(-math.sqrt(R*R-(x+R)**2)+R) or (0<=x<=R) and (-R<=y<=0) and (y>= -(math.sqrt(R*R-x*x))):
 print('Точка попадает в закрашенную область')
else:
 print('Точка не попадает в закрашенную область')
