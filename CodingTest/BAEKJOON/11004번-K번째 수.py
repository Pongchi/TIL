# 문제 주소 : https://www.acmicpc.net/problem/11004

import heapq

N, K = map(int, input().split())
heap = list(map(int, input().split()))

for n in range(K-1):
    heapq.heappop(heap)

print( heapq.heappop(heap) )