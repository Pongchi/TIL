import sys

def min_teleport(distance):
    if distance <= 2:
        return distance

    result = 2
    for i in range(result, distance+1):
        if i  % 2 != 0:
            result += 1

    return result


T = int(sys.stdin.readline())

for i in range(T):
    x, y = map(int, sys.stdin.readline().split())
    print( min_teleport(y - x) )
