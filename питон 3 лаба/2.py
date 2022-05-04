import math
print ('Найдите корень методом деления cos(x) = x')
e = 1e-4
l = 0
r = 1
Max = 500
i = 0
while abs(r-l) > e:
    i += 1
    x = (l + r)/2
    if (math.cos(x) - x)*(math.cos(l) - l) < 0:
        r = x
    else:
        l = x
    if i >= Max:
        print ('Превышено число итераций')
        break
print ('Корень равен ', x)
