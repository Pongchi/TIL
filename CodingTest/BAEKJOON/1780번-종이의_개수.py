# 문제 주소 : https://www.acmicpc.net/problem/1780

import sys

N = int(sys.stdin.readline())
MAP = [ list(map(int, sys.stdin.readline().split())) for _ in range(N) ]
result = [0, 0, 0]

def recur(x, y, n):
    check = MAP[x][y]

    for i in range(x, x+n):
        for j in range(y, y+n):

            if MAP[i][j] != check:
                for k in range(3):
                    for l in range(3):
                        recur(x + k*n//3, y + l*n//3, n//3)
                return
    
    result[check] += 1
    return

recur(0, 0, N)
print(result[-1], result[0], result[1])