import sys

def min_teleport(distance):
    lst = 0
    x = 1
    i = 1
    while lst < distance:
        lst += i
        x += 1
        if  x % 2 != 0:
            i += 1
            
    return x-1

T = int(sys.stdin.readline())

for i in range(T):
    x, y = map(int, sys.stdin.readline().split())
    print( min_teleport(y - x) )
