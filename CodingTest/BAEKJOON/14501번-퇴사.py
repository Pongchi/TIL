# 문제 주소 : https://www.acmicpc.net/problem/14501

import sys
from collections import deque

N = int(sys.stdin.readline())
T, P = [0]*N, [0]*N
for i in range(N):
    T[i], P[i] = map(int, sys.stdin.readline().split())

dp = [0] * N
queue = deque([ (0, 0) ])
while queue:
    days, propit = queue.popleft()
    if days+T[days] < N:
        dp[days] = max(propit+P[days], dp[days])
        queue.append((days+T[days], dp[days]))
    
    for i in range(1, T[days]):
        if days+i < N:
            queue.append((days+i, dp[days]))
        else:
            break

print( dp[-1] )
print(dp)