import math
print ('Вариант 15')
b = float(input('Введите переменную b (ОДЗ b => 2) '))
print ('Исходные данные', end =': ')
print ('b = ', b)
if b >= 2:
 z1 = (math.sqrt(2*b+2*(math.sqrt(b*b-4))))/((math.sqrt(b*b-4))+b+2)
 print ('Результат: z1 = ', z1)
else:
 print('Нет действительных корней')
