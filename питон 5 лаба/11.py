import random

print ('Задача Л5.1')
print ('Исходный массив:')
int_array = [[random.uniform(-100,100) for i in range(8)] for j in range(5)]
for row in int_array:
    print ('\t'.join('{:.3}'.format(x) for x in row))

min_i = 0
min_j = 0
mini = int_array [min_i][min_j]
for i in range (len(int_array)):
    row = int_array[i]
    for j in range (len(row)):
        elem = row[j]
        if abs(elem) < abs(mini):
            mini = elem
            min_i = i
            min_j = j
print ('Наименьший по модулю элемент', mini, 'Его координаты: ', min_i+1, ';', min_j+1)
