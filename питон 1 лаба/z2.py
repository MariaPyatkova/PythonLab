import math
print ('Вариант 15')
b = float(input('Введите переменную b (ОДЗ: b > -2) '))
print ('Исходные данные', end =': ')
print ('b = ', b)
if b > -2:
 z2 = 1/math.sqrt(b+2)
 print ('Результат: z2 = ', z2)
else:
 print('Нет действительных корней')

