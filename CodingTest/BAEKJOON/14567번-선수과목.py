# 문제 주소 : https://www.acmicpc.net/problem/14567

import sys
from queue import deque

N, M = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N) ]
result = [1]*N
indegree = [0] * N
for _ in range(M):
    A, B = map(lambda x : int(x)-1, sys.stdin.readline().split())
    graph[A].append(B)
    indegree[B] += 1
    
queue = deque([])
for i in range(N):
    if indegree[i] == 0:
        queue.append(i)

    while queue:
        now = queue.popleft()
        for j in graph[now]:
            indegree[j] -= 1
            result[j] = max(result[now]+1, result[j])
            if indegree[j] == 0:
                queue.append(j)

print(*result)