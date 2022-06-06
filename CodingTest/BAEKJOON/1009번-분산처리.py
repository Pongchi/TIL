# 문제 주소 : https://www.acmicpc.net/problem/1009

import sys


for _ in range(int(sys.stdin.readline())):
    a, b = map(int, sys.stdin.readline().split())
    result = a

    for _ in range(b-1):
        result = (result*a) % 10
    
    print(result or 10)