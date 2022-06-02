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
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.child = []

def dfs(target):
    return 0

root = Node(1)
N = int(sys.stdin.readline())
for _ in range(N-1):
    a, b = sorted(map(int, sys.stdin.readline().split()))
    parent_a, parent_b = dfs(a), dfs(b)
    if parent_a is None:
        root.child.append(b)
    else:
        if parent_b is None:

'''
'''
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
        stack.extend(TREE[n])

for i in range(2, N+1):
    print( dfs(i) )
'''