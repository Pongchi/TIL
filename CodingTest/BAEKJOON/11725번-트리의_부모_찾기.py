# 문제 주소 : https://www.acmicpc.net/problem/11725

import sys

N = int(sys.stdin.readline())
TREE = [ [] for _ in range(N+1)]
answer = [0] * (N+1)
for _ in range(N-1):
    a, b = sorted(map(int, sys.stdin.readline().split()))
    TREE[a].append(b)
    TREE[b].append(a)

q = [1]
for v in q:
    for ch in TREE[v]:
        if not answer[ch]:
            answer[ch] = v
            q.append(ch)

for i in range(2, N+1):
    print(answer[i])