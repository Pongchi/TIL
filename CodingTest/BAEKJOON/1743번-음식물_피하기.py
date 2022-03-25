# 문제 주소 : https://www.acmicpc.net/problem/1743

import sys

sys.setrecursionlimit(10 ** 6)

N, M, K = map(int, sys.stdin.readline().split())
MAP = [ [0 for j in range(M) ] for i in range(N) ]
for k in range(K):
    r, c = map(lambda x : int(x)-1, sys.stdin.readline().split())
    MAP[r][c] = 1

result = 0
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
def dfs(row, col):
    cnt = 1
    MAP[row][col] = 0
    for i in range(4):
        x = row + dx[i]
        y = col + dy[i]
        if 0 <= x < N and 0 <= y < M and MAP[x][y]:
            cnt += dfs(x, y)

    return cnt

for i in range(N):
    for j in range(M):
        if MAP[i][j]:
            size = dfs(i, j)
            if size > result:
                result = size

print( result )