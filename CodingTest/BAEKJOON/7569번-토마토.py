# 문제 주소 : https://www.acmicpc.net/problem/7576

import sys
from collections import deque

_max = 0
M, N, H = map(int, sys.stdin.readline().split())
BOARD = [ [ list(map(int, sys.stdin.readline().split())) for _ in range(N) ] for i in range(H) ]

queue = deque()
vectorX = [1, -1, 0, 0, 0, 0]
vectorY = [0, 0, 1, -1, 0, 0]
vectorZ = [0, 0, 0, 0, 1, -1]

def checkBoard():
    for h in range(H):
        for i in range(N):
            for j in range(M):
                if BOARD[h][i][j] == 0:
                    return False
    return True

for h in range(H):
    for i in range(N):
        for j in range(M):
            if BOARD[h][i][j] == 1:
                queue.append((i, j, h))

while queue:
    X, Y, Z = queue.popleft()
    if BOARD[Z][X][Y] > _max:
        _max = BOARD[Z][X][Y]

    for i in range(6):
        dX, dY, dZ = X + vectorX[i], Y + vectorY[i], Z + vectorZ[i]
        if 0 <= dX < N and 0 <= dY < M and 0 <= dZ < H and BOARD[dZ][dX][dY] == 0:
            BOARD[dZ][dX][dY] = BOARD[Z][X][Y] + 1
            queue.append((dX, dY, dZ))

print(_max-1 if checkBoard() else -1)