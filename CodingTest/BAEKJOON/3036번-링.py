# 문제 주소 : https://www.acmicpc.net/problem/3036

import sys, fractions

N = int(sys.stdin.readline())
rings = list(map(int, sys.stdin.readline().split()))

for i in range(1, N):
    value = fractions.Fraction(rings[0], rings[i])
    print(value if '/' in str(value) else str(value)+'/1')