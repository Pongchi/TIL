# 문제 주소 : https://www.acmicpc.net/problem/1966
# 문제 분류 : 구현, 자료 구조, 시뮬레이션, 큐

import sys

for t in range(int(sys.stdin.readline())):
    N, M = map(int, sys.stdin.readline().split())
    Priority = sorted({ i:P for i, P in enumerate(map(int, sys.stdin.readline().split()))}.items(), reverse=True, key=lambda x: x[1])

    print( Priority )
