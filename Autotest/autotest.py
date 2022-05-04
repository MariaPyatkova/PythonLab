from lab1 import course
from lab1 import target



def test1():
    assert course(736) == 10


def test2():
    assert target(0.5, -0.5) == True
    assert target(2, 2) == False

