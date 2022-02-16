# 문제 주소 : https://www.acmicpc.net/problem/1260

import sys
from collections import deque

N, M, V = map(int, sys.stdin.readline().split())
tree = {i:set() for i in range(1, N+1)}
result = []

for _ in range(M):
    parent, child = map(int, sys.stdin.readline().split())
    tree[parent].add(child)
    tree[child].add(parent)

def dfs(current_node : int, visited_node : list):
    if result:
        return
    elif len(visited_node) == min(N, M+1):
        result.append(visited_node)
        return
    elif current_node in visited_node:
        return
    
    visited_node.append(current_node)
    for dest in tree[current_node]:
        dfs(dest, visited_node)

def bfs():
    visited_node = []
    queue = deque([V])
    
    while queue:
        n = queue.popleft()
        if n not in visited_node:
            visited_node.append(n)
            queue += tree[n] - set(visited_node)

    return result.append(visited_node)

dfs(V, [])
bfs()
print( " ".join(map(str, result[0])) )
print( " ".join(map(str, result[1])) )