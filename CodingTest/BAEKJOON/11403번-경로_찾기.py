# 문제 주소 : https://www.acmicpc.net/problem/11403

import sys

N = int(sys.stdin.readline())
MAP = [ list(map(int, sys.stdin.readline().split())) for _ in range(N) ]

for k in range(N):
    for i in range(N):
        for j in range(N):
            if MAP[i][j] or (MAP[i][k] and MAP[k][j]):
                MAP[i][j] = 1

for i in range(N):
    print(*MAP[i])