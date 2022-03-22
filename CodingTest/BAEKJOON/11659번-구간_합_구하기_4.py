# 문제 주소 : https://www.acmicpc.net/problem/11659

import sys

N, M = map(int, sys.stdin.readline().split())
n_lst = list(map(int, sys.stdin.readline().split()))

for m in range(M):
    i, j = map(int, sys.stdin.readline().split())
    print( sum(n_lst[i-1:j]) )