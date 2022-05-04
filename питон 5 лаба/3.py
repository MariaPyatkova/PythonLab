import random

def task3(int_array):
    for j in range (len(int_array[0])):
        for i in range (len(int_array)):
            if int_array[i][j] == 0:
                return j

print ('Вариант 15')
print ('Исходный массив:')
int_array = [[random.randint(-10,10) for i in range(9)] for j in range(6)]
for row in int_array:
    print ('\t'.join(str(x) for x in row))
print ('Первый столбец с нулевым элементом', task3(int_array)+1)
