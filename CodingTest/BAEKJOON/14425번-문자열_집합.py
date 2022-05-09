# 문제 주소 : https://www.acmicpc.net/problem/14425

import sys

N, M = map(int, sys.stdin.readline().split())
words = set()
result = 0

for n in range(N):
    words.add(sys.stdin.readline().rstrip())

for m in range(M):
    if sys.stdin.readline().rstrip() in words:
        result += 1

print( result )