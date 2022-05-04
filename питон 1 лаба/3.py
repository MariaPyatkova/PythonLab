import math
a_degree= float(input('Введите переменную a в градусах '))
x = float(input('Введите переменную x '))
a = a_degree * math.pi / 180
x_rad = x * math.pi / 180
print ('Исходные данные', end =': ')
print ('a = ', a,'рад;', 'x = ', x)
znam = 2 * math.tan(2*a)
y = (math.cos(x_rad)*(math.sqrt(math.pi*x)- math.exp(0.2*math.sqrt(a))+ znam + 1.6*10*10*10*2*math.log10(x)))/znam
print ('Результат: y = ', y)

