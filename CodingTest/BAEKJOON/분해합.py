import sys

N = int(sys.stdin.readline())

def DSum(N):
    for i in range(1, N+1):
        S = 0
        S = i + sum(map(int, str(i)))
        print(i, S)
        if N == S:
            return i
    return 0

print(DSum(N))

