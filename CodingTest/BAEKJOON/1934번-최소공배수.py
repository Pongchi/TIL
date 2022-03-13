# 문제 주소 : https://www.acmicpc.net/problem/1037

import sys, math

for t in range(int(sys.stdin.readline())):
    A, B = map(int, sys.stdin.readline().split())
    print( (A*B) // math.gcd(A, B))