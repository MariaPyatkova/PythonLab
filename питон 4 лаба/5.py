import random

print ('Вариaнт 15')
print ('Исходный массив:')
int_array = [random.randint(-10,10) for i in range(10)]
for a in int_array:
    print (a)
m = 0
ans = 1
for a in int_array:
    if abs(a)> m:
        m = abs(a)
        ans = 1
    else:
        ans *= a

print ('Максимальный по модулю элемент ', m)
print ('Произведение элементов, расположенных после максимального по модулю элемента равно', ans)

