import math


def course(r):
    d = 73.6
    a = r/d
    return a


def target(x,y):
    if (x*x + y*y <= 1) or (x <= 0) and (y <= 0) and (y>=-x-2):
        return True
    else:
        return False

