print(' Введите время начала интервала (час мин сек)')
hour1 = int(input())
print('часов') 
min1 = int(input())
print('минут') 
sec1 = int(input())
print('секунд') 
print('Время начала интервала', end =': ')
print(hour1, end = ":")
print(min1, end = ":")
print(sec1)
print(' Введите время конца интервала (час мин сек)')
hour2 = int(input())
print('часов') 
min2 = int(input())
print('минут') 
sec2 = int(input())
print('секунд') 
print('Время конца интервала', end = ': ')
print(hour2, end = ":")
print(min2, end = ":")
print(sec2)
sum_sec = int((hour2 - hour1)*3600 + (min2 - min1) * 60 + sec2 - sec1)
hour = int(sum_sec / 3600)
min = int((sum_sec - hour * 3600) / 60)
sec = int((sum_sec - hour * 3600 - min * 60))
print ('Продолжительность промежутка от ', hour1, ':', min1, ':', sec1, 'до ',
hour2, ':', min2, ':', sec2, ' равна ', hour, 'ч :', min, 'мин :', sec, 'сек')

