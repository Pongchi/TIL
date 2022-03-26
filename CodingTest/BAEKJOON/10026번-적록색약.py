# 문제 주소 : https://www.acmicpc.net/problem/10026

from queue import deque

N = int(input())
MAP = [ list(input()) for i in range(N) ]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

print(MAP)
def bfs(colors):
    area = 0
    for i in range(N):
        for j in range(N):
            if MAP[i][j] in colors:
                color = MAP[i][j]
                area += 1
                queue = deque([(i, j)])
                MAP[i][j] = colors[color]
                while queue:
                    x, y = queue.popleft()
                    for k in range(4):
                        xx = dx[k] + x
                        yy = dy[k] + y
                        if 0 <= xx < N and 0 <= yy < N and MAP[xx][yy] == color:
                            queue.append((xx, yy))
                            MAP[xx][yy] = colors[color]

    print(MAP)
    return area

print( bfs({'R':'GG', 'G':'GG', 'B':'BB'}), bfs({'GG':'', 'BB':''}))