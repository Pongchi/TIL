import sys

def min_teleport(distance):
    lst = []
    x = 1
    i = 1
    while len(lst) < distance:
        lst += [x] * i
        x += 1
        if  x % 2 != 0:
            i += 1
            
    return lst[distance-1]

for i in range(1, 16):
    print( min_teleport(i) )


T = int(sys.stdin.readline())

for i in range(T):
    x, y = map(int, sys.stdin.readline().split())
    print( min_teleport(y - x) )
