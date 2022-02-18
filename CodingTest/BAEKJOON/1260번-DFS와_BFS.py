# 문제 주소 : https://www.acmicpc.net/problem/1260

import sys
from collections import deque

N, M, V = map(int, sys.stdin.readline().split())
tree = {i:set() for i in range(1, N+1)}

for _ in range(M):
    parent, child = map(int, sys.stdin.readline().split())
    tree[parent].add(child)
    tree[child].add(parent)

def dfs():
    visited_node = []
    stack = [V]

    while stack:
        n = stack.pop()
        if n not in visited_node:
            visited_node.append(n)
            stack += sorted(tree[n] - set(visited_node), reverse=True)

    return visited_node

def bfs():
    visited_node = []
    queue = deque([V])
    
    while queue:
        n = queue.popleft()
        if n not in visited_node:
            visited_node.append(n)
            queue += sorted(tree[n] - set(visited_node))

    return visited_node

print( " ".join(map(str, dfs())) )
print( " ".join(map(str, bfs())) )