# 문제 주소 : https://programmers.co.kr/learn/courses/30/lessons/81302

from queue import deque


vx = [1, -1, 0, 0]
vy = [0, 0, 1, -1]
def solution(places):
    def check(place):
        w, h = len(place[0]), len(place)
        place = [ list(place[i]) for i in range(h) ]
        for i in range(h):
            for j in range(w):
                if place[i][j] == 'P':
                    queue = deque([(i, j, 0)])
                    
                    while queue:
                        x, y, d = queue.popleft()
                        place[x][y] = 'O'
                        if d == 2:
                            continue
                        
                        for k in range(4):
                            nx, ny = x+vx[k], y+vy[k]
                            if 0 <= nx < h and 0 <= ny < w:
                                if place[nx][ny] == 'O':
                                    queue.append( (nx, ny, d+1) )
                                elif place[nx][ny] == 'P':
                                    return 0                
        return 1
    
    return [ check(place) for place in places ]

print( solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))
# [ 1, 0, 1, 1, 1]