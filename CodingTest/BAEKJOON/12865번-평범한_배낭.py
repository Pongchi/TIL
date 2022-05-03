# 문제 주소 : https://www.acmicpc.net/problem/12865

import sys

N, K = map(int, sys.stdin.readline().split())
arr = sorted([ tuple(map(int, sys.stdin.readline().split())) for _ in range(N) ])
dp = [0]*(K+1)

for w, v in arr:
    for i in range(K, -1, -1):
        if i-w < 0:
            break

        dp[i] = max(dp[i-w]+v, dp[i])

print(dp[-1])