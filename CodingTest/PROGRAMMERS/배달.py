# 문제 주소 : https://programmers.co.kr/learn/courses/30/lessons/12978

import heapq

def solution(N, road, K):
    graph = [ [] for _ in range(N+1) ]
    distance = [float('inf')] * (N+1)
    
    for a, b, c in road:
        graph[a].append( (b, c) )
        graph[b].append( (a, c) )
        
    queue = []
    heapq.heappush(queue, (0, 1))
    distance[1] = 0
    
    while queue:
        dist, now = heapq.heappop(queue)
        
        if distance[now] < dist:
            continue
        
        for i in graph[now]:
            cost = dist + i[1]
            
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(queue, (cost, i[0]))
                
    return len([ i for i in distance if i <= K ])