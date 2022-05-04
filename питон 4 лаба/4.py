import random

print ('Вариант 15')
print ('Исходный массив:')
int_array = [random.randint(-10000,10000) for i in range(10)]
for a in int_array:
    print (a)

print ('Введите величину С')
c = int(input())

answer = len([i for i in int_array if i > c])
print ('Количество элементов, больших ', c, ':', answer)

