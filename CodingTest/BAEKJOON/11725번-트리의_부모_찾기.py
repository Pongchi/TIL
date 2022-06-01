# 문제 주소 : https://www.acmicpc.net/problem/11725

import sys

N = int(sys.stdin.readline())
TREE = [ [] for _ in range(N+1) ]
for _ in range(N-1):
    a, b = map(int, sys.stdin.readline().split())
    TREE[a].append(b)

def dfs(target):
    parent = 1
    stack = TREE[parent][:]
    while stack:
        n = stack.pop()
        if n == target:
            return parent
        parent = n

for i in range(2, N+1):
    print( dfs(i) )