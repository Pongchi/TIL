# 문제 주소 : https://www.acmicpc.net/problem/1926

from queue import deque

n, m = map(int, input().split())
MAP = [ list(map(int, input().split())) for i in range(n) ]

count = 0
max_size = 0
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
for i in range(n):
    for j in range(m):
        if MAP[i][j]:
            count += 1
            queue = deque([(i, j)])
            size = 1
            MAP[i][j] = 0
            
            while queue:
                x, y = queue.popleft()
                for k in range(4):
                    xx = x + dx[k]
                    yy = y + dy[k]
                    if 0 <= xx < n and 0 <= yy < m and MAP[xx][yy]:
                        MAP[xx][yy] = 0
                        queue.append((xx, yy))
                        size += 1

            if max_size < size:
                max_size = size

print(count)
print(max_size)