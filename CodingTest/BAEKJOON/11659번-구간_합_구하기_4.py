# 문제 주소 : https://www.acmicpc.net/problem/11659

import sys

N, M = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
for i in range(1, N):
    arr[i] += arr[i-1]

for m in range(M):
    i, j = map(lambda x: int(x)-1, sys.stdin.readline().split())
    print( arr[j] - arr[i-1] if i != 0 else arr[j])