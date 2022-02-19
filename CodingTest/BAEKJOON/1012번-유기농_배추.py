# 문제 주소 : https://www.acmicpc.net/problem/1012

import sys

for T in range(int(sys.stdin.readline())):
    M, N, K = map(int, sys.stdin.readline().split())
    farm_land = { tuple(map(int, sys.stdin.readline().split())):True for k in range(K) }
    answer = 0

    for cabbage in farm_land.keys():
        if farm_land[cabbage]:
            answer += 1
            queue = set([cabbage])
            while queue:
                p = queue.pop()
                if farm_land[p]:
                    farm_land[p] = False
                    if farm_land.get((p[0]+1, p[1]), False):
                        queue.add((p[0]+1, p[1]))
                    if farm_land.get((p[0]-1, p[1]), False):
                        queue.add((p[0]-1, p[1]))
                    if farm_land.get((p[0], p[1]+1), False):
                        queue.add((p[0], p[1]+1))
                    if farm_land.get((p[0], p[1]-1), False):
                        queue.add((p[0], p[1]-1))
    print( answer )