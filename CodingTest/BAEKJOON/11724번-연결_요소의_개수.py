# 문제 주소 : https://www.acmicpc.net/problem/11724

import sys
from collections import deque

N, M = map(int ,sys.stdin.readline().split())
visited = set()
answer = 0
Graph = { i:set() for i in range(1, N+1) }

def dfs(root):
    queue = deque([root])

    while queue:
        n = queue.popleft()
        if n not in visited:
            visited.add(n)
            queue += list(Graph[n] - visited)

for m in range(M):
    a, b = map(int, sys.stdin.readline().split())
    Graph[a].add(b)
    Graph[b].add(a)

for root in Graph:
    if len(Graph[root]) == 0:
        answer += 1
    for line in Graph[root]:
        if line not in visited:
            dfs(line)
            answer += 1
        else:
            break

print( answer )