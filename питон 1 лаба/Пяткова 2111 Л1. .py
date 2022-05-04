import math
a = float(input('Введите переменную a '))
x = float(input('Введите переменную x '))
print ('Исходные данные', end =': ')
print ('a = ', a, 'x = ', x)
znam = 2 * math.sin(2*a)/math.cos(2*a)
y = (math.cos(x)*(math.sqrt(math.pi*x)- math.exp(0.2*math.sqrt(a))+ znam + 1.6*10*10*10*2*math.log10(x)))/znam
print ('Результат: y = ', y)
