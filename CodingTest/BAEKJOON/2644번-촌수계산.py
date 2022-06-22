# 문제 주소 : https://www.acmicpc.net/problem/2644

from collections import deque

n = int(input())
A, B = map(lambda x : int(x)-1, input().split())
m = int(input())
graph = [ [] for _ in range(n) ]
for _ in range(m):
    x, y = map(lambda x : int(x)-1, input().split())
    graph[x].append(y)
    graph[y].append(x)

visited = [False] * n
visited[A] = True
queue = deque([(A, 1), (B, 1)])
result = []
while queue:
    current, dist = queue.popleft()
    if dist != 1 and (current == A or current == B):
        result.append(dist)
    
    for i in graph[current]:
        if not visited[i]:
            visited[i] = True
            queue.append((i, dist+1))

print( min(result) if result else -1 )