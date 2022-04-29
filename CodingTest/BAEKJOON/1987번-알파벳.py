# 문제 주소 : https://www.acmicpc.net/problem/1987

from queue import deque

R, C = map(int, input().split())
MAP = [ list(input()) for i in range(R) ]
visited_map = [ [1]*C for i in range(R) ]
visited_map[0][0] = 0
visited_alphabet = [1] * 26
visited_alphabet[ord(MAP[0][0])-65] = 0
answer = 1

vr = [1, -1, 0, 0]
vc = [0, 0, 1, -1]
queue = deque([(0, 0, 1)])

while queue:
    r, c, d = queue.popleft()
    if d > answer:
        answer = d
    
    for i in range(4):
        nr, nc = r+vr[i], c+vc[i]
        
        if 0 <= nr < R and 0 <= nc < C and visited_map[nr][nc] and visited_alphabet[ord(MAP[nr][nc])-65]:
            queue.append((nr, nc, d+1))
            visited_map[nc][nc] = 0
            visited_alphabet[ord(MAP[nr][nc])-65] = 0

print( answer )