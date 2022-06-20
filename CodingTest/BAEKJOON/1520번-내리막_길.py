# 문제 주소 : https://www.acmicpc.net/problem/1520

import sys

sys.setrecursionlimit(10**6)

vx = [1, -1, 0, 0]
vy = [0, 0, 1, -1]

M, N = map(int, sys.stdin.readline().split())
MAP = [ list(map(int, sys.stdin.readline().split())) for _ in range(M) ]
dp = [ [-1]*N for _ in range(M) ]

def dfs(x, y):
    if dp[x][y] != -1:
        return dp[x][y]

    if x == M-1 and y == N-1:
        return 1
    
    dp[x][y] = 0
    for i in range(4):
        nx, ny = x+vx[i], y+vy[i]
        if 0 <= nx < M and 0 <= ny < N and MAP[x][y] > MAP[nx][ny]:
            dp[x][y] += dfs(nx, ny)

    return dp[x][y]

print(dfs(0, 0))