# 문제 주소 : https://www.acmicpc.net/problem/1697

from collections import deque

N, K = map(int, input().split())
queue = deque([N])
visited = [0] * 100001

while queue:
    n = queue.popleft()
    if n == K:
        break

    vector = [n+1, n-1, n*2]
    for v in vector:
        if 0 <= v <= 100000 and visited[v] == 0:
            queue.append(v)
            visited[v] = visited[n] + 1

print( visited[n] )