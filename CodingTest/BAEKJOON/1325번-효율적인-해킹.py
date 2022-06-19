# 문제 주소 : https://www.acmicpc.net/problem/1325

N, M = map(int, input().split())
graph = { i:[] for i in range(N) }
trust = { i:[] for i in range(N) }
for _ in range(M):
    A, B = map(lambda x : int(x)-1, input().split())
    graph[B].append(A)
    trust[A].append(B)

def cnt_hacking(start):
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
    return answer

result = []
for i in trust[ max(trust.keys(), key=lambda x : len(trust[x])) ]:
    result.append((i, cnt_hacking(i)))

_max = max(result, key=lambda x : x[1])[1]
for start, value in result:
    if value == _max:
        print(start+1, end=' ')