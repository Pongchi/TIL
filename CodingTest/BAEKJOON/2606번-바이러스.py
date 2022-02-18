# 문제 주소 : https://www.acmicpc.net/problem/2606
# 풀이 방법 : 전형적인 DFS.

import sys

N = int(sys.stdin.readline())
tree = {i:set() for i in range(1, N+1)}
visited_node = []
stack = [1]

for _ in range(int(sys.stdin.readline())):
    A, B = map(int, sys.stdin.readline().split())
    tree[A].add(B)
    tree[B].add(A)

while stack:
    n = stack.pop()
    if n not in visited_node:
        visited_node.append(n)
        stack += tree[n] - set(visited_node)

print( len(visited_node) - 1 )