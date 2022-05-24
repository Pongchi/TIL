# 문제 주소 : https://www.acmicpc.net/problem/14567

import sys

N, M = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N) ]
result = [1]*N
for _ in range(M):
    A, B = map(lambda x : int(x)-1, sys.stdin.readline().split())
    graph[A].append(B)
    
for a in range(N):
    for b in graph[a]:
        result[b] = max(result[a]+1, result[b])

print(*result)