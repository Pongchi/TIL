import sys

limit = 10000
PRIME = [True] * 10000
for i in range(2, limit):
    if PRIME[i]:
        for j in range(i+i, limit, i):
            PRIME[j] = False

T = int(sys.stdin.readline())
for t in range(T):
    n = int(sys.stdin.readline())
    for i in range(n//2, 1, -1):
        if PRIME[i] and PRIME[n-i]:
            print( i, n-i )
            break
