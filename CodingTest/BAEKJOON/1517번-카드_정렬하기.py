# 문제 주소 : https://www.acmicpc.net/problem/1715

import sys, heapq

N = int(sys.stdin.readline())
heap = []
for _ in range(N):
    heapq.heappush(heap, int(sys.stdin.readline()))

result = 0
while len(heap) >= 2:
    s = heapq.heappop(heap) + heapq.heappop(heap)
    result += s
    heapq.heappush(heap, s)

print( result )