# 문제 주소 : https://www.acmicpc.net/problem/2206

import sys
from queue import deque

N, M = map(int, sys.stdin.readline().split())
MAP = [ list(map(int, list(sys.stdin.readline().rstrip()))) for _ in range(N) ]

vx = [1, -1, 0, 0]
vy = [0, 0, 1, -1]
result = []
def bfs(x, y, d, isBreak):
    queue = deque([(x, y, d)])
    MAP[x][y] = d
    
    while queue:
        x, y, d = queue.popleft()
        
        if x == N-1 and y == M-1:
            return d

        for i in range(4):
            nx, ny = x+vx[i], y+vy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if MAP[nx][ny] == 0:
                    MAP[nx][ny] = d
                    queue.append((nx, ny, d+1))

                elif not isBreak and MAP[nx][ny] == 1:
                    res = bfs(nx, ny, d+1, True)
                    MAP[nx][ny] = 1

                    if res != -1:
                        result.append( res )
    return -1

res = bfs(0, 0, 1, False)
if res == -1:
    print( min(result) if result else -1)

else:
    print( min(res, min(result)) if result else res)