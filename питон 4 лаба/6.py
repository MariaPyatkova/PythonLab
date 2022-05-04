import random

print ('Вариaнт 15')
print ('Исходный массив:')
a = [random.randint(-10000,10000) for i in range(10)]
for b in a:
    print (b)
print ('Преобразованный массив:')
j = 0
for i in range( len(a)): 
    if a[i] < 0:
        a[i], a[j] = a[j], a[i]
        j+= 1
for b in a:
    print (b)
