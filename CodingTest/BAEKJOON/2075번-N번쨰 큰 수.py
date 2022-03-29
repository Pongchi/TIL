# 문제 주소 : https://www.acmicpc.net/problem/2075

import heapq

N = int(input())
heap = []

for n in range(N):
    for i in map(int, input().split()):
        heapq.heappush(heap, -i)

for n in range(N-1):
    heapq.heappop(heap)   

print(-heapq.heappop(heap))