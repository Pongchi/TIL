# 문제 주소 : https://www.acmicpc.net/problem/2981

import sys

N = int(sys.stdin.readline())
memo = [ int(sys.stdin.readline()) for i in range(N) ]

def isValid(n):
    tmp = memo[0] % n
    for m in memo[1:]:
        if tmp != m % n:
            return False
    return True

result = []
for i in range(2, max(memo)+1):
    if isValid(i):
        result.append(i)

print(" ".join(map(str, result)))