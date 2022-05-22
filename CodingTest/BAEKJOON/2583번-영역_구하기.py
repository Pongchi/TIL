# 문제 주소 : https://www.acmicpc.net/problem/2583

from queue import deque

vx = [1, -1, 0, 0]
vy = [0, 0, 1, -1]

M, N, K = map(int, input().split())
MAP = [ [0]*N for _ in range(M) ]
for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(y1, y2):
        for j in range(x1, x2):
            MAP[i][j] = 1

result = []
for i in range(M):
    for j in range(N):
        if not MAP[i][j]:
            size = 1
            MAP[i][j] = 1
            queue = deque([(i, j)])
            
            while queue:
                x, y = queue.popleft()
                
                for k in range(4):
                    nx, ny = x+vx[k], y+vy[k]
                    if 0 <= nx < M and 0 <= ny < N and not MAP[nx][ny]:
                        size += 1
                        MAP[nx][ny] = 1
                        queue.append( (nx, ny) )

            result.append( size )
            

print( len(result) )
print(*sorted(result))