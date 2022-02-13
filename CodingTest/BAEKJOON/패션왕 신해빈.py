import sys

T = int(sys.stdin.readline())

for t in range(T):
    Clothes = dict()
    n = int(sys.stdin.readline())
    result = 1
    
    for i in range(n):
        clothes = sys.stdin.readline().split()
        if clothes[1] not in Clothes:
            Clothes[clothes[1]] = 0
        Clothes[clothes[1]] += 1

    for clothes in Clothes:
        result *= Clothes[clothes] + 1
    
    print( result -1 )
