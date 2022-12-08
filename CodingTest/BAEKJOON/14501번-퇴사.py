# 문제 주소 : https://www.acmicpc.net/problem/14501

import sys
from collections import deque

N = int(sys.stdin.readline())
T, P = [0]*N, [0]*N
for i in range(N):
    T[i], P[i] = map(int, sys.stdin.readline().split())

dp = [0] * N
queue = deque([ (i, P[i]) for i in range(N) if T[i]+i < N ])
while queue:
    days, propit = queue.popleft()
    if days+T[days] < N:
        dp[days] = max(propit+P[days], dp[days])
        for i in range(N-days-T[days]):
            if dp[days+T[days]+i] < dp[days]:
                dp[days+T[days]+i] = dp[days]
                queue.append((days+T[days]+i, dp[days]))

print( dp[-1] )
print(dp)