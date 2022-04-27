# 문제 주소 : https://www.acmicpc.net/problem/1753

import sys, heapq

V, E = map(int, sys.stdin.readline().split())
START = int(sys.stdin.readline())
graph = { node: {} for node in range(1, V+1) }
distances = [0] + [ float('INF') for _ in range(V) ]
distances[START] = 0

for e in range(E):
    u, v, w = map(int, sys.stdin.readline().split())
    graph[u][v] = w

q = []
heapq.heappush(q, (0, START))

while q:
    dist, now = heapq.heappop(q)
    
    if dist > distances[now]:
        continue

    for i in graph[now]:
        cost = dist + graph[now][i]
        if cost < distances[i]:
            distances[i] = cost
            heapq.heappush(q, (cost, i))

for d in distances[1:]:
    print(d if d != float('INF') else 'INF')