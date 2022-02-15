# 문제 주소 : https://www.acmicpc.net/problem/18111

import sys

N, M, B = map(int, sys.stdin.readline().split())
World = [list(map(int, sys.stdin.readline().split())) for i in range(N)]
result = []
RANGE = (0, 255)

def cntTime(height):
    block = B
    time = 0

    return 0
for h in set(World):
    result.append(cntTime(h))