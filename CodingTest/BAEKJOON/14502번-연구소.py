# 문제 주소 : https://www.acmicpc.net/problem/14502

import copy
from queue import deque
from itertools import combinations

N, M = map(int, input().split())
Board = [ list(map(int, input().split())) for i in range(N) ]
virus = [(i, j) for i in range(N) for j in range(M) if Board[i][j] == 2]
space = [(i, j) for i in range(N) for j in range(M) if Board[i][j] == 0]

def safe_size():
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    copy_Board = [ Board[i][:] for i in range(N) ]
    queue = deque(virus)
    while queue:
        X, Y = queue.popleft()
        for i in range(4):
            vx = dx[i] + X
            vy = dy[i] + Y
            if 0 <= vx < N and 0 <= vy < M and copy_Board[vx][vy] == 0:
                queue.append((vx, vy))
                copy_Board[vx][vy] = 2

    return len([True for i in range(N) for j in range(M) if copy_Board[i][j] == 0])

def brute_force():
    max_size = 0
    for s in combinations(space, 3):
        for i, j in s:
            Board[i][j] = 1
        size = safe_size()
        if max_size < size:
            max_size = size
        
        for i, j in s:
            Board[i][j] = 0

    return max_size

print( brute_force() )