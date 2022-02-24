# 문제 주소 : https://www.acmicpc.net/problem/1932

import sys

n = int(sys.stdin.readline())
arr = [ list(map(int, sys.stdin.readline().split())) for _ in range(n) ]
memo = [0] * (n+1)

for i in range(1, n+1):
    pass