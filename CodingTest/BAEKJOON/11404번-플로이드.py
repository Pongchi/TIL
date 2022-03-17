import sys
from math import inf
n, m = map(int, [sys.stdin.readline(), sys.stdin.readline()])
distance = [[inf] * n for i in range(n)]
for M in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    distance[a-1][b-1] = min(distance[a-1][b-1], c)

################################################################
for k in range(n):
    distance[k][k] = 0
    for i in range(n):
        for j in range(n):
            distance[i][j] = min( distance[i][j], distance[i][k]+distance[k][j] )

for start in range(n):
    for end in range(n):
        if distance[start][end] == inf:
            distance[start][end] = 0
    print(*distance[start])