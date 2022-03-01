# 문제 주소 : https://www.acmicpc.net/problem/11279

import sys, heapq

N = int(sys.stdin.readline())
arr = []

for _ in range(N):
    n = int(sys.stdin.readline())
    if n != 0:
        heapq.heappush(arr, -n)
    else:
        print(-heapq.heappop(arr) if arr else 0)