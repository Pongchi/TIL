# 문제 주소 : https://programmers.co.kr/learn/courses/30/lessons/42627

import heapq

def solution(jobs):
    heap = []
    for start, delay in jobs:
        heapq.heappush(heap, (delay, start))

    S = 0
    while heap:
        delay, start = heapq.heappop(heap)

        print(S, start, delay)
        S += (S - start) + delay


    return S // len(jobs)


print( solution([[0, 3], [1, 9], [2, 6]]) )