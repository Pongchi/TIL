# 문제 주소 : https://www.acmicpc.net/problem/1520

vx = [1, -1, 0, 0]
vy = [0, 0, 1, -1]

M, N = map(int, input().split())
MAP = [ list(map(int, input().split())) for _ in range(M) ]
stack = [(0, 0)]
result = 0

while stack:
    x, y = stack.pop()
    if x == M-1 and y == N-1:
        result += 1
        continue
    
    for i in range(4):
        nx, ny = x+vx[i], y+vy[i]
        if 0 <= nx < M and 0 <= ny < N and MAP[x][y] > MAP[nx][ny]:
            stack.append((nx, ny))

print(result)