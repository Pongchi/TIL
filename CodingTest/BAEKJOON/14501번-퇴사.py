# 문제 주소 : https://www.acmicpc.net/problem/14501

import sys

N = int(sys.stdin.readline())
T, P = [0]*N, [0]*N
dp = []
for i in range(N):
    T[i], P[i] = map(int, sys.stdin.readline().split())

print(N, T, P)