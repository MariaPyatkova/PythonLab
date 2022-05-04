import random


def characteristics(row):
    return sum(elem for elem in row if elem < 0 and elem%2 == 0)


def task4(int_array):
    return sorted(int_array, key=characteristics, reverse=True)


print ('Вариант 15')
print ('Исходный массив:')
int_array = [[random.randint(-10,10) for i in range(9)] for j in range(6)]
for row in int_array:
    print ('\t'.join(str(x) for x in row))
print ('Ответ: ')

for row in task4(int_array):
    print ('\t'.join(str(x) for x in row))
