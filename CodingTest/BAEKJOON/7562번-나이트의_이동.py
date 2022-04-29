# 문제 주소 : https://www.acmicpc.net/problem/7562

import sys
from queue import deque

vx = [2, 2, 1, 1, -1, -1, -2, -2]
vy = [1, -1, 2, -2, 2, -2, 1, -1]
def bfs(L, c, d):
    queue = deque([(c[0], c[1], 0)])
    MAP = [ [1]*L for i in range(L) ]
    MAP[c[0]][c[1]] = 0
    
    while queue:
        x, y, cnt = queue.popleft()
        
        if x == d[0] and y == d[1]:
            return cnt
        
        for i in range(8):
            nx = x+vx[i]
            ny = y+vy[i]
            if 0 <= nx < L and 0 <= ny < L and MAP[nx][ny]:
                queue.append([nx, ny, cnt+1])
                MAP[nx][ny] = 0

for T in range(int(sys.stdin.readline())):
    L = int(sys.stdin.readline())
    current_Location = tuple(map(int, sys.stdin.readline().split()))
    dst_Location = tuple(map(int, sys.stdin.readline().split()))

    print(bfs(L, current_Location, dst_Location))