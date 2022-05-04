import random

print ('Вариант 15')
print ('Исходный массив:')
int_array = [random.randint(-10000,10000) for i in range(10)]
for a in int_array:
    print (a)

print ('Введите величину, до которой хотите сжать массив')
c = int(input())

answer = [i for i in int_array if i >= c]
print ('"Сжатый" массив:')
for b in answer:
    print (b)

print ('Готово! Элементы, меньшие', c, 'удалены из массива')

