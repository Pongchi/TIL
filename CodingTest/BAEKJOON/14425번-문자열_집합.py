# 문제 주소 : https://www.acmicpc.net/problem/14425

import sys

N, M = map(int, sys.stdin.readline().split())
words = { i:[] for i in "abcdefghijklmnopqrstuvwxyz" }
result = 0

for n in range(N):
    s = sys.stdin.readline().rstrip()
    words[s[0]].append(s)

for m in range(M):
    s = sys.stdin.readline().rstrip()
    for S in words[s[0]]:
        if s == S:
            result += 1
            break

print( result )