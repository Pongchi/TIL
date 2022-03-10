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

queue = deque([X])

while queue:
    n = queue.popleft()
    
    for i in graph[n]:
        if distance[i] == 0 or distance[i] < distance[n]:
            queue.append(i)
            distance[i] = distance[n] + 1


result = []
for i in range(len(distance)):
    if distance[i] == K:
        result.append(i)

print( "\n".join(map(str, result)) if result else -1 )