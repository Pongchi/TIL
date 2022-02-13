import sys

N, M = sys.stdin.readline().split()
A = list(map(int, sys.stdin.readline().split()))
B = list(map(int, sys.stdin.readline().split()))

print(*sorted(A + B))
