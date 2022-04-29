# 문제 주소 : https://www.acmicpc.net/problem/1987

R, C = map(int, input().split())
MAP = [ list(input()) for i in range(R) ]
visited_map = [ [1]*C for i in range(R) ]
visited_map[0][0] = 0
visited_alphabet = [1] * 26
visited_alphabet[ord(MAP[0][0])-65] = 0
answer = 1

vr = [1, -1, 0, 0]
vc = [0, 0, 1, -1]
def backtracking(distance, row, col):
    global answer
    if distance > answer:
        answer = distance
        
    for i in range(4):
        nr, nc = row+vr[i], col+vc[i]
        if 0 <= nr < R and 0 <= nc < C and visited_map[nr][nc] and visited_alphabet[ord(MAP[nr][nc])-65]:
            visited_map[nr][nc] = 0
            visited_alphabet[ord(MAP[nr][nc])-65] = 0

            backtracking(distance+1, nr, nc)
            
            visited_map[nr][nc] = 1
            visited_alphabet[ord(MAP[nr][nc])-65] = 1

backtracking(1, 0, 0)
print( answer )