# 문제 주소 : https://www.acmicpc.net/problem/1325

N, M = map(int, input().split())
graph = [ [] for _ in range(N) ]
for _ in range(M):
    A, B = map(lambda x : int(x)-1, input().split())
    graph[B].append(A)

result = [ [i,0] for i in range(N) ]
for start in range(N):
    answer = 1
    stack = [start]
    visited = [False] * N
    visited[start] = True
    while stack:
        n = stack.pop()
        for j in graph[n]:
            if not visited[j]:
                stack.append(j)
                visited[j] = True
                answer += 1

    result[start][1] = answer

_max = max(result, key=lambda x : x[1])[1]
for computer, cnt in result:
    if cnt == _max:
        print(computer+1, end=' ')