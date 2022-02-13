import sys

N = int(sys.stdin.readline())
A = sorted(list(map(int, sys.stdin.readline().split())), reverse=True)
B = sorted(list(map(int, sys.stdin.readline().split())))
total = 0

for i in range(N):
    total += A[i] * B[i]
print( total )
