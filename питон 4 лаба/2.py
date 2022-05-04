import random

print ('Введите n')
n = int(input())
m = int
print ('Исходный массив:')
float_array = [random.uniform(-10000,10000) for i in range(n)]
for a in float_array:
    print (a)
mini = n
answer = 0
while mini > 0:
    mini -= 1
    if float_array[mini] < 0:
        break
    else:
        answer = answer + float_array[mini]
print ('Последний отрицательный элемент массива= ', float_array[mini])
print ('Cуммa элементов, расположенных правее последнего отрицательного элемента', answer)
     

