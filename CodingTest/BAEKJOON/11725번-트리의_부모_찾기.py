# 문제 주소 : https://www.acmicpc.net/problem/11725

import sys

N = int(sys.stdin.readline())
TREE = [ [] for _ in range(N+1)]
answer = [0] * (N+1)
for _ in range(N-1):
    a, b = sorted(map(int, sys.stdin.readline().split()))
    TREE[a].append(b)
    TREE[b].append(a)

stack = [1]
visted = [False] * (N+1)
while stack:
    n = stack.pop()
    if not visted[n]:
        stack.extend(TREE[n])

        visted[n] = True
        for i in TREE[n]:
            if not answer[i]:
                answer[i] = n

for i in range(2, N+1):
    print(answer[i])