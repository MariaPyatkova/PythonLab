x = -1
xmax = 1
dx = 0.1
e = 1e-8
Max = 500
print ('   (sin x)/x')
print ('x', '\t', 'y','\t', 'n')
while x <=xmax:
    c = 1
    y = c
    for n in range (Max):
        c *= -(x**2)/((2*n+3)*(2*n+2))
        y += c
        if abs(c) <= e:
            break
    else :
        y = '-'
    print('{:.1f}\t{:.4f}\t{}'.format(x, y, n))
    x+= dx


