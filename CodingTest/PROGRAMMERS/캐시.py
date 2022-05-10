# 문제 주소 : https://programmers.co.kr/learn/courses/30/lessons/17680

from collections import deque

def solution(cacheSize, cities):
    if cacheSize == 0:
        return len(cities) * 5
    
    queue = deque([])
    result = 0
    for city in cities:
        city = city.lower()
        if city in queue:
            result += 1
            queue.remove(city)
        else:
            result += 5
        
        queue.append(city)
        if len(queue) > cacheSize:
            queue.popleft()
    return result