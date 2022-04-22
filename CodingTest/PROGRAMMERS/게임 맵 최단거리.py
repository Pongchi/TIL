# 문제 주소 : https://programmers.co.kr/learn/courses/30/lessons/1844

from queue import deque

def solution(maps):
    n, m = len(maps), len(maps[0])
    vR = [1, -1, 0, 0]
    vC = [0, 0, 1, -1]
    
    q = deque([(0, 0, 0)])
    
    while q:
        r, c, result = q.popleft()
        if r == n-1 and c == m-1:
            return result+1
        
        for i in range(4):
            R, C = r+vR[i], c+vC[i], 
            if 0 <= R < n and 0 <= C < m and maps[R][C]:
                q.append((R, C, result+1))
                maps[R][C] = 0
                
    return -1

print( solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]) )
print( solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]) )