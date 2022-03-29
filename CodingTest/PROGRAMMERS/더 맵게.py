# 문제 주소 : https://programmers.co.kr/learn/courses/30/lessons/42626#

import heapq

def solution(scoville, K):
    result = 0
    heapq.heapify(scoville)
    
    while len(scoville) >= 2 and scoville[0] < K:
        result += 1
        lower1 = heapq.heappop(scoville)
        lower2 = heapq.heappop(scoville) * 2
        
        heapq.heappush(scoville, lower1+lower2)
    
    return result if scoville[0] >= K else -1