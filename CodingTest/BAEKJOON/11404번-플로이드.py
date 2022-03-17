import sys

n, m = map(int, [sys.stdin.readline(), sys.stdin.readline()])
distance = [[100001] * n for i in range(n)]
graph = [dict() for i in range(n+1)]
for M in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    distance[a-1][b-1] = min(distance[a-1][b-1], c)

################################################################
for k in range(n):
    distance[k][k] = 0
    for i in range(n):
        for j in range(n):
            distance[i][j] = min( distance[i][j], distance[i][k]+distance[k][j] )

for row in distance:
    for c in row:
        c = 0 if c == 100001 else c
        print(c, end=' ')
    print()