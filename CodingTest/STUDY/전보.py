import sys
from queue import deque

N, M, C = map(int, sys.stdin.readline().split())
distance = [0] * (N+1)
graph = [[]] * (N+1)
for m in range(M):
    a, b, time = map(int, sys.stdin.readline().split())
    graph[a].append((b, time))
    graph[b].append((a, time))
##############################################################
queue = deque([C])
count = 0
max_delay = 0

while queue:
    city = queue.popleft()
    for c, d in graph[city]:
        if c != C and (distance[c] == 0 or distance[city]+d < distance[c]):
            if distance[c] == 0:
                count += 1
            
            queue.append(c)
            distance[c] = distance[city] + d

            if max_delay < distance[c]:
                max_delay = distance[c]

print(count, max_delay)