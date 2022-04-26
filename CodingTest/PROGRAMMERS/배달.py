# 문제 주소 : https://programmers.co.kr/learn/courses/30/lessons/12978

import heapq

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    queue = []
    heapq.heappush(queue, [distances[start], start])
    
    while queue:
        current_distance, current_node = heapq.heappop(queue)
        
        if distances[current_node] < current_distance:
            continue
        
        for adjacent, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[adjacent]:
                distances[adjacent] = distance
                heapq.heappush(queue, [distance, adjacent])
        
        return distances
    
def solution(N, road, K):
    graph = {i:{} for i in range(1, N+1)}
    for a, b, d in road:
        graph[a][b] = d
        graph[b][a] = d
    
    distance = dijkstra(graph, 1)
    return len([ i for i in distance if distance[i] <= K ])