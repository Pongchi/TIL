# 문제 주소 : https://www.acmicpc.net/problem/1037

import sys

for t in range(int(sys.stdin.readline())):
    A, B = sorted(map(int, sys.stdin.readline().split()))
    for i in range(1, B+1):
        if (A*i) % B == 0:
            print(A*i)
            break