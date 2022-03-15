# 문제 주소 : https://www.acmicpc.net/problem/18352

import sys
from queue import deque

N, M, K, X = map(int, sys.stdin.readline().split())
distance = [0] * (N+1)
graph = [[] for i in range(N+1)]

for m in range(M):
    A, B = map(int, sys.stdin.readline().split())
    graph[A].append(B)

####################################################

queue = deque([(X, 0)])

while queue:
    origin, dst = queue.popleft()

    for destination in graph[origin]:
        if destination == X:
            continue
    
        if distance[destination] == 0 or dst+1 < distance[destination]:
            queue.append((destination, dst+1))
            distance[destination] = dst + 1


result = []
for i in range(len(distance)):
    if distance[i] == K:
        result.append(i)

print( "\n".join(map(str, result)) if result else -1 )