import math
a = float(input('Введите первый операнд: ' ))
op =(input('Введите операцию: ' )) 
b = float(input('Введите второй операнд: ' ))
res1 = a+b
res2 = a-b
res3 = a*b
res4 = a/b
if  op == '+' :
    print(res1)
elif  op == '-' :
    print(res2)
elif  op == '*' :
    print(res3)
elif  op == '/' :
    print(res4)
else:
    print ('Недопустимая операция')


