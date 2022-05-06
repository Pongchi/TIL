# 문제 주소 : https://www.acmicpc.net/problem/2981

import sys

N = int(sys.stdin.readline())
memo = [ int(sys.stdin.readline()) for i in range(N) ]

def isValid(n):
    return True

for i in range(2, min(memo)+1):
    if isValid(n):
        result.append(i)

print(" ".join(map(str, result)))