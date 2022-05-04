# 문제 주소 : https://www.acmicpc.net/problem/14503

import sys

N, M = map(int, sys.stdin.readline())
r, c, d = map(int, sys.stdin.readline())
MAP = [ list(map(int, sys.stdin.readline().split())) for _ in range(N) ]
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
result = 0
step_2a = 0

while step_2a != 4:
    if 0 <= r+dx[(d+1)%4] < N and 0 <= c+dy[(d+1)%4] and MAP[r+dx[(d+1)%4]][c+dy[(d+1)%4]] == 0:
        step_2a += 1
        r += dx[(d+1)%4]
        c += dy[(d+1)%4]
        d = (d+1)%4
    else:
        step_2a = 0
    

print( result )
