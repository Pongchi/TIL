# 문제 주소 : https://www.acmicpc.net/problem/1009

import sys


for _ in range(int(sys.stdin.readline())):
    a, b = map(int, sys.stdin.readline().split())
    print( pow(a, b) % 10 or 10)