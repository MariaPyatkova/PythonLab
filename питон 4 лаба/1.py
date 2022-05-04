import random
print ('Исходный массив:')

int_array = [random.randint(-100000,100000) for i in range(10)]
for a in int_array:
    print (a)

minimal = min (int_array)
maximum = max (int_array)
mini = int_array.index(minimal)
maxi = int_array.index(maximum)
print ('Максимальное число в массиве = ', maximum, 'Минимальное число в массиве', minimal)
if (mini > maxi):
    mini, maxi = maxi, mini
answer = len([i for i in int_array[mini:maxi] if i > 0])

print ('Oтвет: Положительных чисел', answer)


