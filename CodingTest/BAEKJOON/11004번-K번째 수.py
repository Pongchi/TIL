# 문제 주소 : https://www.acmicpc.net/problem/11004

import heapq

def heap_sort(arr, k):
    heap = []
    for i in arr:
        heapq.heappush(heap, i)

    sorted_nums = []
    while heap:
        sorted_nums.append(heapq.heappop(heap))
    
    return sorted_nums[k-1]

N, K = map(int, input().split())
heap = list(map(int, input().split()))

print(heap_sort(heap, K))