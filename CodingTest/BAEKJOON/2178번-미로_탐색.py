# 문제 주소 : https://www.acmicpc.net/problem/2178

import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
MAP = [ list(map(int, sys.stdin.readline().rstrip())) for _ in range(N) ]

def bfs(x, y):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    
    queue = deque([(x,y)])
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nextX = dx[i] + x
            nextY = dy[i] + y
            
            if nextX < 0 or nextX >= N or nextY < 0 or nextY >= M:
                continue
            
            if MAP[nextX][nextY] == 1:
                MAP[nextX][nextY] = MAP[x][y] + 1
                queue.append((nextX, nextY))
            
    return MAP[N-1][M-1]

print( bfs(0, 0) )