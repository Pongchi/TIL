# 문제 주소 : https://www.acmicpc.net/problem/14567

import sys
from queue import deque

N, M = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N) ]
result = [1]*N
for _ in range(M):
    A, B = map(lambda x : int(x)-1, sys.stdin.readline().split())
    graph[A].append(B)
    
queue = deque([])
for i in range(N):
    if not len(graph[i]) == 0:
        queue.append(i)
        while queue:
            now = queue.popleft()
            for j in graph[now]:
                result[j] = max(result[now]+1, result[j])

print(*result)