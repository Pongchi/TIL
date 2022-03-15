# 문제 주소 : https://www.acmicpc.net/problem/18405

import sys
from queue import deque

vectorR = [1, -1, 0, 0]
vectorC = [0, 0, 1, -1]

N, K = map(int, sys.stdin.readline().split())
tube = [ list(map(int, sys.stdin.readline().split())) for i in range(N) ]
S, X, Y = map(int, sys.stdin.readline().split())

queue = []
for row in range(N):
    for column in range(N):
        if tube[row][column] != 0:
            queue.append(((row,column), 0))

queue = deque(sorted(queue, key=lambda x : tube[x[0][0]][x[0][1]]))
###############################################################################
while queue:
    point, time = queue.popleft()
    if time == S:
        break

    for i in range(4):
        vR = point[0] + vectorR[i]
        vC = point[1] + vectorC[i]
        if 0 <= vR < N and 0 <= vC < N and tube[vR][vC] == 0:
            queue.append(((vR, vC), time+1))
            tube[vR][vC] = tube[point[0]][point[1]]

print(tube[X-1][Y-1] if tube[X-1][Y-1] else 0)