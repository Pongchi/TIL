N, M = map(int, input().split())

graph = [ [] for i in range(N+1) ]
for m in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)

print(graph)