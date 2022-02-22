# 문제 주소 : https://www.acmicpc.net/problem/7576

import sys
from collections import deque

_max = 0
M, N = map(int, sys.stdin.readline().split())
BOARD = [ list(map(int, sys.stdin.readline().split())) for _ in range(N) ]
queue = deque()
vectorX = [1, -1, 0, 0]
vectorY = [0, 0, 1, -1]

def checkBoard():
    for i in range(N):
        for j in range(M):
            if BOARD[i][j] == 0:
                return False
    return True

for i in range(N):
    for j in range(M):
        if BOARD[i][j] == 1:
            queue.append((i, j))

while queue:
    X, Y = queue.popleft()
    if BOARD[X][Y] > _max:
        _max = BOARD[X][Y]

    for i in range(4):
        dX, dY = X + vectorX[i], Y + vectorY[i]
        if 0 <= dX < N and 0 <= dY < M and BOARD[dX][dY] == 0:
            BOARD[dX][dY] = BOARD[X][Y] + 1
            queue.append((dX, dY))

print(_max-1 if checkBoard() else -1)