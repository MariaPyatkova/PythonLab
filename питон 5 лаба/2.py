import random

print ('Задача Л5.2')
print ('Исходный массив:')
int_array = [[random.randint(-10,10) for i in range(9)] for j in range(6)]
for row in int_array:
    print ('\t'.join(str(x) for x in row))

for j in range (len(int_array[0])):
    for i in range (len(int_array)):
        if int_array[i][j] == 0:
            print('В', j+1, 'столбце', i+1, 'элемент нулевой')
            break
    else:
        print ('В', j+1, 'столбце нет нулей')