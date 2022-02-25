# 문제 주소 : https://www.acmicpc.net/problem/1932

import sys

n = int(sys.stdin.readline())
arr = [ list(map(int, sys.stdin.readline().split())) for _ in range(n) ]

for i in range(1, n):
    for j in range(len(arr[i])):
        if j == 0 or i == 1:
            arr[i][j] += arr[i-1][0]
        else:
            if j != i:
                arr[i][j] += max(arr[i-1][j-1], arr[i-1][j])
            else:
                arr[i][j] += arr[i-1][j-1]

print( max(arr[-1]) ) 