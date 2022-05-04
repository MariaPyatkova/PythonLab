hour1, min1, sec1 = map(int,input('Введите время начала интервала (час мин сек): ').split())
hour2, min2, sec2 = map(int,input('Введите время конца интервала (час мин сек): ').split())
sum_sec = int((hour2 - hour1)*3600 + (min2 - min1) * 60 + sec2 - sec1)
hour = int(sum_sec / 3600)
min = int((sum_sec - hour * 3600) / 60)
sec = int(sum_sec - hour * 3600 - min * 60)
print ('Продолжительность промежутка от ', hour1, ':', min1, ':', sec1, 'до ',
hour2, ':', min2, ':', sec2, ' равна ', hour, 'ч :', min, 'мин :', sec, 'сек')
