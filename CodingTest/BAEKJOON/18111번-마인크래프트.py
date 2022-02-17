# 문제 주소 : https://www.acmicpc.net/problem/18111

import sys

N, M, B = map(int, sys.stdin.readline().split())
World = [list(map(int, sys.stdin.readline().split())) for i in range(N)]
ans_time = 1000000000000000000000000000
ans_height = 0

for H in range(257):
    place = 0
    dig = 0
    for i in range(N):
        for j in range(M):
            if World[i][j] < H:
                place += H - World[i][j]
            else:
                dig += World[i][j] - H
        
    if B + dig < place:
        continue

    time = place + (2 * dig)
    if time <= ans_time:
        ans_time = time
        ans_height = H

print( ans_time, ans_height )