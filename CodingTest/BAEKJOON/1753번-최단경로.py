# 문제 주소 : https://www.acmicpc.net/problem/1753

import sys, heapq

V, E = map(int, sys.stdin.readline().split())
START = int(sys.stdin.readline())
graph = [ [] for _ in range(V+1) ]
distances = [0] + [ float('INF') for _ in range(V) ]
q = []

for e in range(E):
    u, v, w = map(int, sys.stdin.readline().split())
    graph[u].append([v, w])

def dijkstra(start):
    distances[start] = 0
    heapq.heappush(q, (0, start))

    while q:
        d, now = heapq.heappop(q)

        if distances[now] < d:
            continue
        
        for next_node, dist in graph[now]:
            cost = d + dist

            if cost < distances[next_node]:
                distances[next_node] = cost
                heapq.heappush(q, [cost, next_node])

dijkstra(START)
for d in distances[1:]:
    print(d if d != float('INF') else 'INF')