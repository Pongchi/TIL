from queue import deque

N, M = map(int, input().split())
graph = [[] for i in range(N+1)]
for m in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

X, K = map(int, input().split())
##################################################

def bfs(start, end):
    distance = [0] * (N+1)
    queue = deque([start])
    
    while queue:
        n = queue.popleft()
        if n == end:
            return distance[n]

        for company in graph[n]:
            if company != start and distance[company] == 0:
                queue.append(company)
                distance[company] = distance[n] + 1
        
    return -1

result = [bfs(1, K), bfs(K, X)]
print( sum(result) if not -1 in result else -1)