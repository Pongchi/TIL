# 문제 주소 : https://www.acmicpc.net/problem/18352

import sys

N, M, K, X = map(int, sys.stdin.readline().split())
distance = [0] * (N+1)
graph = dict()

for m in range(M):
    A, B = map(int, sys.stdin.readline())
    if A not in graph:
        graph[A] = []
    graph[A].append(B)

####################################################

